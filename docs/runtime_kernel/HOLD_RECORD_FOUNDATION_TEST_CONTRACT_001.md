# RESEARCH OS — HOLD RECORD FOUNDATION

# TEST CONTRACT 001

**Date:** 2026-07-17
**Project:** Research OS
**Development Version:** v2.0.0
**Status:** ACTIVE / TEST CONTRACT
**Architecture:** RUNTIME KERNEL CANDIDATE ARCHITECTURE FROZEN
**Production Implementation:** HOLD
**Authority:** TEST DESIGN ONLY

**UNKNOWN → HOLD**

---

# PURPOSE

Define the exact tests that must be written before implementation of:

```text
HoldRecord
```

The test suite must prove:

1. immutable Runtime Record Header composition
2. `HOLD` record-category enforcement
3. minimal valid construction
4. context-rich valid construction
5. required target validation
6. target and blocked-consequence separation
7. required scope validation
8. required reason validation
9. required resolution-condition validation
10. optional target-version semantics
11. optional branch and context semantics
12. optional trigger and basis semantics
13. optional owner and placement-actor semantics
14. optional placement- and release-authority semantics
15. placement-time validation
16. effective-time validation
17. review-time validation
18. expiry-time validation
19. temporal separation
20. deterministic validation precedence
21. release-field absence
22. active-state-field absence
23. automatic-release absence
24. immutability
25. full structural equality
26. structural hashing
27. ordering prohibition
28. serialization absence
29. progression, Evaluation, refusal, and failure isolation
30. service and import isolation
31. preservation of all frozen Runtime Kernel foundations

This document does not authorize production implementation.

---

# PREREQUISITE

Immutable Contract 001 froze:

## Production Path

```text
models/hold_record.py
```

## Test Path

```text
tests/runtime/test_hold_record.py
```

## Model

```text
HoldRecord
```

## Required Fields

```python
header: RuntimeRecordHeader
target_ref: str
blocked_consequence_ref: str
scope_ref: str
reason_ref: str
resolution_condition_ref: str
```

## Optional Fields

```python
target_version_ref: str | None = None
branch_ref: str | None = None
context_ref: str | None = None
trigger_ref: str | None = None
basis_ref: str | None = None
owner_ref: str | None = None
placed_by_ref: str | None = None
placement_authority_ref: str | None = None
release_authority_ref: str | None = None
placed_at: datetime | None = None
effective_at: datetime | None = None
review_at: datetime | None = None
expires_at: datetime | None = None
```

## Required Header Category

```text
HOLD
```

## Frozen Boundaries

* control Hold is distinct from progression `HELD`
* control Hold is distinct from Evaluation `HOLD`
* control Hold is distinct from refusal
* control Hold is distinct from failure
* target is distinct from blocked consequence
* reason is distinct from trigger
* trigger is distinct from basis
* owner is distinct from authority
* resolution condition is distinct from release
* expiry does not automatically release
* active Hold state is derived later
* release is separately recorded
* the original Hold record remains immutable
* no persistence
* no services
* no serialization

---

# OPERATING RULES

* Write tests before production implementation.
* Do not create the production model during the test-writing session.
* Do not modify `RuntimeRecordHeader`.
* Do not modify frozen Runtime Kernel models.
* Do not modify application status fields.
* Do not import or initialize ObjectEngine.
* Do not create Runtime Events.
* Do not create Progression Assertion records.
* Do not evaluate authority.
* Do not calculate current Hold status.
* Do not block or refuse operations.
* Keep all tests deterministic and in memory.
* Test observable behavior rather than private helper structure.

---

# TEST FILE STRUCTURE

Create later:

```text
tests/
└── runtime/
    ├── test_runtime_record_identity.py
    ├── test_runtime_event_record.py
    ├── test_runtime_object_version_record.py
    ├── test_progression_assertion_record.py
    └── test_hold_record.py
```

No new `conftest.py` is required.

Production import:

```python
from models.hold_record import HoldRecord
```

Header import:

