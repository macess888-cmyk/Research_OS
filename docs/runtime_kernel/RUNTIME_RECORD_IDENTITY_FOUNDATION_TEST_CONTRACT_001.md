# RESEARCH OS — RUNTIME RECORD IDENTITY FOUNDATION

# TEST CONTRACT 001

**Date:** 2026-07-17
**Project:** Research OS
**Development Version:** v2.0.0
**Status:** ACTIVE / TEST CONTRACT
**Architecture:** FROZEN WITH EXPLICIT DEFERRALS
**Production Implementation:** HOLD
**Authority:** TEST DESIGN ONLY

**UNKNOWN → HOLD**

---

# PURPOSE

Define the exact tests that must be written before implementation of:

```text
RuntimeRecordHeader
```

The test contract must prove:

1. valid construction
2. required-field enforcement
3. type-error behavior
4. value-error behavior
5. identity syntax
6. category syntax
7. timezone awareness
8. schema-version syntax
9. optional-field semantics
10. immutability
11. structural equality
12. structural hashing
13. ordering prohibition
14. import isolation
15. absence of side effects
16. architectural boundary preservation

This document does not authorize production implementation.

---

# PREREQUISITE

Immutable Contract 001 froze:

## Production Model

```text
models/runtime_record_identity.py
```

## Test File

```text
tests/runtime/test_runtime_record_identity.py
```

## Model

```text
RuntimeRecordHeader
```

## Fields

```python
record_id: str
record_category: str
recorded_at: datetime
schema_version: str
provenance_ref: str | None = None
external_id: str | None = None
```

## Required Behavior

* frozen dataclass
* full structural equality
* standard structural hashing
* no ordering
* deterministic construction validation
* wrong type → `TypeError`
* invalid value → `ValueError`
* standard-library dependencies only
* no side effects
* no serialization API

---

# OPERATING RULES

* Write tests before production implementation.
* Do not create the production model in this session.
* Do not weaken assertions to make future implementation easier.
* Do not test deferred serialization behavior.
* Do not test registry uniqueness.
* Do not test identity generation.
* Do not test Platform Kernel integration.
* Do not import application services.
* Keep tests deterministic.
* Keep tests fully in memory.
* Avoid unnecessary fixtures.
* Preserve exact frozen contract boundaries.

---

# TEST DIRECTORY STRUCTURE

Create later:

```text
tests/
└── runtime/
    └── test_runtime_record_identity.py
```

No `conftest.py` is required.

No package `__init__.py` is required unless Python import behavior later proves otherwise.

The first test file must import directly:

```python
from models.runtime_record_identity import RuntimeRecordHeader
```

---

# TEST FRAMEWORK

Use:

```text
pytest
```

Permitted standard-library imports:

```python
from dataclasses import FrozenInstanceError, fields, is_dataclass
from datetime import datetime, timedelta, timezone, tzinfo
import importlib
import sys
```

Permitted pytest import:

```python
import pytest
```

No additional test dependency is authorized.

---

# TEST NAMING CONVENTION

Test names must:

* begin with `test_`
* state one observable behavior
* avoid implementation-specific helper names
* avoid vague names such as `test_valid`
* identify field and expected outcome where applicable

Example:

```python
def test_runtime_record_header_accepts_valid_required_fields():
    ...
```

---

# SHARED VALID VALUES

The test file may define module-level constants:

```python
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
```

These constants are test data only.

They must not become production defaults.

---

# HEADER FACTORY

A private test helper may be used:

```python
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
```

Purpose:

* reduce repeated valid setup
* isolate one invalid field per test
* preserve readable assertions

Boundary:

Test Factory
≠
Production Factory

---

# CUSTOM INVALID TIMEZONE

A custom timezone implementation should test the requirement that `utcoffset()` must not return `None`.

Candidate test helper:

```python
class InvalidTimezone(tzinfo):
    def utcoffset(self, dt):
        return None

    def dst(self, dt):
        return None

    def tzname(self, dt):
        return "INVALID"
```

