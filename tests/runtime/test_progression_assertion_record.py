from dataclasses import FrozenInstanceError, fields, is_dataclass
from datetime import datetime, timedelta, timezone, tzinfo
import importlib
import sys

import pytest

from models.progression_assertion_record import ProgressionAssertionRecord
from models.runtime_record_identity import RuntimeRecordHeader


VALID_RECORDED_AT = datetime(2026, 7, 17, 12, 0, 0, tzinfo=timezone.utc)
VALID_ASSERTED_AT = datetime(2026, 7, 17, 11, 30, 0, tzinfo=timezone.utc)
VALID_EFFECTIVE_AT = datetime(2026, 7, 17, 11, 45, 0, tzinfo=timezone.utc)

VALID_TARGET_REF = "research_os"
VALID_ASSERTED_CONDITION = "ACTIVE"
VALID_SCOPE_REF = "SCOPE-000001"
VALID_TARGET_VERSION_REF = "RR-000000202"
VALID_PRIOR_CONDITION = "PENDING"
VALID_BRANCH_REF = "BRANCH-000001"
VALID_CONTEXT_REF = "CONTEXT-000001"
VALID_ACTOR_REF = "ACTOR-000001"
VALID_SOURCE_REF = "SYSTEM-000001"
VALID_BASIS_REF = "EVAL-000001"

ACCEPTED_CONDITIONS = [
    "PENDING",
    "ACTIVE",
    "HELD",
    "DORMANT",
    "ABANDONED",
]

INVALID_CONDITIONS = [
    "",
    " ",
    "UNKNOWN",
    "CONFLICTING",
    "PASS",
    "FAIL",
    "INCONCLUSIVE",
    "VALID",
    "INVALID",
    "CURRENT",
    "COMPLETED",
    "active",
    "Active",
    "ACTIVE ",
    " ACTIVE",
]

WHITESPACE_ONLY_VALUES = [
    "",
    " ",
    "\t",
    "\n",
    "\r\n",
    "   \t  ",
]

INVALID_REFERENCE_TYPES = [
    1,
    1.0,
    True,
    b"reference",
    [],
    {},
    (),
]


class InvalidTimezone(tzinfo):
    def utcoffset(self, dt):
        return None

    def dst(self, dt):
        return None

    def tzname(self, dt):
        return "INVALID"


def make_progression_header(**overrides):
    values = {
        "record_id": "RR-000000301",
        "record_category": "PROGRESSION_ASSERTION",
        "recorded_at": VALID_RECORDED_AT,
        "schema_version": "1.0",
        "provenance_ref": None,
        "external_id": None,
    }
    values.update(overrides)
    return RuntimeRecordHeader(**values)


def make_assertion(**overrides):
    values = {
        "header": make_progression_header(),
        "target_ref": VALID_TARGET_REF,
        "asserted_condition": VALID_ASSERTED_CONDITION,
        "scope_ref": VALID_SCOPE_REF,
        "target_version_ref": None,
        "prior_condition": None,
        "branch_ref": None,
        "context_ref": None,
        "asserted_at": None,
        "effective_at": None,
        "actor_ref": None,
        "source_ref": None,
        "basis_ref": None,
    }
    values.update(overrides)
    return ProgressionAssertionRecord(**values)


def test_progression_assertion_record_is_a_dataclass():
    assert is_dataclass(ProgressionAssertionRecord)


def test_progression_assertion_record_declares_exact_field_order():
    assert [field.name for field in fields(ProgressionAssertionRecord)] == [
        "header",
        "target_ref",
        "asserted_condition",
        "scope_ref",
        "target_version_ref",
        "prior_condition",
        "branch_ref",
        "context_ref",
        "asserted_at",
        "effective_at",
        "actor_ref",
        "source_ref",
        "basis_ref",
    ]