```python
from models.runtime_record_identity import RuntimeRecordHeader
```

---

# TEST FRAMEWORK

Use:

```text
pytest
```

Permitted imports:

```python
from dataclasses import FrozenInstanceError, fields, is_dataclass
from datetime import datetime, timedelta, timezone, tzinfo
import importlib
import sys

import pytest

from models.hold_record import HoldRecord
from models.runtime_record_identity import RuntimeRecordHeader
```

No additional dependency is authorized.

---

# SHARED VALID VALUES

The test file may define:

```python
VALID_RECORDED_AT = datetime(
    2026,
    7,
    17,
    12,
    0,
    0,
    tzinfo=timezone.utc,
)

VALID_PLACED_AT = datetime(
    2026,
    7,
    17,
    11,
    0,
    0,
    tzinfo=timezone.utc,
)

VALID_EFFECTIVE_AT = datetime(
    2026,
    7,
    17,
    11,
    15,
    0,
    tzinfo=timezone.utc,
)

VALID_REVIEW_AT = datetime(
    2026,
    7,
    18,
    11,
    0,
    0,
    tzinfo=timezone.utc,
)

VALID_EXPIRES_AT = datetime(
    2026,
    7,
    19,
    11,
    0,
    0,
    tzinfo=timezone.utc,
)

VALID_TARGET_REF = "research_os"
VALID_BLOCKED_CONSEQUENCE_REF = "release"
VALID_SCOPE_REF = "SCOPE-000001"
VALID_REASON_REF = "REASON-000001"
VALID_RESOLUTION_CONDITION_REF = "RESOLUTION-000001"
VALID_TARGET_VERSION_REF = "RR-000000202"
VALID_BRANCH_REF = "BRANCH-000001"
VALID_CONTEXT_REF = "CONTEXT-000001"
VALID_TRIGGER_REF = "EVAL-000001"
VALID_BASIS_REF = "EVIDENCE-000001"
VALID_OWNER_REF = "OWNER-000001"
VALID_PLACED_BY_REF = "ACTOR-000001"
VALID_PLACEMENT_AUTHORITY_REF = "AUTHORITY-000001"
VALID_RELEASE_AUTHORITY_REF = "AUTHORITY-000002"
```

These are test values only.

They must not become production defaults.

---

# INVALID TIMEZONE FIXTURE

The suite may define:

```python
class InvalidTimezone(tzinfo):
    def utcoffset(self, dt):
        return None

    def dst(self, dt):
        return None

    def tzname(self, dt):
        return "INVALID"
```

This proves that a non-`None` `tzinfo` without a usable offset remains invalid.

---

# VALID HEADER FACTORY

A private helper may construct a valid Hold header:

```python
def make_hold_header(**overrides):
    values = {
        "record_id": "RR-000000401",
        "record_category": "HOLD",
        "recorded_at": VALID_RECORDED_AT,
        "schema_version": "1.0",
        "provenance_ref": None,
        "external_id": None,
    }
    values.update(overrides)
    return RuntimeRecordHeader(**values)
```

---

# HOLD FACTORY

A private helper may construct a minimal valid Hold:

```python
def make_hold(**overrides):
    values = {
        "header": make_hold_header(),
        "target_ref": VALID_TARGET_REF,
        "blocked_consequence_ref": VALID_BLOCKED_CONSEQUENCE_REF,
        "scope_ref": VALID_SCOPE_REF,
        "reason_ref": VALID_REASON_REF,
        "resolution_condition_ref": VALID_RESOLUTION_CONDITION_REF,
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
```

Boundary:

```text
Test Factory
≠
Production Factory
```

---

# TEST GROUP 1 — MODEL SHAPE

## Test 1

```text
test_hold_record_is_a_dataclass
```

Assert:

```python
assert is_dataclass(HoldRecord)
```

---

## Test 2

```text
test_hold_record_declares_exact_field_order
```

Expected fields:

```python
[
    "header",
    "target_ref",
    "blocked_consequence_ref",
    "scope_ref",
    "reason_ref",
    "resolution_condition_ref",
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
]
```

This also proves absence of prohibited fields such as:

* `hold_id`
* `status`
* `is_active`
* `active`
* `current`
* `expired`
* `inactive`
* `resolved`
* `released`
* `released_at`
* `released_by_ref`
* `release_status`
* `release_decision_ref`
* `progression_condition`
* `evaluation_result`
* `failed`
* `refused`
* `evidence`
* `metadata`
* `payload`

---

# TEST GROUP 2 — MINIMAL CONSTRUCTION

## Test 3

```text
test_hold_record_accepts_required_fields_only
```

Construct with only the six required fields.

Assert:

* header category is `HOLD`
* required values are preserved exactly
* every optional field is `None`

---

## Test 4

```text
test_hold_record_preserves_exact_header_instance
```

Assert:

```python
record.header is header
```

---

## Test 5

```text
test_hold_record_identity_is_supplied_by_header_record_id
```

Assert:

```python
record.header.record_id == "RR-000000401"
assert not hasattr(record, "hold_id")
```

---

# TEST GROUP 3 — CONTEXT-RICH CONSTRUCTION

## Test 6

```text
test_hold_record_accepts_all_valid_optional_fields
```

Supply every optional field and assert exact preservation.

---

## Test 7

```text
test_hold_record_preserves_reference_values_exactly
```

Use values with surrounding whitespace for every reference field.

Assert no normalization.

---

## Test 8

```text
test_hold_record_allows_equal_strings_across_reference_fields
```

Use `"same"` across multiple reference dimensions.

Assert successful construction.

---

# TEST GROUP 4 — REQUIRED FIELDS

## Test 9

```text
test_hold_record_requires_each_required_field
```

Parameterize omission of:

```text
header
target_ref
blocked_consequence_ref
scope_ref
reason_ref
resolution_condition_ref
```

Expected:

```text
TypeError
```

---

# TEST GROUP 5 — HEADER TYPE

## Test 10

```text
test_hold_header_rejects_non_runtime_record_header_values
```

Invalid values:

```python
[
    None,
    "RR-000000401",
    {},
    [],
    (),
    1,
    True,
]
```

Expected:

```text
TypeError mentioning header
```

---

# TEST GROUP 6 — HEADER CATEGORY

## Test 11

```text
test_hold_header_accepts_hold_record_category
```

Use:

```text
HOLD
```

---

## Test 12

```text
test_hold_header_rejects_non_hold_categories
```

Parameterized categories:

```text
EVENT
VERSION
PROGRESSION_ASSERTION
EVALUATION
CUSTOM_RECORD
```

Expected:

```text
ValueError mentioning header or record_category
```

---

# TEST GROUP 7 — REQUIRED REFERENCE TYPES

## Test 13

```text
test_required_references_reject_non_string_values
```

Parameterize fields:

```text
target_ref
blocked_consequence_ref
scope_ref
reason_ref
resolution_condition_ref
```

Invalid values:

```python
[
    None,
    1,
    1.0,
    True,
    b"reference",
    [],
    {},
    (),
]
```

Expected exception must identify the field.

---

# TEST GROUP 8 — REQUIRED REFERENCE VALUES

## Test 14

```text
test_required_references_accept_non_empty_strings
```

Use valid open-vocabulary strings for every required reference.

---

## Test 15

```text
test_required_references_preserve_surrounding_whitespace
```

Assert exact value preservation.

---

## Test 16

```text
test_required_references_reject_empty_or_whitespace_only_values
```

Invalid values:

```python
[
    "",
    " ",
    "\t",
    "\n",
    "\r\n",
    "   \t  ",
]
```

Expected:

```text
ValueError identifying the field
```

---

# TEST GROUP 9 — TARGET AND CONSEQUENCE SEPARATION

## Test 17

```text
test_target_and_blocked_consequence_are_distinct_fields
```

Assert:

```python
record.target_ref == "OBJ-000001"
record.blocked_consequence_ref == "release"
```

