from dataclasses import FrozenInstanceError, fields, is_dataclass
from datetime import datetime, timedelta, timezone, tzinfo
import importlib
import sys

import pytest

from models.hold_record import HoldRecord
from models.runtime_record_identity import RuntimeRecordHeader


RECORDED = datetime(2026, 7, 17, 12, tzinfo=timezone.utc)
PLACED = datetime(2026, 7, 17, 11, tzinfo=timezone.utc)
EFFECTIVE = datetime(2026, 7, 17, 11, 15, tzinfo=timezone.utc)
REVIEW = datetime(2026, 7, 18, 11, tzinfo=timezone.utc)
EXPIRES = datetime(2026, 7, 19, 11, tzinfo=timezone.utc)

REQUIRED_REFS = [
    "target_ref",
    "blocked_consequence_ref",
    "scope_ref",
    "reason_ref",
    "resolution_condition_ref",
]
OPTIONAL_REFS = [
    "target_version_ref",
    "branch_ref",
    "context_ref",
    "trigger_ref",
    "basis_ref",
    "owner_ref",
    "placed_by_ref",
    "placement_authority_ref",
    "release_authority_ref",
]
TIMES = ["placed_at", "effective_at", "review_at", "expires_at"]
WHITESPACE = ["", " ", "\t", "\n", "\r\n", "   \t  "]
BAD_REFS = [1, 1.0, True, b"x", [], {}, ()]
BAD_TIMES = ["2026-07-17T11:00:00Z", 0, 1.0, True, {}, []]


class InvalidTimezone(tzinfo):
    def utcoffset(self, dt):
        return None

    def dst(self, dt):
        return None

    def tzname(self, dt):
        return "INVALID"


def make_header(**overrides):
    values = {
        "record_id": "RR-000000401",
        "record_category": "HOLD",
        "recorded_at": RECORDED,
        "schema_version": "1.0",
        "provenance_ref": None,
        "external_id": None,
    }
    values.update(overrides)
    return RuntimeRecordHeader(**values)


def make_hold(**overrides):
    values = {
        "header": make_header(),
        "target_ref": "research_os",
        "blocked_consequence_ref": "release",
        "scope_ref": "SCOPE-000001",
        "reason_ref": "REASON-000001",
        "resolution_condition_ref": "RESOLUTION-000001",
        "target_version_ref": None,
        "branch_ref": None,
        "context_ref": None,
        "trigger_ref": None,
        "basis_ref": None,
        "owner_ref": None,
        "placed_by_ref": None,
        "placement_authority_ref": None,
        "release_authority_ref": None,
        "placed_at": None,
        "effective_at": None,
        "review_at": None,
        "expires_at": None,
    }
    values.update(overrides)
    return HoldRecord(**values)


def test_hold_record_is_a_dataclass():
    assert is_dataclass(HoldRecord)


def test_hold_record_declares_exact_field_order():
    assert [f.name for f in fields(HoldRecord)] == [
        "header", "target_ref", "blocked_consequence_ref", "scope_ref",
        "reason_ref", "resolution_condition_ref", "target_version_ref",
        "branch_ref", "context_ref", "trigger_ref", "basis_ref",
        "owner_ref", "placed_by_ref", "placement_authority_ref",
        "release_authority_ref", "placed_at", "effective_at",
        "review_at", "expires_at",
    ]


def test_hold_record_accepts_required_fields_only():
    record = make_hold()
    assert record.header.record_category == "HOLD"
    for name in OPTIONAL_REFS + TIMES:
        assert getattr(record, name) is None


def test_hold_record_preserves_exact_header_instance():
    header = make_header()
    assert make_hold(header=header).header is header


def test_hold_record_identity_is_supplied_by_header_record_id():
    record = make_hold()
    assert record.header.record_id == "RR-000000401"
    assert not hasattr(record, "hold_id")


def test_hold_record_accepts_all_valid_optional_fields():
    record = make_hold(
        target_version_ref="RR-000000202",
        branch_ref="BRANCH-000001",
        context_ref="CONTEXT-000001",
        trigger_ref="EVAL-000001",
        basis_ref="EVIDENCE-000001",
        owner_ref="OWNER-000001",
        placed_by_ref="ACTOR-000001",
        placement_authority_ref="AUTHORITY-000001",
        release_authority_ref="AUTHORITY-000002",
        placed_at=PLACED,
        effective_at=EFFECTIVE,
        review_at=REVIEW,
        expires_at=EXPIRES,
    )
    assert record.target_version_ref == "RR-000000202"
    assert record.expires_at == EXPIRES


