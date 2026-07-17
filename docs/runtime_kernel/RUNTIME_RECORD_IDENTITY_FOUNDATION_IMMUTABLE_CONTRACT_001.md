# RESEARCH OS — RUNTIME RECORD IDENTITY FOUNDATION

# IMMUTABLE CONTRACT 001

**Date:** 2026-07-17
**Project:** Research OS
**Development Version:** v2.0.0
**Status:** ACTIVE / IMMUTABLE CONTRACT
**Architecture:** FROZEN WITH EXPLICIT DEFERRALS
**Implementation:** HOLD
**Authority:** CONTRACT ONLY

**UNKNOWN → HOLD**

---

# PURPOSE

Define the exact immutable construction contract for:

```text
RuntimeRecordHeader
```

This session freezes:

1. Python field types
2. constructor shape
3. dataclass configuration
4. validation order
5. type-error rules
6. value-error rules
7. datetime-awareness requirements
8. identity parsing rules
9. optional-field rules
10. equality semantics
11. hashing semantics
12. import boundaries
13. side-effect prohibitions
14. exact testable acceptance criteria

This session does not authorize tests or implementation.

---

# PREREQUISITE

Vocabulary Selection 001 established:

## Model Name

```text
RuntimeRecordHeader
```

## Required Fields

```text
record_id: str
record_category: str
recorded_at: datetime
schema_version: str
```

## Optional Fields

```text
provenance_ref: str | None
external_id: str | None
```

## Candidate Path

```text
models/runtime_record_identity.py
```

## Candidate Test Path

```text
tests/runtime/test_runtime_record_identity.py
```

---

# OPERATING RULES

* Do not implement.
* Do not create tests.
* Do not add dependencies.
* Do not create custom exceptions.
* Do not create automatic identity generation.
* Do not normalize malformed values.
* Do not access the clock.
* Do not access files.
* Do not access registries.
* Do not define serialization.
* Do not introduce semantic payload.
* Freeze only directly testable contract behavior.

---

# MODEL ROLE

`RuntimeRecordHeader` is an immutable structural header for future Runtime Kernel records.

It contains shared record-level identity and attribution fields.

It does not represent:

* a Runtime Object
* a Runtime Event payload
* a progression assertion
* a Hold
* a Branch
* an Evaluation
* a relationship
* a canonical state
* an authority decision

Boundary:

Runtime Record Header
≠
Runtime Record Payload

---

# EXACT IMPORT BOUNDARY

The future implementation may import only:

```python
from dataclasses import dataclass
from datetime import datetime
import re
```

Alternative internal import style may be accepted if semantically equivalent.

The model must not import:

* Streamlit
* pathlib
* JSON modules
* Platform Kernel services
* Runtime Kernel services
* ObjectEngine
* RelationshipEngine
* EventEngine
* PlatformRegistry
* ResearchKernel
* logging services
* external validation libraries

Status:

**FROZEN**

---

# EXACT MODEL DECLARATION

The future model must use:

```python
@dataclass(frozen=True)
class RuntimeRecordHeader:
    ...
```

Required configuration:

* `frozen=True`
* default structural equality
* default structural representation
* no ordering
* no unsafe hash override
* no slots requirement in the first capability

Explicitly prohibited:

```python
order=True
unsafe_hash=True
eq=False
```

Status:

**FROZEN**

---

# FIELD DECLARATION ORDER

The exact field declaration order is:

```python
record_id: str
record_category: str
recorded_at: datetime
schema_version: str
provenance_ref: str | None = None
external_id: str | None = None
```

Required fields must appear before optional fields.

Status:

**FROZEN**

---

# CONSTRUCTOR CONTRACT

The constructor must require explicit values for:

```text
record_id
record_category
recorded_at
schema_version
```

Optional values:

```text
provenance_ref
external_id
```

No default is permitted for:

* `record_id`
* `record_category`
* `recorded_at`
* `schema_version`

Permitted defaults:

```python
provenance_ref = None
external_id = None
```

The constructor must not:

* generate identifiers
* read current time
* infer category
* infer schema version
* resolve provenance
* normalize values

Status:

**FROZEN**

---

# POST-CONSTRUCTION VALIDATION

Validation must occur during object construction through:

```python
__post_init__()
```

