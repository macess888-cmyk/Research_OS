from dataclasses import FrozenInstanceError
from datetime import datetime, timedelta, timezone

import pytest

from models.hold_record import HoldRecord
from models.progression_assertion_record import ProgressionAssertionRecord
from models.runtime_event_record import RuntimeEventRecord
from models.runtime_object_version_record import RuntimeObjectVersionRecord
from models.runtime_record_identity import RuntimeRecordHeader
from models.runtime_record_inspection_report import (
    RuntimeRecordInspectionReport,
)
from services.runtime_record_inspector import RuntimeRecordInspector
from services.runtime_record_registry import RuntimeRecordRegistry
from src.services.inspectable import Inspectable


RECORDED_AT = datetime(
    2026,
    7,
    17,
    12,
    0,
    tzinfo=timezone.utc,
)

OCCURRED_AT = datetime(
    2026,
    7,
    17,
    11,
    0,
    tzinfo=timezone.utc,
)

EFFECTIVE_AT = datetime(
    2026,
    7,
    17,
    13,
    0,
    tzinfo=timezone.utc,
)

REVIEW_AT = datetime(
    2026,
    7,
    18,
    12,
    0,
    tzinfo=timezone.utc,
)

EXPIRES_AT = datetime(
    2026,
    7,
    19,
    12,
    0,
    tzinfo=timezone.utc,
)


EVENT_DECLARED_FIELDS = (
    ("event_type", "OBJECT_CREATED"),
    ("target_ref", "OBJ-001"),
    ("actor_ref", "ACT-001"),
    ("source_ref", "SRC-001"),
    ("scope_ref", "SCP-001"),
    ("branch_ref", "BRN-001"),
    ("occurred_at", OCCURRED_AT),
    ("effective_at", EFFECTIVE_AT),
)

VERSION_DECLARED_FIELDS = (
    ("object_ref", "OBJ-001"),
    ("representation_ref", "REP-001"),
    ("version_label", "v1"),
    ("predecessor_ref", "RR-000000001"),
    ("branch_ref", "BRN-001"),
    ("scope_ref", "SCP-001"),
)

PROGRESSION_DECLARED_FIELDS = (
    ("target_ref", "OBJ-001"),
    ("asserted_condition", "ACTIVE"),
    ("scope_ref", "SCP-001"),
    ("target_version_ref", "RR-000000002"),
    ("prior_condition", "PENDING"),
    ("branch_ref", "BRN-001"),
    ("context_ref", "CTX-001"),
    ("asserted_at", OCCURRED_AT),
    ("effective_at", EFFECTIVE_AT),
    ("actor_ref", "ACT-001"),
    ("source_ref", "SRC-001"),
    ("basis_ref", "BAS-001"),
)

HOLD_DECLARED_FIELDS = (
    ("target_ref", "OBJ-001"),
    ("blocked_consequence_ref", "CON-001"),
    ("scope_ref", "SCP-001"),
    ("reason_ref", "RSN-001"),
    ("resolution_condition_ref", "RSC-001"),
    ("target_version_ref", "RR-000000002"),
    ("branch_ref", "BRN-001"),
    ("context_ref", "CTX-001"),
    ("trigger_ref", "TRG-001"),
    ("basis_ref", "BAS-001"),
    ("owner_ref", "OWN-001"),
    ("placed_by_ref", "ACT-001"),
    ("placement_authority_ref", "AUT-001"),
    ("release_authority_ref", "AUT-002"),
    ("placed_at", OCCURRED_AT),
    ("effective_at", EFFECTIVE_AT),
    ("review_at", REVIEW_AT),
    ("expires_at", EXPIRES_AT),
)


def make_header(
    record_id: str,
    record_category: str,
    *,
    recorded_at: datetime = RECORDED_AT,
    schema_version: str = "1.0",
    provenance_ref: str | None = "PRV-000000001",
    external_id: str | None = "external-001",
) -> RuntimeRecordHeader:
    return RuntimeRecordHeader(
        record_id=record_id,
        record_category=record_category,
        recorded_at=recorded_at,
        schema_version=schema_version,
        provenance_ref=provenance_ref,
        external_id=external_id,
    )


def make_event_record(
    record_id: str = "RR-000000001",
    *,
    all_optional_none: bool = False,
) -> RuntimeEventRecord:
    if all_optional_none:
        return RuntimeEventRecord(
            header=make_header(
                record_id,
                "EVENT",
                provenance_ref=None,
                external_id=None,
            ),
            event_type="OBJECT_CREATED",
        )

    return RuntimeEventRecord(
        header=make_header(record_id, "EVENT"),
        event_type="OBJECT_CREATED",
        target_ref="OBJ-001",
        actor_ref="ACT-001",
        source_ref="SRC-001",
        scope_ref="SCP-001",
        branch_ref="BRN-001",
        occurred_at=OCCURRED_AT,
        effective_at=EFFECTIVE_AT,
    )


def make_version_record(
    record_id: str = "RR-000000002",
    *,
    all_optional_none: bool = False,
) -> RuntimeObjectVersionRecord:
    if all_optional_none:
        return RuntimeObjectVersionRecord(
            header=make_header(
                record_id,
                "VERSION",
                provenance_ref=None,
                external_id=None,
            ),
            object_ref="OBJ-001",
            representation_ref="REP-001",
        )

    return RuntimeObjectVersionRecord(
        header=make_header(record_id, "VERSION"),
        object_ref="OBJ-001",
        representation_ref="REP-001",
        version_label="v1",
        predecessor_ref="RR-000000001",
        branch_ref="BRN-001",
        scope_ref="SCP-001",
    )


def make_progression_record(
    record_id: str = "RR-000000003",
    *,
    all_optional_none: bool = False,
) -> ProgressionAssertionRecord:
    if all_optional_none:
        return ProgressionAssertionRecord(
            header=make_header(
                record_id,
                "PROGRESSION_ASSERTION",
                provenance_ref=None,
                external_id=None,
            ),
            target_ref="OBJ-001",
            asserted_condition="ACTIVE",
            scope_ref="SCP-001",
        )

    return ProgressionAssertionRecord(
        header=make_header(
            record_id,
            "PROGRESSION_ASSERTION",
        ),
        target_ref="OBJ-001",
        asserted_condition="ACTIVE",
        scope_ref="SCP-001",
        target_version_ref="RR-000000002",
        prior_condition="PENDING",
        branch_ref="BRN-001",
        context_ref="CTX-001",
        asserted_at=OCCURRED_AT,
        effective_at=EFFECTIVE_AT,
        actor_ref="ACT-001",
        source_ref="SRC-001",
        basis_ref="BAS-001",
    )