Test value:

```python
datetime(
    2026,
    7,
    17,
    12,
    0,
    tzinfo=InvalidTimezone(),
)
```

Expected result:

```text
ValueError
```

---

# TEST GROUP 1 — MODEL SHAPE

## Test 1

Name:

```text
test_runtime_record_header_is_a_dataclass
```

Proves:

* model uses dataclass semantics

Assertion:

```python
assert is_dataclass(RuntimeRecordHeader)
```

---

## Test 2

Name:

```text
test_runtime_record_header_declares_exact_field_order
```

Expected field order:

```python
[
    "record_id",
    "record_category",
    "recorded_at",
    "schema_version",
    "provenance_ref",
    "external_id",
]
```

Proves:

* constructor stability
* required-before-optional ordering
* no unapproved payload fields

---

## Test 3

Name:

```text
test_runtime_record_header_contains_no_unapproved_fields
```

Proves:

* no target field
* no payload field
* no status field
* no authority field
* no relationship field
* no branch field

This may be combined with exact field-order assertion if duplication is unnecessary.

Decision:

**COMBINE WITH TEST 2**

---

# TEST GROUP 2 — VALID CONSTRUCTION

## Test 3

Name:

```text
test_runtime_record_header_accepts_valid_required_fields
```

Construct using only required fields.

Assert:

```python
header.record_id == VALID_RECORD_ID
header.record_category == VALID_RECORD_CATEGORY
header.recorded_at == VALID_RECORDED_AT
header.schema_version == VALID_SCHEMA_VERSION
header.provenance_ref is None
header.external_id is None
```

---

## Test 4

Name:

```text
test_runtime_record_header_accepts_valid_optional_fields
```

Construct with:

* valid provenance reference
* valid external identity

Assert exact preservation.

---

## Test 5

Name:

```text
test_runtime_record_header_accepts_non_utc_timezone_aware_datetime
```

Use a fixed offset:

```python
timezone(timedelta(hours=-7))
```

Assert the supplied value remains unchanged.

Proves:

* timezone awareness is required
* UTC normalization is not performed

---

## Test 6

Name:

```text
test_runtime_record_header_preserves_external_id_exactly
```

Use:

```text
" external-id "
```

Assert exact preservation including surrounding spaces.

This is valid because it is not whitespace-only.

---

# TEST GROUP 3 — REQUIRED CONSTRUCTOR FIELDS

Parameterized tests should verify omission of each required field raises `TypeError`.

## Test 7

Name:

```text
test_runtime_record_header_requires_record_id
```

## Test 8

Name:

```text
test_runtime_record_header_requires_record_category
```

## Test 9

Name:

```text
test_runtime_record_header_requires_recorded_at
```

## Test 10

Name:

```text
test_runtime_record_header_requires_schema_version
```

These may be represented through one parameterized test that removes each field.

Candidate name:

```text
test_runtime_record_header_requires_each_required_field
```

Expected parameter count:

4 cases

Decision:

**ONE PARAMETERIZED TEST**

---

# TEST GROUP 4 — RECORD_ID TYPE

## Test 8

Name:

```text
test_record_id_rejects_non_string_values
```

Parameterized invalid values:

```python
[
    None,
    1,
    1.0,
    True,
    b"RR-000000001",
    [],
    {},
]
```

Expected:

```text
TypeError
```

Assert message includes:

```text
record_id
```

---

# TEST GROUP 5 — RECORD_ID VALUE

## Test 9

Name:

```text
test_record_id_accepts_valid_values
```

Parameterized valid values:

```text
RR-000000001
RR-000000042
RR-999999999
```

---

## Test 10

Name:

```text
test_record_id_rejects_invalid_values
```

Parameterized invalid values:

```text
""
" "
"RR-000000000"
"rr-000000001"
"RR000000001"
"RR-1"
"RR-00000001"
"RR-0000000001"
"RR-00000001A"
" RR-000000001"
"RR-000000001 "
"EVT-000000001"
```