Because the dataclass is frozen, validation may inspect fields but must not alter them.

No use of:

```python
object.__setattr__()
```

is permitted.

Reason:

The contract prohibits silent normalization and construction-time mutation.

Status:

**FROZEN**

---

# VALIDATION ORDER

Validation must occur in this exact conceptual order:

1. `record_id` type
2. `record_id` value
3. `record_category` type
4. `record_category` value
5. `recorded_at` type
6. `recorded_at` timezone awareness
7. `schema_version` type
8. `schema_version` value
9. `provenance_ref` type
10. `provenance_ref` value
11. `external_id` type
12. `external_id` value

Reason:

* deterministic failure behavior
* required fields before optional fields
* type checks before value checks
* identity before category
* temporal validity before optional attribution

Status:

**FROZEN**

---

# ERROR CONTRACT

## Type Errors

Use:

```python
TypeError
```

when a supplied value is not of the required Python type.

## Value Errors

Use:

```python
ValueError
```

when a value has the correct Python type but violates structural constraints.

No custom exception classes are permitted in the first capability.

Status:

**FROZEN**

---

# ERROR MESSAGE CONTRACT

Error messages must:

* identify the field
* state the violated requirement
* remain deterministic
* avoid exposing internal regex implementation unnecessarily

Exact wording need not be globally frozen, but tests may assert stable meaningful fragments.

Recommended fragments:

```text
record_id must be a string
record_id must match RR-#########
record_category must be a string
record_category must use uppercase underscore syntax
recorded_at must be a datetime
recorded_at must be timezone-aware
schema_version must be a string
schema_version must use MAJOR.MINOR format
provenance_ref must be a string or None
provenance_ref must match PRV-#########
external_id must be a string or None
external_id must not be empty
```

Status:

**FROZEN AT SEMANTIC LEVEL**

---

# RECORD_ID TYPE CONTRACT

Required Python type:

```python
str
```

Invalid types include:

* `None`
* `int`
* `float`
* `bool`
* `bytes`
* lists
* dictionaries
* custom objects

Wrong type result:

```python
TypeError
```

Status:

**FROZEN**

---

# RECORD_ID VALUE CONTRACT

Required syntax:

```text
RR-#########
```

Exact regex:

```text
^RR-[0-9]{9}$
```

Additional semantic rule:

The numeric component must be greater than zero.

Valid:

```text
RR-000000001
RR-000000042
RR-999999999
```

Invalid:

```text
RR-000000000
rr-000000001
RR000000001
RR-1
 RR-000000001
RR-000000001 
RR-00000001A
```

Invalid value result:

```python
ValueError
```

Status:

**FROZEN**

---

# RECORD_ID PARSING RULE

The implementation may inspect the numeric portion using:

```python
int(record_id[3:])
```

or equivalent logic.

It must not:

* return the numeric component
* expose ordering
* generate the next identity
* infer chronology
* compare semantic priority

Status:

**FROZEN**

---

# RECORD_CATEGORY TYPE CONTRACT

Required Python type:

```python
str
```

Wrong type result:

```python
TypeError
```

Status:

**FROZEN**

---

# RECORD_CATEGORY VALUE CONTRACT

Exact regex:

```text
^[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)*$
```

Valid:

```text
EVENT
VERSION
HOLD
RE_ENTRY
INSPECTION_RESULT
CATEGORY2
TYPE_2
```

Invalid:

```text
event
Event
RE-ENTRY
RE ENTRY
_RE_ENTRY
RE_ENTRY_
RE__ENTRY
""
" "
```

The implementation must not:

* trim whitespace
* uppercase input
* replace hyphens
* collapse repeated underscores

Invalid value result:

```python
ValueError
```

Status:

**FROZEN**

---

# RECORDED_AT TYPE CONTRACT

Required Python type:

```python
datetime
```

Wrong type result:

```python
TypeError
```

Invalid examples:

* ISO timestamp string
* Unix integer timestamp
* date-only value
* `None`

Status:

**FROZEN**

---

# RECORDED_AT TIMEZONE-AWARENESS CONTRACT

A valid `recorded_at` must satisfy:

```python
recorded_at.tzinfo is not None
```

and:

```python
recorded_at.utcoffset() is not None
```

A naïve datetime is invalid.

Invalid:

```python
datetime(2026, 7, 17, 12, 0, 0)
```

