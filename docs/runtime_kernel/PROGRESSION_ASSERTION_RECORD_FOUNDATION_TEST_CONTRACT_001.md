# RESEARCH OS — PROGRESSION ASSERTION RECORD FOUNDATION

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
ProgressionAssertionRecord
```

The test suite must prove:

1. immutable header composition
2. `PROGRESSION_ASSERTION` category enforcement
3. minimal valid construction
4. context-rich valid construction
5. required target validation
6. closed asserted-condition vocabulary
7. required scope validation
8. optional target-version semantics
9. optional prior-condition semantics
10. optional branch and context semantics
11. optional actor, source, and basis semantics
12. asserted-time validation
13. effective-time validation
14. temporal separation
15. deterministic validation precedence
16. immutability
17. full structural equality
18. structural hashing
19. ordering prohibition
20. serialization absence
21. application and service isolation
22. preservation of all frozen Runtime Kernel foundations

This document does not authorize production implementation.

---

# PREREQUISITE

Immutable Contract 001 froze:

## Production Path

```text
models/progression_assertion_record.py
```

## Test Path

```text
tests/runtime/test_progression_assertion_record.py
```

## Model

```text
ProgressionAssertionRecord
```

## Required Fields

```python
header: RuntimeRecordHeader
target_ref: str
asserted_condition: str
scope_ref: str
```

## Optional Fields

```python
target_version_ref: str | None = None
prior_condition: str | None = None
branch_ref: str | None = None
context_ref: str | None = None
asserted_at: datetime | None = None
effective_at: datetime | None = None
actor_ref: str | None = None
source_ref: str | None = None
basis_ref: str | None = None
```

## Required Header Category

```text
PROGRESSION_ASSERTION
```

## Accepted Progression Conditions

```text
PENDING
ACTIVE
HELD
DORMANT
ABANDONED
```

## Frozen Boundaries

* assertion does not establish truth
* assertion does not establish authority
* assertion does not establish admission
* assertion does not establish canonical progression
* prior and asserted conditions do not prove transition
* `HELD` does not create a Hold record
* `CONFLICTING` is not a progression condition
* application status is not Runtime progression
* no persistence
* no services
* no serialization

---

# OPERATING RULES

* Write tests before production implementation.
* Do not create the production model during the test-writing session.
* Do not modify `RuntimeRecordHeader`.
* Do not modify any frozen Runtime Kernel model.
* Do not modify application object status fields.
* Do not import or initialize ObjectEngine.
* Do not create Runtime Events.
* Do not create Hold records.
* Do not evaluate authority or admission.
* Do not calculate canonical progression.
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
    └── test_progression_assertion_record.py
```

No new `conftest.py` is required.

Production import:

```python
from models.progression_assertion_record import (
    ProgressionAssertionRecord,
)
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

from models.progression_assertion_record import (
    ProgressionAssertionRecord,
)
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

VALID_ASSERTED_AT = datetime(
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

A private helper may construct a valid Progression Assertion header:

```python
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
```

---

# ASSERTION FACTORY

A private helper may construct a minimal valid assertion:

```python
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
test_progression_assertion_record_is_a_dataclass
```

Assert:

```python
assert is_dataclass(ProgressionAssertionRecord)
```

---

## Test 2

```text
test_progression_assertion_record_declares_exact_field_order
```

Expected fields:

```python
[
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
```

This also proves absence of prohibited fields such as:

* `assertion_id`
* `status`
* `object_status`
* `current_condition`
* `canonical_condition`
* `is_current`
* `valid`
* `admitted`
* `authorized`
* `approved`
* `hold_ref`
* `blocked`
* `conflicting`
* `evidence`
* `evidence_refs`
* `rationale`
* `transitioned`
* `supersedes`

---

# TEST GROUP 2 — MINIMAL CONSTRUCTION

## Test 3

```text
test_progression_assertion_record_accepts_required_fields_only
```

Construct with:

```python
ProgressionAssertionRecord(
    header=make_progression_header(),
    target_ref=VALID_TARGET_REF,
    asserted_condition=VALID_ASSERTED_CONDITION,
    scope_ref=VALID_SCOPE_REF,
)
```

Assert:

* header category is `PROGRESSION_ASSERTION`
* required fields preserve exact values
* every optional field is `None`

---

## Test 4

```text
test_progression_assertion_record_preserves_exact_header_instance
```

Assert:

```python
record.header is header
```

---

## Test 5

```text
test_progression_assertion_identity_is_supplied_by_header_record_id
```

Assert:

```python
record.header.record_id == "RR-000000301"
assert not hasattr(record, "assertion_id")
```

---

# TEST GROUP 3 — CONTEXT-RICH CONSTRUCTION

## Test 6

```text
test_progression_assertion_record_accepts_all_valid_optional_fields
```

Supply every optional field and assert exact preservation.

---

## Test 7

```text
test_progression_assertion_record_preserves_reference_values_exactly
```

Use values with surrounding whitespace:

```text
" target "
" scope "
" target-version "
" branch "
" context "
" actor "
" source "
" basis "
```

Assert no normalization.

---

## Test 8

```text
test_progression_assertion_record_allows_equal_strings_across_reference_fields
```

Use `"same"` for multiple reference dimensions.

Assert successful construction.

This proves equal strings do not establish equal semantic identity.

---

# TEST GROUP 4 — REQUIRED FIELDS

## Test 9

```text
test_progression_assertion_record_requires_each_required_field
```

Parameterize omission of:

```text
header
target_ref
asserted_condition
scope_ref
```

Expected:

```text
TypeError
```

---

# TEST GROUP 5 — HEADER TYPE

## Test 10

```text
test_header_rejects_non_runtime_record_header_values
```

Invalid values:

```python
[
    None,
    "RR-000000301",
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
test_header_accepts_progression_assertion_record_category
```

Use:

```text
PROGRESSION_ASSERTION
```

---

## Test 12

```text
test_header_rejects_non_progression_assertion_categories
```

Parameterized categories:

```text
EVENT
VERSION
HOLD
EVALUATION
CUSTOM_RECORD
```

Expected:

```text
ValueError mentioning header or record_category
```

---

# TEST GROUP 7 — TARGET_REF

## Test 13

```text
test_target_ref_rejects_non_string_values
```

Invalid values include:

```python
[
    None,
    1,
    1.0,
    True,
    b"target",
    [],
    {},
    (),
]
```

Expected:

```text
TypeError mentioning target_ref
```

---

## Test 14

```text
test_target_ref_accepts_non_empty_strings
```

Valid values:

```text
research_os
OBJ-000001
RR-000000202
external/target/42
" target "
0
x
```

Assert exact preservation.

---

## Test 15

```text
test_target_ref_rejects_empty_or_whitespace_only_values
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
ValueError mentioning target_ref
```

---

# TEST GROUP 8 — ASSERTED CONDITION TYPE

## Test 16

```text
test_asserted_condition_rejects_non_string_values
```

Invalid values:

```python
[
    None,
    1,
    1.0,
    True,
    b"ACTIVE",
    [],
    {},
    (),
]
```

Expected:

```text
TypeError mentioning asserted_condition
```

---

# TEST GROUP 9 — ASSERTED CONDITION VOCABULARY

## Test 17

```text
test_asserted_condition_accepts_frozen_progression_vocabulary
```

Parameterized accepted values:

```text
PENDING
ACTIVE
HELD
DORMANT
ABANDONED
```

---

## Test 18

```text
test_asserted_condition_rejects_values_outside_frozen_vocabulary
```

Invalid values:

```text
""
" "
UNKNOWN
CONFLICTING
PASS
FAIL
INCONCLUSIVE
VALID
INVALID
CURRENT
COMPLETED
active
Active
ACTIVE 
 ACTIVE
```

Expected:

```text
ValueError mentioning asserted_condition
```

---

## Test 19

```text
test_asserted_condition_is_not_normalized
```

Prove that:

```text
active
Active
ACTIVE 
```

remain rejected rather than converted to `ACTIVE`.

---

# TEST GROUP 10 — SCOPE_REF

## Test 20

```text
test_scope_ref_rejects_non_string_values
```

Include `None` and common non-string values.

Expected:

```text
TypeError mentioning scope_ref
```

---

## Test 21

```text
test_scope_ref_accepts_non_empty_strings
```

Valid values:

```text
SCOPE-000001
research/program/1
institutional
" scope "
0
x
```

---

## Test 22

```text
test_scope_ref_rejects_empty_or_whitespace_only_values
```

Expected:

```text
ValueError mentioning scope_ref
```

---

# TEST GROUP 11 — TARGET_VERSION_REF

## Test 23

```text
test_target_version_ref_rejects_non_string_non_none_values
```

Expected:

```text
TypeError
```

---

## Test 24

```text
test_target_version_ref_accepts_non_empty_strings
```

Valid values:

```text
RR-000000202
legacy-version
external/version/42
" target-version "
0
```

No prefix restriction is permitted.

---

## Test 25

```text
test_target_version_ref_rejects_empty_or_whitespace_only_values
```

Expected:

```text
ValueError
```

---

# TEST GROUP 12 — PRIOR CONDITION

## Test 26

```text
test_prior_condition_rejects_non_string_non_none_values
```

Expected:

```text
TypeError mentioning prior_condition
```

---

## Test 27

```text
test_prior_condition_accepts_frozen_progression_vocabulary
```

Accept all five frozen conditions.

---

## Test 28

```text
test_prior_condition_rejects_values_outside_frozen_vocabulary
```

Reject the same invalid condition family used for `asserted_condition`.

---

## Test 29

```text
test_prior_condition_may_equal_asserted_condition
```

Examples:

```text
ACTIVE → ACTIVE
HELD → HELD
```

Assert successful construction.

This proves the model does not require transition.

---

# TEST GROUP 13 — OPTIONAL REFERENCE TYPES

## Test 30

```text
test_optional_references_reject_non_string_non_none_values
```

Parameterize fields:

```text
target_version_ref
branch_ref
context_ref
actor_ref
source_ref
basis_ref
```

Parameterize invalid values:

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

# TEST GROUP 14 — OPTIONAL REFERENCE VALUES

## Test 31

```text
test_optional_references_accept_none
```

Parameterize all optional reference fields.

---

## Test 32

```text
test_optional_references_accept_non_empty_strings
```

Use common structurally valid values.

---

## Test 33

```text
test_optional_references_reject_empty_or_whitespace_only_values
```

Use common whitespace-only values.

---

# TEST GROUP 15 — ASSERTED_AT TYPE

## Test 34

```text
test_asserted_at_rejects_non_datetime_non_none_values
```

Invalid values:

```python
[
    "2026-07-17T11:30:00Z",
    0,
    1.0,
    True,
    {},
    [],
]
```

Expected:

```text
TypeError mentioning asserted_at
```

---

## Test 35

```text
test_asserted_at_rejects_naive_datetime
```

Expected:

```text
ValueError
```

---

## Test 36

```text
test_asserted_at_rejects_timezone_with_no_usable_offset
```

Use `InvalidTimezone`.

---

## Test 37

```text
test_asserted_at_accepts_and_preserves_non_utc_timezone
```

Use a fixed offset such as UTC−07:00.

Assert:

* exact datetime preserved
* exact timezone object preserved
* offset unchanged

---

# TEST GROUP 16 — EFFECTIVE_AT TYPE

## Test 38

```text
test_effective_at_rejects_non_datetime_non_none_values
```

Expected:

```text
TypeError mentioning effective_at
```

---

## Test 39

```text
test_effective_at_rejects_naive_datetime
```

---

## Test 40

```text
test_effective_at_rejects_timezone_with_no_usable_offset
```

---

## Test 41

```text
test_effective_at_accepts_and_preserves_non_utc_timezone
```

Use a fixed offset such as UTC+05:30.

---

# TEST GROUP 17 — TEMPORAL SEPARATION

## Test 42

```text
test_asserted_at_does_not_default_to_recorded_at
```

Construct without `asserted_at`.

Assert:

```python
record.asserted_at is None
```

---

## Test 43

```text
test_effective_at_does_not_default_to_asserted_at
```

Supply `asserted_at`, omit `effective_at`.

---

## Test 44

```text
test_effective_at_may_precede_asserted_at
```

Assert successful construction.

---

## Test 45

```text
test_asserted_at_may_follow_recorded_at
```

Assert successful construction.

---

## Test 46

```text
test_effective_at_may_follow_recorded_at
```

Assert successful construction.

---

# TEST GROUP 18 — VALIDATION PRECEDENCE

## Test 47

```text
test_header_type_failure_precedes_target_failure
```

Supply invalid values across all fields.

Expected error identifies `header`.

---

## Test 48

```text
test_header_category_failure_precedes_target_failure
```

Expected error identifies header category.

---

## Test 49

```text
test_target_type_failure_precedes_asserted_condition_failure
```

---

## Test 50

```text
test_target_value_failure_precedes_asserted_condition_failure
```

---

## Test 51

```text
test_asserted_condition_failure_precedes_scope_failure
```

---

## Test 52

```text
test_scope_failure_precedes_target_version_failure
```

---

## Test 53

```text
test_target_version_failure_precedes_prior_condition_failure
```

---

## Test 54

```text
test_prior_condition_failure_precedes_branch_failure
```

---

## Test 55

```text
test_branch_failure_precedes_context_failure
```

---

## Test 56

```text
test_context_failure_precedes_asserted_at_failure
```

---

## Test 57

```text
test_asserted_at_failure_precedes_effective_at_failure
```

---

## Test 58

```text
test_effective_at_failure_precedes_actor_failure
```

---

## Test 59

```text
test_actor_failure_precedes_source_failure
```

---

## Test 60

```text
test_source_failure_precedes_basis_failure
```

---

# TEST GROUP 19 — IMMUTABILITY

## Test 61

```text
test_progression_assertion_record_is_frozen
```

Parameterize all thirteen fields.

Attempt reassignment.

Expected:

```text
FrozenInstanceError
```

---

# TEST GROUP 20 — EQUALITY

## Test 62

```text
test_identical_progression_assertion_records_compare_equal
```

---

## Test 63

```text
test_progression_assertion_record_equality_is_full_structural_equality
```

Parameterize differences across all fields:

* header
* target
* asserted condition
* scope
* target version
* prior condition
* branch
* context
* asserted time
* effective time
* actor
* source
* basis

Assert inequality.

---

## Test 64

```text
test_same_header_with_different_asserted_condition_is_not_equal
```

---

## Test 65

```text
test_same_target_and_condition_with_different_scope_is_not_equal
```

---

## Test 66

```text
test_same_target_condition_and_scope_with_different_basis_is_not_equal
```

---

## Test 67

```text
test_equivalent_temporal_instants_follow_python_datetime_equality
```

Use two different offsets representing the same instant.

Assert standard Python equality remains preserved.

---

# TEST GROUP 21 — HASHING

## Test 68

```text
test_equal_progression_assertion_records_have_equal_hashes
```

---

## Test 69

```text
test_structurally_different_progression_assertion_records_can_coexist_in_a_set
```

---

## Test 70

```text
test_hashing_does_not_change_progression_assertion_record
```

Capture all fields before and after `hash(record)`.

---

# TEST GROUP 22 — ORDERING

## Test 71

```text
test_progression_assertion_records_do_not_support_ordering
```

Assert:

```python
with pytest.raises(TypeError):
    _ = assertion_a < assertion_b
```

---

# TEST GROUP 23 — SERIALIZATION ABSENCE

## Test 72

```text
test_progression_assertion_record_exposes_no_serialization_methods
```

Assert absence of:

```text
to_dict
from_dict
to_json
from_json
```

---

# TEST GROUP 24 — APPLICATION STATUS BOUNDARY

## Test 73

```text
test_progression_assertion_record_does_not_accept_application_object_dictionary_as_header
```

Use:

```python
application_object = {
    "id": "research_os",
    "type": "project",
    "status": "Active",
}
```

Expected:

```text
TypeError mentioning header
```

---

## Test 74

```text
test_application_status_values_are_not_accepted_as_progression_conditions
```

Reject examples:

```text
Active
OPEN
UNKNOWN
```

---

# TEST GROUP 25 — HOLD AND CONFLICT BOUNDARY

## Test 75

```text
test_held_condition_does_not_create_hold_fields
```

Construct with:

```text
asserted_condition = HELD
```

Assert absence of:

```text
hold_ref
blocked
control_status
```

---

## Test 76

```text
test_conflicting_is_not_an_accepted_progression_condition
```

Expected:

```text
ValueError
```

---

# TEST GROUP 26 — SERVICE ISOLATION

## Test 77

```text
test_importing_progression_assertion_record_does_not_import_object_engine
```

Use the safe pre-existing-import pattern.

---

## Test 78

```text
test_importing_progression_assertion_record_does_not_import_runtime_event_record
```

Prove the model does not create event coupling.

---

## Test 79

```text
test_importing_progression_assertion_record_does_not_import_runtime_object_version_record
```

Prove references remain strings rather than model coupling.

---

## Test 80

```text
test_importing_progression_assertion_record_does_not_import_streamlit
```

---

# TEST GROUP 27 — DIRECT IMPORT

## Test 81

```text
test_progression_assertion_record_module_can_be_imported_directly
```

Assert class identity without removing or reloading the module.

---

# TEST GROUP 28 — HEADER PRESERVATION

## Test 82

```text
test_progression_assertion_record_does_not_modify_composed_header
```

Capture every header field before construction.

Assert unchanged afterward.

---

# TEST GROUP 29 — OPEN REFERENCE VOCABULARY

## Test 83

```text
test_progression_assertion_record_does_not_restrict_reference_prefixes
```

Use custom references without expected prefixes.

Assert successful construction.

---

# TEST GROUP 30 — NO CROSS-FIELD IDENTITY INFERENCE

## Test 84

```text
test_progression_assertion_record_allows_reference_fields_to_share_values
```

Use equal strings for:

* target and target version
* scope and context
* actor and source
* source and basis

Assert successful construction.

---

# FINAL LOGICAL TEST LIST

The future test file should contain these 84 logical test functions or parameterized groups:

1. `test_progression_assertion_record_is_a_dataclass`
2. `test_progression_assertion_record_declares_exact_field_order`
3. `test_progression_assertion_record_accepts_required_fields_only`
4. `test_progression_assertion_record_preserves_exact_header_instance`
5. `test_progression_assertion_identity_is_supplied_by_header_record_id`
6. `test_progression_assertion_record_accepts_all_valid_optional_fields`
7. `test_progression_assertion_record_preserves_reference_values_exactly`
8. `test_progression_assertion_record_allows_equal_strings_across_reference_fields`
9. `test_progression_assertion_record_requires_each_required_field`
10. `test_header_rejects_non_runtime_record_header_values`
11. `test_header_accepts_progression_assertion_record_category`
12. `test_header_rejects_non_progression_assertion_categories`
13. `test_target_ref_rejects_non_string_values`
14. `test_target_ref_accepts_non_empty_strings`
15. `test_target_ref_rejects_empty_or_whitespace_only_values`
16. `test_asserted_condition_rejects_non_string_values`
17. `test_asserted_condition_accepts_frozen_progression_vocabulary`
18. `test_asserted_condition_rejects_values_outside_frozen_vocabulary`
19. `test_asserted_condition_is_not_normalized`
20. `test_scope_ref_rejects_non_string_values`
21. `test_scope_ref_accepts_non_empty_strings`
22. `test_scope_ref_rejects_empty_or_whitespace_only_values`
23. `test_target_version_ref_rejects_non_string_non_none_values`
24. `test_target_version_ref_accepts_non_empty_strings`
25. `test_target_version_ref_rejects_empty_or_whitespace_only_values`
26. `test_prior_condition_rejects_non_string_non_none_values`
27. `test_prior_condition_accepts_frozen_progression_vocabulary`
28. `test_prior_condition_rejects_values_outside_frozen_vocabulary`
29. `test_prior_condition_may_equal_asserted_condition`
30. `test_optional_references_reject_non_string_non_none_values`
31. `test_optional_references_accept_none`
32. `test_optional_references_accept_non_empty_strings`
33. `test_optional_references_reject_empty_or_whitespace_only_values`
34. `test_asserted_at_rejects_non_datetime_non_none_values`
35. `test_asserted_at_rejects_naive_datetime`
36. `test_asserted_at_rejects_timezone_with_no_usable_offset`
37. `test_asserted_at_accepts_and_preserves_non_utc_timezone`
38. `test_effective_at_rejects_non_datetime_non_none_values`
39. `test_effective_at_rejects_naive_datetime`
40. `test_effective_at_rejects_timezone_with_no_usable_offset`
41. `test_effective_at_accepts_and_preserves_non_utc_timezone`
42. `test_asserted_at_does_not_default_to_recorded_at`
43. `test_effective_at_does_not_default_to_asserted_at`
44. `test_effective_at_may_precede_asserted_at`
45. `test_asserted_at_may_follow_recorded_at`
46. `test_effective_at_may_follow_recorded_at`
47. `test_header_type_failure_precedes_target_failure`
48. `test_header_category_failure_precedes_target_failure`
49. `test_target_type_failure_precedes_asserted_condition_failure`
50. `test_target_value_failure_precedes_asserted_condition_failure`
51. `test_asserted_condition_failure_precedes_scope_failure`
52. `test_scope_failure_precedes_target_version_failure`
53. `test_target_version_failure_precedes_prior_condition_failure`
54. `test_prior_condition_failure_precedes_branch_failure`
55. `test_branch_failure_precedes_context_failure`
56. `test_context_failure_precedes_asserted_at_failure`
57. `test_asserted_at_failure_precedes_effective_at_failure`
58. `test_effective_at_failure_precedes_actor_failure`
59. `test_actor_failure_precedes_source_failure`
60. `test_source_failure_precedes_basis_failure`
61. `test_progression_assertion_record_is_frozen`
62. `test_identical_progression_assertion_records_compare_equal`
63. `test_progression_assertion_record_equality_is_full_structural_equality`
64. `test_same_header_with_different_asserted_condition_is_not_equal`
65. `test_same_target_and_condition_with_different_scope_is_not_equal`
66. `test_same_target_condition_and_scope_with_different_basis_is_not_equal`
67. `test_equivalent_temporal_instants_follow_python_datetime_equality`
68. `test_equal_progression_assertion_records_have_equal_hashes`
69. `test_structurally_different_progression_assertion_records_can_coexist_in_a_set`
70. `test_hashing_does_not_change_progression_assertion_record`
71. `test_progression_assertion_records_do_not_support_ordering`
72. `test_progression_assertion_record_exposes_no_serialization_methods`
73. `test_progression_assertion_record_does_not_accept_application_object_dictionary_as_header`
74. `test_application_status_values_are_not_accepted_as_progression_conditions`
75. `test_held_condition_does_not_create_hold_fields`
76. `test_conflicting_is_not_an_accepted_progression_condition`
77. `test_importing_progression_assertion_record_does_not_import_object_engine`
78. `test_importing_progression_assertion_record_does_not_import_runtime_event_record`
79. `test_importing_progression_assertion_record_does_not_import_runtime_object_version_record`
80. `test_importing_progression_assertion_record_does_not_import_streamlit`
81. `test_progression_assertion_record_module_can_be_imported_directly`
82. `test_progression_assertion_record_does_not_modify_composed_header`
83. `test_progression_assertion_record_does_not_restrict_reference_prefixes`
84. `test_progression_assertion_record_allows_reference_fields_to_share_values`

---

# EXPECTED PYTEST CASE COUNT

Parameterized groups will expand the logical test count.

Expected new Progression Assertion cases:

```text
approximately 260–340
```

Current frozen baseline:

```text
548 passed
```

Expected eventual full-suite range after implementation:

```text
approximately 808–888 passed
```

The exact collected case count must be recorded after the test file is written.

Behavioral coverage is frozen; the cosmetic total is not.

---

# PARAMETERIZATION RULE

Use `pytest.mark.parametrize` for:

* required-field omission
* invalid header types
* invalid header categories
* accepted and rejected progression conditions
* required-reference type and value cases
* optional-reference fields
* optional-reference type and value cases
* temporal type failures
* immutability fields
* structural inequality fields

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
with pytest.raises(ValueError, match="asserted_condition"):
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
asserted condition
→
scope
→
target version
→
prior condition
→
branch
→
context
→
asserted time
→
effective time
→
actor
→
source
→
basis
```

Tests must not inspect private helper names or source layout.

---

# IMPORT-ISOLATION RULE

Import-isolation tests must not:

* remove the production module from `sys.modules`
* reload the production class
* instantiate ObjectEngine
* load application JSON objects
* import application pages
* create Runtime Events
* create Hold records

They may inspect whether prohibited modules were newly imported.

---

# EXPECTED FAILURE BEFORE IMPLEMENTATION

After creating the test file but before production implementation, run:

```bat
python -m pytest tests\runtime\test_progression_assertion_record.py -q
```

Expected collection failure:

```text
ModuleNotFoundError:
No module named 'models.progression_assertion_record'
```

The failure must be observed and committed before production implementation.

Frozen suites must remain intact:

```bat
python -m pytest tests\runtime\test_runtime_record_identity.py -q
python -m pytest tests\runtime\test_runtime_event_record.py -q
python -m pytest tests\runtime\test_runtime_object_version_record.py -q
```

Expected:

```text
159 passed
203 passed
186 passed
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

1. application page behavior
2. ObjectEngine behavior
3. application-status migration
4. Runtime Event publication
5. Hold creation
6. Hold release
7. authority evaluation
8. admission
9. truth
10. semantic validity
11. canonical progression
12. conflict reconstruction
13. assertion supersession
14. target existence
15. target-version existence
16. target/version compatibility
17. scope existence
18. branch existence
19. context existence
20. actor identity verification
21. source trust
22. basis existence
23. evidence sufficiency
24. transition validity
25. temporal coherence
26. serialization
27. persistence
28. registry uniqueness
29. Platform Registry integration
30. Research Kernel service integration
31. progression-history reconstruction
32. progression enums

---

# TEST CONTRACT INVARIANTS

## Invariant 1

Tests must precede production implementation.

## Invariant 2

Every required field must have omission coverage.

## Invariant 3

Every validated field must have type-failure coverage.

## Invariant 4

Every constrained field must have positive and negative value coverage.

## Invariant 5

Every optional field must accept `None`.

## Invariant 6

Every valid reference must preserve exact input.

## Invariant 7

The accepted progression vocabulary must remain exactly closed.

## Invariant 8

Application statuses must remain outside progression vocabulary.

## Invariant 9

`CONFLICTING` must remain outside progression vocabulary.

## Invariant 10

`HELD` must not introduce Hold-control fields.

## Invariant 11

Prior condition may equal asserted condition.

## Invariant 12

Prior plus asserted condition must not imply verified transition.

## Invariant 13

Recorded, asserted, and effective times must remain distinct.

## Invariant 14

Temporal ordering must remain outside the model.

## Invariant 15

Validation precedence must remain externally observable.

## Invariant 16

Every field must be covered by immutability tests.

## Invariant 17

Every field must participate in structural equality.

## Invariant 18

Hashing must remain consistent with equality.

## Invariant 19

Ordering must remain unsupported.

## Invariant 20

Serialization must remain absent.

## Invariant 21

ObjectEngine, Runtime Event, Runtime Object Version, and Streamlit must remain unimported.

## Invariant 22

The composed header must remain unchanged.

## Invariant 23

No test may require filesystem, service, authority, or projection setup.

## Invariant 24

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

Minimal assertion fixture:
**FROZEN**

Context-rich fixture:
**FROZEN**

Header tests:
**FROZEN**

Target tests:
**FROZEN**

Condition-vocabulary tests:
**FROZEN**

Scope tests:
**FROZEN**

Optional-reference tests:
**FROZEN**

Prior-condition tests:
**FROZEN**

Temporal tests:
**FROZEN**

Temporal-separation tests:
**FROZEN**

Validation-precedence tests:
**FROZEN**

Immutability tests:
**FROZEN**

Equality and hashing tests:
**FROZEN**

Ordering test:
**FROZEN**

Serialization-absence test:
**FROZEN**

Application-status boundary tests:
**FROZEN**

Hold and conflict boundary tests:
**FROZEN**

Service-isolation tests:
**FROZEN**

Direct-import test:
**FROZEN**

Production implementation:
**HOLD**

---

# READINESS CHECKPOINT 4

Progression Assertion Test Contract:

**COMPLETE**

The test suite may now be written before production implementation.

Production implementation remains unauthorized until:

1. the test file is created
2. the expected missing-model failure is observed
3. all frozen suites remain passing independently
4. the test baseline is reviewed
5. the tests are committed before implementation
6. minimal production implementation is separately admitted

---

# NEXT SESSION

Begin:

**PROGRESSION ASSERTION RECORD FOUNDATION — TESTS BEFORE IMPLEMENTATION 001**

Required sequence:

1. create `tests\runtime\test_progression_assertion_record.py`
2. paste the complete frozen test suite
3. run the isolated new suite
4. confirm expected missing-model failure
5. run Runtime Record Identity tests
6. run Runtime Event tests
7. run Runtime Object Version tests
8. confirm frozen suites remain passing
9. inspect Git status
10. commit tests before implementation
11. preserve production implementation HOLD

**UNKNOWN → HOLD**