@pytest.mark.parametrize("field_name", REQUIRED_REFS + OPTIONAL_REFS)
def test_hold_record_preserves_reference_values_exactly(field_name):
    value = f" {field_name} "
    assert getattr(make_hold(**{field_name: value}), field_name) == value


def test_hold_record_allows_equal_strings_across_reference_fields():
    values = {name: "same" for name in REQUIRED_REFS + OPTIONAL_REFS}
    record = make_hold(**values)
    assert all(getattr(record, name) == "same" for name in values)


@pytest.mark.parametrize(
    "missing",
    ["header"] + REQUIRED_REFS,
)
def test_hold_record_requires_each_required_field(missing):
    values = {
        "header": make_header(),
        "target_ref": "target",
        "blocked_consequence_ref": "release",
        "scope_ref": "scope",
        "reason_ref": "reason",
        "resolution_condition_ref": "resolution",
    }
    values.pop(missing)
    with pytest.raises(TypeError):
        HoldRecord(**values)


@pytest.mark.parametrize("bad", [None, "RR-1", {}, [], (), 1, True])
def test_hold_header_rejects_non_runtime_record_header_values(bad):
    with pytest.raises(TypeError, match="header"):
        make_hold(header=bad)


@pytest.mark.parametrize(
    "category",
    ["EVENT", "VERSION", "PROGRESSION_ASSERTION", "EVALUATION", "CUSTOM_RECORD"],
)
def test_hold_header_rejects_non_hold_categories(category):
    with pytest.raises(ValueError, match="header|record_category"):
        make_hold(header=make_header(record_category=category))


def test_hold_header_accepts_hold_record_category():
    assert make_hold().header.record_category == "HOLD"


@pytest.mark.parametrize("field_name", REQUIRED_REFS)
@pytest.mark.parametrize("bad", [None] + BAD_REFS)
def test_required_references_reject_non_string_values(field_name, bad):
    with pytest.raises(TypeError, match=field_name):
        make_hold(**{field_name: bad})


@pytest.mark.parametrize("field_name", REQUIRED_REFS)
@pytest.mark.parametrize("value", ["x", "0", " custom/value ", "A-000001"])
def test_required_references_accept_non_empty_strings(field_name, value):
    assert getattr(make_hold(**{field_name: value}), field_name) == value


@pytest.mark.parametrize("field_name", REQUIRED_REFS)
@pytest.mark.parametrize("bad", WHITESPACE)
def test_required_references_reject_empty_or_whitespace_only_values(field_name, bad):
    with pytest.raises(ValueError, match=field_name):
        make_hold(**{field_name: bad})


def test_target_and_blocked_consequence_are_distinct_fields():
    record = make_hold(target_ref="OBJ-1", blocked_consequence_ref="release")
    assert record.target_ref == "OBJ-1"
    assert record.blocked_consequence_ref == "release"


@pytest.mark.parametrize(
    "value",
    ["progression", "release", "execution", "merge", "revision", "admission",
     "authorization", "publication", "deployment", "custom/consequence",
     " release ", "0", "x"],
)
def test_blocked_consequence_uses_open_reference_vocabulary(value):
    assert make_hold(blocked_consequence_ref=value).blocked_consequence_ref == value


@pytest.mark.parametrize("field_name", OPTIONAL_REFS)
@pytest.mark.parametrize("bad", BAD_REFS)
def test_optional_references_reject_non_string_non_none_values(field_name, bad):
    with pytest.raises(TypeError, match=field_name):
        make_hold(**{field_name: bad})


@pytest.mark.parametrize("field_name", OPTIONAL_REFS)
def test_optional_references_accept_none(field_name):
    assert getattr(make_hold(**{field_name: None}), field_name) is None