def make_hold_record(
    record_id: str = "RR-000000004",
    *,
    all_optional_none: bool = False,
) -> HoldRecord:
    if all_optional_none:
        return HoldRecord(
            header=make_header(
                record_id,
                "HOLD",
                provenance_ref=None,
                external_id=None,
            ),
            target_ref="OBJ-001",
            blocked_consequence_ref="CON-001",
            scope_ref="SCP-001",
            reason_ref="RSN-001",
            resolution_condition_ref="RSC-001",
        )

    return HoldRecord(
        header=make_header(record_id, "HOLD"),
        target_ref="OBJ-001",
        blocked_consequence_ref="CON-001",
        scope_ref="SCP-001",
        reason_ref="RSN-001",
        resolution_condition_ref="RSC-001",
        target_version_ref="RR-000000002",
        branch_ref="BRN-001",
        context_ref="CTX-001",
        trigger_ref="TRG-001",
        basis_ref="BAS-001",
        owner_ref="OWN-001",
        placed_by_ref="ACT-001",
        placement_authority_ref="AUT-001",
        release_authority_ref="AUT-002",
        placed_at=OCCURRED_AT,
        effective_at=EFFECTIVE_AT,
        review_at=REVIEW_AT,
        expires_at=EXPIRES_AT,
    )


def make_valid_event_report(
    **overrides,
) -> RuntimeRecordInspectionReport:
    values = {
        "record_id": "RR-000000001",
        "record_type": "RuntimeEventRecord",
        "record_category": "EVENT",
        "append_position": 0,
        "recorded_at": RECORDED_AT,
        "schema_version": "1.0",
        "provenance_ref": "PRV-000000001",
        "external_id": "external-001",
        "declared_fields": EVENT_DECLARED_FIELDS,
    }
    values.update(overrides)
    return RuntimeRecordInspectionReport(**values)


def inspect_one(record):
    registry = RuntimeRecordRegistry()
    registry.register(record)
    inspector = RuntimeRecordInspector(registry)
    return registry, inspector, inspector.inspect_record(
        record.header.record_id
    )


def replace_declared_value(
    fields: tuple,
    field_name: str,
    value,
) -> tuple:
    return tuple(
        (name, value if name == field_name else current)
        for name, current in fields
    )


def remove_declared_field(
    fields: tuple,
    field_name: str,
) -> tuple:
    return tuple(
        item
        for item in fields
        if item[0] != field_name
    )


def add_declared_field(
    fields: tuple,
    field_name: str = "extra",
    value="value",
) -> tuple:
    return fields + ((field_name, value),)


# ---------------------------------------------------------------------------
# Report construction, immutability, equality, and exact field surface
# ---------------------------------------------------------------------------


def test_report_constructs_with_exact_frozen_field_order():
    report = make_valid_event_report()

    assert tuple(report.__dataclass_fields__) == (
        "record_id",
        "record_type",
        "record_category",
        "append_position",
        "recorded_at",
        "schema_version",
        "provenance_ref",
        "external_id",
        "declared_fields",
    )


def test_report_preserves_all_exact_values():
    report = make_valid_event_report()

    assert report.record_id == "RR-000000001"
    assert report.record_type == "RuntimeEventRecord"
    assert report.record_category == "EVENT"
    assert report.append_position == 0
    assert report.recorded_at is RECORDED_AT
    assert report.schema_version == "1.0"
    assert report.provenance_ref == "PRV-000000001"
    assert report.external_id == "external-001"
    assert report.declared_fields == EVENT_DECLARED_FIELDS


def test_report_accepts_none_provenance_ref():
    assert make_valid_event_report(
        provenance_ref=None
    ).provenance_ref is None


def test_report_accepts_none_external_id():
    assert make_valid_event_report(
        external_id=None
    ).external_id is None


def test_report_accepts_zero_append_position():
    assert make_valid_event_report(
        append_position=0
    ).append_position == 0


def test_report_accepts_timezone_aware_recorded_at():
    assert make_valid_event_report().recorded_at is RECORDED_AT


def test_report_is_hashable():
    assert isinstance(hash(make_valid_event_report()), int)


@pytest.mark.parametrize(
    "field_name,new_value",
    [
        ("record_id", "RR-000000999"),
        ("append_position", 99),
        ("declared_fields", ()),
    ],
)
def test_report_is_frozen(field_name, new_value):
    report = make_valid_event_report()

    with pytest.raises(FrozenInstanceError):
        setattr(report, field_name, new_value)


def test_declared_fields_outer_container_is_tuple():
    assert type(make_valid_event_report().declared_fields) is tuple


def test_each_declared_field_entry_is_tuple():
    report = make_valid_event_report()

    assert all(
        type(entry) is tuple
        for entry in report.declared_fields
    )


def test_equal_reports_are_equal():
    assert make_valid_event_report() == make_valid_event_report()


@pytest.mark.parametrize(
    "override",
    [
        {"record_id": "RR-000000002"},
        {
            "record_type": "HoldRecord",
            "record_category": "HOLD",
            "declared_fields": HOLD_DECLARED_FIELDS,
        },
        {
            "record_type": "RuntimeObjectVersionRecord",
            "record_category": "VERSION",
            "declared_fields": VERSION_DECLARED_FIELDS,
        },
        {"append_position": 1},
        {
            "recorded_at": datetime(
                2026,
                7,
                17,
                12,
                1,
                tzinfo=timezone.utc,
            )
        },
        {"schema_version": "2.0"},
        {"provenance_ref": "PRV-000000002"},
        {"external_id": "external-002"},
        {
            "declared_fields": replace_declared_value(
                EVENT_DECLARED_FIELDS,
                "target_ref",
                "OBJ-002",
            )
        },
    ],
)
def test_reports_with_different_fields_are_not_equal(override):
    assert make_valid_event_report() != make_valid_event_report(
        **override
    )


def test_report_exposes_only_frozen_fields():
    report = make_valid_event_report()

    assert set(report.__dataclass_fields__) == {
        "record_id",
        "record_type",
        "record_category",
        "append_position",
        "recorded_at",
        "schema_version",
        "provenance_ref",
        "external_id",
        "declared_fields",
    }


# ---------------------------------------------------------------------------
# Report identity, type, category, append-position, and header validation
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "value",
    [None, 1, 1.0, True, object()],
)
def test_report_rejects_non_string_record_id(value):
    with pytest.raises(TypeError):
        make_valid_event_report(record_id=value)


@pytest.mark.parametrize(
    "value",
    [
        "",
        " ",
        "rr-000000001",
        "RR-1",
        "EVENT-000000001",
        "RR-000000000",
        "RR-0000000001",
        "RR-00000000A",
        " RR-000000001",
        "RR-000000001 ",
    ],
)
def test_report_rejects_invalid_record_id(value):
    with pytest.raises(ValueError):
        make_valid_event_report(record_id=value)