---

## Test 18

```text
test_blocked_consequence_uses_open_reference_vocabulary
```

Valid examples:

```text
progression
release
execution
merge
revision
admission
authorization
publication
deployment
custom/consequence
" release "
0
x
```

Assert exact preservation.

---

## Test 19

```text
test_blocked_consequence_is_not_normalized
```

Prove values such as:

```text
release
Release
RELEASE
" release "
```

remain distinct preserved strings.

---

# TEST GROUP 10 — OPTIONAL REFERENCE TYPES

## Test 20

```text
test_optional_references_reject_non_string_non_none_values
```

Parameterize fields:

```text
target_version_ref
branch_ref
context_ref
trigger_ref
basis_ref
owner_ref
placed_by_ref
placement_authority_ref
release_authority_ref
```

Invalid values:

```python
[
    1,
    1.0,
    True,
    b"reference",
    [],
    {},
    (),
]
```

Expected exception must identify the field.

---

# TEST GROUP 11 — OPTIONAL REFERENCE VALUES

## Test 21

```text
test_optional_references_accept_none
```

Parameterize all optional reference fields.

---

## Test 22

```text
test_optional_references_accept_non_empty_strings
```

Assert exact preservation.

---

## Test 23

```text
test_optional_references_preserve_surrounding_whitespace
```

Assert no normalization.

---

## Test 24

```text
test_optional_references_reject_empty_or_whitespace_only_values
```

Expected field-specific `ValueError`.

---

# TEST GROUP 12 — REFERENCE SEMANTIC SEPARATION

## Test 25

```text
test_reason_and_trigger_are_distinct_fields
```

---

## Test 26

```text
test_trigger_and_basis_are_distinct_fields
```

---

## Test 27

```text
test_owner_and_placed_by_are_distinct_fields
```

---

## Test 28

```text
test_placement_and_release_authority_are_distinct_fields
```

---

## Test 29

```text
test_equal_reference_values_do_not_fail_cross_field_validation
```

Use the same string across:

* target and target version
* scope and context
* reason and trigger
* trigger and basis
* owner and placed by
* placement and release authority

Assert successful construction.

---

# TEST GROUP 13 — PLACED_AT

## Test 30

```text
test_placed_at_rejects_non_datetime_non_none_values
```

Expected:

```text
TypeError mentioning placed_at
```

---

## Test 31

```text
test_placed_at_rejects_naive_datetime
```

Expected:

```text
ValueError
```

---

## Test 32

```text
test_placed_at_rejects_timezone_with_no_usable_offset
```

Use `InvalidTimezone`.

---

## Test 33

```text
test_placed_at_accepts_and_preserves_non_utc_timezone
```

Use UTC−07:00.

---

# TEST GROUP 14 — EFFECTIVE_AT

## Test 34

```text
test_effective_at_rejects_non_datetime_non_none_values
```

---

## Test 35

```text
test_effective_at_rejects_naive_datetime
```

---

## Test 36

```text
test_effective_at_rejects_timezone_with_no_usable_offset
```

---

## Test 37

```text
test_effective_at_accepts_and_preserves_non_utc_timezone
```

Use UTC+05:30.

---

# TEST GROUP 15 — REVIEW_AT

## Test 38

```text
test_review_at_rejects_non_datetime_non_none_values
```

---

## Test 39

```text
test_review_at_rejects_naive_datetime
```

---

## Test 40

```text
test_review_at_rejects_timezone_with_no_usable_offset
```

---

## Test 41

```text
test_review_at_accepts_and_preserves_non_utc_timezone
```

---

# TEST GROUP 16 — EXPIRES_AT

## Test 42

```text
test_expires_at_rejects_non_datetime_non_none_values
```

---

## Test 43

```text
test_expires_at_rejects_naive_datetime
```

---

## Test 44

```text
test_expires_at_rejects_timezone_with_no_usable_offset
```

---

## Test 45

```text
test_expires_at_accepts_and_preserves_non_utc_timezone
```