def test_progression_assertion_record_accepts_required_fields_only():
    record = ProgressionAssertionRecord(
        header=make_progression_header(),
        target_ref=VALID_TARGET_REF,
        asserted_condition=VALID_ASSERTED_CONDITION,
        scope_ref=VALID_SCOPE_REF,
    )

    assert record.header.record_category == "PROGRESSION_ASSERTION"
    assert record.target_ref == VALID_TARGET_REF
    assert record.asserted_condition == VALID_ASSERTED_CONDITION
    assert record.scope_ref == VALID_SCOPE_REF
    assert record.target_version_ref is None
    assert record.prior_condition is None
    assert record.branch_ref is None
    assert record.context_ref is None
    assert record.asserted_at is None
    assert record.effective_at is None
    assert record.actor_ref is None
    assert record.source_ref is None
    assert record.basis_ref is None


def test_progression_assertion_record_preserves_exact_header_instance():
    header = make_progression_header()
    record = make_assertion(header=header)
    assert record.header is header


def test_progression_assertion_identity_is_supplied_by_header_record_id():
    record = make_assertion()
    assert record.header.record_id == "RR-000000301"
    assert not hasattr(record, "assertion_id")


def test_progression_assertion_record_accepts_all_valid_optional_fields():
    record = make_assertion(
        target_version_ref=VALID_TARGET_VERSION_REF,
        prior_condition=VALID_PRIOR_CONDITION,
        branch_ref=VALID_BRANCH_REF,
        context_ref=VALID_CONTEXT_REF,
        asserted_at=VALID_ASSERTED_AT,
        effective_at=VALID_EFFECTIVE_AT,
        actor_ref=VALID_ACTOR_REF,
        source_ref=VALID_SOURCE_REF,
        basis_ref=VALID_BASIS_REF,
    )

    assert record.target_version_ref == VALID_TARGET_VERSION_REF
    assert record.prior_condition == VALID_PRIOR_CONDITION
    assert record.branch_ref == VALID_BRANCH_REF
    assert record.context_ref == VALID_CONTEXT_REF
    assert record.asserted_at == VALID_ASSERTED_AT
    assert record.effective_at == VALID_EFFECTIVE_AT
    assert record.actor_ref == VALID_ACTOR_REF
    assert record.source_ref == VALID_SOURCE_REF
    assert record.basis_ref == VALID_BASIS_REF


def test_progression_assertion_record_preserves_reference_values_exactly():
    record = make_assertion(
        target_ref=" target ",
        scope_ref=" scope ",
        target_version_ref=" target-version ",
        branch_ref=" branch ",
        context_ref=" context ",
        actor_ref=" actor ",
        source_ref=" source ",
        basis_ref=" basis ",
    )

    assert record.target_ref == " target "
    assert record.scope_ref == " scope "
    assert record.target_version_ref == " target-version "
    assert record.branch_ref == " branch "
    assert record.context_ref == " context "
    assert record.actor_ref == " actor "
    assert record.source_ref == " source "
    assert record.basis_ref == " basis "


def test_progression_assertion_record_allows_equal_strings_across_reference_fields():
    record = make_assertion(
        target_ref="same",
        scope_ref="same",
        target_version_ref="same",
        branch_ref="same",
        context_ref="same",
        actor_ref="same",
        source_ref="same",
        basis_ref="same",
    )
    assert all(
        getattr(record, field_name) == "same"
        for field_name in (
            "target_ref",
            "scope_ref",
            "target_version_ref",
            "branch_ref",
            "context_ref",
            "actor_ref",
            "source_ref",
            "basis_ref",
        )
    )


@pytest.mark.parametrize(
    "missing_field",
    ["header", "target_ref", "asserted_condition", "scope_ref"],
)
def test_progression_assertion_record_requires_each_required_field(missing_field):
    values = {
        "header": make_progression_header(),
        "target_ref": VALID_TARGET_REF,
        "asserted_condition": VALID_ASSERTED_CONDITION,
        "scope_ref": VALID_SCOPE_REF,
    }
    values.pop(missing_field)
    with pytest.raises(TypeError):
        ProgressionAssertionRecord(**values)


