# RESEARCH OS — RUNTIME RECORD IDENTITY FOUNDATION

# VOCABULARY SELECTION 001

**Date:** 2026-07-17
**Project:** Research OS
**Development Version:** v2.0.0
**Status:** ACTIVE / VOCABULARY SELECTION
**Architecture:** FROZEN WITH EXPLICIT DEFERRALS
**Implementation:** HOLD
**Authority:** VOCABULARY ONLY

**UNKNOWN → HOLD**

---

# PURPOSE

Select the exact vocabulary required for the first immutable Runtime Kernel record contract.

This session will define:

1. model name
2. field names
3. field meanings
4. required and optional fields
5. local identity syntax
6. record-category semantics
7. recorded-time semantics
8. provenance-reference semantics
9. external-identity semantics
10. schema-version semantics
11. equality boundaries
12. serialization boundaries
13. explicit non-goals

This session does not authorize tests or implementation.

---

# PREREQUISITE

Repository Inspection 001 established:

* top-level models use Python dataclasses
* no immutable domain model currently exists
* no typed identity contract currently exists
* no formal model serialization contract exists
* no test suite currently exists
* the first model should remain isolated
* candidate model path is:

```text
models/runtime_record_identity.py
```

* candidate test path is:

```text
tests/runtime/test_runtime_record_identity.py
```

---

# OPERATING RULES

* Do not implement.
* Do not create the model file.
* Do not create tests.
* Do not create an enumeration.
* Do not add automatic identity generation.
* Do not define registry behavior.
* Do not define Runtime Event semantics.
* Do not define Runtime Object semantics.
* Do not define authority behavior.
* Do not define canonical projection.
* Use exact and non-overloaded field names.
* Preserve local and external identity separation.
* Freeze only vocabulary that survives reduction.

---

# PRIMARY QUESTION

What is the smallest vocabulary required for an immutable Runtime Kernel record to remain:

* uniquely identifiable
* categorically distinguishable
* temporally attributable
* provenance-reference capable
* externally traceable
* schema attributable
* semantically neutral
* free of side effects

---

# MODEL NAME CANDIDATES

## Candidate A — RuntimeRecordIdentity

Advantages:

* directly names the first capability
* emphasizes identity
* small conceptual surface

Problems:

* the proposed record also contains category, time, provenance reference, external identity, and schema version
* may imply the model is an identity value object only

Result:

**REJECTED AS MODEL NAME**

May remain the capability name.

---

## Candidate B — RuntimeRecordHeader

Advantages:

* accurately describes common immutable record-level fields
* does not imply full record content
* does not collapse semantic record types
* permits later composition
* distinguishes shared record envelope from domain payload

Problems:

* “header” may sound transport-oriented
* must not imply serialization format

Result:

**STRONGLY SUPPORTED**

---

## Candidate C — RuntimeRecordDescriptor

Advantages:

* indicates descriptive record information
* avoids transport terminology

Problems:

* may be confused with descriptive Metadata
* “descriptor” may imply mutable documentation

Result:

**REJECTED**

---

## Candidate D — RuntimeRecordReference

Advantages:

* emphasizes addressability

Problems:

* a reference should not normally contain recorded time, schema version, or provenance reference
* may imply indirection rather than the record’s own structural identity

Result:

**REJECTED**

---

# MODEL NAME DECISION

Selected model name:

```text
RuntimeRecordHeader
```

Definition:

A `RuntimeRecordHeader` is the immutable, semantically neutral structural header shared by future Runtime Kernel records.

It identifies:

* the local record
* the record family
* when the record entered the local runtime
* its minimal provenance reference
* any declared external identity
* the schema contract used to construct it

It does not define the record’s semantic payload.

Status:

**SELECTED**

---

# CAPABILITY NAME

The capability remains:

```text
Runtime Record Identity Foundation
```

The implementation model is:

```text
RuntimeRecordHeader
```

Boundary:

Capability Name
≠
Model Name

Status:

**SELECTED**