---

# TEST GROUP 17 — TEMPORAL SEPARATION

## Test 46

```text
test_placed_at_does_not_default_to_recorded_at
```

Assert:

```python
record.placed_at is None
```

---

## Test 47

```text
test_effective_at_does_not_default_to_placed_at
```

---

## Test 48

```text
test_review_at_does_not_default_from_effective_at
```

---

## Test 49

```text
test_expires_at_does_not_default_from_review_at
```

---

## Test 50

```text
test_effective_at_may_precede_placed_at
```

Assert successful construction.

---

## Test 51

```text
test_review_at_may_precede_effective_at
```

Assert successful construction.

---

## Test 52

```text
test_expires_at_may_precede_review_at
```

Assert successful construction.

---

## Test 53

```text
test_expires_at_may_precede_effective_at
```

Assert successful construction.

---

## Test 54

```text
test_past_expiry_is_structurally_accepted
```

Use an aware expiry earlier than the recorded time.

Assert successful construction and exact preservation.

---

# TEST GROUP 18 — VALIDATION PRECEDENCE

## Test 55

```text
test_header_type_failure_precedes_target_failure
```

---

## Test 56

```text
test_header_category_failure_precedes_target_failure
```

---

## Test 57

```text
test_target_failure_precedes_blocked_consequence_failure
```

---

## Test 58

```text
test_blocked_consequence_failure_precedes_scope_failure
```

---

## Test 59

```text
test_scope_failure_precedes_reason_failure
```

---

## Test 60

```text
test_reason_failure_precedes_resolution_condition_failure
```

---

## Test 61

```text
test_resolution_condition_failure_precedes_target_version_failure
```

---

## Test 62

```text
test_target_version_failure_precedes_branch_failure
```

---

## Test 63

```text
test_branch_failure_precedes_context_failure
```

---

## Test 64

```text
test_context_failure_precedes_trigger_failure
```

---

## Test 65

```text
test_trigger_failure_precedes_basis_failure
```

---

## Test 66

```text
test_basis_failure_precedes_owner_failure
```

---

## Test 67

```text
test_owner_failure_precedes_placed_by_failure
```

---

## Test 68

```text
test_placed_by_failure_precedes_placement_authority_failure
```

---

## Test 69

```text
test_placement_authority_failure_precedes_release_authority_failure
```

---

## Test 70

```text
test_release_authority_failure_precedes_placed_at_failure
```

---

## Test 71

```text
test_placed_at_failure_precedes_effective_at_failure
```

---

## Test 72

```text
test_effective_at_failure_precedes_review_at_failure
```

---

## Test 73

```text
test_review_at_failure_precedes_expires_at_failure
```

---

# TEST GROUP 19 — RELEASE-FIELD ABSENCE

## Test 74

```text
test_hold_record_exposes_no_release_fields
```

Assert absence of:

```text
released
release_status
released_at
released_by_ref
release_decision_ref
resolved
resolution_status
```

---

# TEST GROUP 20 — ACTIVE-STATE ABSENCE

## Test 75

```text
test_hold_record_exposes_no_active_state_fields
```

Assert absence of:

```text
is_active
active
current
expired
inactive
```

---

# TEST GROUP 21 — AUTOMATIC RELEASE ABSENCE

## Test 76

```text
test_past_expiry_does_not_add_release_or_active_state
```

Construct with past `expires_at`.

Assert release and active-state fields remain absent.

---

## Test 77

```text
test_resolution_condition_reference_does_not_create_release_state
```

Assert the presence of `resolution_condition_ref` does not create release fields.

---

# TEST GROUP 22 — CONTROL BOUNDARIES

## Test 78

```text
test_hold_record_contains_no_progression_condition_field
```

---

## Test 79

```text
test_hold_record_contains_no_evaluation_result_field
```

---

## Test 80

```text
test_hold_record_contains_no_refusal_fields
```

Assert absence of:

```text
refused
refusal_reason
```

---

## Test 81