@pytest.mark.parametrize(
    "record_type,record_category,declared_fields",
    [
        (
            "RuntimeEventRecord",
            "EVENT",
            EVENT_DECLARED_FIELDS,
        ),
        (
            "RuntimeObjectVersionRecord",
            "VERSION",
            VERSION_DECLARED_FIELDS,
        ),
        (
            "ProgressionAssertionRecord",
            "PROGRESSION_ASSERTION",
            PROGRESSION_DECLARED_FIELDS,
        ),
        (
            "HoldRecord",
            "HOLD",
            HOLD_DECLARED_FIELDS,
        ),
    ],
)
def test_report_accepts_supported_record_types(
    record_type,
    record_category,
    declared_fields,
):
    report = make_valid_event_report(
        record_type=record_type,
        record_category=record_category,
        declared_fields=declared_fields,
    )

    assert report.record_type == record_type


@pytest.mark.parametrize(
    "value",
    [None, 1, 1.0, True, object()],
)
def test_report_rejects_non_string_record_type(value):
    with pytest.raises(TypeError):
        make_valid_event_report(record_type=value)


@pytest.mark.parametrize(
    "value",
    [
        "",
        " ",
        "runtimeeventrecord",
        "Event",
        "EVENT",
        "RuntimeRecord",
        "hold_record",
    ],
)
def test_report_rejects_unsupported_record_type(value):
    with pytest.raises(ValueError):
        make_valid_event_report(record_type=value)


@pytest.mark.parametrize(
    "value",
    [None, 1, 1.0, True, object()],
)
def test_report_rejects_non_string_record_category(value):
    with pytest.raises(TypeError):
        make_valid_event_report(record_category=value)


@pytest.mark.parametrize(
    "value",
    [
        "",
        " ",
        "event",
        "UNKNOWN",
        "RuntimeEventRecord",
    ],
)
def test_report_rejects_unsupported_record_category(value):
    with pytest.raises(ValueError):
        make_valid_event_report(record_category=value)


@pytest.mark.parametrize(
    "record_type,record_category,declared_fields",
    [
        (
            "RuntimeEventRecord",
            "HOLD",
            EVENT_DECLARED_FIELDS,
        ),
        (
            "RuntimeObjectVersionRecord",
            "EVENT",
            VERSION_DECLARED_FIELDS,
        ),
        (
            "ProgressionAssertionRecord",
            "VERSION",
            PROGRESSION_DECLARED_FIELDS,
        ),
        (
            "HoldRecord",
            "PROGRESSION_ASSERTION",
            HOLD_DECLARED_FIELDS,
        ),
    ],
)
def test_report_rejects_type_category_mismatch(
    record_type,
    record_category,
    declared_fields,
):
    with pytest.raises(ValueError):
        make_valid_event_report(
            record_type=record_type,
            record_category=record_category,
            declared_fields=declared_fields,
        )


@pytest.mark.parametrize(
    "value",
    [True, False],
)
def test_report_rejects_bool_append_position(value):
    with pytest.raises(TypeError):
        make_valid_event_report(append_position=value)


@pytest.mark.parametrize(
    "value",
    [None, 1.0, "1", object()],
)
def test_report_rejects_non_integer_append_position(value):
    with pytest.raises(TypeError):
        make_valid_event_report(append_position=value)


def test_report_rejects_negative_append_position():
    with pytest.raises(ValueError):
        make_valid_event_report(append_position=-1)


def test_report_accepts_positive_append_position():
    assert make_valid_event_report(
        append_position=12
    ).append_position == 12


@pytest.mark.parametrize(
    "value",
    [None, "2026-07-17", 1, object()],
)
def test_report_rejects_non_datetime_recorded_at(value):
    with pytest.raises(TypeError):
        make_valid_event_report(recorded_at=value)


def test_report_rejects_naive_recorded_at():
    with pytest.raises(ValueError):
        make_valid_event_report(
            recorded_at=datetime(2026, 7, 17, 12, 0)
        )


def test_report_accepts_non_utc_timezone_aware_recorded_at():
    value = datetime(
        2026,
        7,
        17,
        12,
        0,
        tzinfo=timezone(timedelta(hours=-7)),
    )

    assert make_valid_event_report(
        recorded_at=value
    ).recorded_at is value


@pytest.mark.parametrize(
    "value",
    [None, 1, 1.0, True, object()],
)
def test_report_rejects_non_string_schema_version(value):
    with pytest.raises(TypeError):
        make_valid_event_report(schema_version=value)


@pytest.mark.parametrize(
    "value",
    [
        "",
        " ",
        "0.1",
        "1",
        "1.0.0",
        "v1.0",
        "-1.0",
        " 1.0",
        "1.0 ",
    ],
)
def test_report_rejects_invalid_schema_version(value):
    with pytest.raises(ValueError):
        make_valid_event_report(schema_version=value)


@pytest.mark.parametrize(
    "value",
    ["1.0", "10.4", "999.0"],
)
def test_report_accepts_valid_schema_version(value):
    assert make_valid_event_report(
        schema_version=value
    ).schema_version == value


@pytest.mark.parametrize(
    "value",
    [1, 1.0, True, object()],
)
def test_report_rejects_non_string_provenance_ref(value):
    with pytest.raises(TypeError):
        make_valid_event_report(provenance_ref=value)


@pytest.mark.parametrize(
    "value",
    [
        "",
        " ",
        "ABC-000000001",
        "PRV-1",
        "PRV-000000000",
        "prv-000000001",
        " PRV-000000001",
        "PRV-000000001 ",
    ],
)
def test_report_rejects_invalid_provenance_ref(value):
    with pytest.raises(ValueError):
        make_valid_event_report(provenance_ref=value)


def test_report_accepts_valid_provenance_ref():
    assert make_valid_event_report(
        provenance_ref="PRV-999999999"
    ).provenance_ref == "PRV-999999999"


@pytest.mark.parametrize(
    "value",
    [1, 1.0, True, object()],
)
def test_report_rejects_non_string_external_id(value):
    with pytest.raises(TypeError):
        make_valid_event_report(external_id=value)


@pytest.mark.parametrize(
    "value",
    ["", " ", "\t"],
)
def test_report_rejects_empty_external_id(value):
    with pytest.raises(ValueError):
        make_valid_event_report(external_id=value)


def test_report_preserves_external_id_exactly():
    value = "  external-preserved  "
    report = make_valid_event_report(external_id=value)

    assert report.external_id == value


# ---------------------------------------------------------------------------
# Declared-field container, name, ordering, and value validation
# ---------------------------------------------------------------------------


class TupleSubclass(tuple):
    pass


@pytest.mark.parametrize(
    "value",
    [
        list(EVENT_DECLARED_FIELDS),
        dict(EVENT_DECLARED_FIELDS),
        set(EVENT_DECLARED_FIELDS),
        (item for item in EVENT_DECLARED_FIELDS),
        None,
        "declared-fields",
        TupleSubclass(EVENT_DECLARED_FIELDS),
    ],
)
def test_report_rejects_non_exact_tuple_declared_fields(value):
    with pytest.raises(TypeError):
        make_valid_event_report(declared_fields=value)