---

# CANDIDATE FIELD SET

Selected candidate fields:

1. `record_id`
2. `record_category`
3. `recorded_at`
4. `provenance_ref`
5. `external_id`
6. `schema_version`

---

# FIELD 1 — RECORD_ID

Selected name:

```text
record_id
```

Definition:

The stable local identifier assigned to one immutable Runtime Kernel record.

It must remain:

* locally unique
* non-empty
* normalized
* stable
* non-reassignable
* independent from content
* independent from storage location
* independent from external identity

Boundary:

`record_id`
≠
Runtime Object identity

`record_id`
≠
target identity

`record_id`
≠
content hash

`record_id`
≠
external identifier

Status:

**REQUIRED**

---

# RECORD_ID SYNTAX

Candidate syntax:

```text
RR-000000001
```

Where:

* `RR` means Runtime Record
* separator is one hyphen
* numeric component contains nine digits
* numeric component is greater than zero
* alphabetic prefix is uppercase

Candidate regular expression:

```text
^RR-[0-9]{9}$
```

Valid examples:

```text
RR-000000001
RR-000000042
RR-999999999
```

Invalid examples:

```text
RR-000000000
rr-000000001
RR000000001
RR-1
 EVT-000000001
```

Pressure:

The zero value technically matches the regular expression but should remain invalid because it does not identify a usable record.

Candidate semantic rule:

```text
record_id must match ^RR-[0-9]{9}$
and numeric portion must be greater than zero
```

Status:

**STRONGLY SUPPORTED**

---

# RECORD_ID NORMALIZATION

Question:

Should input be automatically trimmed or uppercased?

Candidate decision:

No.

Automatic normalization would hide malformed input and weaken exact identity preservation.

Therefore:

* leading whitespace is invalid
* trailing whitespace is invalid
* lowercase prefix is invalid
* internal formatting differences are invalid

Boundary:

Validation
≠
Silent Normalization

Status:

**SELECTED**

---

# RECORD_ID GENERATION

The model must not generate identities.

Identity generation belongs to a future separately reduced capability.

The constructor must receive an explicit `record_id`.

Boundary:

Identity Contract
≠
Identity Generator

Status:

**DEFERRED / NON-GOAL**

---

# FIELD 2 — RECORD_CATEGORY

Selected name:

```text
record_category
```

Definition:

A declared string identifying the family of Runtime Kernel record represented by the containing record.

Examples may later include:

* EVENT
* VERSION
* PROGRESSION_ASSERTION
* HOLD
* REVISION
* BRANCH
* MERGE
* EVALUATION
* RE_ENTRY
* INSPECTION_RESULT
* RECONSTRUCTION_RESULT

These values are not frozen in this session.

Boundary:

`record_category`
≠
Runtime Object Type

`record_category`
≠
Runtime Event Type

`record_category`
≠
progression condition

`record_category`
≠
canonical effect

Status:

**REQUIRED**

---

# RECORD_CATEGORY REPRESENTATION

Candidate representation:

```text
str
```

Do not create an enumeration yet.

Reason:

* exact record-category vocabulary remains deferred
* the first contract must not prematurely freeze all future record families
* string validation can preserve structure without overcommitting semantics

Status:

**SELECTED**

---

# RECORD_CATEGORY SYNTAX

Candidate syntax:

* uppercase ASCII letters
* digits permitted after the first character
* underscore separators permitted
* no spaces
* no hyphens
* no leading or trailing underscore
* no repeated underscore

Candidate regular expression:

```text
^[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)*$
```

Valid examples:

```text
EVENT
VERSION
HOLD
RE_ENTRY
INSPECTION_RESULT
```

Invalid examples:

```text
event
Progression Assertion
RE-ENTRY
_RE_ENTRY
RE_ENTRY_
RE__ENTRY
```

Status:

**STRONGLY SUPPORTED**

---

# RECORD_CATEGORY NORMALIZATION

Do not uppercase or trim category values automatically.