```text
test_hold_record_contains_no_failure_fields
```

Assert absence of:

```text
failed
failure_reason
```

---

# TEST GROUP 23 — IMMUTABILITY

## Test 82

```text
test_hold_record_is_frozen
```

Parameterize all nineteen fields.

Attempt reassignment.

Expected:

```text
FrozenInstanceError
```

---

# TEST GROUP 24 — EQUALITY

## Test 83

```text
test_identical_hold_records_compare_equal
```

---

## Test 84

```text
test_hold_record_equality_is_full_structural_equality
```

Parameterize differences across all nineteen fields.

Assert inequality.

---

## Test 85

```text
test_same_header_with_different_target_is_not_equal
```

---

## Test 86

```text
test_same_target_with_different_blocked_consequence_is_not_equal
```

---

## Test 87

```text
test_same_target_and_consequence_with_different_scope_is_not_equal
```

---

## Test 88

```text
test_same_hold_with_different_reason_is_not_equal
```

---

## Test 89

```text
test_same_hold_with_different_resolution_condition_is_not_equal
```

---

## Test 90

```text
test_same_hold_with_different_authority_reference_is_not_equal
```

---

## Test 91

```text
test_equivalent_temporal_instants_follow_python_datetime_equality
```

Use two offsets representing the same instant.

---

# TEST GROUP 25 — HASHING

## Test 92

```text
test_equal_hold_records_have_equal_hashes
```

---

## Test 93

```text
test_structurally_different_hold_records_can_coexist_in_a_set
```

---

## Test 94

```text
test_hashing_does_not_change_hold_record
```

---

# TEST GROUP 26 — ORDERING

## Test 95

```text
test_hold_records_do_not_support_ordering
```

Assert:

```python
with pytest.raises(TypeError):
    _ = hold_a < hold_b
```

---

# TEST GROUP 27 — SERIALIZATION ABSENCE

## Test 96

```text
test_hold_record_exposes_no_serialization_methods
```

Assert absence of:

```text
to_dict
from_dict
to_json
from_json
```

---

# TEST GROUP 28 — APPLICATION BOUNDARY

## Test 97

```text
test_hold_record_does_not_accept_application_object_dictionary_as_header
```

Expected:

```text
TypeError mentioning header
```

---

## Test 98

```text
test_application_status_values_do_not_create_hold_records
```

Application values such as:

```text
UNKNOWN
Active
OPEN
```

must not appear as implicit Hold state or accepted header substitutes.

---

# TEST GROUP 29 — SERVICE ISOLATION

## Test 99

```text
test_importing_hold_record_does_not_import_object_engine
```

---

## Test 100

```text
test_importing_hold_record_does_not_import_progression_assertion_record
```

---

## Test 101

```text
test_importing_hold_record_does_not_import_runtime_event_record
```

---

## Test 102

```text
test_importing_hold_record_does_not_import_runtime_object_version_record
```

---

## Test 103

```text
test_importing_hold_record_does_not_import_streamlit
```

Use the safe pre-existing-import pattern.

---

# TEST GROUP 30 — DIRECT IMPORT

## Test 104

```text
test_hold_record_module_can_be_imported_directly
```

Assert class identity without removing or reloading the module.

---

# TEST GROUP 31 — HEADER PRESERVATION

## Test 105

```text
test_hold_record_does_not_modify_composed_header
```

Capture all header fields before construction.

Assert unchanged afterward.

---

# TEST GROUP 32 — OPEN REFERENCE VOCABULARY

## Test 106

```text
test_hold_record_does_not_restrict_reference_prefixes
```

Use custom references without expected prefixes.

Assert successful construction.

---

# TEST GROUP 33 — NO CROSS-FIELD IDENTITY INFERENCE

## Test 107

```text
test_hold_record_allows_reference_fields_to_share_values
```

Use equal strings across all semantically distinct reference dimensions.

Assert successful construction.

---

# TEST GROUP 34 — NO SIDE EFFECTS

## Test 108

