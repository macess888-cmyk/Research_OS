from dataclasses import FrozenInstanceError, fields, is_dataclass
from datetime import datetime, timedelta, timezone, tzinfo
import importlib
import sys

import pytest

from models.runtime_record_identity import RuntimeRecordHeader


VALID_RECORD_ID = "RR-000000001"
VALID_RECORD_CATEGORY = "EVENT"
VALID_RECORDED_AT = datetime(
    2026,
    7,
    17,
    12,
    0,
    0,
    tzinfo=timezone.utc,
)
VALID_SCHEMA_VERSION = "1.0"
VALID_PROVENANCE_REF = "PRV-000000001"
VALID_EXTERNAL_ID = "external-system-record-42"


def make_header(**overrides):
    values = {
        "record_id": VALID_RECORD_ID,
        "record_category": VALID_RECORD_CATEGORY,
        "recorded_at": VALID_RECORDED_AT,
        "schema_version": VALID_SCHEMA_VERSION,
        "provenance_ref": None,
        "external_id": None,
    }
    values.update(overrides)
    return RuntimeRecordHeader(**values)


class InvalidTimezone(tzinfo):
    def utcoffset(self, dt):
        return None

    def dst(self, dt):
        return None

    def tzname(self, dt):
        return "INVALID"


def test_runtime_record_header_is_a_dataclass():
    assert is_dataclass(RuntimeRecordHeader)


def test_runtime_record_header_declares_exact_field_order():
    assert [field.name for field in fields(RuntimeRecordHeader)] == [
        "record_id",
        "record_category",
        "recorded_at",
        "schema_version",
        "provenance_ref",
        "external_id",
    ]


def test_runtime_record_header_accepts_valid_required_fields():
    header = RuntimeRecordHeader(
        record_id=VALID_RECORD_ID,
        record_category=VALID_RECORD_CATEGORY,
        recorded_at=VALID_RECORDED_AT,
        schema_version=VALID_SCHEMA_VERSION,
    )

    assert header.record_id == VALID_RECORD_ID
    assert header.record_category == VALID_RECORD_CATEGORY
    assert header.recorded_at == VALID_RECORDED_AT
    assert header.schema_version == VALID_SCHEMA_VERSION
    assert header.provenance_ref is None
    assert header.external_id is None


def test_runtime_record_header_accepts_valid_optional_fields():
    header = make_header(
        provenance_ref=VALID_PROVENANCE_REF,
        external_id=VALID_EXTERNAL_ID,
    )

    assert header.provenance_ref == VALID_PROVENANCE_REF
    assert header.external_id == VALID_EXTERNAL_ID


def test_runtime_record_header_accepts_non_utc_timezone_aware_datetime():
    recorded_at = datetime(
        2026,
        7,
        17,
        12,
        0,
        tzinfo=timezone(timedelta(hours=-7)),
    )

    header = make_header(recorded_at=recorded_at)

    assert header.recorded_at == recorded_at
    assert header.recorded_at.utcoffset() == timedelta(hours=-7)


def test_runtime_record_header_preserves_external_id_exactly():
    external_id = " external-id "

    header = make_header(external_id=external_id)

    assert header.external_id == external_id


@pytest.mark.parametrize(
    "missing_field",
    [
        "record_id",
        "record_category",
        "recorded_at",
        "schema_version",
    ],
)
def test_runtime_record_header_requires_each_required_field(missing_field):
    values = {
        "record_id": VALID_RECORD_ID,
        "record_category": VALID_RECORD_CATEGORY,
        "recorded_at": VALID_RECORDED_AT,
        "schema_version": VALID_SCHEMA_VERSION,
    }
    values.pop(missing_field)

    with pytest.raises(TypeError):
        RuntimeRecordHeader(**values)