Malformed category values must be refused.

Status:

**SELECTED**

---

# FIELD 3 — RECORDED_AT

Selected name:

```text
recorded_at
```

Definition:

The timezone-aware datetime at which the immutable record entered the local Runtime Kernel record domain.

It does not mean:

* when an external occurrence happened
* when source content was created
* when an observation occurred
* when an operation became effective
* when a record was imported

Boundary:

`recorded_at`
≠
`occurred_at`

`recorded_at`
≠
`effective_at`

`recorded_at`
≠
`created_at`

`recorded_at`
≠
`imported_at`

Status:

**REQUIRED**

---

# RECORDED_AT TYPE

Selected type:

```text
datetime
```

Requirements:

* must be timezone-aware
* must have a non-`None` UTC offset
* must be supplied explicitly
* must not default to the current time
* must remain immutable

Reason:

An automatic default would introduce construction-time side effects and make tests less explicit.

Status:

**SELECTED**

---

# UTC NORMALIZATION

Question:

Should every supplied datetime be converted automatically to UTC?

Candidate decision:

No automatic conversion inside the immutable model.

The exact supplied timezone-aware instant should remain preserved.

Equivalent instants with different offsets may compare equal under Python datetime semantics, but the model must not rewrite the supplied value.

Serialization may later standardize output separately.

Status:

**SELECTED WITH QUALIFICATION**

---

# FIELD 4 — PROVENANCE_REF

Selected name:

```text
provenance_ref
```

Definition:

An optional local reference to an independently addressable provenance record associated with the Runtime Kernel record.

Boundary:

`provenance_ref` present
≠
provenance verified

`provenance_ref` absent
≠
provenance does not exist

`provenance_ref`
≠
source identity

Status:

**OPTIONAL**

---

# PROVENANCE_REF REPRESENTATION

Selected representation:

```text
str | None
```

Candidate syntax where present:

```text
PRV-000000001
```

Candidate rule:

```text
^PRV-[0-9]{9}$
```

Numeric component must be greater than zero.

Question:

Should unresolved provenance use a special string marker?

Candidate decision:

No.

Use:

```text
provenance_ref = None
```

An absent reference means:

```text
no local provenance reference is established in this header
```

It does not mean:

* provenance is false
* provenance is unavailable
* provenance is verified
* provenance is complete

A future provenance-bearing record may express more precise conditions.

Status:

**SELECTED**

---

# FIELD 5 — EXTERNAL_ID

Selected name:

```text
external_id
```

Definition:

An optional identifier assigned to the same record by an external source or system.

Boundary:

`external_id`
≠
local `record_id`

`external_id`
≠
verified identity mapping

`external_id`
≠
trusted provenance

Status:

**OPTIONAL**

---

# EXTERNAL_ID REPRESENTATION

Selected representation:

```text
str | None
```

Requirements where present:

* non-empty
* not whitespace-only
* exact value preserved
* no automatic normalization
* no assumption of global uniqueness
* no assumption of namespace validity
* no assumption of trust

Question:

Should namespace be a separate field?

Candidate decision:

Not in the first contract.

A future external-identity model may introduce:

* namespace
* source system
* mapping condition
* verification status

Status:

**SELECTED WITH EXPLICIT DEFERRAL**

---

# FIELD 6 — SCHEMA_VERSION

Selected name:

```text
schema_version
```

Definition:

The version of the structural model contract under which the Runtime Record Header was constructed.

Boundary:

`schema_version`
≠
Runtime Object Version

`schema_version`
≠
application version

`schema_version`
≠
Research Release version

`schema_version`
≠
record revision number

Status:

**REQUIRED**

---

# SCHEMA_VERSION REPRESENTATION

Selected representation:

```text
str
```

Candidate syntax:

```text
1.0
```

Candidate regular expression:

```text
^[1-9][0-9]*\.[0-9]+$
```

Valid examples:

```text
1.0
1.1
2.0
12.4
```

Invalid examples:

```text
v1.0
1
01.0
1.0.0
1.x
```

Pressure:

Semantic versioning normally permits three components.

However, the first structural schema contract only requires major and minor versions.

Candidate decision:

Use:

```text
MAJOR.MINOR
```

Patch-level implementation releases remain outside the model schema vocabulary.

Status:

**STRONGLY SUPPORTED**

---

# REQUIRED FIELD SUMMARY

Required:

```text
record_id
record_category
recorded_at
schema_version
```

Optional:

```text
provenance_ref
external_id
```

No field may receive an implicit semantic default.

Candidate constructor shape:

```text
RuntimeRecordHeader(
    record_id=...,
    record_category=...,
    recorded_at=...,
    schema_version=...,
    provenance_ref=None,
    external_id=None,
)
```

Status:

**SELECTED**

---

# FIELD ORDER

Selected declaration order:

1. `record_id`
2. `record_category`
3. `recorded_at`
4. `schema_version`
5. `provenance_ref`
6. `external_id`

Reason:

* required fields first
* optional fields last
* stable constructor readability
* schema attribution remains part of required identity-bearing structure

Status:

**SELECTED**

---

# IMMUTABILITY VOCABULARY

Selected term:

```text
immutable
```

Meaning:

After successful construction, no field may be reassigned.

Likely later implementation mechanism:

```text
@dataclass(frozen=True)
```

This mechanism remains unimplemented.

Boundary:

Immutable
≠
Cryptographically Tamper-Proof

Immutable
≠
Persisted

Immutable
≠
Uniqueness Enforced Globally

Status:

**SELECTED**

---

# STRUCTURAL VALIDITY

Selected term:

```text
structurally valid
```

Meaning:

The header satisfies its local construction constraints.

Structural validity does not establish:

* record admission
* record uniqueness across a registry
* provenance verification
* authority
* canonical effect
* semantic correctness
* persistence

Boundary:

Structurally Valid
≠
Admitted

Status:

**SELECTED**

---

# EQUALITY SEMANTICS

Candidate question:

Should equality be based only on `record_id`?

Possible models:

## Identity-Only Equality

Two headers with the same `record_id` compare equal even when other fields differ.

Problem:

This can conceal contradictory immutable representations of one record identity.

## Full Structural Equality

Two headers compare equal only when every field is equal.

Benefit:

* detects structural discrepancies
* follows standard frozen dataclass behavior
* avoids hidden identity-only semantics
* preserves deterministic tests

Selected decision:

```text
full structural equality
```

Boundary:

Same `record_id`
≠
Same Header Automatically

If two headers share `record_id` but differ structurally, a future registry must detect an identity conflict.

Status:

**SELECTED**

---

# HASHING SEMANTICS

A frozen dataclass may become hashable when all fields are hashable.

All selected fields are hashable.

Candidate decision:

Permit standard structural hashing if later provided naturally by the immutable model.

Do not define custom identity-only hashing.

Boundary:

Hash Equality
≠
Registry Uniqueness

Status:

**SELECTED**

---

# ORDERING SEMANTICS

Do not define ordering between Runtime Record Headers.

A lower or higher record number must not imply:

* temporal priority
* authority
* validity
* semantic precedence

No `order=True` behavior is permitted.

Boundary:

Identifier Order
≠
Event Order

Status:

**SELECTED**

---

# STRING REPRESENTATION

Do not define a custom human-readable `__str__` contract in the first capability.

A default representation may be used during testing.

Reason:

Custom display formats risk becoming accidental serialization contracts.

Status:

**DEFERRED**

---

# SERIALIZATION BOUNDARY

The first capability must not implement:

* `to_dict`
* `from_dict`
* JSON encoding
* JSON decoding
* file persistence
* schema migration
* content hashing

Reason:

Serialization requires separate decisions concerning:

* datetime format
* field ordering
* omission of `None`
* schema compatibility
* external identity preservation
* provenance references

Status:

**DEFERRED**

---

# CONSTRUCTION VALIDATION