@pytest.mark.parametrize(
    "invalid_value",
    [None, "RR-000000301", {}, [], (), 1, True],
)
def test_header_rejects_non_runtime_record_header_values(invalid_value):
    with pytest.raises(TypeError, match="header"):
        make_assertion(header=invalid_value)


def test_header_accepts_progression_assertion_record_category():
    record = make_assertion(
        header=make_progression_header(
            record_category="PROGRESSION_ASSERTION",
        ),
    )
    assert record.header.record_category == "PROGRESSION_ASSERTION"


@pytest.mark.parametrize(
    "record_category",
    ["EVENT", "VERSION", "HOLD", "EVALUATION", "CUSTOM_RECORD"],
)
def test_header_rejects_non_progression_assertion_categories(record_category):
    header = make_progression_header(record_category=record_category)
    with pytest.raises(ValueError, match="header|record_category"):
        make_assertion(header=header)


@pytest.mark.parametrize(
    "invalid_value",
    [None, 1, 1.0, True, b"target", [], {}, ()],
)
def test_target_ref_rejects_non_string_values(invalid_value):
    with pytest.raises(TypeError, match="target_ref"):
        make_assertion(target_ref=invalid_value)


@pytest.mark.parametrize(
    "valid_value",
    [
        "research_os",
        "OBJ-000001",
        "RR-000000202",
        "external/target/42",
        " target ",
        "0",
        "x",
    ],
)
def test_target_ref_accepts_non_empty_strings(valid_value):
    record = make_assertion(target_ref=valid_value)
    assert record.target_ref == valid_value


@pytest.mark.parametrize("invalid_value", WHITESPACE_ONLY_VALUES)
def test_target_ref_rejects_empty_or_whitespace_only_values(invalid_value):
    with pytest.raises(ValueError, match="target_ref"):
        make_assertion(target_ref=invalid_value)


@pytest.mark.parametrize(
    "invalid_value",
    [None, 1, 1.0, True, b"ACTIVE", [], {}, ()],
)
def test_asserted_condition_rejects_non_string_values(invalid_value):
    with pytest.raises(TypeError, match="asserted_condition"):
        make_assertion(asserted_condition=invalid_value)


@pytest.mark.parametrize("condition", ACCEPTED_CONDITIONS)
def test_asserted_condition_accepts_frozen_progression_vocabulary(condition):
    record = make_assertion(asserted_condition=condition)
    assert record.asserted_condition == condition


@pytest.mark.parametrize("condition", INVALID_CONDITIONS)
def test_asserted_condition_rejects_values_outside_frozen_vocabulary(condition):
    with pytest.raises(ValueError, match="asserted_condition"):
        make_assertion(asserted_condition=condition)


@pytest.mark.parametrize("condition", ["active", "Active", "ACTIVE "])
def test_asserted_condition_is_not_normalized(condition):
    with pytest.raises(ValueError, match="asserted_condition"):
        make_assertion(asserted_condition=condition)


@pytest.mark.parametrize(
    "invalid_value",
    [None, 1, 1.0, True, b"scope", [], {}, ()],
)
def test_scope_ref_rejects_non_string_values(invalid_value):
    with pytest.raises(TypeError, match="scope_ref"):
        make_assertion(scope_ref=invalid_value)


@pytest.mark.parametrize(
    "valid_value",
    [
        "SCOPE-000001",
        "research/program/1",
        "institutional",
        " scope ",
        "0",
        "x",
    ],
)
def test_scope_ref_accepts_non_empty_strings(valid_value):
    record = make_assertion(scope_ref=valid_value)
    assert record.scope_ref == valid_value


@pytest.mark.parametrize("invalid_value", WHITESPACE_ONLY_VALUES)
def test_scope_ref_rejects_empty_or_whitespace_only_values(invalid_value):
    with pytest.raises(ValueError, match="scope_ref"):
        make_assertion(scope_ref=invalid_value)


@pytest.mark.parametrize("invalid_value", INVALID_REFERENCE_TYPES)
def test_target_version_ref_rejects_non_string_non_none_values(invalid_value):
    with pytest.raises(TypeError, match="target_version_ref"):
        make_assertion(target_version_ref=invalid_value)