Expected:

```text
ValueError
```

Assert message includes:

```text
record_id
```

---

## Test 11

Name:

```text
test_record_id_is_preserved_without_normalization
```

A valid identity should remain exactly unchanged.

Malformed input should be refused rather than normalized.

The exact preservation assertion may already be covered by valid construction.

Decision:

**NO SEPARATE TEST REQUIRED**

---

# TEST GROUP 6 — RECORD_CATEGORY TYPE

## Test 11

Name:

```text
test_record_category_rejects_non_string_values
```

Parameterized invalid values:

```python
[
    None,
    1,
    1.0,
    True,
    b"EVENT",
    [],
    {},
]
```

Expected:

```text
TypeError
```

---

# TEST GROUP 7 — RECORD_CATEGORY VALUE

## Test 12

Name:

```text
test_record_category_accepts_valid_values
```

Parameterized values:

```text
EVENT
VERSION
HOLD
RE_ENTRY
INSPECTION_RESULT
CATEGORY2
TYPE_2
A
A1
```

---

## Test 13

Name:

```text
test_record_category_rejects_invalid_values
```

Parameterized invalid values:

```text
""
" "
"event"
"Event"
"RE-ENTRY"
"RE ENTRY"
"_RE_ENTRY"
"RE_ENTRY_"
"RE__ENTRY"
"2EVENT"
" EVENT"
"EVENT "
```

Expected:

```text
ValueError
```

---

# TEST GROUP 8 — RECORDED_AT TYPE

## Test 14

Name:

```text
test_recorded_at_rejects_non_datetime_values
```

Parameterized invalid values:

```python
[
    None,
    "2026-07-17T12:00:00Z",
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

# TEST GROUP 9 — RECORDED_AT VALUE

## Test 15

Name:

```text
test_recorded_at_rejects_naive_datetime
```

Use:

```python
datetime(2026, 7, 17, 12, 0, 0)
```

Expected:

```text
ValueError
```

---

## Test 16

Name:

```text
test_recorded_at_rejects_timezone_with_no_utc_offset
```

Use `InvalidTimezone`.

Expected:

```text
ValueError
```

---

## Test 17

Name:

```text
test_recorded_at_preserves_supplied_timezone_and_offset
```

Use:

```python
timezone(timedelta(hours=5, minutes=30))
```

Assert:

* equality with original datetime
* `tzinfo` remains the supplied timezone object or equivalent preserved value
* no conversion to UTC occurred

---

# TEST GROUP 10 — SCHEMA_VERSION TYPE

## Test 18

Name:

```text
test_schema_version_rejects_non_string_values
```

Parameterized invalid values:

```python
[
    None,
    1,
    1.0,
    True,
    b"1.0",
    [],
    {},
]
```

Expected:

```text
TypeError
```

---

# TEST GROUP 11 — SCHEMA_VERSION VALUE

## Test 19

Name:

```text
test_schema_version_accepts_valid_values
```

Parameterized valid values:

```text
1.0
1.1
2.0
12.4
999.999
```

---

## Test 20

Name:

```text
test_schema_version_rejects_invalid_values
```

Parameterized invalid values:

```text
""
" "
"v1.0"
"1"
"1.0.0"
"01.0"
"0.1"
"1.x"
"1."
".1"
" 1.0"
"1.0 "
```

Expected:

```text
ValueError
```

---

# TEST GROUP 12 — PROVENANCE_REF TYPE

## Test 21

Name:

```text
test_provenance_ref_accepts_none
```

This is also covered by required-fields construction.

Decision:

**NO SEPARATE TEST REQUIRED**

---

## Test 21

Name:

```text
test_provenance_ref_rejects_non_string_non_none_values
```

Parameterized invalid values:

```python
[
    1,
    1.0,
    True,
    b"PRV-000000001",
    [],
    {},
]
```

Expected:

```text
TypeError
```

---

# TEST GROUP 13 — PROVENANCE_REF VALUE

## Test 22

Name:

```text
test_provenance_ref_accepts_valid_values
```

Parameterized valid values:

```text
PRV-000000001
PRV-000000042
PRV-999999999
```

---

## Test 23

Name:

```text
test_provenance_ref_rejects_invalid_values
```

Parameterized invalid values:

```text
""
" "
"PRV-000000000"
"prv-000000001"
"PRV000000001"
"PRV-1"
"PRV-00000001"
"PRV-0000000001"
"PRV-00000001A"
" PRV-000000001"
"PRV-000000001 "
```

Expected:

```text
ValueError
```

---

# TEST GROUP 14 — EXTERNAL_ID TYPE

## Test 24

Name:

```text
test_external_id_rejects_non_string_non_none_values
```

Parameterized invalid values:

```python
[
    1,
    1.0,
    True,
    b"external",
    [],
    {},
]
```

Expected:

```text
TypeError
```

---

# TEST GROUP 15 — EXTERNAL_ID VALUE

## Test 25

Name:

```text
test_external_id_accepts_non_empty_values
```

Parameterized valid values:

```text
EXT-123
doi:10.1000/example
external/system/record/42
" abc"
"abc "
" a "
"0"
```

Assert exact preservation.

---

## Test 26

Name:

```text
test_external_id_rejects_empty_or_whitespace_only_values
```

Parameterized invalid values:

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
ValueError
```