@pytest.mark.parametrize("field_name", OPTIONAL_REFS)
@pytest.mark.parametrize("value", ["x", "0", " custom/value ", "A-000001"])
def test_optional_references_accept_non_empty_strings(field_name, value):
    assert getattr(make_hold(**{field_name: value}), field_name) == value


@pytest.mark.parametrize("field_name", OPTIONAL_REFS)
@pytest.mark.parametrize("bad", WHITESPACE)
def test_optional_references_reject_empty_or_whitespace_only_values(field_name, bad):
    with pytest.raises(ValueError, match=field_name):
        make_hold(**{field_name: bad})


@pytest.mark.parametrize(
    ("left", "right"),
    [
        ("reason_ref", "trigger_ref"),
        ("trigger_ref", "basis_ref"),
        ("owner_ref", "placed_by_ref"),
        ("placement_authority_ref", "release_authority_ref"),
    ],
)
def test_reference_roles_are_distinct_fields(left, right):
    record = make_hold(**{left: "left", right: "right"})
    assert getattr(record, left) == "left"
    assert getattr(record, right) == "right"


@pytest.mark.parametrize("field_name", TIMES)
@pytest.mark.parametrize("bad", BAD_TIMES)
def test_temporal_fields_reject_non_datetime_non_none_values(field_name, bad):
    with pytest.raises(TypeError, match=field_name):
        make_hold(**{field_name: bad})


@pytest.mark.parametrize("field_name", TIMES)
def test_temporal_fields_reject_naive_datetime(field_name):
    with pytest.raises(ValueError, match=field_name):
        make_hold(**{field_name: datetime(2026, 7, 17, 11)})


@pytest.mark.parametrize("field_name", TIMES)
def test_temporal_fields_reject_timezone_with_no_usable_offset(field_name):
    value = datetime(2026, 7, 17, 11, tzinfo=InvalidTimezone())
    with pytest.raises(ValueError, match=field_name):
        make_hold(**{field_name: value})


@pytest.mark.parametrize(
    ("field_name", "offset"),
    [
        ("placed_at", timedelta(hours=-7)),
        ("effective_at", timedelta(hours=5, minutes=30)),
        ("review_at", timedelta(hours=2)),
        ("expires_at", timedelta(hours=-4)),
    ],
)
def test_temporal_fields_accept_and_preserve_non_utc_timezone(field_name, offset):
    tz = timezone(offset)
    value = datetime(2026, 7, 17, 11, tzinfo=tz)
    stored = getattr(make_hold(**{field_name: value}), field_name)
    assert stored is value
    assert stored.tzinfo is tz
    assert stored.utcoffset() == offset


def test_placed_at_does_not_default_to_recorded_at():
    assert make_hold().placed_at is None


def test_effective_at_does_not_default_to_placed_at():
    assert make_hold(placed_at=PLACED).effective_at is None


def test_review_at_does_not_default_from_effective_at():
    assert make_hold(effective_at=EFFECTIVE).review_at is None


def test_expires_at_does_not_default_from_review_at():
    assert make_hold(review_at=REVIEW).expires_at is None


@pytest.mark.parametrize(
    "values",
    [
        {"placed_at": PLACED, "effective_at": PLACED - timedelta(hours=1)},
        {"effective_at": EFFECTIVE, "review_at": EFFECTIVE - timedelta(hours=1)},
        {"review_at": REVIEW, "expires_at": REVIEW - timedelta(hours=1)},
        {"effective_at": EFFECTIVE, "expires_at": EFFECTIVE - timedelta(hours=1)},
    ],
)
def test_temporal_order_is_not_enforced(values):
    assert make_hold(**values)


def test_past_expiry_is_structurally_accepted():
    expiry = RECORDED - timedelta(days=1)
    assert make_hold(expires_at=expiry).expires_at is expiry