@pytest.mark.parametrize(
    "valid_value",
    [
        "RR-000000202",
        "legacy-version",
        "external/version/42",
        " target-version ",
        "0",
    ],
)
def test_target_version_ref_accepts_non_empty_strings(valid_value):
    record = make_assertion(target_version_ref=valid_value)
    assert record.target_version_ref == valid_value


@pytest.mark.parametrize("invalid_value", WHITESPACE_ONLY_VALUES)
def test_target_version_ref_rejects_empty_or_whitespace_only_values(invalid_value):
    with pytest.raises(ValueError, match="target_version_ref"):
        make_assertion(target_version_ref=invalid_value)


@pytest.mark.parametrize("invalid_value", INVALID_REFERENCE_TYPES)
def test_prior_condition_rejects_non_string_non_none_values(invalid_value):
    with pytest.raises(TypeError, match="prior_condition"):
        make_assertion(prior_condition=invalid_value)


@pytest.mark.parametrize("condition", ACCEPTED_CONDITIONS)
def test_prior_condition_accepts_frozen_progression_vocabulary(condition):
    record = make_assertion(prior_condition=condition)
    assert record.prior_condition == condition


@pytest.mark.parametrize("condition", INVALID_CONDITIONS)
def test_prior_condition_rejects_values_outside_frozen_vocabulary(condition):
    with pytest.raises(ValueError, match="prior_condition"):
        make_assertion(prior_condition=condition)


@pytest.mark.parametrize("condition", ["ACTIVE", "HELD"])
def test_prior_condition_may_equal_asserted_condition(condition):
    record = make_assertion(
        asserted_condition=condition,
        prior_condition=condition,
    )
    assert record.prior_condition == record.asserted_condition


@pytest.mark.parametrize(
    "field_name",
    [
        "target_version_ref",
        "branch_ref",
        "context_ref",
        "actor_ref",
        "source_ref",
        "basis_ref",
    ],
)
@pytest.mark.parametrize("invalid_value", INVALID_REFERENCE_TYPES)
def test_optional_references_reject_non_string_non_none_values(
    field_name,
    invalid_value,
):
    with pytest.raises(TypeError, match=field_name):
        make_assertion(**{field_name: invalid_value})


@pytest.mark.parametrize(
    "field_name",
    [
        "target_version_ref",
        "branch_ref",
        "context_ref",
        "actor_ref",
        "source_ref",
        "basis_ref",
    ],
)
def test_optional_references_accept_none(field_name):
    record = make_assertion(**{field_name: None})
    assert getattr(record, field_name) is None


@pytest.mark.parametrize(
    ("field_name", "valid_value"),
    [
        ("target_version_ref", "custom-version"),
        ("branch_ref", "custom-branch"),
        ("context_ref", "custom-context"),
        ("actor_ref", "custom-actor"),
        ("source_ref", "custom-source"),
        ("basis_ref", "custom-basis"),
    ],
)
def test_optional_references_accept_non_empty_strings(field_name, valid_value):
    record = make_assertion(**{field_name: valid_value})
    assert getattr(record, field_name) == valid_value


@pytest.mark.parametrize(
    "field_name",
    [
        "target_version_ref",
        "branch_ref",
        "context_ref",
        "actor_ref",
        "source_ref",
        "basis_ref",
    ],
)
@pytest.mark.parametrize("invalid_value", WHITESPACE_ONLY_VALUES)
def test_optional_references_reject_empty_or_whitespace_only_values(
    field_name,
    invalid_value,
):
    with pytest.raises(ValueError, match=field_name):
        make_assertion(**{field_name: invalid_value})


@pytest.mark.parametrize(
    "invalid_value",
    ["2026-07-17T11:30:00Z", 0, 1.0, True, {}, []],
)
def test_asserted_at_rejects_non_datetime_non_none_values(invalid_value):
    with pytest.raises(TypeError, match="asserted_at"):
        make_assertion(asserted_at=invalid_value)


