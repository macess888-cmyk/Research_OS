from dataclasses import FrozenInstanceError, fields, is_dataclass
from datetime import datetime, timedelta, timezone, tzinfo
import importlib
import sys

import pytest

from models.runtime_event_record import RuntimeEventRecord
from models.runtime_record_identity import RuntimeRecordHeader


VALID_HEADER_RECORDED_AT = datetime(
    2026,
    7,
    17,
    12,
    0,
    0,
    tzinfo=timezone.utc,
)

VALID_OCCURRED_AT = datetime(
    2026,
    7,
    17,
    11,
    30,
    0,
    tzinfo=timezone.utc,
)

VALID_EFFECTIVE_AT = datetime(
    2026,
    7,
    17,
    11,
    45,
    0,
    tzinfo=timezone.utc,
)

VALID_EVENT_TYPE = "OBJECT_CREATED"
VALID_TARGET_REF = "OBJ-000001"
VALID_ACTOR_REF = "ACTOR-000001"
VALID_SOURCE_REF = "SYSTEM-000001"
VALID_SCOPE_REF = "SCOPE-000001"
VALID_BRANCH_REF = "BRANCH-000001"


def make_event_header(**overrides):
    values = {
        "record_id": "RR-000000101",
        "record_category": "EVENT",
        "recorded_at": VALID_HEADER_RECORDED_AT,
        "schema_version": "1.0",
        "provenance_ref": None,
        "external_id": None,
    }
    values.update(overrides)
    return RuntimeRecordHeader(**values)


def make_event(**overrides):
    values = {
        "header": make_event_header(),
        "event_type": VALID_EVENT_TYPE,
        "target_ref": None,
        "actor_ref": None,
        "source_ref": None,
        "scope_ref": None,
        "branch_ref": None,
        "occurred_at": None,
        "effective_at": None,
    }
    values.update(overrides)
    return RuntimeEventRecord(**values)


class InvalidTimezone(tzinfo):
    def utcoffset(self, dt):
        return None

    def dst(self, dt):
        return None

    def tzname(self, dt):
        return "INVALID"


def test_runtime_event_record_is_a_dataclass():
    assert is_dataclass(RuntimeEventRecord)


def test_runtime_event_record_declares_exact_field_order():
    assert [field.name for field in fields(RuntimeEventRecord)] == [
        "header",
        "event_type",
        "target_ref",
        "actor_ref",
        "source_ref",
        "scope_ref",
        "branch_ref",
        "occurred_at",
        "effective_at",
    ]


def test_runtime_event_record_accepts_header_and_event_type_only():
    event = RuntimeEventRecord(
        header=make_event_header(),
        event_type=VALID_EVENT_TYPE,
    )

    assert event.header.record_category == "EVENT"
    assert event.event_type == VALID_EVENT_TYPE
    assert event.target_ref is None
    assert event.actor_ref is None
    assert event.source_ref is None
    assert event.scope_ref is None
    assert event.branch_ref is None
    assert event.occurred_at is None
    assert event.effective_at is None


def test_runtime_event_record_preserves_exact_header_instance():
    header = make_event_header()
    event = make_event(header=header)

    assert event.header is header


def test_runtime_event_identity_is_supplied_by_header_record_id():
    event = make_event()

    assert event.header.record_id == "RR-000000101"
    assert not hasattr(event, "event_id")


def test_runtime_event_record_accepts_all_valid_context_fields():
    event = make_event(
        target_ref=VALID_TARGET_REF,
        actor_ref=VALID_ACTOR_REF,
        source_ref=VALID_SOURCE_REF,
        scope_ref=VALID_SCOPE_REF,
        branch_ref=VALID_BRANCH_REF,
        occurred_at=VALID_OCCURRED_AT,
        effective_at=VALID_EFFECTIVE_AT,
    )

    assert event.target_ref == VALID_TARGET_REF
    assert event.actor_ref == VALID_ACTOR_REF
    assert event.source_ref == VALID_SOURCE_REF
    assert event.scope_ref == VALID_SCOPE_REF
    assert event.branch_ref == VALID_BRANCH_REF
    assert event.occurred_at == VALID_OCCURRED_AT
    assert event.effective_at == VALID_EFFECTIVE_AT


def test_runtime_event_record_preserves_reference_values_exactly():
    event = make_event(
        target_ref=" target ",
        actor_ref=" actor ",
        source_ref=" source ",
        scope_ref=" scope ",
        branch_ref=" branch ",
    )

    assert event.target_ref == " target "
    assert event.actor_ref == " actor "
    assert event.source_ref == " source "
    assert event.scope_ref == " scope "
    assert event.branch_ref == " branch "


