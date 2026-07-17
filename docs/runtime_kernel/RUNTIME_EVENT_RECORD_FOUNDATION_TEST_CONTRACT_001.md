# RESEARCH OS — RUNTIME EVENT RECORD FOUNDATION

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

Define the complete test contract that must be written before implementation of:

```text
RuntimeEventRecord
```

The test suite must prove:

1. immutable header composition
2. `EVENT` record-category enforcement
3. minimal structural completeness
4. context-rich construction
5. event-type validation
6. optional-reference validation
7. reference preservation
8. occurred-time validation
9. effective-time validation
10. temporal separation
11. deterministic validation precedence
12. immutability
13. structural equality
14. structural hashing
15. ordering prohibition
16. serialization absence
17. direct module import
18. EventEngine isolation
19. absence of side effects
20. preservation of the frozen `RuntimeRecordHeader`

This document does not authorize production implementation.

---

# PREREQUISITE

Context Sufficiency and Immutable Contract 001 froze:

## Production Path

```text
models/runtime_event_record.py
```

## Test Path

```text
tests/runtime/test_runtime_event_record.py
```

## Model

```text
RuntimeEventRecord
```

## Required Fields

```python
header: RuntimeRecordHeader
event_type: str
```

## Optional References

```python
target_ref: str | None = None
actor_ref: str | None = None
source_ref: str | None = None
scope_ref: str | None = None
branch_ref: str | None = None
```

## Optional Temporal Fields

```python
occurred_at: datetime | None = None
effective_at: datetime | None = None
```

## Frozen Header Rule

```text
header.record_category == EVENT
```

## Frozen Behavior

* immutable dataclass
* full structural equality
* structural hashing
* no ordering
* no serialization
* no persistence
* no EventEngine coupling
* no authority semantics
* no canonical effect
* no generic payload

---

# OPERATING RULES

* Write tests before production implementation.
* Do not create `models/runtime_event_record.py` in the test-writing session.
* Do not weaken the frozen event contract.
* Do not modify `RuntimeRecordHeader`.
* Do not modify existing Runtime Record Identity tests.
* Do not import or instantiate `EventEngine`.
* Do not access `events.json`.
* Do not create files or directories.
* Do not test deferred persistence.
* Do not test authority.
* Do not test canonical projection.
* Keep all tests deterministic and in memory.
* Test observable behavior rather than helper implementation.

---

# TEST FILE STRUCTURE

Create later:

```text
tests/
└── runtime/
    ├── test_runtime_record_identity.py
    └── test_runtime_event_record.py
```

No new `conftest.py` is required.

No package `__init__.py` is required unless direct import behavior proves otherwise.

Production import:

```python
from models.runtime_event_record import RuntimeEventRecord
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

from models.runtime_event_record import RuntimeEventRecord
from models.runtime_record_identity import RuntimeRecordHeader
```

No additional dependency is authorized.

---

# SHARED VALID VALUES

The test file may define:

```python
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
```

These are test values only.

They must not become production defaults.

---

# VALID EVENT HEADER FACTORY

A private helper may construct a frozen valid event header:

```python
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
```

The header identity should not overlap conceptually with target references.

---

# EVENT FACTORY

A private helper may construct a minimal valid event:

```python
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
```

Boundary:

```text
Test Factory
≠
Production Factory
```

---

# INVALID TIMEZONE HELPER

Use the same invalid timezone structure as the frozen header suite:

```python
class InvalidTimezone(tzinfo):
    def utcoffset(self, dt):
        return None

    def dst(self, dt):
        return None

    def tzname(self, dt):
        return "INVALID"
```

This tests timezone objects whose `tzinfo` exists but whose offset is unusable.

---

# TEST GROUP 1 — MODEL SHAPE

## Test 1

Name:

```text
test_runtime_event_record_is_a_dataclass
```

Assertion:

```python
assert is_dataclass(RuntimeEventRecord)
```

---

## Test 2

Name:

```text
test_runtime_event_record_declares_exact_field_order
```

Expected fields:

```python
[
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
```

This test also proves absence of unapproved fields such as:

* `event_id`
* `payload`
* `details`
* `status`
* `authority_ref`
* `canonical_effect`
* `resulting_state`
* `timestamp`

No separate payload-field test is needed.

---

# TEST GROUP 2 — MINIMAL VALID CONSTRUCTION

## Test 3

Name:

```text
test_runtime_event_record_accepts_header_and_event_type_only
```

Construct:

```python
event = RuntimeEventRecord(
    header=make_event_header(),
    event_type=VALID_EVENT_TYPE,
)
```

Assert:

```python
event.header.record_category == "EVENT"
event.event_type == VALID_EVENT_TYPE
event.target_ref is None
event.actor_ref is None
event.source_ref is None
event.scope_ref is None
event.branch_ref is None
event.occurred_at is None
event.effective_at is None
```

This proves context-free structural admission.

---

## Test 4

Name:

```text
test_runtime_event_record_preserves_exact_header_instance
```

Construct with one header object.

Assert:

```python
event.header is header
```

This proves composition rather than duplication or reconstruction.

---

## Test 5

Name:

```text
test_runtime_event_identity_is_supplied_by_header_record_id
```

Assert:

```python
event.header.record_id == "RR-000000101"
assert not hasattr(event, "event_id")
```

This protects the no-duplicate-event-identity boundary.

---

# TEST GROUP 3 — CONTEXT-RICH VALID CONSTRUCTION

## Test 6

Name:

```text
test_runtime_event_record_accepts_all_valid_context_fields
```

Construct with every optional field.

Assert exact preservation.

---

## Test 7

Name:

```text
test_runtime_event_record_preserves_reference_values_exactly
```

Use values with surrounding spaces:

```text
" target "
" actor "
" source "
" scope "
" branch "
```

Assert exact preservation.

These are valid because they are not whitespace-only.

---

## Test 8

Name:

```text
test_runtime_event_record_accepts_non_utc_occurred_and_effective_times
```

Use distinct fixed offsets.

Assert:

* exact datetime preservation
* exact UTC offsets
* no UTC conversion

---

# TEST GROUP 4 — REQUIRED CONSTRUCTOR FIELDS

A parameterized test must prove that each required field is mandatory.

## Test 9

Name:

```text
test_runtime_event_record_requires_each_required_field
```

Cases:

```text
header
event_type
```

Expected:

```text
TypeError
```

No automatic header or event-type generation is permitted.

---

# TEST GROUP 5 — HEADER TYPE

## Test 10

Name:

```text
test_header_rejects_non_runtime_record_header_values
```

Parameterized invalid values:

```python
[
    None,
    "RR-000000101",
    {},
    [],
    (),
    1,
    True,
]
```

Expected:

```text
TypeError
```

Assert message contains:

```text
header
```

---

# TEST GROUP 6 — HEADER CATEGORY

## Test 11

Name:

```text
test_header_accepts_event_record_category
```

Construct with category:

```text
EVENT
```

Assert success.

---

## Test 12

Name:

```text
test_header_rejects_non_event_record_categories
```

Parameterized categories:

```text
VERSION
HOLD
EVALUATION
CUSTOM_RECORD
INSPECTION_RESULT
```

Each category should first be accepted by `RuntimeRecordHeader`, then rejected by `RuntimeEventRecord`.

Expected:

```text
ValueError
```

Assert message contains:

```text
header
```

or:

```text
record_category
```

---

# TEST GROUP 7 — EVENT_TYPE TYPE

## Test 13

Name:

```text
test_event_type_rejects_non_string_values
```

Parameterized invalid values:

```python
[
    None,
    1,
    1.0,
    True,
    b"OBJECT_CREATED",
    [],
    {},
]
```

Expected:

```text
TypeError
```

Assert message contains:

```text
event_type
```

---

# TEST GROUP 8 — EVENT_TYPE VALUE

## Test 14

Name:

```text
test_event_type_accepts_valid_values
```

Parameterized valid values:

```text
OBJECT_CREATED
VERSION_RECORDED
PROGRESSION_ASSERTED
RE_ENTRY_RECORDED
EVENT2
A
A1
CUSTOM_EVENT
```

This proves the vocabulary remains structurally open.

---