def test_asserted_at_rejects_naive_datetime():
    with pytest.raises(ValueError, match="asserted_at"):
        make_assertion(asserted_at=datetime(2026, 7, 17, 11, 30))


def test_asserted_at_rejects_timezone_with_no_usable_offset():
    invalid = datetime(2026, 7, 17, 11, 30, tzinfo=InvalidTimezone())
    with pytest.raises(ValueError, match="asserted_at"):
        make_assertion(asserted_at=invalid)


def test_asserted_at_accepts_and_preserves_non_utc_timezone():
    tz = timezone(timedelta(hours=-7))
    asserted_at = datetime(2026, 7, 17, 11, 30, tzinfo=tz)
    record = make_assertion(asserted_at=asserted_at)
    assert record.asserted_at is asserted_at
    assert record.asserted_at.tzinfo is tz
    assert record.asserted_at.utcoffset() == timedelta(hours=-7)


@pytest.mark.parametrize(
    "invalid_value",
    ["2026-07-17T11:45:00Z", 0, 1.0, True, {}, []],
)
def test_effective_at_rejects_non_datetime_non_none_values(invalid_value):
    with pytest.raises(TypeError, match="effective_at"):
        make_assertion(effective_at=invalid_value)


def test_effective_at_rejects_naive_datetime():
    with pytest.raises(ValueError, match="effective_at"):
        make_assertion(effective_at=datetime(2026, 7, 17, 11, 45))


def test_effective_at_rejects_timezone_with_no_usable_offset():
    invalid = datetime(2026, 7, 17, 11, 45, tzinfo=InvalidTimezone())
    with pytest.raises(ValueError, match="effective_at"):
        make_assertion(effective_at=invalid)


def test_effective_at_accepts_and_preserves_non_utc_timezone():
    tz = timezone(timedelta(hours=5, minutes=30))
    effective_at = datetime(2026, 7, 17, 11, 45, tzinfo=tz)
    record = make_assertion(effective_at=effective_at)
    assert record.effective_at is effective_at
    assert record.effective_at.tzinfo is tz
    assert record.effective_at.utcoffset() == timedelta(hours=5, minutes=30)


def test_asserted_at_does_not_default_to_recorded_at():
    record = make_assertion()
    assert record.asserted_at is None
    assert record.header.recorded_at == VALID_RECORDED_AT


def test_effective_at_does_not_default_to_asserted_at():
    record = make_assertion(asserted_at=VALID_ASSERTED_AT)
    assert record.asserted_at == VALID_ASSERTED_AT
    assert record.effective_at is None


def test_effective_at_may_precede_asserted_at():
    effective_at = VALID_ASSERTED_AT - timedelta(hours=1)
    record = make_assertion(
        asserted_at=VALID_ASSERTED_AT,
        effective_at=effective_at,
    )
    assert record.effective_at < record.asserted_at


def test_asserted_at_may_follow_recorded_at():
    asserted_at = VALID_RECORDED_AT + timedelta(hours=1)
    record = make_assertion(asserted_at=asserted_at)
    assert record.asserted_at > record.header.recorded_at


def test_effective_at_may_follow_recorded_at():
    effective_at = VALID_RECORDED_AT + timedelta(hours=1)
    record = make_assertion(effective_at=effective_at)
    assert record.effective_at > record.header.recorded_at


def test_header_type_failure_precedes_target_failure():
    with pytest.raises(TypeError, match="header"):
        ProgressionAssertionRecord(
            header={},
            target_ref=1,
            asserted_condition=1,
            scope_ref=1,
            target_version_ref=1,
            prior_condition=1,
            branch_ref=1,
            context_ref=1,
            asserted_at=1,
            effective_at=1,
            actor_ref=1,
            source_ref=1,
            basis_ref=1,
        )


def test_header_category_failure_precedes_target_failure():
    with pytest.raises(ValueError, match="header|record_category"):
        make_assertion(
            header=make_progression_header(record_category="EVENT"),
            target_ref=1,
        )