Valid:

```python
datetime(2026, 7, 17, 12, 0, 0, tzinfo=timezone.utc)
```

A custom timezone object returning `None` from `utcoffset()` is invalid.

Invalid value result:

```python
ValueError
```

Status:

**FROZEN**

---

# RECORDED_AT PRESERVATION RULE

The model must preserve the supplied datetime object value without converting it to UTC or replacing its timezone.

No call to:

```python
astimezone()
replace()
datetime.now()
datetime.utcnow()
```

is permitted during construction.

Boundary:

Timezone-Aware Validation
≠
Timezone Normalization

Status:

**FROZEN**

---

# SCHEMA_VERSION TYPE CONTRACT

Required Python type:

```python
str
```

Wrong type result:

```python
TypeError
```

Status:

**FROZEN**

---

# SCHEMA_VERSION VALUE CONTRACT

Exact regex:

```text
^[1-9][0-9]*\.[0-9]+$
```

Valid:

```text
1.0
1.1
2.0
12.4
999.999
```

Invalid:

```text
v1.0
1
1.0.0
01.0
0.1
1.x
1.
.1
""
" "
```

The major version must be greater than zero.

The minor component may be zero.

The implementation must not normalize:

```text
01.0
```

to:

```text
1.0
```

Invalid value result:

```python
ValueError
```

Status:

**FROZEN**

---

# PROVENANCE_REF TYPE CONTRACT

Permitted types:

```python
str | None
```

Wrong types include:

* integers
* lists
* dictionaries
* bytes
* booleans

Wrong type result:

```python
TypeError
```

Status:

**FROZEN**

---

# PROVENANCE_REF VALUE CONTRACT

When present, required syntax:

```text
PRV-#########
```

Exact regex:

```text
^PRV-[0-9]{9}$
```

Additional semantic rule:

The numeric component must be greater than zero.

Valid:

```text
PRV-000000001
PRV-999999999
```

Invalid:

```text
PRV-000000000
prv-000000001
PRV000000001
PRV-1
 PRV-000000001
PRV-000000001 
```

Invalid value result:

```python
ValueError
```

Status:

**FROZEN**

---

# PROVENANCE_REF NONE SEMANTICS

```python
provenance_ref=None
```

means only:

```text
No local provenance record reference is established in this header.
```

It does not mean:

* provenance is absent
* provenance is invalid
* provenance is unknown
* provenance is unavailable
* provenance is verified
* provenance is not required

Status:

**FROZEN**

---

# EXTERNAL_ID TYPE CONTRACT

Permitted types:

```python
str | None
```

Wrong type result:

```python
TypeError
```

Status:

**FROZEN**

---

# EXTERNAL_ID VALUE CONTRACT

When present, `external_id` must:

* contain at least one character
* not be whitespace-only
* preserve its exact supplied value

The following are invalid:

```text
""
" "
"\t"
"\n"
```

The following may be valid:

```text
EXT-123
doi:10.1000/example
external/system/record/42
 abc
abc 
```

Important qualification:

Leading or trailing whitespace inside a non-whitespace-only external identifier is preserved in the first contract.

Reason:

The first model does not define external namespace normalization.

The model only rejects empty or whitespace-only values.

Status:

**FROZEN WITH QUALIFICATION**

---

# EXTERNAL_ID NORMALIZATION RULE

The model must not:

* strip whitespace
* lowercase
* uppercase
* parse namespace
* validate URI syntax
* establish trust
* establish uniqueness

Status:

**FROZEN**

---

# IMMUTABILITY CONTRACT

After construction, attempts to assign any field must fail through standard frozen-dataclass behavior.

Fields include:

* `record_id`
* `record_category`
* `recorded_at`
* `schema_version`
* `provenance_ref`
* `external_id`

Expected exception:

```python
dataclasses.FrozenInstanceError
```

The model must not expose mutation methods.

Prohibited methods include:

```text
update
replace_field
set_record_id
set_category
set_external_id
```

Status:

**FROZEN**

---

# SHALLOW IMMUTABILITY BOUNDARY

All selected fields are immutable scalar or immutable-reference values.

The model contains no mutable lists, dictionaries, or sets.

Therefore shallow dataclass immutability is sufficient for this capability.

Status:

**FROZEN**