---

# TEST GROUP 16 — VALIDATION ORDER

Validation order is frozen and should be tested at selected collision points.

Testing every combination would create unnecessary brittleness.

Required tests:

## Test 27

Name:

```text
test_record_id_type_failure_precedes_other_field_failures
```

Construct with:

* invalid record ID type
* invalid category value
* naïve time
* invalid schema version

Expected:

```text
TypeError mentioning record_id
```

---

## Test 28

Name:

```text
test_record_id_value_failure_precedes_record_category_failure
```

Construct with:

* invalid string record ID
* invalid category

Expected:

```text
ValueError mentioning record_id
```

---

## Test 29

Name:

```text
test_required_field_validation_precedes_optional_field_validation
```

Construct with:

* valid required identity except invalid schema version
* invalid provenance-reference type

Expected:

```text
ValueError mentioning schema_version
```

These tests prove deterministic validation precedence without coupling to exact full error strings.

---

# TEST GROUP 17 — IMMUTABILITY

## Test 30

Name:

```text
test_runtime_record_header_is_frozen
```

Assert reassignment of each field raises:

```python
FrozenInstanceError
```

Parameterized fields:

```text
record_id
record_category
recorded_at
schema_version
provenance_ref
external_id
```

A single parameterized test is sufficient.

---

## Test 31

Name:

```text
test_runtime_record_header_exposes_no_mutation_methods
```

Candidate prohibited names:

```text
update
replace_field
set_record_id
set_category
set_external_id
```

Decision:

Avoid testing speculative method names.

The frozen dataclass assertion is sufficient.

**NO SEPARATE TEST**

---

# TEST GROUP 18 — EQUALITY

## Test 31

Name:

```text
test_identical_runtime_record_headers_compare_equal
```

Construct two separate instances with identical values.

Assert:

```python
header_a == header_b
```

---

## Test 32

Name:

```text
test_runtime_record_header_equality_is_full_structural_equality
```

Parameterized field overrides:

* different `record_id`
* different `record_category`
* different `recorded_at`
* different `schema_version`
* different `provenance_ref`
* different `external_id`

For every case:

```python
header_a != header_b
```

---

## Test 33

Name:

```text
test_same_record_id_with_different_structure_is_not_equal
```

This is specifically important enough to remain explicit despite overlap.

Use same record ID and different category.

Assert inequality.

---

## Test 34

Name:

```text
test_equivalent_timezone_aware_instants_follow_python_datetime_equality
```

Example:

```python
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
```

Headers otherwise identical should compare equal because the datetime values represent the same instant under standard Python equality.

This confirms no custom datetime comparison.

---

# TEST GROUP 19 — HASHING

## Test 35

Name:

```text
test_equal_runtime_record_headers_have_equal_hashes
```

Assert:

```python
hash(header_a) == hash(header_b)
```

---

## Test 36

Name:

```text
test_structurally_different_headers_can_coexist_in_a_set
```

Construct two unequal headers.

Assert:

```python
len({header_a, header_b}) == 2
```

---

## Test 37

Name:

```text
test_hashing_does_not_change_runtime_record_header
```

Record tuple of all fields.

Call `hash(header)`.

Assert all values remain unchanged.

This may be logically redundant because the dataclass is frozen.

Decision:

**OPTIONAL BUT RETAINED**

---

# TEST GROUP 20 — ORDERING

## Test 38

Name:

```text
test_runtime_record_headers_do_not_support_ordering
```

Construct two headers.

Assert:

```python
with pytest.raises(TypeError):
    _ = header_a < header_b
```

No greater-than or sorting test is required.

---

# TEST GROUP 21 — REPRESENTATION

## Test 39

Name:

```text
test_runtime_record_header_uses_dataclass_representation
```

Pressure:

This risks coupling tests to non-essential formatting.

Decision:

**DO NOT TEST**

Representation remains default but is not part of the substantive first capability.

---

# TEST GROUP 22 — SERIALIZATION ABSENCE

## Test 39

Name:

```text
test_runtime_record_header_exposes_no_serialization_methods
```

Assert absence of:

```text
to_dict
from_dict
to_json
from_json
```

Pressure:

This directly protects a frozen non-goal.

Decision:

**RETAIN**

---

# TEST GROUP 23 — IMPORT ISOLATION

## Test 40

Name:

```text
test_importing_runtime_record_identity_does_not_import_application_frameworks
```

Before import:

* remove the module from `sys.modules` if present
* snapshot selected prohibited module names

Import:

```python
importlib.import_module("models.runtime_record_identity")
```

Assert import did not newly introduce:

```text
streamlit
src.kernel.kernel
src.services.object_engine
src.services.relationship_engine
src.services.event_engine
src.services.platform_registry
```

Qualification:

This test must avoid false failures caused by other test imports.

A safer approach is a subprocess, but that adds complexity.

Preferred design:

Use source-level import inspection only if required later.

Alternative:

Test the production module’s namespace after import for prohibited class references.

Decision:

Use a minimal import-isolation test asserting the module imports successfully without importing `streamlit` when `streamlit` was absent beforehand.

The test must account for pre-existing imports.

Status:

**TEST DESIGN REQUIRES CARE**

---

# TEST GROUP 24 — MODULE BOUNDARY

## Test 41

Name:

```text
test_runtime_record_identity_module_exports_only_runtime_record_header_as_public_model
```

Inspect module names not beginning with `_`.

Pressure:

Imported names such as `dataclass`, `datetime`, and `re` may appear publicly unless imported under private aliases.

This test would overconstrain internal import style.

Decision:

**DO NOT TEST**

Only the existence and direct import of `RuntimeRecordHeader` are required.

---

# TEST GROUP 25 — SIDE-EFFECT ABSENCE

## Test 41

Name:

```text
test_runtime_record_header_construction_requires_no_filesystem_or_service_setup
```

The test constructs a header without:

* temporary directories
* monkeypatches
* environment variables
* registry fixtures
* services

A simple construction test already demonstrates this.

Decision:

**NO SEPARATE TEST REQUIRED**

---

## Test 41

Name:

```text
test_runtime_record_identity_module_does_not_modify_requirements
```

This is not a unit-test concern.

Decision:

**REJECTED**

---

# TEST GROUP 26 — SEMANTIC NEUTRALITY

## Test 41

Name:

```text
test_record_category_does_not_restrict_values_to_current_examples
```