@pytest.mark.parametrize(
    "entry",
    [
        ["event_type", "OBJECT_CREATED"],
        {"event_type": "OBJECT_CREATED"},
        TupleSubclass(("event_type", "OBJECT_CREATED")),
    ],
)
def test_report_rejects_non_exact_tuple_declared_field_entry(
    entry,
):
    fields = (entry,) + EVENT_DECLARED_FIELDS[1:]

    with pytest.raises(TypeError):
        make_valid_event_report(declared_fields=fields)


@pytest.mark.parametrize(
    "entry",
    [
        (),
        ("event_type",),
        ("event_type", "OBJECT_CREATED", "extra"),
    ],
)
def test_report_rejects_wrong_length_declared_field_entry(entry):
    fields = (entry,) + EVENT_DECLARED_FIELDS[1:]

    with pytest.raises(ValueError):
        make_valid_event_report(declared_fields=fields)


@pytest.mark.parametrize(
    "name,exception",
    [
        (None, TypeError),
        (1, TypeError),
        ("", ValueError),
        (" ", ValueError),
    ],
)
def test_report_rejects_invalid_declared_field_name(
    name,
    exception,
):
    fields = ((name, "OBJECT_CREATED"),) + (
        EVENT_DECLARED_FIELDS[1:]
    )

    with pytest.raises(exception):
        make_valid_event_report(declared_fields=fields)


def test_report_rejects_duplicate_declared_field_names():
    fields = (
        ("event_type", "OBJECT_CREATED"),
        ("event_type", "OBJ-001"),
    ) + EVENT_DECLARED_FIELDS[2:]

    with pytest.raises(ValueError):
        make_valid_event_report(declared_fields=fields)


def test_report_rejects_header_declared_field():
    fields = (
        ("header", "not-allowed"),
    ) + EVENT_DECLARED_FIELDS[1:]

    with pytest.raises(ValueError):
        make_valid_event_report(declared_fields=fields)


def test_report_rejects_unexpected_declared_field_name():
    fields = (
        ("unexpected", "OBJECT_CREATED"),
    ) + EVENT_DECLARED_FIELDS[1:]

    with pytest.raises(ValueError):
        make_valid_event_report(declared_fields=fields)


def test_report_rejects_missing_declared_field():
    fields = remove_declared_field(
        EVENT_DECLARED_FIELDS,
        "effective_at",
    )

    with pytest.raises(ValueError):
        make_valid_event_report(declared_fields=fields)


def test_report_rejects_extra_declared_field():
    with pytest.raises(ValueError):
        make_valid_event_report(
            declared_fields=add_declared_field(
                EVENT_DECLARED_FIELDS
            )
        )


def test_report_rejects_reordered_declared_fields():
    fields = (
        EVENT_DECLARED_FIELDS[1],
        EVENT_DECLARED_FIELDS[0],
    ) + EVENT_DECLARED_FIELDS[2:]

    with pytest.raises(ValueError):
        make_valid_event_report(declared_fields=fields)


@pytest.mark.parametrize(
    "value,exception",
    [
        (None, TypeError),
        (1, TypeError),
        ("", ValueError),
        (" ", ValueError),
    ],
)
def test_event_report_rejects_invalid_event_type(
    value,
    exception,
):
    fields = replace_declared_value(
        EVENT_DECLARED_FIELDS,
        "event_type",
        value,
    )

    with pytest.raises(exception):
        make_valid_event_report(declared_fields=fields)


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
    "value,exception",
    [
        (1, TypeError),
        ("", ValueError),
        (" ", ValueError),
    ],
)
def test_event_report_rejects_invalid_optional_reference(
    field_name,
    value,
    exception,
):
    fields = replace_declared_value(
        EVENT_DECLARED_FIELDS,
        field_name,
        value,
    )

    with pytest.raises(exception):
        make_valid_event_report(declared_fields=fields)


@pytest.mark.parametrize(
    "field_name",
    ["occurred_at", "effective_at"],
)
def test_event_report_rejects_non_datetime_optional_time(
    field_name,
):
    fields = replace_declared_value(
        EVENT_DECLARED_FIELDS,
        field_name,
        "2026-07-17",
    )

    with pytest.raises(TypeError):
        make_valid_event_report(declared_fields=fields)


@pytest.mark.parametrize(
    "field_name",
    ["occurred_at", "effective_at"],
)
def test_event_report_rejects_naive_optional_time(field_name):
    fields = replace_declared_value(
        EVENT_DECLARED_FIELDS,
        field_name,
        datetime(2026, 7, 17, 12, 0),
    )

    with pytest.raises(ValueError):
        make_valid_event_report(declared_fields=fields)


def test_event_report_accepts_none_optional_fields():
    fields = (
        ("event_type", "OBJECT_CREATED"),
        ("target_ref", None),
        ("actor_ref", None),
        ("source_ref", None),
        ("scope_ref", None),
        ("branch_ref", None),
        ("occurred_at", None),
        ("effective_at", None),
    )

    assert make_valid_event_report(
        provenance_ref=None,
        external_id=None,
        declared_fields=fields,
    ).declared_fields == fields


@pytest.mark.parametrize(
    "field_name",
    ["object_ref", "representation_ref"],
)
@pytest.mark.parametrize(
    "value,exception",
    [
        (None, TypeError),
        (1, TypeError),
        ("", ValueError),
        (" ", ValueError),
    ],
)
def test_version_report_rejects_invalid_required_reference(
    field_name,
    value,
    exception,
):
    fields = replace_declared_value(
        VERSION_DECLARED_FIELDS,
        field_name,
        value,
    )

    with pytest.raises(exception):
        make_valid_event_report(
            record_type="RuntimeObjectVersionRecord",
            record_category="VERSION",
            declared_fields=fields,
        )


@pytest.mark.parametrize(
    "field_name",
    [
        "version_label",
        "predecessor_ref",
        "branch_ref",
        "scope_ref",
    ],
)
@pytest.mark.parametrize(
    "value,exception",
    [
        (1, TypeError),
        ("", ValueError),
        (" ", ValueError),
    ],
)
def test_version_report_rejects_invalid_optional_reference(
    field_name,
    value,
    exception,
):
    fields = replace_declared_value(
        VERSION_DECLARED_FIELDS,
        field_name,
        value,
    )

    with pytest.raises(exception):
        make_valid_event_report(
            record_type="RuntimeObjectVersionRecord",
            record_category="VERSION",
            declared_fields=fields,
        )


def test_version_report_accepts_none_optional_fields():
    fields = (
        ("object_ref", "OBJ-001"),
        ("representation_ref", "REP-001"),
        ("version_label", None),
        ("predecessor_ref", None),
        ("branch_ref", None),
        ("scope_ref", None),
    )

    report = make_valid_event_report(
        record_type="RuntimeObjectVersionRecord",
        record_category="VERSION",
        declared_fields=fields,
    )

    assert report.declared_fields == fields