---

# EQUALITY CONTRACT

Use standard dataclass full structural equality.

Two headers are equal only when all fields compare equal.

Compared fields:

1. `record_id`
2. `record_category`
3. `recorded_at`
4. `schema_version`
5. `provenance_ref`
6. `external_id`

Same `record_id` with different structure:

```text
NOT EQUAL
```

Different `record_id` with identical remaining fields:

```text
NOT EQUAL
```

Status:

**FROZEN**

---

# DATETIME EQUALITY QUALIFICATION

Python timezone-aware datetimes representing the same instant may compare equal even when their timezone offsets differ.

The model accepts standard Python datetime equality.

It must not override datetime comparison.

Status:

**FROZEN**

---

# HASHING CONTRACT

Use standard frozen-dataclass hashing behavior.

The model must not define a custom:

```python
__hash__()
```

Hashing remains structural and consistent with equality.

The hash must not be used to establish:

* registry uniqueness
* persistence identity
* content integrity
* semantic equivalence

Status:

**FROZEN**

---

# ORDERING CONTRACT

The model must not support structural ordering.

Do not use:

```python
order=True
```

Operations such as:

```python
header_a < header_b
```

should not be defined by the model.

Record-number order must not imply:

* creation order
* temporal order
* authority
* semantic priority
* currentness

Status:

**FROZEN**

---

# REPRESENTATION CONTRACT

Use the standard dataclass-generated `repr`.

Do not implement:

* custom `__str__`
* custom `__repr__`
* display formatting
* redaction formatting

Reason:

Representation must not become an accidental serialization contract.

Status:

**FROZEN FOR FIRST CAPABILITY**

---

# SERIALIZATION CONTRACT

No serialization methods are permitted.

Do not implement:

* `to_dict`
* `from_dict`
* `to_json`
* `from_json`
* file writing
* file reading
* pickle helpers
* schema migration

Tests must not assume a serialization API.

Status:

**FROZEN AS DEFERRED**

---

# SIDE-EFFECT CONTRACT

Constructing `RuntimeRecordHeader` must not:

* read files
* write files
* create directories
* read environment variables
* access network resources
* access registries
* emit logs
* publish events
* access the current clock
* mutate external objects
* create relationships
* register itself

Status:

**FROZEN**

---

# DEPENDENCY CONTRACT

The production model must use only the Python standard library.

No new dependency may be added to:

```text
requirements.txt
```

Status:

**FROZEN**

---

# MODULE CONTRACT

Candidate production path:

```text
models/runtime_record_identity.py
```

The module should define only:

```text
RuntimeRecordHeader
```

Internal compiled regex constants may also exist.

It must not define:

* registries
* services
* generators
* payload records
* enums
* exceptions
* persistence
* inspection services

Status:

**FROZEN**

---

# MODULE EXPORT CONTRACT

No modification to a package `__init__.py` is required because the top-level `models` directory currently has no package export contract.

Tests should import directly:

```python
from models.runtime_record_identity import RuntimeRecordHeader
```

Status:

**FROZEN**

---

# VALIDATION IMPLEMENTATION SHAPE

The future implementation may use private module-level regex constants:

```python
_RECORD_ID_PATTERN
_RECORD_CATEGORY_PATTERN
_PROVENANCE_REF_PATTERN
_SCHEMA_VERSION_PATTERN
```

These constants are implementation details.

They must not be treated as public API.

Status:

**PERMITTED**

---

# VALIDATION HELPER BOUNDARY

Private helper functions may be used if they:

* remain module-local
* introduce no side effects
* preserve validation order
* do not become public API
* do not normalize input

A single `__post_init__()` implementation is also acceptable.

Status:

**SAFE IMPLEMENTATION DEFERRAL**

---

# ACCEPTANCE CRITERIA — VALID CONSTRUCTION

The model must successfully construct when provided:

```python
RuntimeRecordHeader(
    record_id="RR-000000001",
    record_category="EVENT",
    recorded_at=aware_datetime,
    schema_version="1.0",
)
```

It must preserve:

```text
provenance_ref = None
external_id = None
```

It must also construct successfully with valid optional values.

Status:

**FROZEN**

---

# ACCEPTANCE CRITERIA — IDENTITY

The model must:

1. accept valid `RR-#########`
2. reject zero identity
3. reject lowercase prefix
4. reject malformed separators
5. reject incorrect digit count
6. reject surrounding whitespace
7. reject non-string values
8. preserve exact valid identity

Status:

**FROZEN**

---

# ACCEPTANCE CRITERIA — CATEGORY

The model must:

1. accept uppercase categories
2. accept valid underscore-separated categories
3. accept digits after the first character
4. reject lowercase
5. reject spaces
6. reject hyphens
7. reject repeated underscores
8. reject leading or trailing underscores
9. reject empty values
10. reject non-string values

Status:

**FROZEN**

---

# ACCEPTANCE CRITERIA — TIME

The model must:

1. accept timezone-aware datetime
2. reject naïve datetime
3. reject datetime with unusable timezone offset
4. reject non-datetime values
5. preserve the supplied datetime value
6. avoid clock access
7. avoid timezone conversion

Status:

**FROZEN**

---

# ACCEPTANCE CRITERIA — SCHEMA VERSION

The model must:

1. accept `MAJOR.MINOR`
2. accept zero minor version
3. reject zero major version
4. reject leading-zero major version
5. reject prefixed version
6. reject three-component version
7. reject non-string values
8. preserve exact valid value

Status:

**FROZEN**

---

# ACCEPTANCE CRITERIA — PROVENANCE REFERENCE

The model must:

1. accept `None`
2. accept valid `PRV-#########`
3. reject zero provenance identity
4. reject malformed provenance identity
5. reject lowercase prefix
6. reject surrounding whitespace
7. reject non-string and non-`None` values
8. preserve exact valid reference

Status:

**FROZEN**

---

# ACCEPTANCE CRITERIA — EXTERNAL IDENTITY

The model must:

1. accept `None`
2. accept non-empty string
3. reject empty string
4. reject whitespace-only string
5. reject non-string and non-`None` values
6. preserve exact supplied value
7. perform no namespace validation
8. perform no normalization

Status:

**FROZEN**

---

# ACCEPTANCE CRITERIA — IMMUTABILITY

The model must reject reassignment of every field after construction.

The tests must verify standard frozen-dataclass failure behavior.

Status:

**FROZEN**

---

# ACCEPTANCE CRITERIA — EQUALITY

The tests must prove:

1. identical structure compares equal
2. different `record_id` compares unequal
3. different category compares unequal
4. different time compares unequal
5. different schema version compares unequal
6. different provenance reference compares unequal
7. different external identity compares unequal
8. same identity with different structure compares unequal

Status:

**FROZEN**

---

# ACCEPTANCE CRITERIA — HASHING

The tests must prove:

1. equal headers have equal hashes
2. structurally different headers may coexist in a set
3. hashing does not mutate the object
4. no custom identity-only hashing is present

Status:

**FROZEN**

---

# ACCEPTANCE CRITERIA — NO ORDERING

The tests must prove that ordering comparison is unsupported.

Example:

```python
header_a < header_b
```

should raise:

```python
TypeError
```

Status:

**FROZEN**

---

# ACCEPTANCE CRITERIA — NO SIDE EFFECTS

The first test suite must not require:

* temporary directories
* file cleanup
* registry resets
* network mocks
* clock mocks
* environment patches
* service fixtures

The model must be constructible entirely in memory.

Status:

**FROZEN**

---

# ACCEPTANCE CRITERIA — IMPORT ISOLATION

Importing the model must not import:

* Streamlit
* Platform Kernel services
* graph engines
* event engines
* object engines
* relationship engines
* application context
* kernel instances

Status:

**FROZEN**

---

# ADVERSARIAL CONTRACT TESTS

## Test 1 — Frozen Model with Normalization

Proposal:

Use `object.__setattr__()` to uppercase category values.

Finding:

Violates exact-input preservation.

Result:

**REJECTED**

---

## Test 2 — Default Timestamp

Proposal:

Use `default_factory=datetime.utcnow`.

Finding:

Creates naïve time and hidden clock dependence.

Result:

**REJECTED**

---

## Test 3 — Default Schema Version

Proposal:

Default to `"1.0"`.

Finding:

Hides structural contract selection.

Result:

**REJECTED**

---

## Test 4 — Custom Identity Equality

Proposal:

Compare only `record_id`.

Finding:

Conceals structural identity conflicts.