def test_runtime_event_record_accepts_non_utc_occurred_and_effective_times():
    occurred_at = datetime(
        2026,
        7,
        17,
        11,
        30,
        tzinfo=timezone(timedelta(hours=-7)),
    )
    effective_at = datetime(
        2026,
        7,
        17,
        21,
        15,
        tzinfo=timezone(timedelta(hours=5, minutes=30)),
    )

    event = make_event(
        occurred_at=occurred_at,
        effective_at=effective_at,
    )

    assert event.occurred_at == occurred_at
    assert event.effective_at == effective_at
    assert event.occurred_at.utcoffset() == timedelta(hours=-7)
    assert event.effective_at.utcoffset() == timedelta(hours=5, minutes=30)


@pytest.mark.parametrize("missing_field", ["header", "event_type"])
def test_runtime_event_record_requires_each_required_field(missing_field):
    values = {
        "header": make_event_header(),
        "event_type": VALID_EVENT_TYPE,
    }
    values.pop(missing_field)

    with pytest.raises(TypeError):
        RuntimeEventRecord(**values)


@pytest.mark.parametrize(
    "invalid_value",
    [
        None,
        "RR-000000101",
        {},
        [],
        (),
        1,
        True,
    ],
)
def test_header_rejects_non_runtime_record_header_values(invalid_value):
    with pytest.raises(TypeError, match="header"):
        make_event(header=invalid_value)


def test_header_accepts_event_record_category():
    event = make_event(header=make_event_header(record_category="EVENT"))

    assert event.header.record_category == "EVENT"


@pytest.mark.parametrize(
    "record_category",
    [
        "VERSION",
        "HOLD",
        "EVALUATION",
        "CUSTOM_RECORD",
        "INSPECTION_RESULT",
    ],
)
def test_header_rejects_non_event_record_categories(record_category):
    header = make_event_header(record_category=record_category)

    with pytest.raises(ValueError, match="header|record_category"):
        make_event(header=header)


@pytest.mark.parametrize(
    "invalid_value",
    [
        None,
        1,
        1.0,
        True,
        b"OBJECT_CREATED",
        [],
        {},
    ],
)
def test_event_type_rejects_non_string_values(invalid_value):
    with pytest.raises(TypeError, match="event_type"):
        make_event(event_type=invalid_value)


@pytest.mark.parametrize(
    "valid_value",
    [
        "OBJECT_CREATED",
        "VERSION_RECORDED",
        "PROGRESSION_ASSERTED",
        "RE_ENTRY_RECORDED",
        "EVENT2",
        "A",
        "A1",
        "CUSTOM_EVENT",
    ],
)
def test_event_type_accepts_valid_values(valid_value):
    assert make_event(event_type=valid_value).event_type == valid_value


@pytest.mark.parametrize(
    "invalid_value",
    [
        "",
        " ",
        "object_created",
        "ObjectCreated",
        "OBJECT-CREATED",
        "OBJECT CREATED",
        "_OBJECT_CREATED",
        "OBJECT_CREATED_",
        "OBJECT__CREATED",
        "2OBJECT",
        " OBJECT_CREATED",
        "OBJECT_CREATED ",
    ],
)
def test_event_type_rejects_invalid_values(invalid_value):
    with pytest.raises(ValueError, match="event_type"):
        make_event(event_type=invalid_value)


@pytest.mark.parametrize(
    "field_name",
    [
        "target_ref",
        "actor_ref",
        "source_ref",
        "scope_ref",
        "branch_ref",
    ],
)
@pytest.mark.parametrize(
    "invalid_value",
    [
        1,
        1.0,
        True,
        b"reference",
        [],
        {},
    ],
)
def test_optional_references_reject_non_string_non_none_values(
    field_name,
    invalid_value,
):
    with pytest.raises(TypeError, match=field_name):
        make_event(**{field_name: invalid_value})


@pytest.mark.parametrize(
    "field_name",
    [
        "target_ref",
        "actor_ref",
        "source_ref",
        "scope_ref",
        "branch_ref",
    ],
)
def test_optional_references_accept_none(field_name):
    event = make_event(**{field_name: None})

    assert getattr(event, field_name) is None


@pytest.mark.parametrize(
    "field_name",
    [
        "target_ref",
        "actor_ref",
        "source_ref",
        "scope_ref",
        "branch_ref",
    ],
)
@pytest.mark.parametrize(
    "valid_value",
    [
        "REF-001",
        "external/reference",
        " ref ",
        "0",
        "x",
    ],
)
def test_optional_references_accept_non_empty_strings(
    field_name,
    valid_value,
):
    event = make_event(**{field_name: valid_value})

    assert getattr(event, field_name) == valid_value