@pytest.mark.parametrize(
    "field_name",
    ["target_ref", "scope_ref"],
)
@pytest.mark.parametrize(
    "value,exception",
    [
        (None, TypeError),
        (1, TypeError),
        ("", ValueError),
        (" ", ValueError),
    ],
)
def test_progression_report_rejects_invalid_required_reference(
    field_name,
    value,
    exception,
):
    fields = replace_declared_value(
        PROGRESSION_DECLARED_FIELDS,
        field_name,
        value,
    )

    with pytest.raises(exception):
        make_valid_event_report(
            record_type="ProgressionAssertionRecord",
            record_category="PROGRESSION_ASSERTION",
            declared_fields=fields,
        )


@pytest.mark.parametrize(
    "condition",
    [
        "PENDING",
        "ACTIVE",
        "HELD",
        "DORMANT",
        "ABANDONED",
    ],
)
def test_progression_report_accepts_supported_condition(
    condition,
):
    fields = replace_declared_value(
        PROGRESSION_DECLARED_FIELDS,
        "asserted_condition",
        condition,
    )

    report = make_valid_event_report(
        record_type="ProgressionAssertionRecord",
        record_category="PROGRESSION_ASSERTION",
        declared_fields=fields,
    )

    assert dict(report.declared_fields)[
        "asserted_condition"
    ] == condition


@pytest.mark.parametrize(
    "field_name,value,exception",
    [
        ("asserted_condition", None, TypeError),
        ("asserted_condition", "UNKNOWN", ValueError),
        ("prior_condition", "UNKNOWN", ValueError),
        ("prior_condition", 1, TypeError),
    ],
)
def test_progression_report_rejects_invalid_condition(
    field_name,
    value,
    exception,
):
    fields = replace_declared_value(
        PROGRESSION_DECLARED_FIELDS,
        field_name,
        value,
    )

    with pytest.raises(exception):
        make_valid_event_report(
            record_type="ProgressionAssertionRecord",
            record_category="PROGRESSION_ASSERTION",
            declared_fields=fields,
        )


@pytest.mark.parametrize(
    "field_name",
    ["asserted_at", "effective_at"],
)
@pytest.mark.parametrize(
    "value,exception",
    [
        ("2026-07-17", TypeError),
        (datetime(2026, 7, 17, 12, 0), ValueError),
    ],
)
def test_progression_report_rejects_invalid_optional_time(
    field_name,
    value,
    exception,
):
    fields = replace_declared_value(
        PROGRESSION_DECLARED_FIELDS,
        field_name,
        value,
    )

    with pytest.raises(exception):
        make_valid_event_report(
            record_type="ProgressionAssertionRecord",
            record_category="PROGRESSION_ASSERTION",
            declared_fields=fields,
        )


def test_progression_report_accepts_none_optional_fields():
    fields = (
        ("target_ref", "OBJ-001"),
        ("asserted_condition", "ACTIVE"),
        ("scope_ref", "SCP-001"),
        ("target_version_ref", None),
        ("prior_condition", None),
        ("branch_ref", None),
        ("context_ref", None),
        ("asserted_at", None),
        ("effective_at", None),
        ("actor_ref", None),
        ("source_ref", None),
        ("basis_ref", None),
    )

    report = make_valid_event_report(
        record_type="ProgressionAssertionRecord",
        record_category="PROGRESSION_ASSERTION",
        declared_fields=fields,
    )

    assert report.declared_fields == fields


@pytest.mark.parametrize(
    "field_name",
    [
        "target_ref",
        "blocked_consequence_ref",
        "scope_ref",
        "reason_ref",
        "resolution_condition_ref",
    ],
)
@pytest.mark.parametrize(
    "value,exception",
    [
        (None, TypeError),
        (1, TypeError),
        ("", ValueError),
        (" ", ValueError),
    ],
)
def test_hold_report_rejects_invalid_required_reference(
    field_name,
    value,
    exception,
):
    fields = replace_declared_value(
        HOLD_DECLARED_FIELDS,
        field_name,
        value,
    )

    with pytest.raises(exception):
        make_valid_event_report(
            record_type="HoldRecord",
            record_category="HOLD",
            declared_fields=fields,
        )


@pytest.mark.parametrize(
    "field_name",
    [
        "target_version_ref",
        "branch_ref",
        "context_ref",
        "trigger_ref",
        "basis_ref",
        "owner_ref",
        "placed_by_ref",
        "placement_authority_ref",
        "release_authority_ref",
    ],
)
@pytest.mark.parametrize(
    "value,exception",
    [
        (1, TypeError),
        ("", ValueError),
        (" ", ValueError),
    ],
)
def test_hold_report_rejects_invalid_optional_reference(
    field_name,
    value,
    exception,
):
    fields = replace_declared_value(
        HOLD_DECLARED_FIELDS,
        field_name,
        value,
    )

    with pytest.raises(exception):
        make_valid_event_report(
            record_type="HoldRecord",
            record_category="HOLD",
            declared_fields=fields,
        )


@pytest.mark.parametrize(
    "field_name",
    [
        "placed_at",
        "effective_at",
        "review_at",
        "expires_at",
    ],
)
@pytest.mark.parametrize(
    "value,exception",
    [
        ("2026-07-17", TypeError),
        (datetime(2026, 7, 17, 12, 0), ValueError),
    ],
)
def test_hold_report_rejects_invalid_optional_time(
    field_name,
    value,
    exception,
):
    fields = replace_declared_value(
        HOLD_DECLARED_FIELDS,
        field_name,
        value,
    )

    with pytest.raises(exception):
        make_valid_event_report(
            record_type="HoldRecord",
            record_category="HOLD",
            declared_fields=fields,
        )


def test_hold_report_accepts_none_optional_fields():
    fields = (
        ("target_ref", "OBJ-001"),
        ("blocked_consequence_ref", "CON-001"),
        ("scope_ref", "SCP-001"),
        ("reason_ref", "RSN-001"),
        ("resolution_condition_ref", "RSC-001"),
        ("target_version_ref", None),
        ("branch_ref", None),
        ("context_ref", None),
        ("trigger_ref", None),
        ("basis_ref", None),
        ("owner_ref", None),
        ("placed_by_ref", None),
        ("placement_authority_ref", None),
        ("release_authority_ref", None),
        ("placed_at", None),
        ("effective_at", None),
        ("review_at", None),
        ("expires_at", None),
    )

    report = make_valid_event_report(
        record_type="HoldRecord",
        record_category="HOLD",
        declared_fields=fields,
    )

    assert report.declared_fields == fields


# ---------------------------------------------------------------------------
# Inspector construction and empty-registry behavior
# ---------------------------------------------------------------------------


def test_inspector_constructs_with_exact_runtime_record_registry():
    registry = RuntimeRecordRegistry()

    assert isinstance(
        RuntimeRecordInspector(registry),
        RuntimeRecordInspector,
    )


def test_inspector_preserves_exact_registry_instance():
    registry = RuntimeRecordRegistry()
    inspector = RuntimeRecordInspector(registry)

    assert inspector._registry is registry


@pytest.mark.parametrize(
    "value",
    [None, object(), {}, []],
)
def test_inspector_rejects_invalid_registry(value):
    with pytest.raises(TypeError):
        RuntimeRecordInspector(value)