def test_target_type_failure_precedes_asserted_condition_failure():
    with pytest.raises(TypeError, match="target_ref"):
        make_assertion(target_ref=1, asserted_condition=1)


def test_target_value_failure_precedes_asserted_condition_failure():
    with pytest.raises(ValueError, match="target_ref"):
        make_assertion(target_ref=" ", asserted_condition=1)


def test_asserted_condition_failure_precedes_scope_failure():
    with pytest.raises(ValueError, match="asserted_condition"):
        make_assertion(asserted_condition="UNKNOWN", scope_ref=1)


def test_scope_failure_precedes_target_version_failure():
    with pytest.raises(TypeError, match="scope_ref"):
        make_assertion(scope_ref=1, target_version_ref=1)


def test_target_version_failure_precedes_prior_condition_failure():
    with pytest.raises(TypeError, match="target_version_ref"):
        make_assertion(target_version_ref=1, prior_condition=1)


def test_prior_condition_failure_precedes_branch_failure():
    with pytest.raises(TypeError, match="prior_condition"):
        make_assertion(prior_condition=1, branch_ref=1)


def test_branch_failure_precedes_context_failure():
    with pytest.raises(TypeError, match="branch_ref"):
        make_assertion(branch_ref=1, context_ref=1)


def test_context_failure_precedes_asserted_at_failure():
    with pytest.raises(TypeError, match="context_ref"):
        make_assertion(context_ref=1, asserted_at=1)


def test_asserted_at_failure_precedes_effective_at_failure():
    with pytest.raises(TypeError, match="asserted_at"):
        make_assertion(asserted_at=1, effective_at=1)


def test_effective_at_failure_precedes_actor_failure():
    with pytest.raises(TypeError, match="effective_at"):
        make_assertion(effective_at=1, actor_ref=1)


def test_actor_failure_precedes_source_failure():
    with pytest.raises(TypeError, match="actor_ref"):
        make_assertion(actor_ref=1, source_ref=1)


def test_source_failure_precedes_basis_failure():
    with pytest.raises(TypeError, match="source_ref"):
        make_assertion(source_ref=1, basis_ref=1)


@pytest.mark.parametrize(
    ("field_name", "new_value"),
    [
        ("header", make_progression_header(record_id="RR-000000302")),
        ("target_ref", "target-2"),
        ("asserted_condition", "HELD"),
        ("scope_ref", "SCOPE-000002"),
        ("target_version_ref", "RR-000000203"),
        ("prior_condition", "DORMANT"),
        ("branch_ref", "BRANCH-000002"),
        ("context_ref", "CONTEXT-000002"),
        (
            "asserted_at",
            VALID_ASSERTED_AT + timedelta(minutes=1),
        ),
        (
            "effective_at",
            VALID_EFFECTIVE_AT + timedelta(minutes=1),
        ),
        ("actor_ref", "ACTOR-000002"),
        ("source_ref", "SYSTEM-000002"),
        ("basis_ref", "EVAL-000002"),
    ],
)
def test_progression_assertion_record_is_frozen(field_name, new_value):
    record = make_assertion()
    with pytest.raises(FrozenInstanceError):
        setattr(record, field_name, new_value)


def test_identical_progression_assertion_records_compare_equal():
    assert make_assertion() == make_assertion()


@pytest.mark.parametrize(
    ("field_name", "different_value"),
    [
        ("header", make_progression_header(record_id="RR-000000302")),
        ("target_ref", "target-2"),
        ("asserted_condition", "HELD"),
        ("scope_ref", "SCOPE-000002"),
        ("target_version_ref", "RR-000000203"),
        ("prior_condition", "DORMANT"),
        ("branch_ref", "BRANCH-000002"),
        ("context_ref", "CONTEXT-000002"),
        (
            "asserted_at",
            VALID_ASSERTED_AT + timedelta(minutes=1),
        ),
        (
            "effective_at",
            VALID_EFFECTIVE_AT + timedelta(minutes=1),
        ),
        ("actor_ref", "ACTOR-000002"),
        ("source_ref", "SYSTEM-000002"),
        ("basis_ref", "EVAL-000002"),
    ],
)
def test_progression_assertion_record_equality_is_full_structural_equality(
    field_name,
    different_value,
):
    assert make_assertion() != make_assertion(
        **{field_name: different_value},
    )