## Test 15

Name:

```text
test_event_type_rejects_invalid_values
```

Parameterized invalid values:

```text
""
" "
"object_created"
"ObjectCreated"
"OBJECT-CREATED"
"OBJECT CREATED"
"_OBJECT_CREATED"
"OBJECT_CREATED_"
"OBJECT__CREATED"
"2OBJECT"
" OBJECT_CREATED"
"OBJECT_CREATED "
```

Expected:

```text
ValueError
```

---

# TEST GROUP 9 — OPTIONAL REFERENCE TYPE

Use one parameterized test across all five reference fields.

## Test 16

Name:

```text
test_optional_references_reject_non_string_non_none_values
```

Parameters:

```python
field_name in [
    "target_ref",
    "actor_ref",
    "source_ref",
    "scope_ref",
    "branch_ref",
]
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
]
```

Expected:

```text
TypeError
```

Assert message contains the field name.

---

# TEST GROUP 10 — OPTIONAL REFERENCE VALUE

## Test 17

Name:

```text
test_optional_references_accept_none
```

For every reference field:

```python
assert make_event(**{field_name: None})
```

This may be one parameterized test.

---

## Test 18

Name:

```text
test_optional_references_accept_non_empty_strings
```

Values may include:

```text
REF-001
external/reference
" ref "
0
x
```

Assert exact preservation.

---

## Test 19

Name:

```text
test_optional_references_reject_empty_or_whitespace_only_values
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

Run across all five reference fields.

Expected:

```text
ValueError
```

---

# TEST GROUP 11 — OCCURRED_AT TYPE

## Test 20

Name:

```text
test_occurred_at_rejects_non_datetime_non_none_values
```

Parameterized invalid values:

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
TypeError
```

---

## Test 21

Name:

```text
test_occurred_at_accepts_none
```

Covered by minimal construction.

Decision:

**NO SEPARATE TEST REQUIRED**

---

## Test 21

Name:

```text
test_occurred_at_rejects_naive_datetime
```

Expected:

```text
ValueError
```

---

## Test 22

Name:

```text
test_occurred_at_rejects_timezone_with_no_utc_offset
```

Expected:

```text
ValueError
```

---

## Test 23

Name:

```text
test_occurred_at_preserves_supplied_timezone_and_offset
```

Use a non-UTC timezone.

Assert exact preservation.

---

# TEST GROUP 12 — EFFECTIVE_AT TYPE

## Test 24

Name:

```text
test_effective_at_rejects_non_datetime_non_none_values
```

Use the same invalid values as `occurred_at`.

Expected:

```text
TypeError
```

---

## Test 25

Name:

```text
test_effective_at_rejects_naive_datetime
```

Expected:

```text
ValueError
```

---

## Test 26

Name:

```text
test_effective_at_rejects_timezone_with_no_utc_offset
```

Expected:

```text
ValueError
```

---

## Test 27

Name:

```text
test_effective_at_preserves_supplied_timezone_and_offset
```

Use a non-UTC timezone.

Assert exact preservation.

---

# TEST GROUP 13 — TEMPORAL SEPARATION

## Test 28

Name:

```text
test_runtime_event_record_does_not_default_occurred_at_to_recorded_at
```

Minimal event:

```python
assert event.occurred_at is None
assert event.header.recorded_at is not None
```

---

## Test 29

Name:

```text
test_runtime_event_record_does_not_default_effective_at_to_occurred_at
```

Construct with `occurred_at` only.

Assert:

```python
event.effective_at is None
```

---

## Test 30

Name:

```text
test_runtime_event_record_allows_effective_time_before_occurred_time
```

Construct:

```text
effective_at < occurred_at
```

Assert successful construction.

---

## Test 31

Name:

```text
test_runtime_event_record_allows_effective_time_after_recorded_time
```

Construct:

```text
effective_at > header.recorded_at
```

Assert successful construction.

---

## Test 32

Name:

```text
test_runtime_event_record_allows_occurred_time_after_recorded_time
```

Although unusual, the structural model must not impose chronology.

Assert successful construction.

---

# TEST GROUP 14 — VALIDATION PRECEDENCE

## Test 33