Future construction validation should reject:

* invalid `record_id`
* invalid `record_category`
* naïve `recorded_at`
* invalid `schema_version`
* malformed `provenance_ref`
* empty `external_id`
* whitespace-only `external_id`

Candidate error type:

```text
ValueError
```

Reason:

* standard library
* no custom exception hierarchy required
* explicit construction failure
* dependency-light

Custom exceptions remain deferred.

Status:

**SELECTED**

---

# TYPE VALIDATION

Question:

Should incorrect Python types raise `TypeError` or `ValueError`?

Candidate rule:

* wrong field type → `TypeError`
* correct type with invalid value → `ValueError`

Examples:

```text
record_id = 123
→ TypeError
```

```text
record_id = "invalid"
→ ValueError
```

Status:

**SELECTED**

---

# NONE SEMANTICS

Required fields must reject `None`.

Optional fields may accept `None`.

No required field receives an implicit replacement value.

Status:

**SELECTED**

---

# BOOLEAN VALUES

Python `bool` is a subclass of `int`.

The model contains no integer fields, so this does not currently create ambiguity.

No Boolean field is included.

Status:

**NO ACTION REQUIRED**

---

# LOCAL UNIQUENESS

The model can validate identity syntax.

It cannot establish local uniqueness across multiple instances.

Uniqueness belongs to a future registry.

Boundary:

Valid `record_id`
≠
Unique `record_id`

Status:

**DEFERRED**

---

# PROVENANCE COMPLETENESS

The first header only carries a provenance reference.

It does not establish:

* provenance completeness
* source identity
* actor identity
* method
* environment
* evidence
* verification
* authority

Status:

**EXPLICIT NON-GOAL**

---

# RECORD PAYLOAD

The first model contains no semantic payload field.

It does not contain:

* target
* source
* action
* event type
* progression condition
* branch
* criteria
* result
* rationale
* relationship
* state
* authority

Future record models may compose or contain the header.

Status:

**SELECTED**

---

# COMPOSITION BOUNDARY

Future domain records may use the header through:

* composition
* inheritance
* field expansion

No composition mechanism is frozen yet.

Candidate preference:

```text
composition
```

Reason:

A shared header should not create one universal semantic behavior hierarchy.

Status:

**SAFE DEFERRAL**

---

# EXPLICIT NON-GOALS

The Runtime Record Header must not:

1. represent a Runtime Object
2. represent a Runtime Event payload
3. create identity automatically
4. enforce registry uniqueness
5. persist itself
6. serialize itself
7. create files
8. create directories
9. access environment variables
10. access the clock
11. mutate Platform Kernel records
12. create graph relationships
13. infer progression
14. infer authority
15. validate provenance
16. establish canonical effect
17. compare semantic priority
18. order records
19. resolve conflicts
20. inspect services
21. register itself
22. modify the Research Kernel
23. modify the Platform Registry
24. define every future record category
25. define a universal base-class hierarchy

---

# SELECTED VOCABULARY SUMMARY

## Capability

```text
Runtime Record Identity Foundation
```

## Model

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

## Identity Syntax

```text
RR-000000001
```

## Record Category Syntax

```text
UPPERCASE_UNDERSCORE
```

## Provenance Reference Syntax

```text
PRV-000000001
```

## Schema Version Syntax

```text
MAJOR.MINOR
```

## Equality

```text
full structural equality
```

## Ordering

```text
not supported
```

## Serialization

```text
deferred
```

## Automatic Identity Generation

```text
prohibited
```

## File-System Side Effects

```text
prohibited
```

---

# VOCABULARY INVARIANTS

## Invariant 1

`RuntimeRecordHeader` identifies shared immutable record structure but does not define semantic record payload.

## Invariant 2

`record_id` identifies the local Runtime Kernel record and must not be derived from content or external identity.

## Invariant 3

`record_category` identifies a record family and must not imply semantic effect, authority, or Runtime Object Type.

## Invariant 4