```text
test_constructing_hold_record_does_not_create_progression_assertion
```

Assert no progression object or field is created.

---

## Test 109

```text
test_constructing_hold_record_does_not_create_runtime_event
```

Assert no event object or field is created.

---

## Test 110

```text
test_constructing_hold_record_does_not_enforce_blocking
```

Assert construction returns only the immutable record and invokes no external service.

---

# FINAL LOGICAL TEST LIST

The future test file should contain these 110 logical test functions or parameterized groups.

Parameterized groups will expand into substantially more collected cases.

Behavioral coverage is frozen; the cosmetic collected total is not.

---

# EXPECTED PYTEST CASE COUNT

Expected new Hold Record cases:

```text
approximately 350–450
```

Current frozen baseline:

```text
869 passed
```

Expected eventual full-suite range after implementation:

```text
approximately 1,219–1,319 passed
```

The exact collected case count must be recorded after the test file is written.

---

# PARAMETERIZATION RULE

Use `pytest.mark.parametrize` for:

* required-field omission
* invalid header types
* invalid header categories
* required-reference fields
* required-reference type and value cases
* optional-reference fields
* optional-reference type and value cases
* temporal fields
* temporal type failures
* immutability fields
* structural inequality fields
* validation precedence groups where appropriate

Do not combine unrelated semantic responsibilities into one oversized test.

---

# ERROR ASSERTION RULE

Tests should assert:

* exception class
* meaningful field-name fragment

Examples:

```python
with pytest.raises(TypeError, match="target_ref"):
    ...
```

```python
with pytest.raises(ValueError, match="resolution_condition_ref"):
    ...
```

Do not freeze complete punctuation unnecessarily.

---

# VALIDATION PRECEDENCE RULE

Tests must validate externally observable precedence only.

Frozen sequence:

```text
header
→
header category
→
target
→
blocked consequence
→
scope
→
reason
→
resolution condition
→
target version
→
branch
→
context
→
trigger
→
basis
→
owner
→
placed by
→
placement authority
→
release authority
→
placed time
→
effective time
→
review time
→
expiry time
```

Tests must not inspect private helper names or source layout.

---

# IMPORT-ISOLATION RULE

Import-isolation tests must not:

* remove the production module from `sys.modules`
* reload the production class
* instantiate ObjectEngine
* load application JSON
* import application pages
* create Runtime Events
* create progression assertions
* invoke authority or release services

They may inspect whether prohibited modules were newly imported.

---

# EXPECTED FAILURE BEFORE IMPLEMENTATION

After creating the test file but before production implementation, run:

```bat
python -m pytest tests\runtime\test_hold_record.py -q
```

Expected collection failure:

```text
ModuleNotFoundError:
No module named 'models.hold_record'
```

The failure must be observed and committed before production implementation.

Frozen suites must remain intact:

```bat
python -m pytest tests\runtime\test_runtime_record_identity.py -q
python -m pytest tests\runtime\test_runtime_event_record.py -q
python -m pytest tests\runtime\test_runtime_object_version_record.py -q
python -m pytest tests\runtime\test_progression_assertion_record.py -q
```

Expected:

```text
159 passed
203 passed
186 passed
321 passed
```

Boundary:

```text
Expected Missing-Model Failure
≠
Architecture Failure
```

---

# TEST CONTRACT NON-GOALS

The suite must not test:

1. application-page behavior
2. ObjectEngine behavior
3. application-status migration
4. actual consequence blocking
5. operation refusal
6. Runtime Event publication
7. progression `HELD` creation
8. Evaluation `HOLD` creation
9. placement-authority validity
10. release-authority validity
11. active-Hold projection
12. release eligibility
13. Hold release
14. automatic expiry handling
15. resolution-condition satisfaction
16. target existence
17. target-version existence
18. target/version compatibility
19. scope existence
20. branch existence
21. context existence
22. trigger causality
23. basis sufficiency
24. owner capability
25. temporal coherence
26. serialization
27. persistence
28. registry uniqueness
29. Platform Registry integration
30. Research Kernel service integration
31. Hold-history reconstruction
32. Hold supersession
33. Hold invalidation
34. release-record design