def test_same_header_with_different_asserted_condition_is_not_equal():
    header = make_progression_header()
    assert make_assertion(
        header=header,
        asserted_condition="ACTIVE",
    ) != make_assertion(
        header=header,
        asserted_condition="HELD",
    )


def test_same_target_and_condition_with_different_scope_is_not_equal():
    assert make_assertion(scope_ref="SCOPE-000001") != make_assertion(
        scope_ref="SCOPE-000002",
    )


def test_same_target_condition_and_scope_with_different_basis_is_not_equal():
    assert make_assertion(basis_ref="EVAL-000001") != make_assertion(
        basis_ref="EVAL-000002",
    )


def test_equivalent_temporal_instants_follow_python_datetime_equality():
    instant_utc = datetime(2026, 7, 17, 12, 0, tzinfo=timezone.utc)
    instant_offset = datetime(
        2026,
        7,
        17,
        5,
        0,
        tzinfo=timezone(timedelta(hours=-7)),
    )

    assert instant_utc == instant_offset
    assert make_assertion(asserted_at=instant_utc) == make_assertion(
        asserted_at=instant_offset,
    )


def test_equal_progression_assertion_records_have_equal_hashes():
    assert hash(make_assertion()) == hash(make_assertion())


def test_structurally_different_progression_assertion_records_can_coexist_in_a_set():
    assertion_a = make_assertion()
    assertion_b = make_assertion(
        header=make_progression_header(record_id="RR-000000302"),
    )
    assert len({assertion_a, assertion_b}) == 2


def test_hashing_does_not_change_progression_assertion_record():
    record = make_assertion(
        target_version_ref=VALID_TARGET_VERSION_REF,
        prior_condition=VALID_PRIOR_CONDITION,
        branch_ref=VALID_BRANCH_REF,
        context_ref=VALID_CONTEXT_REF,
        asserted_at=VALID_ASSERTED_AT,
        effective_at=VALID_EFFECTIVE_AT,
        actor_ref=VALID_ACTOR_REF,
        source_ref=VALID_SOURCE_REF,
        basis_ref=VALID_BASIS_REF,
    )
    before = tuple(getattr(record, field.name) for field in fields(record))
    hash(record)
    after = tuple(getattr(record, field.name) for field in fields(record))
    assert after == before


def test_progression_assertion_records_do_not_support_ordering():
    with pytest.raises(TypeError):
        _ = make_assertion() < make_assertion(
            header=make_progression_header(
                record_id="RR-000000302",
            ),
        )


def test_progression_assertion_record_exposes_no_serialization_methods():
    record = make_assertion()
    assert not hasattr(record, "to_dict")
    assert not hasattr(record, "from_dict")
    assert not hasattr(record, "to_json")
    assert not hasattr(record, "from_json")


def test_progression_assertion_record_does_not_accept_application_object_dictionary_as_header():
    application_object = {
        "id": "research_os",
        "type": "project",
        "status": "Active",
    }
    with pytest.raises(TypeError, match="header"):
        ProgressionAssertionRecord(
            header=application_object,
            target_ref=VALID_TARGET_REF,
            asserted_condition=VALID_ASSERTED_CONDITION,
            scope_ref=VALID_SCOPE_REF,
        )


@pytest.mark.parametrize("application_status", ["Active", "OPEN", "UNKNOWN"])
def test_application_status_values_are_not_accepted_as_progression_conditions(
    application_status,
):
    with pytest.raises(ValueError, match="asserted_condition"):
        make_assertion(asserted_condition=application_status)