@pytest.mark.parametrize(
    "invalid_value",
    [
        None,
        1,
        1.0,
        True,
        b"RR-000000001",
        [],
        {},
    ],
)
def test_record_id_rejects_non_string_values(invalid_value):
    with pytest.raises(TypeError, match="record_id"):
        make_header(record_id=invalid_value)


@pytest.mark.parametrize(
    "valid_value",
    [
        "RR-000000001",
        "RR-000000042",
        "RR-999999999",
    ],
)
def test_record_id_accepts_valid_values(valid_value):
    assert make_header(record_id=valid_value).record_id == valid_value


@pytest.mark.parametrize(
    "invalid_value",
    [
        "",
        " ",
        "RR-000000000",
        "rr-000000001",
        "RR000000001",
        "RR-1",
        "RR-00000001",
        "RR-0000000001",
        "RR-00000001A",
        " RR-000000001",
        "RR-000000001 ",
        "EVT-000000001",
    ],
)
def test_record_id_rejects_invalid_values(invalid_value):
    with pytest.raises(ValueError, match="record_id"):
        make_header(record_id=invalid_value)


@pytest.mark.parametrize(
    "invalid_value",
    [
        None,
        1,
        1.0,
        True,
        b"EVENT",
        [],
        {},
    ],
)
def test_record_category_rejects_non_string_values(invalid_value):
    with pytest.raises(TypeError, match="record_category"):
        make_header(record_category=invalid_value)


@pytest.mark.parametrize(
    "valid_value",
    [
        "EVENT",
        "VERSION",
        "HOLD",
        "RE_ENTRY",
        "INSPECTION_RESULT",
        "CATEGORY2",
        "TYPE_2",
        "A",
        "A1",
    ],
)
def test_record_category_accepts_valid_values(valid_value):
    assert make_header(record_category=valid_value).record_category == valid_value


@pytest.mark.parametrize(
    "invalid_value",
    [
        "",
        " ",
        "event",
        "Event",
        "RE-ENTRY",
        "RE ENTRY",
        "_RE_ENTRY",
        "RE_ENTRY_",
        "RE__ENTRY",
        "2EVENT",
        " EVENT",
        "EVENT ",
    ],
)
def test_record_category_rejects_invalid_values(invalid_value):
    with pytest.raises(ValueError, match="record_category"):
        make_header(record_category=invalid_value)


@pytest.mark.parametrize(
    "invalid_value",
    [
        None,
        "2026-07-17T12:00:00Z",
        0,
        1.0,
        True,
        {},
        [],
    ],
)
def test_recorded_at_rejects_non_datetime_values(invalid_value):
    with pytest.raises(TypeError, match="recorded_at"):
        make_header(recorded_at=invalid_value)


def test_recorded_at_rejects_naive_datetime():
    with pytest.raises(ValueError, match="recorded_at"):
        make_header(recorded_at=datetime(2026, 7, 17, 12, 0, 0))


def test_recorded_at_rejects_timezone_with_no_utc_offset():
    invalid_datetime = datetime(
        2026,
        7,
        17,
        12,
        0,
        tzinfo=InvalidTimezone(),
    )

    with pytest.raises(ValueError, match="recorded_at"):
        make_header(recorded_at=invalid_datetime)


def test_recorded_at_preserves_supplied_timezone_and_offset():
    supplied_timezone = timezone(timedelta(hours=5, minutes=30))
    recorded_at = datetime(
        2026,
        7,
        17,
        12,
        0,
        tzinfo=supplied_timezone,
    )

    header = make_header(recorded_at=recorded_at)

    assert header.recorded_at == recorded_at
    assert header.recorded_at.tzinfo is supplied_timezone
    assert header.recorded_at.utcoffset() == timedelta(hours=5, minutes=30)


@pytest.mark.parametrize(
    "invalid_value",
    [
        None,
        1,
        1.0,
        True,
        b"1.0",
        [],
        {},
    ],
)
def test_schema_version_rejects_non_string_values(invalid_value):
    with pytest.raises(TypeError, match="schema_version"):
        make_header(schema_version=invalid_value)