@pytest.mark.parametrize(
    "field_name",
    [
        "target_ref",
        "actor_ref",
        "source_ref",
        "scope_ref",
        "branch_ref",
    ],
)
@pytest.mark.parametrize(
    "invalid_value",
    [
        "",
        " ",
        "\t",
        "\n",
        "\r\n",
        "   \t  ",
    ],
)
def test_optional_references_reject_empty_or_whitespace_only_values(
    field_name,
    invalid_value,
):
    with pytest.raises(ValueError, match=field_name):
        make_event(**{field_name: invalid_value})


@pytest.mark.parametrize(
    "invalid_value",
    [
        "2026-07-17T11:30:00Z",
        0,
        1.0,
        True,
        {},
        [],
    ],
)
def test_occurred_at_rejects_non_datetime_non_none_values(invalid_value):
    with pytest.raises(TypeError, match="occurred_at"):
        make_event(occurred_at=invalid_value)


def test_occurred_at_rejects_naive_datetime():
    with pytest.raises(ValueError, match="occurred_at"):
        make_event(
            occurred_at=datetime(2026, 7, 17, 11, 30),
        )


def test_occurred_at_rejects_timezone_with_no_utc_offset():
    value = datetime(
        2026,
        7,
        17,
        11,
        30,
        tzinfo=InvalidTimezone(),
    )

    with pytest.raises(ValueError, match="occurred_at"):
        make_event(occurred_at=value)


def test_occurred_at_preserves_supplied_timezone_and_offset():
    supplied_timezone = timezone(timedelta(hours=-7))
    value = datetime(
        2026,
        7,
        17,
        11,
        30,
        tzinfo=supplied_timezone,
    )

    event = make_event(occurred_at=value)

    assert event.occurred_at == value
    assert event.occurred_at.tzinfo is supplied_timezone
    assert event.occurred_at.utcoffset() == timedelta(hours=-7)


@pytest.mark.parametrize(
    "invalid_value",
    [
        "2026-07-17T11:45:00Z",
        0,
        1.0,
        True,
        {},
        [],
    ],
)
def test_effective_at_rejects_non_datetime_non_none_values(invalid_value):
    with pytest.raises(TypeError, match="effective_at"):
        make_event(effective_at=invalid_value)


def test_effective_at_rejects_naive_datetime():
    with pytest.raises(ValueError, match="effective_at"):
        make_event(
            effective_at=datetime(2026, 7, 17, 11, 45),
        )


def test_effective_at_rejects_timezone_with_no_utc_offset():
    value = datetime(
        2026,
        7,
        17,
        11,
        45,
        tzinfo=InvalidTimezone(),
    )

    with pytest.raises(ValueError, match="effective_at"):
        make_event(effective_at=value)


def test_effective_at_preserves_supplied_timezone_and_offset():
    supplied_timezone = timezone(timedelta(hours=5, minutes=30))
    value = datetime(
        2026,
        7,
        17,
        11,
        45,
        tzinfo=supplied_timezone,
    )

    event = make_event(effective_at=value)

    assert event.effective_at == value
    assert event.effective_at.tzinfo is supplied_timezone
    assert event.effective_at.utcoffset() == timedelta(hours=5, minutes=30)


def test_runtime_event_record_does_not_default_occurred_at_to_recorded_at():
    event = make_event()

    assert event.occurred_at is None
    assert event.header.recorded_at == VALID_HEADER_RECORDED_AT


def test_runtime_event_record_does_not_default_effective_at_to_occurred_at():
    event = make_event(occurred_at=VALID_OCCURRED_AT)

    assert event.occurred_at == VALID_OCCURRED_AT
    assert event.effective_at is None


def test_runtime_event_record_allows_effective_time_before_occurred_time():
    occurred_at = datetime(
        2026,
        7,
        17,
        12,
        0,
        tzinfo=timezone.utc,
    )
    effective_at = datetime(
        2026,
        7,
        17,
        11,
        0,
        tzinfo=timezone.utc,
    )

    event = make_event(
        occurred_at=occurred_at,
        effective_at=effective_at,
    )

    assert event.effective_at < event.occurred_at


def test_runtime_event_record_allows_effective_time_after_recorded_time():
    effective_at = datetime(
        2026,
        7,
        18,
        12,
        0,
        tzinfo=timezone.utc,
    )

    event = make_event(effective_at=effective_at)

    assert event.effective_at > event.header.recorded_at