def test_inspector_rejects_duck_typed_registry():
    class DuckRegistry:
        def get(self, record_id):
            raise KeyError(record_id)

        def records(self):
            return ()

        def records_by_category(self, record_category):
            return ()

    with pytest.raises(TypeError):
        RuntimeRecordInspector(DuckRegistry())


def test_inspector_rejects_runtime_record_registry_subclass():
    class RegistrySubclass(RuntimeRecordRegistry):
        pass

    with pytest.raises(TypeError):
        RuntimeRecordInspector(RegistrySubclass())


def test_inspector_construction_does_not_snapshot_records():
    registry = RuntimeRecordRegistry()
    inspector = RuntimeRecordInspector(registry)
    record = make_event_record()

    registry.register(record)

    assert inspector.inspect_record(
        record.header.record_id
    ).record_id == record.header.record_id


def test_inspector_construction_does_not_mutate_registry():
    registry = RuntimeRecordRegistry()
    before = registry.records()

    RuntimeRecordInspector(registry)

    assert registry.records() == before
    assert registry.count() == 0


def test_inspect_records_returns_empty_tuple_for_empty_registry():
    inspector = RuntimeRecordInspector(
        RuntimeRecordRegistry()
    )

    result = inspector.inspect_records()

    assert type(result) is tuple
    assert result == ()


def test_inspect_records_by_category_returns_empty_tuple_for_empty_registry():
    inspector = RuntimeRecordInspector(
        RuntimeRecordRegistry()
    )

    result = inspector.inspect_records_by_category("EVENT")

    assert type(result) is tuple
    assert result == ()


def test_empty_registry_inspection_is_deterministic():
    inspector = RuntimeRecordInspector(
        RuntimeRecordRegistry()
    )

    assert inspector.inspect_records() == inspector.inspect_records()


# ---------------------------------------------------------------------------
# Exact record transformations
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "record_factory,expected_type,expected_category,expected_fields",
    [
        (
            make_event_record,
            "RuntimeEventRecord",
            "EVENT",
            EVENT_DECLARED_FIELDS,
        ),
        (
            make_version_record,
            "RuntimeObjectVersionRecord",
            "VERSION",
            VERSION_DECLARED_FIELDS,
        ),
        (
            make_progression_record,
            "ProgressionAssertionRecord",
            "PROGRESSION_ASSERTION",
            PROGRESSION_DECLARED_FIELDS,
        ),
        (
            make_hold_record,
            "HoldRecord",
            "HOLD",
            HOLD_DECLARED_FIELDS,
        ),
    ],
)
def test_inspect_record_returns_exact_report(
    record_factory,
    expected_type,
    expected_category,
    expected_fields,
):
    record = record_factory()
    registry, _, report = inspect_one(record)

    assert type(report) is RuntimeRecordInspectionReport
    assert report.record_id == record.header.record_id
    assert report.record_type == expected_type
    assert report.record_category == expected_category
    assert report.append_position == 0
    assert report.recorded_at is record.header.recorded_at
    assert report.schema_version == record.header.schema_version
    assert report.provenance_ref == record.header.provenance_ref
    assert report.external_id == record.header.external_id
    assert report.declared_fields == expected_fields
    assert registry.get(record.header.record_id) is record


@pytest.mark.parametrize(
    "record_factory",
    [
        make_event_record,
        make_version_record,
        make_progression_record,
        make_hold_record,
    ],
)
def test_inspection_preserves_source_record(record_factory):
    record = record_factory()
    registry = RuntimeRecordRegistry()
    registry.register(record)
    inspector = RuntimeRecordInspector(registry)
    before = registry.records()

    inspector.inspect_record(record.header.record_id)

    after = registry.records()
    assert after == before
    assert after[0] is record


@pytest.mark.parametrize(
    "record_factory,optional_names",
    [
        (
            make_event_record,
            {
                "target_ref",
                "actor_ref",
                "source_ref",
                "scope_ref",
                "branch_ref",
                "occurred_at",
                "effective_at",
            },
        ),
        (
            make_version_record,
            {
                "version_label",
                "predecessor_ref",
                "branch_ref",
                "scope_ref",
            },
        ),
        (
            make_progression_record,
            {
                "target_version_ref",
                "prior_condition",
                "branch_ref",
                "context_ref",
                "asserted_at",
                "effective_at",
                "actor_ref",
                "source_ref",
                "basis_ref",
            },
        ),
        (
            make_hold_record,
            {
                "target_version_ref",
                "branch_ref",
                "context_ref",
                "trigger_ref",
                "basis_ref",
                "owner_ref",
                "placed_by_ref",
                "placement_authority_ref",
                "release_authority_ref",
                "placed_at",
                "effective_at",
                "review_at",
                "expires_at",
            },
        ),
    ],
)
def test_report_preserves_all_none_optional_fields(
    record_factory,
    optional_names,
):
    record = record_factory(all_optional_none=True)
    _, _, report = inspect_one(record)
    payload = dict(report.declared_fields)

    assert report.provenance_ref is None
    assert report.external_id is None
    assert optional_names.issubset(payload)
    assert all(payload[name] is None for name in optional_names)


# ---------------------------------------------------------------------------
# Single lookup failures and exact behavior
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "value",
    [None, 1, 1.0, True, object()],
)
def test_inspect_record_rejects_non_string_record_id(value):
    inspector = RuntimeRecordInspector(
        RuntimeRecordRegistry()
    )

    with pytest.raises(TypeError):
        inspector.inspect_record(value)


def test_inspect_record_does_not_normalize_record_id():
    registry = RuntimeRecordRegistry()
    registry.register(make_event_record())
    inspector = RuntimeRecordInspector(registry)

    with pytest.raises(KeyError) as error:
        inspector.inspect_record(" RR-000000001")

    assert error.value.args == (" RR-000000001",)


def test_inspect_record_raises_key_error_for_missing_record():
    inspector = RuntimeRecordInspector(
        RuntimeRecordRegistry()
    )

    with pytest.raises(KeyError) as error:
        inspector.inspect_record("RR-000000999")

    assert error.value.args == ("RR-000000999",)


def test_missing_record_does_not_mutate_registry():
    registry = RuntimeRecordRegistry()
    inspector = RuntimeRecordInspector(registry)
    before = registry.records()

    with pytest.raises(KeyError):
        inspector.inspect_record("RR-000000999")

    assert registry.records() == before
    assert registry.count() == 0


# ---------------------------------------------------------------------------
# All-record inspection and global append order
# ---------------------------------------------------------------------------


def make_populated_registry() -> tuple:
    registry = RuntimeRecordRegistry()
    records = (
        make_event_record("RR-000000001"),
        make_hold_record("RR-000000004"),
        make_version_record("RR-000000002"),
        make_progression_record("RR-000000003"),
    )

    for record in records:
        registry.register(record)

    return registry, records


