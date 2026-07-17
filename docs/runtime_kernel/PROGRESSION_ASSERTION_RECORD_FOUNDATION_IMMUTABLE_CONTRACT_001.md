# RESEARCH OS — PROGRESSION ASSERTION RECORD FOUNDATION

# IMMUTABLE CONTRACT 001

**Date:** 2026-07-17
**Project:** Research OS
**Development Version:** v2.0.0
**Status:** ACTIVE / IMMUTABLE CONTRACT
**Architecture:** RUNTIME KERNEL CANDIDATE ARCHITECTURE FROZEN
**Implementation:** HOLD
**Authority:** CONTRACT REDUCTION ONLY

**UNKNOWN → HOLD**

---

# PURPOSE

Freeze the exact immutable construction contract for:

```text
ProgressionAssertionRecord
```

This session defines:

1. exact Python field types
2. field declaration order
3. constructor shape
4. dataclass configuration
5. header composition
6. record-category enforcement
7. required-reference validation
8. optional-reference validation
9. closed progression-condition validation
10. temporal validation
11. validation order
12. error behavior
13. immutability
14. equality
15. hashing
16. ordering prohibition
17. serialization boundary
18. side-effect boundary
19. acceptance criteria
20. explicit non-goals

This session does not authorize tests or implementation.

---

# PREREQUISITE

Target, Condition, Scope, and Basis Separation 001 selected:

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

## Prohibited Semantics

* truth
* validity
* authority
* admission
* canonical currentness
* automatic transition
* conflict result
* Hold control
* generic evidence payload
* persistence

---

# OPERATING RULES

* Do not implement.
* Do not create tests.
* Do not modify `RuntimeRecordHeader`.
* Do not modify existing Runtime Kernel models.
* Do not modify application statuses.
* Do not add progression services.
* Do not add Hold behavior.
* Do not add authority evaluation.
* Do not calculate canonical progression.
* Do not normalize references.
* Do not normalize progression conditions.
* Do not infer temporal ordering.
* Freeze only construction-level structural behavior.

---

# EXACT MODEL ROLE

`ProgressionAssertionRecord` is an immutable structural Runtime record declaring that a specified target is asserted to have a specified progression condition within one declared scope and any explicitly available version, branch, context, temporal, actor, source, and basis dimensions.

It establishes:

* immutable assertion-record identity
* target reference
* asserted progression condition
* explicit scope reference
* optional target-version reference
* optional declared prior condition
* optional branch context
* optional runtime context
* optional assertion time
* optional effective time
* optional actor reference
* optional source reference
* optional basis reference

It does not establish:

* truth
* semantic validity
* authority
* admission
* transition validity
* current progression
* canonical effect
* Hold placement
* conflict
* complete evidence
* complete provenance

---

# EXACT IMPORT BOUNDARY

The future implementation may import only:

```python
from dataclasses import dataclass
from datetime import datetime

from models.runtime_record_identity import RuntimeRecordHeader
```

Private immutable constants and private validation helpers are permitted.

The model must not import:

* `RuntimeEventRecord`
* `RuntimeObjectVersionRecord`
* ObjectEngine
* RelationshipEngine
* Evaluation services
* Hold services
* authority services
* projection services
* PlatformRegistry
* ResearchKernel
* Streamlit
* JSON
* pathlib
* persistence services
* logging services

Status:

**FROZEN**

---

# DATACLASS CONTRACT

The future model must use:

```python
@dataclass(frozen=True)
class ProgressionAssertionRecord:
    ...
```

Required behavior:

* `frozen=True`
* default full structural equality
* standard structural hashing
* no ordering
* no unsafe hash
* no custom equality
* no mutation methods
* no slots requirement
* standard dataclass representation

Prohibited:

```python
order=True
unsafe_hash=True
eq=False
```

Status:

**FROZEN**

---

# FIELD DECLARATION ORDER

The exact declaration order is:

```python
header: RuntimeRecordHeader
target_ref: str
asserted_condition: str
scope_ref: str
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

Status:

**FROZEN**

---

# CONSTRUCTOR CONTRACT

Required constructor arguments:

```text
header
target_ref
asserted_condition
scope_ref
```

Optional constructor arguments:

```text
target_version_ref
prior_condition
branch_ref
context_ref
asserted_at
effective_at
actor_ref
source_ref
basis_ref
```

The constructor must not:

* generate a header
* generate an assertion identity
* infer a target
* infer a scope
* infer a progression condition
* infer a prior condition
* infer branch
* infer context
* infer actor
* infer source
* infer basis
* access the current clock
* default assertion time to record time
* default effective time to assertion time
* create Runtime Events
* create Hold records
* resolve references
* evaluate authority
* evaluate admission
* calculate current progression
* persist the assertion

Status:

**FROZEN**

---

# HEADER TYPE CONTRACT

Required Python type:

```python
RuntimeRecordHeader
```

Wrong types include:

* `None`
* string
* dictionary
* tuple
* list
* raw record ID
* application object dictionary
* Runtime Event dictionary
* generic object

Wrong type result:

```text
TypeError
```

Recommended error fragment:

```text
header
```

Status:

**FROZEN**

---

# HEADER CATEGORY CONTRACT

A valid Progression Assertion header must satisfy:

```python
header.record_category == "PROGRESSION_ASSERTION"
```

A structurally valid header belonging to another record family must be rejected.

Invalid categories include:

```text
EVENT
VERSION
HOLD
EVALUATION
CUSTOM_RECORD
```

Wrong category result:

```text
ValueError
```

Recommended error fragment:

```text
header record_category
```

Boundary:

```text
Valid RuntimeRecordHeader
≠
Valid Progression Assertion Header
```

Status:

**FROZEN**

---

# ASSERTION-RECORD IDENTITY CONTRACT

The local identity of the Progression Assertion record is:

```text
header.record_id
```

The model must not expose:

```text
assertion_id
```

The model must not:

* generate identity
* validate registry uniqueness
* derive identity from target
* derive identity from condition
* derive identity from scope
* derive identity from basis

Status:

**FROZEN**

---

# TARGET_REF TYPE CONTRACT

Required Python type:

```python
str
```

Wrong types include:

* `None`
* integer
* float
* Boolean
* bytes
* list
* tuple
* dictionary

Wrong type result:

```text
TypeError
```

Status:

**FROZEN**

---

# TARGET_REF VALUE CONTRACT

`target_ref` must:

* contain at least one non-whitespace character
* preserve the exact supplied value
* remain unnormalized
* remain unresolved
* carry no target-type inference

Invalid values:

```text
""
" "
"\t"
"\n"
"\r\n"
"   \t  "
```

Valid examples:

```text
research_os
OBJ-000001
RR-000000202
external/target/42
" target "
0
x
```

The model must not:

* strip whitespace
* lowercase
* uppercase
* parse prefixes
* query ObjectEngine
* query a registry
* check target existence
* determine target category
* determine target currentness

Invalid value result:

```text
ValueError
```

Status:

**FROZEN**

---

# ASSERTED_CONDITION TYPE CONTRACT

Required Python type:

```python
str
```

Wrong types include:

* `None`
* integer
* float
* Boolean
* bytes
* list
* tuple
* dictionary

Wrong type result:

```text
TypeError
```

Status:

**FROZEN**

---

# ACCEPTED CONDITION CONSTANT

The implementation may define one private immutable accepted-value set:

```python
_ACCEPTED_PROGRESSION_CONDITIONS = frozenset(
    {
        "PENDING",
        "ACTIVE",
        "HELD",
        "DORMANT",
        "ABANDONED",
    }
)
```

Equivalent immutable tuple or frozenset representation is permitted.

The accepted vocabulary must remain exactly:

```text
PENDING
ACTIVE
HELD
DORMANT
ABANDONED
```

Status:

**FROZEN**

---

# ASSERTED_CONDITION VALUE CONTRACT

`asserted_condition` must exactly equal one accepted value.

Valid values:

```text
PENDING
ACTIVE
HELD
DORMANT
ABANDONED
```

Invalid examples:

```text
""
" "
"UNKNOWN"
"CONFLICTING"
"PASS"
"FAIL"
"INCONCLUSIVE"
"VALID"
"INVALID"
"CURRENT"
"COMPLETED"
"active"
"Active"
"ACTIVE "
" ACTIVE"
```

No automatic normalization is permitted.

Invalid value result:

```text
ValueError
```

Recommended error fragment:

```text
asserted_condition
```

Status:

**FROZEN**

---

# SCOPE_REF TYPE CONTRACT

Required Python type:

```python
str
```

Wrong values such as `None` or non-string types produce:

```text
TypeError
```

Status:

**FROZEN**

---

# SCOPE_REF VALUE CONTRACT

`scope_ref` must:

* contain at least one non-whitespace character
* preserve exact input
* remain unresolved
* establish explicit local scope syntax only
* carry no universal validity inference
* carry no authority inference

Valid examples:

```text
SCOPE-000001
research/program/1
institutional
" scope "
0
x
```

Invalid examples:

```text
""
" "
"\t"
"\n"
```

The model must not:

* infer global scope
* parse dimensions
* query scope existence
* normalize input
* broaden scope
* compare scope authority

Invalid value result:

```text
ValueError
```

Status:

**FROZEN**

---

# TARGET_VERSION_REF TYPE CONTRACT

Permitted Python types:

```python
str | None
```

Wrong non-`None` types produce:

```text
TypeError
```

Status:

**FROZEN**

---

# TARGET_VERSION_REF VALUE CONTRACT

When present, `target_version_ref` must:

* contain at least one non-whitespace character
* preserve exact input
* remain unresolved
* carry no target-version existence inference
* carry no same-target inference
* carry no current-version inference

The model must not:

* require Runtime Record ID syntax
* import `RuntimeObjectVersionRecord`
* query a registry
* verify target/version compatibility
* normalize input

Invalid empty or whitespace-only values produce:

```text
ValueError
```

Status:

**FROZEN**

---

# TARGET_VERSION_REF NONE SEMANTICS

```python
target_version_ref = None
```

means only:

```text
No exact target-version reference is established in this assertion.
```

It does not mean:

* all versions
* current version
* no version exists
* target version is irrelevant
* target is not versioned

Status:

**FROZEN**

---

# PRIOR_CONDITION TYPE CONTRACT

Permitted Python types:

```python
str | None
```

Wrong non-`None` types produce:

```text
TypeError
```

Status:

**FROZEN**

---

# PRIOR_CONDITION VALUE CONTRACT

When present, `prior_condition` must exactly equal one accepted progression condition:

```text
PENDING
ACTIVE
HELD
DORMANT
ABANDONED
```

Invalid examples include:

```text
UNKNOWN
CONFLICTING
PASS
FAIL
ACTIVE 
active
```

No normalization is permitted.

Invalid value result:

```text
ValueError
```

Recommended error fragment:

```text
prior_condition
```

Status:

**FROZEN**

---

# PRIOR_CONDITION NONE SEMANTICS

```python
prior_condition = None
```

means only:

```text
No declared prior progression condition is established in this record.
```

It does not mean:

* no prior condition existed
* this is the first progression assertion
* the target was previously pending
* progression history is complete

Status:

**FROZEN**

---

# EQUAL PRIOR AND ASSERTED CONDITION

The model must accept:

```python
prior_condition == asserted_condition
```

Reason:

The record may represent:

* reaffirmation
* repeated external assertion
* continued-condition assertion
* corrected surrounding context
* imported duplicate claim

Boundary:

```text
Equal Prior and Asserted Conditions
≠
Invalid Assertion
```

Status:

**FROZEN**

---

# TRANSITION NON-CLAIM

The presence of both:

```text
prior_condition
asserted_condition
```

must not establish a verified transition.

The model must not:

* validate transition admissibility
* require different values
* infer causal progression
* create a transition event
* verify chronological order

Boundary:

```text
Prior + Asserted Condition
≠
Verified Transition
```

Status:

**FROZEN**

---

# BRANCH_REF TYPE CONTRACT

Permitted Python types:

```python
str | None
```

Wrong non-`None` types produce:

```text
TypeError
```

Status:

**FROZEN**

---

# BRANCH_REF VALUE CONTRACT

When present, `branch_ref` must:

* contain at least one non-whitespace character
* preserve exact input
* remain unresolved
* carry no root inference
* carry no branch-validity inference
* carry no branch-currentness inference

The model must not:

* check branch existence
* create a branch
* infer root or main
* normalize input
* compare branch lineage

Invalid empty or whitespace-only values produce:

```text
ValueError
```

Status:

**FROZEN**

---

# BRANCH_REF NONE SEMANTICS

```python
branch_ref = None
```

means only:

```text
No branch reference is established in this assertion.
```

It does not mean:

* root branch
* main branch
* universal branch
* branch-independent progression
* branch scope is unnecessary

Status:

**FROZEN**

---

# CONTEXT_REF TYPE CONTRACT

Permitted Python types:

```python
str | None
```

Wrong non-`None` types produce:

```text
TypeError
```

Status:

**FROZEN**

---

# CONTEXT_REF VALUE CONTRACT

When present, `context_ref` must:

* contain at least one non-whitespace character
* preserve exact input
* remain unresolved
* carry no universal-context inference
* carry no environment-validity inference
* carry no authority inference

The model must not:

* inspect context type
* query context existence
* normalize input
* infer environment or operation
* broaden context

Invalid empty or whitespace-only values produce:

```text
ValueError
```

Status:

**FROZEN**

---

# CONTEXT_REF NONE SEMANTICS

```python
context_ref = None
```

means only:

```text
No explicit runtime context reference is established in this assertion.
```

It does not mean:

* universal context
* context-free validity
* no context exists
* context is irrelevant

Status:

**FROZEN**

---

# ASSERTED_AT TYPE CONTRACT

Permitted Python types:

```python
datetime | None
```

Wrong non-`None` types produce:

```text
TypeError
```

Status:

**FROZEN**

---

# ASSERTED_AT VALUE CONTRACT

When present, `asserted_at` must be timezone-aware.

It must satisfy:

```python
asserted_at.tzinfo is not None
```

and:

```python
asserted_at.utcoffset() is not None
```

A naïve datetime or unusable timezone is invalid.

Invalid value result:

```text
ValueError
```

The supplied value must be preserved exactly.

Status:

**FROZEN**

---

# ASSERTED_AT NONE SEMANTICS

```python
asserted_at = None
```

means only:

```text
No separate assertion time is established in this record.
```

It does not mean:

* assertion time equals recorded time
* assertion occurred immediately
* assertion time is globally unknown
* record time is assertion time

Status:

**FROZEN**

---

# EFFECTIVE_AT TYPE CONTRACT

Permitted Python types:

```python
datetime | None
```

Wrong non-`None` types produce:

```text
TypeError
```

Status:

**FROZEN**

---

# EFFECTIVE_AT VALUE CONTRACT

When present, `effective_at` must be timezone-aware and have a usable UTC offset.

A naïve datetime or timezone with no usable offset is invalid.

Invalid value result:

```text
ValueError
```

The exact supplied datetime must be preserved.

Status:

**FROZEN**

---

# EFFECTIVE_AT NONE SEMANTICS

```python
effective_at = None
```

means only:

```text
No effective time is established in this assertion.
```

It does not mean:

* immediately effective
* effective at record time
* effective at assertion time
* not effective

Status:

**FROZEN**

---

# TEMPORAL PRESERVATION CONTRACT

The model must not call:

```text
datetime.now
datetime.utcnow
astimezone
replace
```

during construction.

It must not:

* normalize to UTC
* default one time from another
* alter offsets
* access the system clock

Status:

**FROZEN**

---

# TEMPORAL ORDER CONTRACT

The model must not enforce ordering among:

```text
header.recorded_at
asserted_at
effective_at
```

The following may be structurally representable:

```text
asserted_at < header.recorded_at
asserted_at > header.recorded_at
effective_at < asserted_at
effective_at > header.recorded_at
asserted_at = None
effective_at = None
```

Temporal coherence belongs to later Evaluation, inspection, admission, or reconstruction.

Boundary:

```text
Structurally Valid Times
≠
Temporally Coherent Assertion
```

Status:

**FROZEN**

---

# ACTOR_REF TYPE CONTRACT

Permitted Python types:

```python
str | None
```

Wrong non-`None` types produce:

```text
TypeError
```

Status:

**FROZEN**

---

# ACTOR_REF VALUE CONTRACT

When present, `actor_ref` must:

* contain at least one non-whitespace character
* preserve exact input
* remain unresolved
* carry no authority inference
* carry no identity-verification inference

The model must not:

* check actor existence
* verify identity
* infer authorization
* normalize input

Invalid empty or whitespace-only values produce:

```text
ValueError
```

Status:

**FROZEN**

---

# ACTOR_REF NONE SEMANTICS

```python
actor_ref = None
```

means only:

```text
No local actor reference is established in this assertion.
```

It does not mean:

* no actor existed
* the runtime asserted automatically
* anonymous authority
* invalid assertion

Status:

**FROZEN**

---

# SOURCE_REF TYPE CONTRACT

Permitted Python types:

```python
str | None
```

Wrong non-`None` types produce:

```text
TypeError
```

Status:

**FROZEN**

---

# SOURCE_REF VALUE CONTRACT

When present, `source_ref` must:

* contain at least one non-whitespace character
* preserve exact input
* remain unresolved
* carry no trust inference
* carry no provenance-completeness inference

The model must not:

* check source existence
* validate trust
* infer actor identity
* normalize input

Invalid empty or whitespace-only values produce:

```text
ValueError
```

Status:

**FROZEN**

---

# SOURCE_REF NONE SEMANTICS

```python
source_ref = None
```

means only:

```text
No local source reference is established in this assertion.
```

It does not mean:

* no source exists
* source is trusted
* source is unknown globally
* provenance is absent

Status:

**FROZEN**

---

# BASIS_REF TYPE CONTRACT

Permitted Python types:

```python
str | None
```

Wrong non-`None` types produce:

```text
TypeError
```

Status:

**FROZEN**

---

# BASIS_REF VALUE CONTRACT

When present, `basis_ref` must:

* contain at least one non-whitespace character
* preserve exact input
* remain unresolved
* carry no truth inference
* carry no evidentiary sufficiency inference
* carry no admission inference

The model must not:

* load basis content
* check basis existence
* validate evidence
* evaluate sufficiency
* normalize input

Invalid empty or whitespace-only values produce:

```text
ValueError
```

Status:

**FROZEN**

---

# BASIS_REF NONE SEMANTICS

```python
basis_ref = None
```

means only:

```text
No primary basis reference is established in this assertion.
```

It does not mean:

* assertion is false
* assertion is unsupported globally
* assertion is admissible
* evidence does not exist

Status:

**FROZEN**

---

# COMMON REQUIRED-REFERENCE CONTRACT

The following required references use one structural rule:

```text
target_ref
scope_ref
```

Each must:

1. be a string
2. contain at least one non-whitespace character
3. preserve exact input
4. remain unresolved
5. remain unnormalized

Status:

**FROZEN**

---

# COMMON OPTIONAL-REFERENCE CONTRACT

The following optional references use one structural rule:

```text
target_version_ref
branch_ref
context_ref
actor_ref
source_ref
basis_ref
```

Each accepts:

```python
str | None
```

When present, each must:

1. be a string
2. contain at least one non-whitespace character
3. preserve exact input
4. remain unresolved
5. remain unnormalized

Status:

**FROZEN**

---

# CROSS-FIELD EQUALITY RULES

The model must not reject equal strings among:

```text
target_ref
target_version_ref
scope_ref
branch_ref
context_ref
actor_ref
source_ref
basis_ref
```

Reason:

Equal syntax does not prove equal semantic identity.

Examples structurally permitted:

```text
target_ref == target_version_ref
scope_ref == context_ref
actor_ref == source_ref
source_ref == basis_ref
```

No cross-field reference inequality rule is selected.

Status:

**FROZEN**

---

# VALIDATION ORDER

Validation must occur in this conceptual order:

1. `header` type
2. header record category
3. `target_ref` type
4. `target_ref` value
5. `asserted_condition` type
6. `asserted_condition` value
7. `scope_ref` type
8. `scope_ref` value
9. `target_version_ref` type
10. `target_version_ref` value
11. `prior_condition` type
12. `prior_condition` value
13. `branch_ref` type
14. `branch_ref` value
15. `context_ref` type
16. `context_ref` value
17. `asserted_at` type
18. `asserted_at` timezone awareness
19. `effective_at` type
20. `effective_at` timezone awareness
21. `actor_ref` type
22. `actor_ref` value
23. `source_ref` type
24. `source_ref` value
25. `basis_ref` type
26. `basis_ref` value

Reason:

* immutable record identity first
* target binding second
* primary semantic assertion third
* required scope before optional context
* optional target refinement before prior-condition context
* branch and runtime context before temporal claims
* actor, source, and basis last
* type validation before value validation
* deterministic external failure behavior

Status:

**FROZEN**

---

# POST-CONSTRUCTION VALIDATION

Validation must occur through:

```python
__post_init__()
```

The frozen model may inspect but must not modify fields.

Prohibited:

```python
object.__setattr__()
```

No construction-time normalization is permitted.

Status:

**FROZEN**

---

# ERROR CONTRACT

Wrong Python type:

```text
TypeError
```

Correct Python type with structurally invalid value:

```text
ValueError
```

No custom exception classes are permitted.

Future tests should assert:

* exception class
* meaningful field-name fragment

Full punctuation should not be frozen unnecessarily.

Status:

**FROZEN**

---

# IMMUTABILITY CONTRACT

After construction, every field is immutable.

Attempts to assign:

* `header`
* `target_ref`
* `asserted_condition`
* `scope_ref`
* `target_version_ref`
* `prior_condition`
* `branch_ref`
* `context_ref`
* `asserted_at`
* `effective_at`
* `actor_ref`
* `source_ref`
* `basis_ref`

must raise standard frozen-dataclass behavior.

Expected exception:

```text
FrozenInstanceError
```

Status:

**FROZEN**

---

# EQUALITY CONTRACT

Equality is full structural equality across all thirteen fields.

Two records compare equal only when every field compares equal.

Same header with different asserted condition:

```text
NOT EQUAL
```

Same target and condition with different scope:

```text
NOT EQUAL
```

Same target, condition, and scope with different branch:

```text
NOT EQUAL
```

Same assertion with different basis:

```text
NOT EQUAL
```

Same assertion with different temporal values:

```text
NOT EQUAL
```

Status:

**FROZEN**

---

# DATETIME EQUALITY QUALIFICATION

Standard Python timezone-aware datetime equality is accepted.

Two datetime values representing the same instant may compare equal despite different offsets.

The model must not override datetime equality.

Status:

**FROZEN**

---

# HASHING CONTRACT

Use standard frozen-dataclass structural hashing.

Do not define a custom `__hash__`.

Hashing must not establish:

* assertion truth
* assertion uniqueness in a registry
* semantic equivalence
* authority
* admission
* canonicality
* progression order
* transition validity
* evidentiary sufficiency

Status:

**FROZEN**

---

# ORDERING CONTRACT

The model must not support ordering.

Do not use:

```python
order=True
```

The following must not imply ordering:

* header record ID
* header recorded time
* asserted time
* effective time
* prior condition
* asserted condition
* target reference

Operations such as:

```python
assertion_a < assertion_b
```

must remain unsupported.

Status:

**FROZEN**

---

# REPRESENTATION CONTRACT

Use standard dataclass `repr`.

Do not define:

* custom `__repr__`
* custom `__str__`
* application-status formatting
* progression summary formatting
* canonical-condition display logic

Status:

**FROZEN FOR FIRST CAPABILITY**

---

# SERIALIZATION CONTRACT

Do not implement:

* `to_dict`
* `from_dict`
* `to_json`
* `from_json`
* application-status conversion
* Runtime Event conversion
* Hold conversion
* persistence
* schema migration
* canonical projection

Status:

**DEFERRED**

---

# SIDE-EFFECT CONTRACT

Importing or constructing `ProgressionAssertionRecord` must not:

* read files
* write files
* create directories
* access the clock
* access environment variables
* access network resources
* query ObjectEngine
* resolve references
* create Runtime Events
* create Hold records
* evaluate authority
* evaluate admission
* compare other assertions
* detect conflict
* calculate canonical progression
* emit logs
* modify application statuses
* mutate its composed header

Status:

**FROZEN**

---

# PRODUCTION MODULE CONTRACT

Production path:

```text
models/progression_assertion_record.py
```

The module should define only:

```text
ProgressionAssertionRecord
```

Private immutable condition constants and private validation helpers are permitted.

The module must not define:

* progression services
* registries
* identity generators
* Hold models
* Evaluation models
* transition engines
* canonical projectors
* conflict detectors
* persistence
* enums
* application adapters

Status:

**FROZEN**

---

# MODULE IMPORT CONTRACT

Future tests should import directly:

```python
from models.progression_assertion_record import (
    ProgressionAssertionRecord,
)
```

No package export modification is required.

Status:

**FROZEN**

---

# MINIMAL VALID CONSTRUCTION

The following must construct successfully:

```python
ProgressionAssertionRecord(
    header=valid_progression_assertion_header,
    target_ref="research_os",
    asserted_condition="ACTIVE",
    scope_ref="SCOPE-000001",
)
```

Expected optional values:

```python
target_version_ref is None
prior_condition is None
branch_ref is None
context_ref is None
asserted_at is None
effective_at is None
actor_ref is None
source_ref is None
basis_ref is None
```

Status:

**FROZEN**

---

# CONTEXT-RICH VALID CONSTRUCTION

The following must construct successfully when all values are structurally valid:

```python
ProgressionAssertionRecord(
    header=valid_progression_assertion_header,
    target_ref="research_os",
    asserted_condition="ACTIVE",
    scope_ref="SCOPE-000001",
    target_version_ref="RR-000000202",
    prior_condition="PENDING",
    branch_ref="BRANCH-000001",
    context_ref="CONTEXT-000001",
    asserted_at=aware_asserted_at,
    effective_at=aware_effective_at,
    actor_ref="ACTOR-000001",
    source_ref="SYSTEM-000001",
    basis_ref="EVAL-000001",
)
```

No lookup, authority, admission, transition, conflict, or canonical-projection check is performed.

Status:

**FROZEN**

---

# HEADER ACCEPTANCE CRITERIA

The model must:

1. accept a valid `RuntimeRecordHeader` with category `PROGRESSION_ASSERTION`
2. reject non-header values
3. reject valid headers with another category
4. preserve the exact header instance
5. expose no `assertion_id`
6. leave the header unchanged

Status:

**FROZEN**

---

# REQUIRED REFERENCE ACCEPTANCE CRITERIA

For:

```text
target_ref
scope_ref
```

the model must:

1. require explicit constructor values
2. accept non-empty strings
3. accept strings with surrounding whitespace
4. preserve exact input
5. reject empty strings
6. reject whitespace-only strings
7. reject non-string values
8. perform no lookup
9. perform no normalization

Status:

**FROZEN**

---

# ASSERTED CONDITION ACCEPTANCE CRITERIA

The model must:

1. require an explicit condition
2. accept `PENDING`
3. accept `ACTIVE`
4. accept `HELD`
5. accept `DORMANT`
6. accept `ABANDONED`
7. reject non-string values
8. reject all unlisted strings
9. reject lowercase and mixed-case forms
10. reject surrounding whitespace
11. perform no normalization
12. preserve the exact accepted value

Status:

**FROZEN**

---

# PRIOR CONDITION ACCEPTANCE CRITERIA

The model must:

1. accept `None`
2. accept every accepted progression condition
3. reject non-string and non-`None` values
4. reject unlisted strings
5. allow equality with `asserted_condition`
6. perform no transition validation
7. preserve exact accepted values

Status:

**FROZEN**

---

# OPTIONAL REFERENCE ACCEPTANCE CRITERIA

For:

```text
target_version_ref
branch_ref
context_ref
actor_ref
source_ref
basis_ref
```

the model must:

1. accept `None`
2. accept non-empty strings
3. accept strings with surrounding whitespace
4. preserve exact input
5. reject empty strings
6. reject whitespace-only strings
7. reject non-string and non-`None` values
8. perform no lookup
9. perform no normalization

Status:

**FROZEN**

---

# TEMPORAL ACCEPTANCE CRITERIA

For both:

```text
asserted_at
effective_at
```

the model must:

1. accept `None`
2. accept timezone-aware datetime
3. accept non-UTC fixed offsets
4. reject naïve datetime
5. reject timezone objects with unusable UTC offset
6. reject non-datetime and non-`None` values
7. preserve exact supplied values
8. perform no UTC conversion
9. perform no defaulting
10. perform no temporal ordering validation
11. perform no clock access

Status:

**FROZEN**

---

# TEMPORAL SEPARATION ACCEPTANCE CRITERIA

Future tests must prove:

1. `asserted_at` does not default to `header.recorded_at`
2. `effective_at` does not default to `asserted_at`
3. `effective_at` may precede `asserted_at`
4. `asserted_at` may follow `header.recorded_at`
5. `effective_at` may follow `header.recorded_at`
6. supplied offsets remain unchanged

Status:

**FROZEN**

---

# EQUALITY ACCEPTANCE CRITERIA

Future tests must prove:

1. identical structures compare equal
2. different headers compare unequal
3. different targets compare unequal
4. different asserted conditions compare unequal
5. different scopes compare unequal
6. different target versions compare unequal
7. different prior conditions compare unequal
8. different branches compare unequal
9. different contexts compare unequal
10. different asserted times compare unequal
11. different effective times compare unequal
12. different actors compare unequal
13. different sources compare unequal
14. different bases compare unequal

Status:

**FROZEN**

---

# HASHING ACCEPTANCE CRITERIA

Future tests must prove:

1. equal records have equal hashes
2. structurally different records can coexist in a set
3. hashing does not mutate the assertion
4. hashing does not use target-only identity
5. hashing does not use header-only identity

Status:

**FROZEN**

---

# ORDERING ACCEPTANCE CRITERIA

Future tests must prove:

```python
assertion_a < assertion_b
```

raises:

```text
TypeError
```

No sorting semantics are permitted.

Status:

**FROZEN**

---

# VALIDATION PRECEDENCE ACCEPTANCE CRITERIA

Future tests must prove:

1. invalid header type fails before target validation
2. wrong header category fails before target validation
3. target type failure precedes condition failure
4. target value failure precedes condition failure
5. asserted-condition failure precedes scope failure
6. scope failure precedes target-version failure
7. target-version failure precedes prior-condition failure
8. prior-condition failure precedes branch failure
9. branch failure precedes context failure
10. context failure precedes asserted-time failure
11. asserted-time failure precedes effective-time failure
12. effective-time failure precedes actor failure
13. actor failure precedes source failure
14. source failure precedes basis failure

Status:

**FROZEN**

---

# EXPLICIT NON-GOALS

The Progression Assertion foundation must not:

1. modify `RuntimeRecordHeader`
2. modify application statuses
3. modify ObjectEngine
4. generate assertion identities
5. generate target identities
6. generate scope references
7. infer target version
8. infer prior condition
9. default branch or context
10. default temporal values
11. normalize progression conditions
12. normalize references
13. resolve references
14. validate target existence
15. validate version existence
16. validate target/version compatibility
17. verify prior condition
18. verify transition
19. detect progression conflict
20. create Hold records
21. publish Runtime Events
22. infer truth
23. infer validity
24. infer authority
25. infer admission
26. infer canonical current progression
27. evaluate evidence
28. evaluate basis sufficiency
29. persist records
30. serialize records
31. migrate application statuses
32. integrate with Platform Registry
33. integrate with Research Kernel services
34. calculate progression history

---

# ADVERSARIAL CONTRACT TESTS

## Test 1 — Open Condition Vocabulary

Proposal:

Accept any uppercase string.

Finding:

Would admit Evaluation results, conflict states, and application statuses.

Result:

**REJECTED**

---

## Test 2 — Normalize Condition Input

Proposal:

Convert `active` to `ACTIVE`.

Finding:

Conceals malformed input and changes supplied assertion semantics.

Result:

**REJECTED**

---

## Test 3 — Optional Scope

Finding:

Would permit silent universalization.

Result:

**REJECTED**

---

## Test 4 — Require Branch

Finding:

Would prevent unresolved and non-branch-specific assertions from being represented structurally.

Result:

**REJECTED AS CONSTRUCTION REQUIREMENT**

---

## Test 5 — Default Asserted Time

Proposal:

Use `header.recorded_at`.

Finding:

Collapses recording and assertion time.

Result:

**REJECTED**

---

## Test 6 — Default Effective Time

Proposal:

Use `asserted_at`.

Finding:

Collapses declaration and claimed applicability.

Result:

**REJECTED**

---

## Test 7 — Require Different Prior Condition

Finding:

Would prevent reaffirmation and repeated assertions.

Result:

**REJECTED**

---

## Test 8 — Add Authorized Boolean

Finding:

Collapses authority evaluation into assertion representation.

Result:

**REJECTED**

---

## Test 9 — Add Hold Reference

Finding:

Couples progression semantics to a separate control capability.

Result:

**REJECTED**

---

## Test 10 — Add Current Condition Boolean

Finding:

Collapses canonical projection into one assertion record.

Result:

**REJECTED**

---

# CONTRACT INVARIANTS

## Invariant 1

Every Progression Assertion record composes one valid `RuntimeRecordHeader`.

## Invariant 2

The header category must equal `PROGRESSION_ASSERTION`.

## Invariant 3

Assertion-record identity remains `header.record_id`.

## Invariant 4

No separate `assertion_id` may be introduced.

## Invariant 5

Every assertion declares one exact non-empty target reference.

## Invariant 6

Every assertion declares one accepted progression condition.

## Invariant 7

Every assertion declares one exact non-empty scope reference.

## Invariant 8

Target-version reference remains optional and unresolved.

## Invariant 9

Prior condition remains optional and declarative.

## Invariant 10

Prior condition uses the same closed progression vocabulary.

## Invariant 11

Equal prior and asserted conditions remain valid.

## Invariant 12

Prior and asserted conditions do not establish a verified transition.

## Invariant 13

Branch reference remains optional and unresolved.

## Invariant 14

Missing branch does not establish root or universal branch.

## Invariant 15

Context reference remains optional and unresolved.

## Invariant 16

Missing context does not establish universal context.

## Invariant 17

Recorded, asserted, and effective times remain distinct.

## Invariant 18

Temporal order remains outside the model.

## Invariant 19

Actor remains optional and does not establish authority.

## Invariant 20

Source remains optional and distinct from actor.

## Invariant 21

Basis remains optional and does not establish truth or sufficiency.

## Invariant 22

Equal reference strings do not establish equal semantic identity.

## Invariant 23

The record does not create a Hold.

## Invariant 24

The record does not detect conflict.

## Invariant 25

The record does not determine authority, admission, validity, truth, or canonical progression.

## Invariant 26

The model remains immutable.

## Invariant 27

Equality and hashing remain structural.

## Invariant 28

Ordering remains unsupported.

## Invariant 29

Serialization and persistence remain absent.

## Invariant 30

Construction remains side-effect free.

Status:

**FROZEN**

---

# CONTRACT DECISION

Model name:
**FROZEN**

Production path:
**FROZEN**

Field types:
**FROZEN**

Field order:
**FROZEN**

Constructor contract:
**FROZEN**

Dataclass configuration:
**FROZEN**

Header-category enforcement:
**FROZEN**

Required-reference validation:
**FROZEN**

Optional-reference validation:
**FROZEN**

Closed condition vocabulary:
**FROZEN**

Prior-condition behavior:
**FROZEN**

Datetime validation:
**FROZEN**

Temporal separation:
**FROZEN**

Validation order:
**FROZEN**

Error behavior:
**FROZEN**

Immutability:
**FROZEN**

Equality and hashing:
**FROZEN**

Ordering prohibition:
**FROZEN**

Serialization boundary:
**FROZEN**

Side-effect boundary:
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

No application status behavior was changed.

No Hold, authority, admission, or canonical-projection behavior was introduced.

---

# NEXT SESSION

Begin:

**PROGRESSION ASSERTION RECORD FOUNDATION — TEST CONTRACT 001**

Primary question:

What exact tests must be written before implementation to prove header composition, category enforcement, closed progression-condition vocabulary, required target and scope, optional version and context references, temporal separation, validation precedence, immutability, equality, hashing, ordering prohibition, serialization absence, service isolation, and preservation of existing Runtime Kernel foundations?

Required work:

1. define test file
2. define valid Progression Assertion header
3. define minimal assertion fixture
4. define context-rich assertion fixture
5. define header tests
6. define required target and scope tests
7. define asserted-condition tests
8. define prior-condition tests
9. define optional-reference tests
10. define datetime tests
11. define temporal-separation tests
12. define validation-precedence tests
13. define immutability tests
14. define equality and hashing tests
15. define no-ordering test
16. define serialization-absence test
17. define service-isolation tests
18. preserve production implementation HOLD

**UNKNOWN → HOLD**