`recorded_at` records local entry time and remains distinct from occurrence, creation, import, and effective times.

## Invariant 5

`recorded_at` must be timezone-aware and explicitly supplied.

## Invariant 6

`provenance_ref` remains optional and does not imply verified provenance.

## Invariant 7

`external_id` remains optional, exact, untrusted, and distinct from local identity.

## Invariant 8

`schema_version` identifies the structural contract, not the represented Runtime Object version.

## Invariant 9

Construction validates structure only.

## Invariant 10

Full structural equality must not be replaced by identity-only equality.

## Invariant 11

No ordering semantics may be inferred from record identity.

## Invariant 12

No field may be mutated after successful construction.

## Invariant 13

No automatic normalization may conceal malformed identity or category input.

## Invariant 14

No file-system, registry, graph, authority, or projection side effect is permitted.

## Invariant 15

Local uniqueness remains a future registry responsibility.

Status:

**STRONGLY SUPPORTED**

**NOT YET IMPLEMENTED**

---

# ADVERSARIAL VOCABULARY TESTS

## Test 1 — Model Named RuntimeRecordIdentity

Finding:

Name underrepresents category, time, provenance reference, external identity, and schema version.

Result:

**REJECTED**

---

## Test 2 — Category as Enum Immediately

Finding:

Prematurely freezes deferred record families.

Result:

**REJECTED**

---

## Test 3 — Automatic Uppercasing

Finding:

Conceals malformed input.

Result:

**REJECTED**

---

## Test 4 — Default Current Time

Finding:

Introduces hidden clock dependence and weakens deterministic construction.

Result:

**REJECTED**

---

## Test 5 — Provenance Marker String

Finding:

A special string such as `UNKNOWN` overloads reference identity and provenance condition.

Result:

Use `None`.

**REJECTED**

---

## Test 6 — Identity-Only Equality

Finding:

Conceals conflicting structural representations sharing one identity.

Result:

**REJECTED**

---

## Test 7 — Custom Ordering by Record Number

Finding:

Identifier sequence does not establish temporal or semantic order.

Result:

**REJECTED**

---

## Test 8 — Serialization Included

Finding:

Datetime and schema semantics require separate reduction.

Result:

**DEFERRED**

---

## Test 9 — Namespace Field for External ID

Finding:

Useful but not required for the smallest first capability.

Result:

**SAFE DEFERRAL**

---

## Test 10 — Record Payload Dictionary

Finding:

Would create an untyped universal record envelope and weaken category separation.

Result:

**REJECTED**

---

# VOCABULARY DECISION

Model name:
**SELECTED**

Field names:
**SELECTED**

Required fields:
**SELECTED**

Optional fields:
**SELECTED**

Identity syntax:
**SELECTED**

Category representation:
**SELECTED**

Temporal requirement:
**SELECTED**

Provenance-reference semantics:
**SELECTED**

External-identity semantics:
**SELECTED**

Schema-version semantics:
**SELECTED**

Equality semantics:
**SELECTED**

Ordering semantics:
**SELECTED**

Serialization:
**DEFERRED**

Implementation:
**HOLD**

---

# READINESS CHECKPOINT 2

Vocabulary Selection:

**COMPLETE**

The vocabulary is ready for immutable contract reduction.

No production file was created.

No test file was created.

No implementation authority was granted.

---

# NEXT SESSION

Begin:

**RUNTIME RECORD IDENTITY FOUNDATION — IMMUTABLE CONTRACT 001**

Primary question:

What exact construction, validation, immutability, equality, hashing, error, and boundary rules must define `RuntimeRecordHeader` before tests are written?

Required work:

1. define exact Python field types
2. define exact constructor contract
3. define validation order
4. define type errors
5. define value errors
6. define datetime-awareness test
7. define identity parsing rules
8. define optional-field rules
9. define equality and hashing
10. define dataclass configuration
11. define import boundary
12. define exact testable acceptance criteria
13. preserve implementation HOLD

**UNKNOWN → HOLD**