Name:

```text
test_header_type_failure_precedes_event_type_failure
```

Supply:

* invalid header type
* invalid event type
* invalid references
* invalid times

Expected:

```text
TypeError mentioning header
```

---

## Test 34

Name:

```text
test_header_category_failure_precedes_event_type_failure
```

Supply:

* valid non-EVENT header
* invalid event type

Expected:

```text
ValueError mentioning header or record_category
```

---

## Test 35

Name:

```text
test_event_type_type_failure_precedes_reference_failure
```

Supply:

* event type as integer
* invalid target reference

Expected:

```text
TypeError mentioning event_type
```

---

## Test 36

Name:

```text
test_event_type_value_failure_precedes_reference_failure
```

Supply:

* invalid event-type string
* invalid target reference

Expected:

```text
ValueError mentioning event_type
```

---

## Test 37

Name:

```text
test_target_reference_failure_precedes_actor_reference_failure
```

Supply invalid values for both.

Expected error identifies:

```text
target_ref
```

---

## Test 38

Name:

```text
test_branch_reference_failure_precedes_temporal_failure
```

Supply:

* invalid branch reference
* naïve occurred time

Expected error identifies:

```text
branch_ref
```

---

## Test 39

Name:

```text
test_occurred_at_failure_precedes_effective_at_failure
```

Supply naïve values for both.

Expected error identifies:

```text
occurred_at
```

---

# TEST GROUP 15 — IMMUTABILITY

## Test 40

Name:

```text
test_runtime_event_record_is_frozen
```

Parameterize all nine fields:

```text
header
event_type
target_ref
actor_ref
source_ref
scope_ref
branch_ref
occurred_at
effective_at
```

Attempt reassignment.

Expected:

```text
FrozenInstanceError
```

---

# TEST GROUP 16 — EQUALITY

## Test 41

Name:

```text
test_identical_runtime_event_records_compare_equal
```

Construct two distinct records with equal structures.

Assert equality.

---

## Test 42

Name:

```text
test_runtime_event_record_equality_is_full_structural_equality
```

Parameterize different values for every field:

* different header
* different event type
* different target
* different actor
* different source
* different scope
* different branch
* different occurred time
* different effective time

Assert inequality.

---

## Test 43

Name:

```text
test_same_header_with_different_event_type_is_not_equal
```

This remains explicit because one header identity with conflicting event structure must not compare equal.

---

## Test 44

Name:

```text
test_same_header_and_event_type_with_different_context_is_not_equal
```

Use different target reference.

Assert inequality.

---

## Test 45

Name:

```text
test_equivalent_temporal_instants_follow_python_datetime_equality
```

Use equal instants with different timezone offsets.

Records otherwise identical should compare equal.

---

# TEST GROUP 17 — HASHING

## Test 46

Name:

```text
test_equal_runtime_event_records_have_equal_hashes
```

---

## Test 47

Name:

```text
test_structurally_different_runtime_event_records_can_coexist_in_a_set
```

---

## Test 48

Name:

```text
test_hashing_does_not_change_runtime_event_record
```

Record every field before and after hashing.

Assert no change.

---

# TEST GROUP 18 — ORDERING

## Test 49

Name:

```text
test_runtime_event_records_do_not_support_ordering
```

Assert:

```python
with pytest.raises(TypeError):
    _ = event_a < event_b
```

No sorting semantics are permitted.

---

# TEST GROUP 19 — SERIALIZATION ABSENCE

## Test 50

Name:

```text
test_runtime_event_record_exposes_no_serialization_methods
```

Assert absence of:

```text
to_dict
from_dict
to_json
from_json
```

---

# TEST GROUP 20 — APPLICATION EVENT BOUNDARY

## Test 51

Name:

```text
test_runtime_event_record_contains_no_application_event_fields
```

Protected by exact field-order test.

Decision:

**NO SEPARATE TEST REQUIRED**

---

## Test 51

Name:

```text
test_runtime_event_record_does_not_accept_application_event_dictionary_as_header
```

Pass an existing application-shaped dictionary:

```python
{
    "timestamp": "2026-07-01T12:55:23",
    "category": "Build Center",
    "action": "Faculty dossier generated",
    "status": "SUCCESS",
    "details": {},
}
```

Expected:

```text
TypeError mentioning header
```

This directly protects the Application Activity Event boundary.

---

# TEST GROUP 21 — EVENTENGINE ISOLATION

## Test 52

Name:

```text
test_importing_runtime_event_record_does_not_import_event_engine
```

Candidate pattern:

```python
def test_importing_runtime_event_record_does_not_import_event_engine():
    event_engine_was_loaded = "src.services.event_engine" in sys.modules

    module = importlib.import_module("models.runtime_event_record")

    assert hasattr(module, "RuntimeEventRecord")

    if not event_engine_was_loaded:
        assert "src.services.event_engine" not in sys.modules
```

Do not remove the Runtime Event module from `sys.modules`, because doing so may create a second class object and break later identity assertions.

---

## Test 53

Name:

```text
test_importing_runtime_event_record_does_not_import_streamlit
```

Use the same pre-existing-import safeguard.

---

# TEST GROUP 22 — DIRECT IMPORT

## Test 54

Name:

```text
test_runtime_event_record_module_can_be_imported_directly
```

Assert:

```python
from models.runtime_event_record import RuntimeEventRecord as ImportedRecord

assert ImportedRecord is RuntimeEventRecord
```

---

# TEST GROUP 23 — HEADER IMMUTABILITY PRESERVATION

## Test 55

Name:

```text
test_runtime_event_record_does_not_modify_composed_header
```

Capture every header field.

Construct a Runtime Event record.

Assert the header remains unchanged.

---

## Test 56

Name:

```text
test_runtime_event_record_does_not_replace_composed_header
```

Assert:

```python
event.header is header
```

This overlaps with Test 4.

Decision:

**NO SEPARATE TEST REQUIRED**

---

# TEST GROUP 24 — OPEN EVENT-TYPE VOCABULARY

## Test 56

Name:

```text
test_runtime_event_record_does_not_restrict_event_type_to_current_examples
```

Use:

```text
CUSTOM_RUNTIME_OCCURRENCE
```

Assert successful construction.

This proves no event-type enumeration has been introduced.

---

# TEST GROUP 25 — NO SIDE EFFECTS

A separate filesystem test is unnecessary if the model constructs entirely in memory.

The test suite must not require:

* temporary paths
* event files
* service fixtures
* clock patching
* environment patching
* network mocks
* registry cleanup

The minimal and context-rich construction tests establish this boundary.

---

# FINAL LOGICAL TEST LIST

The test file should contain these 56 logical test functions or parameterized groups:

1. `test_runtime_event_record_is_a_dataclass`
2. `test_runtime_event_record_declares_exact_field_order`
3. `test_runtime_event_record_accepts_header_and_event_type_only`
4. `test_runtime_event_record_preserves_exact_header_instance`
5. `test_runtime_event_identity_is_supplied_by_header_record_id`
6. `test_runtime_event_record_accepts_all_valid_context_fields`
7. `test_runtime_event_record_preserves_reference_values_exactly`
8. `test_runtime_event_record_accepts_non_utc_occurred_and_effective_times`
9. `test_runtime_event_record_requires_each_required_field`
10. `test_header_rejects_non_runtime_record_header_values`
11. `test_header_accepts_event_record_category`
12. `test_header_rejects_non_event_record_categories`
13. `test_event_type_rejects_non_string_values`
14. `test_event_type_accepts_valid_values`
15. `test_event_type_rejects_invalid_values`
16. `test_optional_references_reject_non_string_non_none_values`
17. `test_optional_references_accept_none`
18. `test_optional_references_accept_non_empty_strings`
19. `test_optional_references_reject_empty_or_whitespace_only_values`
20. `test_occurred_at_rejects_non_datetime_non_none_values`
21. `test_occurred_at_rejects_naive_datetime`
22. `test_occurred_at_rejects_timezone_with_no_utc_offset`
23. `test_occurred_at_preserves_supplied_timezone_and_offset`
24. `test_effective_at_rejects_non_datetime_non_none_values`
25. `test_effective_at_rejects_naive_datetime`
26. `test_effective_at_rejects_timezone_with_no_utc_offset`
27. `test_effective_at_preserves_supplied_timezone_and_offset`
28. `test_runtime_event_record_does_not_default_occurred_at_to_recorded_at`
29. `test_runtime_event_record_does_not_default_effective_at_to_occurred_at`
30. `test_runtime_event_record_allows_effective_time_before_occurred_time`
31. `test_runtime_event_record_allows_effective_time_after_recorded_time`
32. `test_runtime_event_record_allows_occurred_time_after_recorded_time`
33. `test_header_type_failure_precedes_event_type_failure`
34. `test_header_category_failure_precedes_event_type_failure`
35. `test_event_type_type_failure_precedes_reference_failure`
36. `test_event_type_value_failure_precedes_reference_failure`
37. `test_target_reference_failure_precedes_actor_reference_failure`
38. `test_branch_reference_failure_precedes_temporal_failure`
39. `test_occurred_at_failure_precedes_effective_at_failure`
40. `test_runtime_event_record_is_frozen`
41. `test_identical_runtime_event_records_compare_equal`
42. `test_runtime_event_record_equality_is_full_structural_equality`
43. `test_same_header_with_different_event_type_is_not_equal`
44. `test_same_header_and_event_type_with_different_context_is_not_equal`
45. `test_equivalent_temporal_instants_follow_python_datetime_equality`
46. `test_equal_runtime_event_records_have_equal_hashes`
47. `test_structurally_different_runtime_event_records_can_coexist_in_a_set`
48. `test_hashing_does_not_change_runtime_event_record`
49. `test_runtime_event_records_do_not_support_ordering`
50. `test_runtime_event_record_exposes_no_serialization_methods`
51. `test_runtime_event_record_does_not_accept_application_event_dictionary_as_header`
52. `test_importing_runtime_event_record_does_not_import_event_engine`
53. `test_importing_runtime_event_record_does_not_import_streamlit`
54. `test_runtime_event_record_module_can_be_imported_directly`
55. `test_runtime_event_record_does_not_modify_composed_header`
56. `test_runtime_event_record_does_not_restrict_event_type_to_current_examples`

---

# EXPECTED PYTEST CASE COUNT

Parameterized groups will expand the logical test count.

Expected new Runtime Event test cases:

```text
approximately 170–220
```

Current frozen baseline:

```text
159 passed
```

Expected eventual full-suite range after implementation:

```text
approximately 329–379 passed
```

The exact total must be recorded after the test file is written.

Behavioral coverage is frozen; the cosmetic count is not.

---

# PARAMETERIZATION RULE

Use `pytest.mark.parametrize` for:

* required-field omission
* invalid header types
* invalid header categories
* event-type type failures
* valid event types
* invalid event types
* reference fields
* invalid reference types
* valid reference values
* invalid reference values
* datetime types
* immutability fields
* structural inequality fields

Do not combine unrelated semantic responsibilities into one oversized test.

---

# ERROR ASSERTION RULE

Tests should assert:

* error class
* meaningful field-name fragment

Examples:

```python
with pytest.raises(TypeError, match="header"):
    ...
```

```python
with pytest.raises(ValueError, match="event_type"):
    ...
```

Full error-message punctuation should not be frozen unnecessarily.

---

# VALIDATION PRECEDENCE RULE

Tests must validate externally observable precedence only.

They must not inspect private helpers or source order.

Required precedence:

```text
header
→
header category
→
event type
→
target
→
actor
→
source
→
scope
→
branch
→
occurred time
→
effective time
```

---

# IMPORT-ISOLATION RULE

Import-isolation tests must not:

* remove `models.runtime_event_record` from `sys.modules`
* reload the production class
* instantiate EventEngine
* access the file system

They may inspect whether prohibited modules were newly imported.

This prevents the class-identity issue previously encountered in the Runtime Record Identity suite.

---

# TEST FAILURE EXPECTATION BEFORE IMPLEMENTATION

After the test file is created but before production implementation, run:

```bat
python -m pytest tests\runtime\test_runtime_event_record.py -q
```

Expected collection failure:

```text
ModuleNotFoundError:
No module named 'models.runtime_event_record'
```

This failure must be recorded and committed before production implementation.

Boundary:

```text
Expected Test Failure
≠
Contract Failure
```

---

# TEST CONTRACT NON-GOALS

The test suite must not test:

1. event persistence
2. EventEngine publication
3. application activity rendering
4. Runtime Event registry behavior
5. record uniqueness
6. event identity generation
7. target existence
8. actor existence
9. source trust
10. scope resolution
11. branch existence
12. authority
13. admission
14. canonical effect
15. causal relationships
16. event ordering
17. temporal consistency
18. serialization
19. schema migration
20. graph topology
21. service inspection
22. Platform Registry integration
23. Research Kernel integration
24. specialized event payloads
25. event-type enumeration

---

# ARCHITECTURE TEST REQUIREMENTS

The test suite must prove:

* Runtime Event identity is inherited through composition from the header
* record category and event type remain distinct
* minimal context is structurally valid
* missing context remains `None`
* context absence is not converted into defaults
* optional references remain unresolved and exact
* temporal dimensions remain distinct
* chronology is not enforced
* generic payload fields are absent
* authority fields are absent
* canonical-effect fields are absent
* application event dictionaries are rejected
* EventEngine remains unimported
* RuntimeRecordHeader remains unchanged
* the model remains standard-library only apart from its frozen header dependency

---

# TEST CONTRACT INVARIANTS

## Invariant 1

Tests must precede production implementation.

## Invariant 2

Every required field must have omission coverage.

## Invariant 3

Every validated field must have type-failure coverage.

## Invariant 4

Every constrained string field must have positive and negative value coverage.

## Invariant 5

Every optional reference must accept `None`.

## Invariant 6

Every optional reference must preserve exact non-empty input.

## Invariant 7

Both optional temporal fields must accept timezone-aware datetimes and reject naïve datetimes.

## Invariant 8

Temporal order must remain unvalidated.

## Invariant 9

Validation precedence must remain externally testable.

## Invariant 10

Every field must be covered by immutability tests.

## Invariant 11

Every field must participate in structural equality.

## Invariant 12

Hashing must remain consistent with equality.

## Invariant 13

Ordering must remain unsupported.

## Invariant 14

Serialization must remain absent.

## Invariant 15

The model must remain isolated from EventEngine and Streamlit.

## Invariant 16

Application activity dictionaries must not be accepted as Runtime Event headers.

## Invariant 17

The composed header must remain unchanged.

## Invariant 18

No test may require filesystem or service setup.

## Invariant 19

No event-type enumeration may be introduced.

## Invariant 20

The failing pre-implementation baseline must be recorded.

Status:

**FROZEN**

---

# TEST CONTRACT DECISION

Test path:
**FROZEN**

Framework:
**FROZEN**

Valid header fixture:
**FROZEN**

Minimal event fixture:
**FROZEN**

Context-rich fixture:
**FROZEN**

Header tests:
**FROZEN**

Category-enforcement tests:
**FROZEN**

Event-type tests:
**FROZEN**

Reference tests:
**FROZEN**

Temporal tests:
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

EventEngine-isolation tests:
**FROZEN**

Direct-import test:
**FROZEN**

Production implementation:
**HOLD**

---

# READINESS CHECKPOINT 4

Runtime Event Test Contract:

**COMPLETE**

The test suite may now be written before production implementation.

Production implementation remains unauthorized until:

1. the test file is created
2. the expected import failure is observed
3. the test file is reviewed
4. the failing test baseline is committed
5. minimal production implementation is separately admitted

---

# NEXT SESSION

Begin:

**RUNTIME EVENT RECORD FOUNDATION — TESTS BEFORE IMPLEMENTATION 001**

Required sequence:

1. create `tests\runtime\test_runtime_event_record.py`
2. paste the complete frozen test suite
3. run the isolated Runtime Event test file
4. confirm expected collection failure
5. run the existing Runtime Record Identity suite
6. confirm the 159-test baseline remains intact
7. inspect Git status
8. commit tests before implementation
9. keep production implementation HOLD

**UNKNOWN → HOLD**