@pytest.mark.parametrize(
    "valid_value",
    [
        "1.0",
        "1.1",
        "2.0",
        "12.4",
        "999.999",
    ],
)
def test_schema_version_accepts_valid_values(valid_value):
    assert make_header(schema_version=valid_value).schema_version == valid_value


@pytest.mark.parametrize(
    "invalid_value",
    [
        "",
        " ",
        "v1.0",
        "1",
        "1.0.0",
        "01.0",
        "0.1",
        "1.x",
        "1.",
        ".1",
        " 1.0",
        "1.0 ",
    ],
)
def test_schema_version_rejects_invalid_values(invalid_value):
    with pytest.raises(ValueError, match="schema_version"):
        make_header(schema_version=invalid_value)


@pytest.mark.parametrize(
    "invalid_value",
    [
        1,
        1.0,
        True,
        b"PRV-000000001",
        [],
        {},
    ],
)
def test_provenance_ref_rejects_non_string_non_none_values(invalid_value):
    with pytest.raises(TypeError, match="provenance_ref"):
        make_header(provenance_ref=invalid_value)


@pytest.mark.parametrize(
    "valid_value",
    [
        "PRV-000000001",
        "PRV-000000042",
        "PRV-999999999",
    ],
)
def test_provenance_ref_accepts_valid_values(valid_value):
    assert make_header(provenance_ref=valid_value).provenance_ref == valid_value


@pytest.mark.parametrize(
    "invalid_value",
    [
        "",
        " ",
        "PRV-000000000",
        "prv-000000001",
        "PRV000000001",
        "PRV-1",
        "PRV-00000001",
        "PRV-0000000001",
        "PRV-00000001A",
        " PRV-000000001",
        "PRV-000000001 ",
    ],
)
def test_provenance_ref_rejects_invalid_values(invalid_value):
    with pytest.raises(ValueError, match="provenance_ref"):
        make_header(provenance_ref=invalid_value)


@pytest.mark.parametrize(
    "invalid_value",
    [
        1,
        1.0,
        True,
        b"external",
        [],
        {},
    ],
)
def test_external_id_rejects_non_string_non_none_values(invalid_value):
    with pytest.raises(TypeError, match="external_id"):
        make_header(external_id=invalid_value)


@pytest.mark.parametrize(
    "valid_value",
    [
        "EXT-123",
        "doi:10.1000/example",
        "external/system/record/42",
        " abc",
        "abc ",
        " a ",
        "0",
    ],
)
def test_external_id_accepts_non_empty_values(valid_value):
    assert make_header(external_id=valid_value).external_id == valid_value


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
def test_external_id_rejects_empty_or_whitespace_only_values(invalid_value):
    with pytest.raises(ValueError, match="external_id"):
        make_header(external_id=invalid_value)


def test_record_id_type_failure_precedes_other_field_failures():
    with pytest.raises(TypeError, match="record_id"):
        RuntimeRecordHeader(
            record_id=1,
            record_category="invalid",
            recorded_at=datetime(2026, 7, 17, 12, 0),
            schema_version="invalid",
            provenance_ref=1,
            external_id=1,
        )


def test_record_id_value_failure_precedes_record_category_failure():
    with pytest.raises(ValueError, match="record_id"):
        RuntimeRecordHeader(
            record_id="invalid",
            record_category="invalid",
            recorded_at=VALID_RECORDED_AT,
            schema_version=VALID_SCHEMA_VERSION,
        )


def test_required_field_validation_precedes_optional_field_validation():
    with pytest.raises(ValueError, match="schema_version"):
        RuntimeRecordHeader(
            record_id=VALID_RECORD_ID,
            record_category=VALID_RECORD_CATEGORY,
            recorded_at=VALID_RECORDED_AT,
            schema_version="invalid",
            provenance_ref=1,
        )