def test_inspect_records_returns_tuple():
    registry, _ = make_populated_registry()

    assert type(
        RuntimeRecordInspector(registry).inspect_records()
    ) is tuple


def test_inspect_records_returns_one_report_per_registered_record():
    registry, records = make_populated_registry()
    reports = RuntimeRecordInspector(registry).inspect_records()

    assert len(reports) == len(records)


def test_inspect_records_preserves_registry_append_order():
    registry, records = make_populated_registry()
    reports = RuntimeRecordInspector(registry).inspect_records()

    assert tuple(
        report.record_id for report in reports
    ) == tuple(
        record.header.record_id for record in records
    )


def test_inspect_records_assigns_global_zero_based_append_positions():
    registry, _ = make_populated_registry()
    reports = RuntimeRecordInspector(registry).inspect_records()

    assert tuple(
        report.append_position for report in reports
    ) == (0, 1, 2, 3)


def test_inspect_records_preserves_exact_record_types():
    registry, _ = make_populated_registry()
    reports = RuntimeRecordInspector(registry).inspect_records()

    assert tuple(
        report.record_type for report in reports
    ) == (
        "RuntimeEventRecord",
        "HoldRecord",
        "RuntimeObjectVersionRecord",
        "ProgressionAssertionRecord",
    )


def test_inspect_records_preserves_exact_categories():
    registry, _ = make_populated_registry()
    reports = RuntimeRecordInspector(registry).inspect_records()

    assert tuple(
        report.record_category for report in reports
    ) == (
        "EVENT",
        "HOLD",
        "VERSION",
        "PROGRESSION_ASSERTION",
    )


def test_inspect_records_returns_new_tuple_on_each_call():
    registry, _ = make_populated_registry()
    inspector = RuntimeRecordInspector(registry)

    first = inspector.inspect_records()
    second = inspector.inspect_records()

    assert first == second
    assert first is not second


def test_inspect_records_does_not_mutate_registry():
    registry, records = make_populated_registry()
    inspector = RuntimeRecordInspector(registry)
    before = registry.records()

    inspector.inspect_records()

    after = registry.records()
    assert after == before
    assert all(
        current is original
        for current, original in zip(after, records)
    )


# ---------------------------------------------------------------------------
# Category-filtered inspection and global positions
# ---------------------------------------------------------------------------


def test_inspect_records_by_category_returns_only_exact_category():
    registry = RuntimeRecordRegistry()
    records = (
        make_event_record("RR-000000001"),
        make_hold_record("RR-000000002"),
        make_event_record("RR-000000003"),
        make_version_record("RR-000000004"),
    )

    for record in records:
        registry.register(record)

    reports = RuntimeRecordInspector(
        registry
    ).inspect_records_by_category("EVENT")

    assert type(reports) is tuple
    assert tuple(
        report.record_id for report in reports
    ) == (
        "RR-000000001",
        "RR-000000003",
    )
    assert tuple(
        report.append_position for report in reports
    ) == (0, 2)


def test_filtered_inspection_returns_empty_tuple_for_no_matches():
    registry = RuntimeRecordRegistry()
    registry.register(make_event_record())

    assert RuntimeRecordInspector(
        registry
    ).inspect_records_by_category("HOLD") == ()


@pytest.mark.parametrize(
    "category",
    ["event", "UNKNOWN_CATEGORY"],
)
def test_filtered_inspection_does_not_normalize_or_expand_category(
    category,
):
    registry = RuntimeRecordRegistry()
    registry.register(make_event_record())

    assert RuntimeRecordInspector(
        registry
    ).inspect_records_by_category(category) == ()


@pytest.mark.parametrize(
    "value",
    [None, 1, 1.0, True, object()],
)
def test_filtered_inspection_rejects_non_string_category(value):
    inspector = RuntimeRecordInspector(
        RuntimeRecordRegistry()
    )

    with pytest.raises(TypeError):
        inspector.inspect_records_by_category(value)


@pytest.mark.parametrize(
    "value",
    ["", " ", "\t"],
)
def test_filtered_inspection_rejects_empty_category(value):
    inspector = RuntimeRecordInspector(
        RuntimeRecordRegistry()
    )

    with pytest.raises(ValueError):
        inspector.inspect_records_by_category(value)


def test_filtered_inspection_returns_new_tuple_on_each_call():
    registry = RuntimeRecordRegistry()
    registry.register(make_event_record())
    inspector = RuntimeRecordInspector(registry)

    first = inspector.inspect_records_by_category("EVENT")
    second = inspector.inspect_records_by_category("EVENT")

    assert first == second
    assert first is not second


def test_filtered_inspection_does_not_mutate_registry():
    registry, _ = make_populated_registry()
    inspector = RuntimeRecordInspector(registry)
    before = registry.records()

    inspector.inspect_records_by_category("EVENT")

    assert registry.records() == before


# ---------------------------------------------------------------------------
# Determinism, snapshot stability, and current registry visibility
# ---------------------------------------------------------------------------


def test_repeated_single_record_inspection_is_equal():
    registry = RuntimeRecordRegistry()
    registry.register(make_event_record())
    inspector = RuntimeRecordInspector(registry)

    assert inspector.inspect_record(
        "RR-000000001"
    ) == inspector.inspect_record(
        "RR-000000001"
    )


def test_repeated_category_inspection_is_equal():
    registry = RuntimeRecordRegistry()
    registry.register(make_event_record())
    inspector = RuntimeRecordInspector(registry)

    assert inspector.inspect_records_by_category(
        "EVENT"
    ) == inspector.inspect_records_by_category(
        "EVENT"
    )


def test_old_all_record_snapshot_remains_unchanged_after_registration():
    registry = RuntimeRecordRegistry()
    registry.register(make_event_record())
    inspector = RuntimeRecordInspector(registry)

    first = inspector.inspect_records()
    registry.register(make_hold_record())
    second = inspector.inspect_records()

    assert len(first) == 1
    assert len(second) == 2
    assert first[0].record_id == "RR-000000001"


def test_old_filtered_snapshot_remains_unchanged_after_registration():
    registry = RuntimeRecordRegistry()
    registry.register(make_event_record("RR-000000001"))
    inspector = RuntimeRecordInspector(registry)

    first = inspector.inspect_records_by_category("EVENT")
    registry.register(make_event_record("RR-000000002"))
    second = inspector.inspect_records_by_category("EVENT")

    assert tuple(
        report.record_id for report in first
    ) == ("RR-000000001",)
    assert tuple(
        report.record_id for report in second
    ) == (
        "RR-000000001",
        "RR-000000002",
    )


def test_old_filtered_snapshot_ignores_later_non_matching_registration():
    registry = RuntimeRecordRegistry()
    registry.register(make_event_record())
    inspector = RuntimeRecordInspector(registry)

    first = inspector.inspect_records_by_category("EVENT")
    registry.register(make_hold_record())
    second = inspector.inspect_records_by_category("EVENT")

    assert first == second
    assert first is not second