def test_runtime_event_record_allows_occurred_time_after_recorded_time():
    occurred_at = datetime(
        2026,
        7,
        18,
        12,
        0,
        tzinfo=timezone.utc,
    )

    event = make_event(occurred_at=occurred_at)

    assert event.occurred_at > event.header.recorded_at


def test_header_type_failure_precedes_event_type_failure():
    with pytest.raises(TypeError, match="header"):
        RuntimeEventRecord(
            header={},
            event_type=1,
            target_ref=1,
            occurred_at="invalid",
        )


def test_header_category_failure_precedes_event_type_failure():
    header = make_event_header(record_category="VERSION")

    with pytest.raises(ValueError, match="header|record_category"):
        RuntimeEventRecord(
            header=header,
            event_type=1,
        )


def test_event_type_type_failure_precedes_reference_failure():
    with pytest.raises(TypeError, match="event_type"):
        make_event(
            event_type=1,
            target_ref=1,
        )


def test_event_type_value_failure_precedes_reference_failure():
    with pytest.raises(ValueError, match="event_type"):
        make_event(
            event_type="invalid",
            target_ref=1,
        )


def test_target_reference_failure_precedes_actor_reference_failure():
    with pytest.raises(TypeError, match="target_ref"):
        make_event(
            target_ref=1,
            actor_ref=1,
        )


def test_branch_reference_failure_precedes_temporal_failure():
    with pytest.raises(TypeError, match="branch_ref"):
        make_event(
            branch_ref=1,
            occurred_at=datetime(2026, 7, 17, 11, 30),
        )


def test_occurred_at_failure_precedes_effective_at_failure():
    with pytest.raises(ValueError, match="occurred_at"):
        make_event(
            occurred_at=datetime(2026, 7, 17, 11, 30),
            effective_at=datetime(2026, 7, 17, 11, 45),
        )


@pytest.mark.parametrize(
    ("field_name", "new_value"),
    [
        (
            "header",
            make_event_header(record_id="RR-000000102"),
        ),
        ("event_type", "VERSION_RECORDED"),
        ("target_ref", "OBJ-000002"),
        ("actor_ref", "ACTOR-000002"),
        ("source_ref", "SYSTEM-000002"),
        ("scope_ref", "SCOPE-000002"),
        ("branch_ref", "BRANCH-000002"),
        (
            "occurred_at",
            datetime(2026, 7, 18, 11, 30, tzinfo=timezone.utc),
        ),
        (
            "effective_at",
            datetime(2026, 7, 18, 11, 45, tzinfo=timezone.utc),
        ),
    ],
)
def test_runtime_event_record_is_frozen(field_name, new_value):
    event = make_event()

    with pytest.raises(FrozenInstanceError):
        setattr(event, field_name, new_value)


def test_identical_runtime_event_records_compare_equal():
    assert make_event() == make_event()


@pytest.mark.parametrize(
    ("field_name", "different_value"),
    [
        (
            "header",
            make_event_header(record_id="RR-000000102"),
        ),
        ("event_type", "VERSION_RECORDED"),
        ("target_ref", "OBJ-000002"),
        ("actor_ref", "ACTOR-000002"),
        ("source_ref", "SYSTEM-000002"),
        ("scope_ref", "SCOPE-000002"),
        ("branch_ref", "BRANCH-000002"),
        (
            "occurred_at",
            datetime(2026, 7, 18, 11, 30, tzinfo=timezone.utc),
        ),
        (
            "effective_at",
            datetime(2026, 7, 18, 11, 45, tzinfo=timezone.utc),
        ),
    ],
)
def test_runtime_event_record_equality_is_full_structural_equality(
    field_name,
    different_value,
):
    event_a = make_event()
    event_b = make_event(**{field_name: different_value})

    assert event_a != event_b


def test_same_header_with_different_event_type_is_not_equal():
    header = make_event_header()

    event_a = make_event(
        header=header,
        event_type="OBJECT_CREATED",
    )
    event_b = make_event(
        header=header,
        event_type="VERSION_RECORDED",
    )

    assert event_a != event_b


def test_same_header_and_event_type_with_different_context_is_not_equal():
    header = make_event_header()

    event_a = make_event(
        header=header,
        target_ref="OBJ-000001",
    )
    event_b = make_event(
        header=header,
        target_ref="OBJ-000002",
    )

    assert event_a != event_b