Use a structurally valid but not previously listed category:

```text
CUSTOM_RECORD
```

Assert successful construction.

This proves the model does not prematurely introduce a record-category enum.

---

## Test 42

Name:

```text
test_runtime_record_header_contains_no_semantic_payload
```

This is already proven by the exact field list.

Decision:

**NO SEPARATE TEST**

---

# TEST GROUP 27 — NO AUTOMATIC GENERATION

## Test 42

Name:

```text
test_runtime_record_header_does_not_generate_missing_record_id
```

Covered by required-field omission.

Decision:

**NO SEPARATE TEST**

---

## Test 42

Name:

```text
test_runtime_record_header_does_not_generate_recorded_at
```

Covered by required-field omission.

Decision:

**NO SEPARATE TEST**

---

# TEST GROUP 28 — NO NORMALIZATION

## Test 42

Name:

```text
test_runtime_record_header_rejects_values_instead_of_normalizing_them
```

Parameterized examples:

* lowercase record ID
* lowercase category
* prefixed schema version
* whitespace-surrounded provenance reference

These are already covered by invalid-value tests.

Decision:

**NO SEPARATE TEST**

---

# FINAL TEST LIST

The first test file should contain the following 42 logical test functions or parameterized test groups:

1. `test_runtime_record_header_is_a_dataclass`
2. `test_runtime_record_header_declares_exact_field_order`
3. `test_runtime_record_header_accepts_valid_required_fields`
4. `test_runtime_record_header_accepts_valid_optional_fields`
5. `test_runtime_record_header_accepts_non_utc_timezone_aware_datetime`
6. `test_runtime_record_header_preserves_external_id_exactly`
7. `test_runtime_record_header_requires_each_required_field`
8. `test_record_id_rejects_non_string_values`
9. `test_record_id_accepts_valid_values`
10. `test_record_id_rejects_invalid_values`
11. `test_record_category_rejects_non_string_values`
12. `test_record_category_accepts_valid_values`
13. `test_record_category_rejects_invalid_values`
14. `test_recorded_at_rejects_non_datetime_values`
15. `test_recorded_at_rejects_naive_datetime`
16. `test_recorded_at_rejects_timezone_with_no_utc_offset`
17. `test_recorded_at_preserves_supplied_timezone_and_offset`
18. `test_schema_version_rejects_non_string_values`
19. `test_schema_version_accepts_valid_values`
20. `test_schema_version_rejects_invalid_values`
21. `test_provenance_ref_rejects_non_string_non_none_values`
22. `test_provenance_ref_accepts_valid_values`
23. `test_provenance_ref_rejects_invalid_values`
24. `test_external_id_rejects_non_string_non_none_values`
25. `test_external_id_accepts_non_empty_values`
26. `test_external_id_rejects_empty_or_whitespace_only_values`
27. `test_record_id_type_failure_precedes_other_field_failures`
28. `test_record_id_value_failure_precedes_record_category_failure`
29. `test_required_field_validation_precedes_optional_field_validation`
30. `test_runtime_record_header_is_frozen`
31. `test_identical_runtime_record_headers_compare_equal`
32. `test_runtime_record_header_equality_is_full_structural_equality`
33. `test_same_record_id_with_different_structure_is_not_equal`
34. `test_equivalent_timezone_aware_instants_follow_python_datetime_equality`
35. `test_equal_runtime_record_headers_have_equal_hashes`
36. `test_structurally_different_headers_can_coexist_in_a_set`
37. `test_hashing_does_not_change_runtime_record_header`
38. `test_runtime_record_headers_do_not_support_ordering`
39. `test_runtime_record_header_exposes_no_serialization_methods`
40. `test_importing_runtime_record_identity_does_not_import_application_frameworks`
41. `test_record_category_does_not_restrict_values_to_current_examples`
42. `test_runtime_record_header_module_can_be_imported_directly`

---

# EXPECTED PYTEST CASE COUNT