PRECEDENCE_CASES = [
    ({"target_ref": 1, "blocked_consequence_ref": 1}, TypeError, "target_ref"),
    ({"blocked_consequence_ref": 1, "scope_ref": 1}, TypeError, "blocked_consequence_ref"),
    ({"scope_ref": 1, "reason_ref": 1}, TypeError, "scope_ref"),
    ({"reason_ref": 1, "resolution_condition_ref": 1}, TypeError, "reason_ref"),
    ({"resolution_condition_ref": 1, "target_version_ref": 1}, TypeError, "resolution_condition_ref"),
    ({"target_version_ref": 1, "branch_ref": 1}, TypeError, "target_version_ref"),
    ({"branch_ref": 1, "context_ref": 1}, TypeError, "branch_ref"),
    ({"context_ref": 1, "trigger_ref": 1}, TypeError, "context_ref"),
    ({"trigger_ref": 1, "basis_ref": 1}, TypeError, "trigger_ref"),
    ({"basis_ref": 1, "owner_ref": 1}, TypeError, "basis_ref"),
    ({"owner_ref": 1, "placed_by_ref": 1}, TypeError, "owner_ref"),
    ({"placed_by_ref": 1, "placement_authority_ref": 1}, TypeError, "placed_by_ref"),
    ({"placement_authority_ref": 1, "release_authority_ref": 1}, TypeError, "placement_authority_ref"),
    ({"release_authority_ref": 1, "placed_at": 1}, TypeError, "release_authority_ref"),
    ({"placed_at": 1, "effective_at": 1}, TypeError, "placed_at"),
    ({"effective_at": 1, "review_at": 1}, TypeError, "effective_at"),
    ({"review_at": 1, "expires_at": 1}, TypeError, "review_at"),
]


def test_header_type_failure_precedes_target_failure():
    with pytest.raises(TypeError, match="header"):
        make_hold(header={}, target_ref=1)


def test_header_category_failure_precedes_target_failure():
    with pytest.raises(ValueError, match="header|record_category"):
        make_hold(header=make_header(record_category="EVENT"), target_ref=1)


@pytest.mark.parametrize(("overrides", "error_type", "match"), PRECEDENCE_CASES)
def test_validation_precedence(overrides, error_type, match):
    with pytest.raises(error_type, match=match):
        make_hold(**overrides)


def test_hold_record_exposes_no_release_fields():
    record = make_hold()
    for name in (
        "released", "release_status", "released_at", "released_by_ref",
        "release_decision_ref", "resolved", "resolution_status",
    ):
        assert not hasattr(record, name)


def test_hold_record_exposes_no_active_state_fields():
    record = make_hold()
    for name in ("is_active", "active", "current", "expired", "inactive"):
        assert not hasattr(record, name)


def test_past_expiry_does_not_add_release_or_active_state():
    record = make_hold(expires_at=RECORDED - timedelta(days=1))
    assert not hasattr(record, "released")
    assert not hasattr(record, "is_active")
    assert not hasattr(record, "expired")


def test_resolution_condition_reference_does_not_create_release_state():
    record = make_hold(resolution_condition_ref="RESOLUTION-2")
    assert record.resolution_condition_ref == "RESOLUTION-2"
    assert not hasattr(record, "released")


@pytest.mark.parametrize(
    "field_name",
    ["progression_condition", "asserted_condition", "evaluation_result",
     "result", "refused", "refusal_reason", "failed", "failure_reason"],
)
def test_hold_record_contains_no_other_control_semantic_fields(field_name):
    assert not hasattr(make_hold(), field_name)


MUTATIONS = [
    ("header", make_header(record_id="RR-000000402")),
    ("target_ref", "target-2"),
    ("blocked_consequence_ref", "execution"),
    ("scope_ref", "scope-2"),
    ("reason_ref", "reason-2"),
    ("resolution_condition_ref", "resolution-2"),
    ("target_version_ref", "version-2"),
    ("branch_ref", "branch-2"),
    ("context_ref", "context-2"),
    ("trigger_ref", "trigger-2"),
    ("basis_ref", "basis-2"),
    ("owner_ref", "owner-2"),
    ("placed_by_ref", "actor-2"),
    ("placement_authority_ref", "authority-3"),
    ("release_authority_ref", "authority-4"),
    ("placed_at", PLACED + timedelta(minutes=1)),
    ("effective_at", EFFECTIVE + timedelta(minutes=1)),
    ("review_at", REVIEW + timedelta(minutes=1)),
    ("expires_at", EXPIRES + timedelta(minutes=1)),
]


@pytest.mark.parametrize(("field_name", "value"), MUTATIONS)
def test_hold_record_is_frozen(field_name, value):
    with pytest.raises(FrozenInstanceError):
        setattr(make_hold(), field_name, value)