def test_equivalent_temporal_instants_follow_python_datetime_equality():
    utc_value = datetime(
        2026,
        7,
        17,
        12,
        0,
        tzinfo=timezone.utc,
    )
    offset_value = datetime(
        2026,
        7,
        17,
        5,
        0,
        tzinfo=timezone(timedelta(hours=-7)),
    )

    event_a = make_event(occurred_at=utc_value)
    event_b = make_event(occurred_at=offset_value)

    assert utc_value == offset_value
    assert event_a == event_b


def test_equal_runtime_event_records_have_equal_hashes():
    event_a = make_event()
    event_b = make_event()

    assert hash(event_a) == hash(event_b)


def test_structurally_different_runtime_event_records_can_coexist_in_a_set():
    event_a = make_event()
    event_b = make_event(
        header=make_event_header(record_id="RR-000000102"),
    )

    assert len({event_a, event_b}) == 2


def test_hashing_does_not_change_runtime_event_record():
    event = make_event(
        target_ref=VALID_TARGET_REF,
        actor_ref=VALID_ACTOR_REF,
        source_ref=VALID_SOURCE_REF,
        scope_ref=VALID_SCOPE_REF,
        branch_ref=VALID_BRANCH_REF,
        occurred_at=VALID_OCCURRED_AT,
        effective_at=VALID_EFFECTIVE_AT,
    )

    before = (
        event.header,
        event.event_type,
        event.target_ref,
        event.actor_ref,
        event.source_ref,
        event.scope_ref,
        event.branch_ref,
        event.occurred_at,
        event.effective_at,
    )

    hash(event)

    after = (
        event.header,
        event.event_type,
        event.target_ref,
        event.actor_ref,
        event.source_ref,
        event.scope_ref,
        event.branch_ref,
        event.occurred_at,
        event.effective_at,
    )

    assert after == before


def test_runtime_event_records_do_not_support_ordering():
    event_a = make_event()
    event_b = make_event(
        header=make_event_header(record_id="RR-000000102"),
    )

    with pytest.raises(TypeError):
        _ = event_a < event_b


def test_runtime_event_record_exposes_no_serialization_methods():
    event = make_event()

    assert not hasattr(event, "to_dict")
    assert not hasattr(event, "from_dict")
    assert not hasattr(event, "to_json")
    assert not hasattr(event, "from_json")


def test_runtime_event_record_does_not_accept_application_event_dictionary_as_header():
    application_event = {
        "timestamp": "2026-07-01T12:55:23",
        "category": "Build Center",
        "action": "Faculty dossier generated",
        "status": "SUCCESS",
        "details": {},
    }

    with pytest.raises(TypeError, match="header"):
        RuntimeEventRecord(
            header=application_event,
            event_type=VALID_EVENT_TYPE,
        )


def test_importing_runtime_event_record_does_not_import_event_engine():
    event_engine_was_loaded = "src.services.event_engine" in sys.modules

    module = importlib.import_module("models.runtime_event_record")

    assert hasattr(module, "RuntimeEventRecord")

    if not event_engine_was_loaded:
        assert "src.services.event_engine" not in sys.modules


def test_importing_runtime_event_record_does_not_import_streamlit():
    streamlit_was_loaded = "streamlit" in sys.modules

    module = importlib.import_module("models.runtime_event_record")

    assert hasattr(module, "RuntimeEventRecord")

    if not streamlit_was_loaded:
        assert "streamlit" not in sys.modules


def test_runtime_event_record_module_can_be_imported_directly():
    from models.runtime_event_record import (
        RuntimeEventRecord as ImportedRecord,
    )

    assert ImportedRecord is RuntimeEventRecord


def test_runtime_event_record_does_not_modify_composed_header():
    header = make_event_header(
        provenance_ref="PRV-000000001",
        external_id="external-event-101",
    )

    before = (
        header.record_id,
        header.record_category,
        header.recorded_at,
        header.schema_version,
        header.provenance_ref,
        header.external_id,
    )

    make_event(
        header=header,
        target_ref=VALID_TARGET_REF,
        actor_ref=VALID_ACTOR_REF,
        source_ref=VALID_SOURCE_REF,
        scope_ref=VALID_SCOPE_REF,
        branch_ref=VALID_BRANCH_REF,
        occurred_at=VALID_OCCURRED_AT,
        effective_at=VALID_EFFECTIVE_AT,
    )

    after = (
        header.record_id,
        header.record_category,
        header.recorded_at,
        header.schema_version,
        header.provenance_ref,
        header.external_id,
    )

    assert after == before


def test_runtime_event_record_does_not_restrict_event_type_to_current_examples():
    event = make_event(
        event_type="CUSTOM_RUNTIME_OCCURRENCE",
    )

    assert event.event_type == "CUSTOM_RUNTIME_OCCURRENCE"