def test_inspector_sees_record_registered_after_construction():
    registry = RuntimeRecordRegistry()
    inspector = RuntimeRecordInspector(registry)

    registry.register(make_event_record())

    assert inspector.inspect_record(
        "RR-000000001"
    ).record_id == "RR-000000001"


def test_inspector_does_not_cache_empty_registry_state():
    registry = RuntimeRecordRegistry()
    inspector = RuntimeRecordInspector(registry)

    assert inspector.inspect_records() == ()

    registry.register(make_event_record())

    assert len(inspector.inspect_records()) == 1


# ---------------------------------------------------------------------------
# Exact-value preservation
# ---------------------------------------------------------------------------


def test_inspector_preserves_recorded_at_object_identity():
    record = make_event_record()
    _, _, report = inspect_one(record)

    assert report.recorded_at is record.header.recorded_at


def test_inspector_preserves_datetime_payload_objects():
    record = make_event_record()
    _, _, report = inspect_one(record)
    payload = dict(report.declared_fields)

    assert payload["occurred_at"] is record.occurred_at
    assert payload["effective_at"] is record.effective_at


def test_inspector_preserves_reference_strings_exactly():
    record = RuntimeEventRecord(
        header=make_header(
            "RR-000000001",
            "EVENT",
            external_id=" External Identifier ",
        ),
        event_type="OBJECT_CREATED",
        target_ref=" Target Reference ",
    )

    _, _, report = inspect_one(record)
    payload = dict(report.declared_fields)

    assert report.external_id == " External Identifier "
    assert payload["target_ref"] == " Target Reference "


def test_inspector_preserves_declared_field_order():
    _, _, report = inspect_one(make_hold_record())

    assert tuple(
        field_name
        for field_name, _ in report.declared_fields
    ) == tuple(
        field_name
        for field_name, _ in HOLD_DECLARED_FIELDS
    )


# ---------------------------------------------------------------------------
# Boundary absence and prohibited service surface
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "field_name",
    [
        "service",
        "status",
        "healthy",
        "valid",
        "validity",
        "admitted",
        "admission_status",
        "eligible",
        "accepted",
        "approved",
        "authorized",
        "authority_valid",
        "current",
        "canonical",
        "superseded",
        "active",
        "active_hold",
        "current_progression",
        "current_version",
        "effective_version",
        "authoritative",
        "complete_history",
        "history_status",
        "reconstruction_status",
        "evaluation",
        "evaluation_status",
        "confidence",
        "severity",
        "warning",
        "error",
        "persistent",
        "persisted",
        "durable",
        "file_path",
        "database_id",
        "inspection_id",
        "inspected_at",
        "registered",
        "record",
        "source_record",
        "original_record",
        "header",
        "registry",
    ],
)
def test_report_has_no_prohibited_field(field_name):
    assert not hasattr(make_valid_event_report(), field_name)


@pytest.mark.parametrize(
    "method_name",
    [
        "inspect",
        "register",
        "delete",
        "remove",
        "replace",
        "update",
        "upsert",
        "clear",
        "persist",
        "save",
        "load",
        "restore",
        "serialize",
        "publish",
        "evaluate",
        "validate",
        "admit",
        "authorize",
        "project",
        "reconstruct",
        "search",
        "summarize",
        "health",
        "status",
        "count_summary",
        "category_summary",
        "earliest_record",
        "latest_record",
    ],
)
def test_inspector_has_no_prohibited_method(method_name):
    inspector = RuntimeRecordInspector(
        RuntimeRecordRegistry()
    )

    assert not hasattr(inspector, method_name)


def test_inspector_does_not_inherit_platform_inspectable():
    inspector = RuntimeRecordInspector(
        RuntimeRecordRegistry()
    )

    assert not isinstance(inspector, Inspectable)


def test_inspection_report_has_no_to_dict_method():
    assert not hasattr(make_valid_event_report(), "to_dict")


def test_inspection_report_has_no_to_json_method():
    assert not hasattr(make_valid_event_report(), "to_json")


# ---------------------------------------------------------------------------
# No mutation, file creation, event creation, or serialization
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "inspection_action",
    [
        lambda inspector: inspector.inspect_record(
            "RR-000000001"
        ),
        lambda inspector: inspector.inspect_records(),
        lambda inspector: inspector.inspect_records_by_category(
            "EVENT"
        ),
    ],
)
def test_inspection_does_not_change_registry_count(
    inspection_action,
):
    registry = RuntimeRecordRegistry()
    record = make_event_record()
    registry.register(record)
    inspector = RuntimeRecordInspector(registry)
    before_count = registry.count()
    before_records = registry.records()

    inspection_action(inspector)

    assert registry.count() == before_count
    assert registry.records() == before_records
    assert registry.records()[0] is record


def test_report_construction_creates_no_files(
    tmp_path,
    monkeypatch,
):
    monkeypatch.chdir(tmp_path)
    before = tuple(tmp_path.iterdir())

    make_valid_event_report()

    assert tuple(tmp_path.iterdir()) == before


def test_inspector_construction_creates_no_files(
    tmp_path,
    monkeypatch,
):
    monkeypatch.chdir(tmp_path)
    before = tuple(tmp_path.iterdir())

    RuntimeRecordInspector(RuntimeRecordRegistry())

    assert tuple(tmp_path.iterdir()) == before


@pytest.mark.parametrize(
    "inspection_action",
    [
        lambda inspector: inspector.inspect_record(
            "RR-000000001"
        ),
        lambda inspector: inspector.inspect_records(),
        lambda inspector: inspector.inspect_records_by_category(
            "EVENT"
        ),
    ],
)
def test_inspection_creates_no_files(
    inspection_action,
    tmp_path,
    monkeypatch,
):
    monkeypatch.chdir(tmp_path)
    registry = RuntimeRecordRegistry()
    registry.register(make_event_record())
    inspector = RuntimeRecordInspector(registry)
    before = tuple(tmp_path.iterdir())

    inspection_action(inspector)

    assert tuple(tmp_path.iterdir()) == before


def test_inspection_creates_no_runtime_event_records():
    registry = RuntimeRecordRegistry()
    registry.register(make_event_record())
    inspector = RuntimeRecordInspector(registry)

    inspector.inspect_record("RR-000000001")

    assert registry.count() == 1
    assert registry.records()[0].header.record_id == (
        "RR-000000001"
    )


def test_inspection_does_not_register_inspection_reports():
    registry = RuntimeRecordRegistry()
    record = make_event_record()
    registry.register(record)
    inspector = RuntimeRecordInspector(registry)

    report = inspector.inspect_record("RR-000000001")

    assert registry.count() == 1
    assert registry.records() == (record,)
    assert report not in registry.records()


def test_inspection_creates_no_json_files(
    tmp_path,
    monkeypatch,
):
    monkeypatch.chdir(tmp_path)
    registry = RuntimeRecordRegistry()
    registry.register(make_event_record())

    RuntimeRecordInspector(registry).inspect_records()

    assert tuple(tmp_path.glob("*.json")) == ()