def test_held_condition_does_not_create_hold_fields():
    record = make_assertion(asserted_condition="HELD")
    assert not hasattr(record, "hold_ref")
    assert not hasattr(record, "blocked")
    assert not hasattr(record, "control_status")


def test_conflicting_is_not_an_accepted_progression_condition():
    with pytest.raises(ValueError, match="asserted_condition"):
        make_assertion(asserted_condition="CONFLICTING")


def test_importing_progression_assertion_record_does_not_import_object_engine():
    was_loaded = "src.services.object_engine" in sys.modules
    module = importlib.import_module(
        "models.progression_assertion_record",
    )
    assert hasattr(module, "ProgressionAssertionRecord")
    if not was_loaded:
        assert "src.services.object_engine" not in sys.modules


def test_importing_progression_assertion_record_does_not_import_runtime_event_record():
    was_loaded = "models.runtime_event_record" in sys.modules
    module = importlib.import_module(
        "models.progression_assertion_record",
    )
    assert hasattr(module, "ProgressionAssertionRecord")
    if not was_loaded:
        assert "models.runtime_event_record" not in sys.modules


def test_importing_progression_assertion_record_does_not_import_runtime_object_version_record():
    was_loaded = "models.runtime_object_version_record" in sys.modules
    module = importlib.import_module(
        "models.progression_assertion_record",
    )
    assert hasattr(module, "ProgressionAssertionRecord")
    if not was_loaded:
        assert "models.runtime_object_version_record" not in sys.modules


def test_importing_progression_assertion_record_does_not_import_streamlit():
    was_loaded = "streamlit" in sys.modules
    module = importlib.import_module(
        "models.progression_assertion_record",
    )
    assert hasattr(module, "ProgressionAssertionRecord")
    if not was_loaded:
        assert "streamlit" not in sys.modules


def test_progression_assertion_record_module_can_be_imported_directly():
    from models.progression_assertion_record import (
        ProgressionAssertionRecord as ImportedRecord,
    )

    assert ImportedRecord is ProgressionAssertionRecord


def test_progression_assertion_record_does_not_modify_composed_header():
    header = make_progression_header(
        provenance_ref="PRV-000000001",
        external_id="external-assertion-301",
    )
    before = (
        header.record_id,
        header.record_category,
        header.recorded_at,
        header.schema_version,
        header.provenance_ref,
        header.external_id,
    )

    make_assertion(
        header=header,
        target_version_ref=VALID_TARGET_VERSION_REF,
        prior_condition=VALID_PRIOR_CONDITION,
        branch_ref=VALID_BRANCH_REF,
        context_ref=VALID_CONTEXT_REF,
        asserted_at=VALID_ASSERTED_AT,
        effective_at=VALID_EFFECTIVE_AT,
        actor_ref=VALID_ACTOR_REF,
        source_ref=VALID_SOURCE_REF,
        basis_ref=VALID_BASIS_REF,
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


def test_progression_assertion_record_does_not_restrict_reference_prefixes():
    record = make_assertion(
        target_ref="custom-target",
        scope_ref="custom-scope",
        target_version_ref="custom-version",
        branch_ref="custom-branch",
        context_ref="custom-context",
        actor_ref="custom-actor",
        source_ref="custom-source",
        basis_ref="custom-basis",
    )

    assert record.target_ref == "custom-target"
    assert record.scope_ref == "custom-scope"
    assert record.target_version_ref == "custom-version"
    assert record.branch_ref == "custom-branch"
    assert record.context_ref == "custom-context"
    assert record.actor_ref == "custom-actor"
    assert record.source_ref == "custom-source"
    assert record.basis_ref == "custom-basis"


def test_progression_assertion_record_allows_reference_fields_to_share_values():
    record = make_assertion(
        target_ref="same",
        target_version_ref="same",
        scope_ref="same",
        context_ref="same",
        actor_ref="same",
        source_ref="same",
        basis_ref="same",
    )

    assert record.target_ref == record.target_version_ref
    assert record.scope_ref == record.context_ref
    assert record.actor_ref == record.source_ref
    assert record.source_ref == record.basis_ref