@pytest.mark.parametrize(
    ("field_name", "new_value"),
    [
        ("record_id", "RR-000000002"),
        ("record_category", "VERSION"),
        (
            "recorded_at",
            datetime(2026, 7, 18, 12, 0, tzinfo=timezone.utc),
        ),
        ("schema_version", "2.0"),
        ("provenance_ref", "PRV-000000002"),
        ("external_id", "external-2"),
    ],
)
def test_runtime_record_header_is_frozen(field_name, new_value):
    header = make_header()

    with pytest.raises(FrozenInstanceError):
        setattr(header, field_name, new_value)


def test_identical_runtime_record_headers_compare_equal():
    assert make_header() == make_header()


@pytest.mark.parametrize(
    ("field_name", "different_value"),
    [
        ("record_id", "RR-000000002"),
        ("record_category", "VERSION"),
        (
            "recorded_at",
            datetime(2026, 7, 18, 12, 0, tzinfo=timezone.utc),
        ),
        ("schema_version", "2.0"),
        ("provenance_ref", "PRV-000000002"),
        ("external_id", "external-2"),
    ],
)
def test_runtime_record_header_equality_is_full_structural_equality(
    field_name,
    different_value,
):
    header_a = make_header()
    header_b = make_header(**{field_name: different_value})

    assert header_a != header_b


def test_same_record_id_with_different_structure_is_not_equal():
    header_a = make_header(record_category="EVENT")
    header_b = make_header(record_category="VERSION")

    assert header_a.record_id == header_b.record_id
    assert header_a != header_b


def test_equivalent_timezone_aware_instants_follow_python_datetime_equality():
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

    header_a = make_header(recorded_at=utc_value)
    header_b = make_header(recorded_at=offset_value)

    assert utc_value == offset_value
    assert header_a == header_b


def test_equal_runtime_record_headers_have_equal_hashes():
    header_a = make_header()
    header_b = make_header()

    assert hash(header_a) == hash(header_b)


def test_structurally_different_headers_can_coexist_in_a_set():
    header_a = make_header()
    header_b = make_header(record_id="RR-000000002")

    assert len({header_a, header_b}) == 2


def test_hashing_does_not_change_runtime_record_header():
    header = make_header(
        provenance_ref=VALID_PROVENANCE_REF,
        external_id=VALID_EXTERNAL_ID,
    )
    before = (
        header.record_id,
        header.record_category,
        header.recorded_at,
        header.schema_version,
        header.provenance_ref,
        header.external_id,
    )

    hash(header)

    after = (
        header.record_id,
        header.record_category,
        header.recorded_at,
        header.schema_version,
        header.provenance_ref,
        header.external_id,
    )

    assert after == before


def test_runtime_record_headers_do_not_support_ordering():
    header_a = make_header()
    header_b = make_header(record_id="RR-000000002")

    with pytest.raises(TypeError):
        _ = header_a < header_b


def test_runtime_record_header_exposes_no_serialization_methods():
    header = make_header()

    assert not hasattr(header, "to_dict")
    assert not hasattr(header, "from_dict")
    assert not hasattr(header, "to_json")
    assert not hasattr(header, "from_json")


def test_importing_runtime_record_identity_does_not_import_application_frameworks():
    sys.modules.pop("models.runtime_record_identity", None)
    streamlit_was_loaded = "streamlit" in sys.modules

    module = importlib.import_module("models.runtime_record_identity")

    assert hasattr(module, "RuntimeRecordHeader")

    if not streamlit_was_loaded:
        assert "streamlit" not in sys.modules


def test_record_category_does_not_restrict_values_to_current_examples():
    header = make_header(record_category="CUSTOM_RECORD")

    assert header.record_category == "CUSTOM_RECORD"


def test_runtime_record_header_module_can_be_imported_directly():
    from models.runtime_record_identity import (
        RuntimeRecordHeader as ImportedHeader,
    )

    assert ImportedHeader is RuntimeRecordHeader