Result:

**REJECTED**

---

## Test 5 — Custom Ordering

Proposal:

Order by numeric record identity.

Finding:

Introduces unsupported chronology.

Result:

**REJECTED**

---

## Test 6 — External ID Stripping

Proposal:

Strip leading and trailing whitespace.

Finding:

Introduces undefined external-namespace normalization.

Result:

**REJECTED**

---

## Test 7 — Provenance UNKNOWN Marker

Proposal:

Use `"UNKNOWN"` instead of `None`.

Finding:

Mixes identity reference with epistemic condition.

Result:

**REJECTED**

---

## Test 8 — Generic Payload Field

Proposal:

Add:

```python
payload: dict
```

Finding:

Creates an untyped universal record envelope.

Result:

**REJECTED**

---

## Test 9 — Registry Uniqueness Check During Construction

Proposal:

Check `record_id` against a registry.

Finding:

Introduces side effects and service coupling.

Result:

**REJECTED**

---

## Test 10 — Serialization Methods

Proposal:

Add `to_dict()` for convenience.

Finding:

Serialization contract remains deferred.

Result:

**REJECTED FOR FIRST CAPABILITY**

---

# IMMUTABLE CONTRACT SUMMARY

## Model

```text
RuntimeRecordHeader
```

## Dataclass

```text
frozen=True
```

## Equality

```text
full structural equality
```

## Hashing

```text
standard frozen-dataclass hashing
```

## Ordering

```text
unsupported
```

## Validation

```text
construction-time
type before value
deterministic order
```

## Errors

```text
wrong type → TypeError
invalid value → ValueError
```

## Serialization

```text
not implemented
```

## Side Effects

```text
none
```

## Dependencies

```text
Python standard library only
```

---

# CONTRACT INVARIANTS

## Invariant 1

The model must remain immutable after successful construction.

## Invariant 2

The model must not alter supplied valid values.

## Invariant 3

Type validation must occur before value validation.

## Invariant 4

Required fields must never receive implicit defaults.

## Invariant 5

`recorded_at` must be timezone-aware and explicitly supplied.

## Invariant 6

Local identity must remain distinct from external identity.

## Invariant 7

Provenance reference absence must remain represented by `None`.

## Invariant 8

Full structural equality must remain intact.

## Invariant 9

No custom ordering may be introduced.

## Invariant 10

No construction-time side effects are permitted.

## Invariant 11

No registry uniqueness may be inferred.

## Invariant 12

No semantic payload may be introduced.

## Invariant 13

No serialization API may be introduced.

## Invariant 14

No external dependency may be introduced.

## Invariant 15

No Platform Kernel or Runtime service coupling may be introduced.

Status:

**FROZEN**

---

# CONTRACT DECISION

Python field types:
**FROZEN**

Constructor contract:
**FROZEN**

Dataclass configuration:
**FROZEN**

Validation order:
**FROZEN**

Type-error rules:
**FROZEN**

Value-error rules:
**FROZEN**

Datetime-awareness rule:
**FROZEN**

Identity parsing rules:
**FROZEN**

Optional-field rules:
**FROZEN**

Equality semantics:
**FROZEN**

Hashing semantics:
**FROZEN**

Ordering prohibition:
**FROZEN**

Serialization boundary:
**FROZEN**

Import boundary:
**FROZEN**

Acceptance criteria:
**FROZEN**

Implementation:
**HOLD**

---

# READINESS CHECKPOINT 3

Immutable Contract:

**COMPLETE**

The contract is ready for test design.

No production model was created.

No tests were created.

No implementation authority was granted.

---

# NEXT SESSION

Begin:

**RUNTIME RECORD IDENTITY FOUNDATION — TEST CONTRACT 001**

Primary question:

What exact tests must be written before implementation to prove construction validity, invalid-input refusal, immutability, equality, hashing, ordering prohibition, import isolation, and absence of side effects?

Required work:

1. define test file structure
2. define valid fixtures
3. define parameterized invalid identities
4. define category tests
5. define datetime tests
6. define schema-version tests
7. define optional-field tests
8. define immutability tests
9. define equality tests
10. define hashing tests
11. define no-ordering test
12. define import-isolation test
13. define test count
14. preserve production implementation HOLD

**UNKNOWN → HOLD**