---

# TEST CONTRACT INVARIANTS

## Invariant 1

Tests must precede production implementation.

## Invariant 2

Every required field must have omission coverage.

## Invariant 3

Every validated field must have type-failure coverage.

## Invariant 4

Every constrained reference must have positive and negative value coverage.

## Invariant 5

Every optional field must accept `None`.

## Invariant 6

Every valid reference must preserve exact input.

## Invariant 7

Target and blocked consequence remain separate.

## Invariant 8

Reason and trigger remain separate.

## Invariant 9

Trigger and basis remain separate.

## Invariant 10

Owner and authority remain separate.

## Invariant 11

Resolution condition does not create release state.

## Invariant 12

Expiry does not create release or inactive state.

## Invariant 13

Recorded, placed, effective, review, and expiry times remain distinct.

## Invariant 14

Temporal ordering remains outside the model.

## Invariant 15

Validation precedence remains externally observable.

## Invariant 16

Every field is covered by immutability tests.

## Invariant 17

Every field participates in structural equality.

## Invariant 18

Hashing remains consistent with equality.

## Invariant 19

Ordering remains unsupported.

## Invariant 20

Release fields remain absent.

## Invariant 21

Active-state fields remain absent.

## Invariant 22

Serialization remains absent.

## Invariant 23

Progression, Evaluation, refusal, and failure semantics remain absent.

## Invariant 24

ObjectEngine, progression, event, version, and Streamlit modules remain unimported.

## Invariant 25

The composed header remains unchanged.

## Invariant 26

No test requires filesystem, service, authority, blocking, or release setup.

## Invariant 27

The failing pre-implementation baseline must be recorded.

Status:

**FROZEN**

---

# TEST CONTRACT DECISION

Test path:
**FROZEN**

Framework:
**FROZEN**

Header fixture:
**FROZEN**

Minimal Hold fixture:
**FROZEN**

Context-rich Hold fixture:
**FROZEN**

Header tests:
**FROZEN**

Required-reference tests:
**FROZEN**

Optional-reference tests:
**FROZEN**

Target and consequence separation tests:
**FROZEN**

Reason, trigger, and basis tests:
**FROZEN**

Owner and authority separation tests:
**FROZEN**

Temporal tests:
**FROZEN**

Temporal-separation tests:
**FROZEN**

Validation-precedence tests:
**FROZEN**

Release-field absence tests:
**FROZEN**

Active-state absence tests:
**FROZEN**

Automatic-release absence tests:
**FROZEN**

Control-boundary tests:
**FROZEN**

Immutability tests:
**FROZEN**

Equality and hashing tests:
**FROZEN**

Ordering test:
**FROZEN**

Serialization-absence test:
**FROZEN**

Service-isolation tests:
**FROZEN**

Direct-import test:
**FROZEN**

Production implementation:
**HOLD**

---

# READINESS CHECKPOINT 4

Hold Record Test Contract:

**COMPLETE**

The test suite may now be written before production implementation.

Production implementation remains unauthorized until:

1. the test file is created
2. the expected missing-model failure is observed
3. all frozen suites remain independently passing
4. the test baseline is reviewed
5. the tests are committed before implementation
6. minimal production implementation is separately admitted

---

# NEXT SESSION

Begin:

**HOLD RECORD FOUNDATION — TESTS BEFORE IMPLEMENTATION 001**

Required sequence:

1. create `tests\runtime\test_hold_record.py`
2. paste the complete frozen test suite
3. run the isolated new suite
4. confirm expected missing-model failure
5. run Runtime Record Identity tests
6. run Runtime Event tests
7. run Runtime Object Version tests
8. run Progression Assertion tests
9. confirm frozen suites remain passing
10. inspect Git status
11. commit tests before implementation
12. preserve production implementation HOLD

**UNKNOWN → HOLD**