def test_identical_hold_records_compare_equal():
    assert make_hold() == make_hold()


@pytest.mark.parametrize(("field_name", "value"), MUTATIONS)
def test_hold_record_equality_is_full_structural_equality(field_name, value):
    assert make_hold() != make_hold(**{field_name: value})


def test_equivalent_temporal_instants_follow_python_datetime_equality():
    utc = datetime(2026, 7, 17, 12, tzinfo=timezone.utc)
    offset = datetime(2026, 7, 17, 5, tzinfo=timezone(timedelta(hours=-7)))
    assert make_hold(placed_at=utc) == make_hold(placed_at=offset)


def test_equal_hold_records_have_equal_hashes():
    assert hash(make_hold()) == hash(make_hold())


def test_structurally_different_hold_records_can_coexist_in_a_set():
    other = make_hold(header=make_header(record_id="RR-000000402"))
    assert len({make_hold(), other}) == 2


def test_hashing_does_not_change_hold_record():
    record = make_hold(placed_at=PLACED, expires_at=EXPIRES)
    before = tuple(getattr(record, f.name) for f in fields(record))
    hash(record)
    assert tuple(getattr(record, f.name) for f in fields(record)) == before


def test_hold_records_do_not_support_ordering():
    with pytest.raises(TypeError):
        _ = make_hold() < make_hold(header=make_header(record_id="RR-000000402"))


def test_hold_record_exposes_no_serialization_methods():
    record = make_hold()
    for name in ("to_dict", "from_dict", "to_json", "from_json"):
        assert not hasattr(record, name)


def test_hold_record_does_not_accept_application_object_dictionary_as_header():
    with pytest.raises(TypeError, match="header"):
        make_hold(header={"id": "research_os", "status": "Active"})


@pytest.mark.parametrize("status", ["UNKNOWN", "Active", "OPEN"])
def test_application_status_values_do_not_create_hold_state(status):
    record = make_hold(reason_ref=status)
    assert record.reason_ref == status
    assert not hasattr(record, "status")
    assert not hasattr(record, "is_active")


@pytest.mark.parametrize(
    "module_name",
    [
        "src.services.object_engine",
        "models.progression_assertion_record",
        "models.runtime_event_record",
        "models.runtime_object_version_record",
        "streamlit",
    ],
)
def test_importing_hold_record_does_not_import_prohibited_modules(module_name):
    was_loaded = module_name in sys.modules
    module = importlib.import_module("models.hold_record")
    assert hasattr(module, "HoldRecord")
    if not was_loaded:
        assert module_name not in sys.modules


def test_hold_record_module_can_be_imported_directly():
    from models.hold_record import HoldRecord as ImportedHoldRecord
    assert ImportedHoldRecord is HoldRecord


def test_hold_record_does_not_modify_composed_header():
    header = make_header(provenance_ref="PRV-1", external_id="external-hold")
    before = tuple(getattr(header, name) for name in (
        "record_id", "record_category", "recorded_at", "schema_version",
        "provenance_ref", "external_id",
    ))
    make_hold(header=header, placed_at=PLACED, expires_at=EXPIRES)
    after = tuple(getattr(header, name) for name in (
        "record_id", "record_category", "recorded_at", "schema_version",
        "provenance_ref", "external_id",
    ))
    assert after == before


def test_hold_record_does_not_restrict_reference_prefixes():
    values = {name: f"custom-{name}" for name in REQUIRED_REFS + OPTIONAL_REFS}
    record = make_hold(**values)
    assert all(getattr(record, name).startswith("custom-") for name in values)


def test_constructing_hold_record_does_not_create_progression_assertion():
    record = make_hold()
    assert not hasattr(record, "asserted_condition")


def test_constructing_hold_record_does_not_create_runtime_event():
    record = make_hold()
    assert not hasattr(record, "event_type")
    assert not hasattr(record, "occurred_at")


def test_constructing_hold_record_does_not_enforce_blocking():
    record = make_hold(blocked_consequence_ref="release")
    assert record.blocked_consequence_ref == "release"
    assert not hasattr(record, "block")
    assert not hasattr(record, "execute")
    assert not hasattr(record, "refuse")