Because several tests are parameterized, pytest will report more than 42 collected cases.

Expected approximate case count:

```text
100–120 tests
```

Exact count depends on the final parameter sets.

The exact case count should be recorded after the test file is written.

The contract freezes behavior, not a cosmetic target count.

---

# ERROR ASSERTION RULE

Tests should assert:

* exception class
* meaningful field-name fragment

Tests should not assert full exact error strings unless necessary.

Example:

```python
with pytest.raises(TypeError, match="record_id"):
    ...
```

Reason:

* preserves semantic stability
* avoids brittle punctuation coupling
* still verifies deterministic field attribution

---

# PARAMETERIZATION RULE

Use `pytest.mark.parametrize` for:

* wrong field types
* valid identity values
* invalid identity values
* valid categories
* invalid categories
* valid schema versions
* invalid schema versions
* provenance references
* external identities
* equality field differences
* immutability field assignments

Do not combine unrelated fields into one giant parameterized test.

Each group should preserve one semantic responsibility.

---

# TEST ISOLATION RULE

Each test must:

* construct its own header or use the stateless helper
* avoid shared mutable state
* avoid file operations
* avoid environment dependence
* avoid current time
* avoid service construction
* avoid network access
* avoid test ordering dependence

---

# IMPORT-ISOLATION TEST CONTRACT

The import-isolation test must:

1. avoid importing the application kernel
2. avoid instantiating services
3. import the model module directly
4. confirm `RuntimeRecordHeader` is available
5. confirm no new `streamlit` import occurs when it was not already loaded

Candidate pattern:

```python
def test_importing_runtime_record_identity_does_not_import_application_frameworks():
    sys.modules.pop("models.runtime_record_identity", None)
    streamlit_was_loaded = "streamlit" in sys.modules

    module = importlib.import_module("models.runtime_record_identity")

    assert hasattr(module, "RuntimeRecordHeader")

    if not streamlit_was_loaded:
        assert "streamlit" not in sys.modules
```

This does not prove every prohibited dependency is absent, but it provides a stable first-capability boundary test without source-code introspection.

Status:

**SELECTED**

---

# DIRECT IMPORT TEST CONTRACT

Test:

```python
def test_runtime_record_header_module_can_be_imported_directly():
    from models.runtime_record_identity import RuntimeRecordHeader as ImportedHeader

    assert ImportedHeader is RuntimeRecordHeader
```

Purpose:

* verifies candidate module path
* verifies no package-export mutation is required
* protects direct import boundary

---

# NO SERIALIZATION TEST CONTRACT

Test must assert:

```python
header = make_header()

assert not hasattr(header, "to_dict")
assert not hasattr(header, "from_dict")
assert not hasattr(header, "to_json")
assert not hasattr(header, "from_json")
```

This protects the explicit serialization deferral.

---

# DATACLASS FIELD TEST CONTRACT

Use:

```python
[field.name for field in fields(RuntimeRecordHeader)]
```

Expected:

```python
[
    "record_id",
    "record_category",
    "recorded_at",
    "schema_version",
    "provenance_ref",
    "external_id",
]
```

This test protects:

* exact field order
* no semantic payload
* no hidden status
* no authority field
* no target field
* no unapproved timestamp

---

# IMMUTABILITY TEST CONTRACT

Parameterized candidate:

```python
@pytest.mark.parametrize(
    ("field_name", "new_value"),
    [
        ("record_id", "RR-000000002"),
        ("record_category", "VERSION"),
        (
            "recorded_at",
            datetime(2026, 7, 18, tzinfo=timezone.utc),
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
```

Status:

**SELECTED**

---

# EQUALITY TEST CONTRACT

Parameterized differing-field values:

```python
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
]
```

For each:

```python
assert make_header() != make_header(**{field_name: value})
```

Status:

**SELECTED**

---

# VALIDATION PRECEDENCE CONTRACT

Tests must not inspect internal function order.

They should verify only externally observable precedence.

Required:

* invalid record ID type wins first
* invalid record ID value precedes category
* invalid required schema version precedes optional provenance

This is sufficient to protect the frozen validation order without testing implementation internals.

---

# TEST FAILURE EXPECTATION BEFORE IMPLEMENTATION

After creating the test file but before creating the production model, running:

```bat
python -m pytest tests\runtime\test_runtime_record_identity.py -q
```

should fail during collection with:

```text
ModuleNotFoundError
```

or equivalent import failure for:

```text
models.runtime_record_identity
```

This initial failure is expected and must be recorded.

Boundary:

Expected Test Failure
≠
Architecture Failure

---

# TEST CONTRACT NON-GOALS

The first test suite must not test:

1. registry uniqueness
2. automatic ID generation
3. persistence
4. JSON serialization
5. file creation
6. service inspection
7. Platform Registry integration
8. Research Kernel integration
9. event publication
10. graph relationships
11. authority
12. progression
13. branching
14. merge
15. Evaluation
16. provenance verification
17. schema migration
18. custom exceptions
19. slots
20. performance
21. thread safety
22. cryptographic integrity
23. external namespace parsing
24. content hashing
25. Runtime Object identity

---

# ARCHITECTURE TESTS

The tests must prove indirectly that:

* the model contains no semantic payload
* category remains string-based
* the model does not generate identity
* the model does not access the clock
* the model does not normalize malformed values
* the model does not serialize itself
* the model does not order records
* the model remains structurally immutable
* the model imports independently
* the model does not require application services

---

# TEST CONTRACT INVARIANTS

## Invariant 1

Tests must precede production implementation.

## Invariant 2

Every frozen field constraint must have at least one positive and one negative test where applicable.

## Invariant 3

Type failures and value failures must remain distinguishable.

## Invariant 4

Validation precedence must be externally verified.

## Invariant 5

The test suite must remain fully in memory.

## Invariant 6

No test may depend on the current clock.

## Invariant 7

No test may depend on filesystem state.

## Invariant 8

No test may require Platform Kernel or service construction.

## Invariant 9

Immutability must be verified for every field.

## Invariant 10

Full structural equality must be verified across every field.

## Invariant 11

Hashing must remain consistent with equality.

## Invariant 12

Ordering must remain unsupported.

## Invariant 13

Serialization deferral must remain protected.

## Invariant 14

The direct module import path must remain protected.

## Invariant 15

The category vocabulary must remain structurally open.

Status:

**FROZEN**

---

# TEST CONTRACT DECISION

Test path:
**FROZEN**

Framework:
**FROZEN**

Shared valid values:
**FROZEN**

Factory helper:
**PERMITTED**

Invalid timezone helper:
**FROZEN**

Positive construction tests:
**FROZEN**

Type tests:
**FROZEN**

Value tests:
**FROZEN**

Validation precedence tests:
**FROZEN**

Immutability tests:
**FROZEN**

Equality tests:
**FROZEN**

Hashing tests:
**FROZEN**

Ordering prohibition test:
**FROZEN**

Serialization-absence test:
**FROZEN**

Import-isolation test:
**FROZEN**

Direct-import test:
**FROZEN**

Production implementation:
**HOLD**

---

# READINESS CHECKPOINT 4

Test Contract:

**COMPLETE**

The test suite may now be written before production implementation.

The production model remains unauthorized until:

1. the test file is created
2. the expected import failure is recorded
3. the test content is reviewed
4. production implementation is explicitly admitted

---

# NEXT SESSION

Begin:

**RUNTIME RECORD IDENTITY FOUNDATION — TESTS BEFORE IMPLEMENTATION 001**

Required sequence:

1. create `tests\runtime`
2. create `test_runtime_record_identity.py`
3. paste the complete frozen test suite
4. run the isolated test file
5. confirm expected collection failure
6. inspect the test file
7. record exact collected-case target
8. preserve production implementation HOLD

**UNKNOWN → HOLD**
