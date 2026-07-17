# RESEARCH OS — HOLD RECORD FOUNDATION

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
HoldRecord
```

This session defines:

1. exact Python field types
2. exact field declaration order
3. constructor shape
4. dataclass configuration
5. Runtime Record Header composition
6. `HOLD` record-category enforcement
7. required-reference validation
8. optional-reference validation
9. datetime validation
10. temporal separation
11. deterministic validation order
12. exception behavior
13. immutability
14. structural equality
15. structural hashing
16. ordering prohibition
17. release-field absence
18. active-state absence
19. serialization boundary
20. service and side-effect isolation
21. acceptance criteria
22. explicit non-goals

This session does not authorize tests or production implementation.

---

# PREREQUISITE

Target, Scope, Reason, Owner, and Release Separation 001 selected:

## Model

```text
HoldRecord
```

## Production Path

```text
models/hold_record.py
```

## Test Path

```text
tests/runtime/test_hold_record.py
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
* resolution is distinct from release
* expiry does not automatically release
* active Hold state is reconstructed later
* release is separately recorded
* original Hold record remains immutable

---

# OPERATING RULES

* Do not implement.
* Do not create tests.
* Do not modify existing Runtime Kernel models.
* Do not modify application statuses.
* Do not add Hold placement services.
* Do not add release services.
* Do not evaluate authority.
* Do not calculate active Hold state.
* Do not block or refuse operations.
* Do not publish Runtime Events.
* Do not infer progression `HELD`.
* Do not normalize references.
* Do not infer temporal ordering.
* Freeze construction-level structural behavior only.

---

# EXACT MODEL ROLE

`HoldRecord` is an immutable Runtime control record declaring that a specified consequence is held for a specified target within a specified scope, for a declared reason, pending a declared resolution condition.

It may additionally preserve:

* exact target-version reference
* branch reference
* context reference
* triggering record reference
* basis reference
* owner reference
* placement actor reference
* placement authority reference
* release authority reference
* placement time
* effective time
* review time
* expiry time

It does not establish:

* placement authority validity
* release authority validity
* truth of the triggering condition
* evidentiary sufficiency
* operational admission
* current active status
* resolution
* release
* automatic expiry
* universal blocking
* progression `HELD`
* Evaluation `HOLD`
* refusal
* failure

---

# EXACT IMPORT BOUNDARY

The future implementation may import only:

```python
from dataclasses import dataclass
from datetime import datetime

from models.runtime_record_identity import RuntimeRecordHeader
```

Private validation helpers are permitted.

The model must not import:

* `ProgressionAssertionRecord`
* `RuntimeEventRecord`
* `RuntimeObjectVersionRecord`
* ObjectEngine
* RelationshipEngine
* Evaluation services
* authority services
* release services
* refusal services
* progression services
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
class HoldRecord:
    ...
```

Required behavior:

* `frozen=True`
* default structural equality
* standard structural hashing
* no ordering
* no custom equality
* no custom hash
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
blocked_consequence_ref: str
scope_ref: str
reason_ref: str
resolution_condition_ref: str
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

Status:

**FROZEN**

---

# CONSTRUCTOR CONTRACT

Required constructor arguments:

```text
header
target_ref
blocked_consequence_ref
scope_ref
reason_ref
resolution_condition_ref
```

Optional constructor arguments:

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
placed_at
effective_at
review_at
expires_at
```

The constructor must not:

* generate a Runtime Record Header
* generate Hold identity
* infer a target
* infer a blocked consequence
* infer scope
* infer reason
* infer resolution condition
* infer owner
* infer authority
* infer active state
* infer release state
* access the clock
* default one timestamp from another
* publish Runtime Events
* create progression assertions
* block operations
* refuse operations
* resolve references
* evaluate authority
* persist the record

Status:

**FROZEN**

---

# HEADER TYPE CONTRACT

Required Python type:

```python
RuntimeRecordHeader
```

Wrong values include:

* `None`
* string
* dictionary
* tuple
* list
* raw record ID
* application object dictionary
* generic object

Wrong type result:

```text
TypeError
```

Required error fragment:

```text
header
```

Status:

**FROZEN**

---

# HEADER CATEGORY CONTRACT

A valid Hold header must satisfy:

```python
header.record_category == "HOLD"
```

Valid Runtime Record Headers belonging to another category must be rejected.

Invalid categories include:

```text
EVENT
VERSION
PROGRESSION_ASSERTION
EVALUATION
CUSTOM_RECORD
```

Wrong category result:

```text
ValueError
```

Required error fragment:

```text
header
```

or:

```text
record_category
```

Boundary:

```text
Valid RuntimeRecordHeader
≠
Valid Hold Header
```

Status:

**FROZEN**

---

# HOLD-RECORD IDENTITY CONTRACT

The local identity of the Hold record is:

```text
header.record_id
```

The model must not expose:

```text
hold_id
```

The model must not:

* generate identity
* derive identity from the target
* derive identity from the consequence
* derive identity from the reason
* validate registry uniqueness

Status:

**FROZEN**

---

# REQUIRED REFERENCE SET

The following fields are required references:

```text
target_ref
blocked_consequence_ref
scope_ref
reason_ref
resolution_condition_ref
```

Each uses the same structural validation contract.

Status:

**FROZEN**

---

# REQUIRED REFERENCE TYPE CONTRACT

Each required reference must be:

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

The exception message must identify the field.

Status:

**FROZEN**

---

# REQUIRED REFERENCE VALUE CONTRACT

Each required reference must:

* contain at least one non-whitespace character
* preserve the exact supplied string
* remain unresolved
* remain unnormalized
* carry no existence inference
* carry no authority inference

Invalid values include:

```text
""
" "
"\t"
"\n"
"\r\n"
"   \t  "
```

Valid examples include:

```text
research_os
RELEASE
SCOPE-000001
REASON-000001
RESOLUTION-000001
" reference "
0
x
```

The model must not:

* strip whitespace
* lowercase
* uppercase
* validate prefixes
* query registries
* load referenced content
* infer reference category

Invalid structural value result:

```text
ValueError
```

Status:

**FROZEN**

---

# TARGET_REF CONTRACT

Field:

```text
target_ref
```

Meaning:

Identifies the entity, operation, relationship, release, execution request, branch, or other consequence-bearing subject to which the Hold applies.

The model does not verify:

* target existence
* target type
* target currentness
* target admission
* target ownership

Boundary:

```text
Target Reference
≠
Target Proven
```

Status:

**FROZEN**

---

# BLOCKED_CONSEQUENCE_REF CONTRACT

Field:

```text
blocked_consequence_ref
```

Meaning:

Identifies the consequence that is declared blocked.

The model does not use a closed consequence vocabulary.

Valid examples may include:

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
```

The model does not:

* perform blocking
* verify that the consequence exists
* infer that unrelated consequences are blocked
* convert the value to uppercase
* validate a prefix

Boundary:

```text
Blocked Consequence Declared
≠
Blocking Enforced
```

Status:

**FROZEN**

---

# SCOPE_REF CONTRACT

Field:

```text
scope_ref
```

Every Hold requires explicit scope.

The model does not:

* infer universal scope
* validate scope existence
* broaden scope
* compare scope authority

Boundary:

```text
Hold in Scope A
≠
Hold Universally
```

Status:

**FROZEN**

---

# REASON_REF CONTRACT

Field:

```text
reason_ref
```

The field identifies the declared Hold reason.

It does not establish:

* reason truth
* reason validity
* reason sufficiency
* reason authority
* trigger identity

Boundary:

```text
Reason Referenced
≠
Reason Proven
```

Status:

**FROZEN**

---

# RESOLUTION_CONDITION_REF CONTRACT

Field:

```text
resolution_condition_ref
```

The field identifies the declared condition that must be addressed before release may be considered.

It does not establish:

* condition satisfaction
* release eligibility
* release authority
* release occurrence
* automatic expiry behavior

Boundary:

```text
Resolution Condition Referenced
≠
Resolution Achieved
```

Status:

**FROZEN**

---

# OPTIONAL REFERENCE SET

The following fields are optional references:

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

Each accepts:

```python
str | None
```

Status:

**FROZEN**

---

# OPTIONAL REFERENCE TYPE CONTRACT

When an optional reference is not `None`, it must be a string.

Wrong non-`None` type result:

```text
TypeError
```

The exception message must identify the field.

Status:

**FROZEN**

---

# OPTIONAL REFERENCE VALUE CONTRACT

When present, each optional reference must:

* contain at least one non-whitespace character
* preserve exact supplied input
* remain unresolved
* remain unnormalized
* carry no existence inference
* carry no authority inference unless separately evaluated

Empty or whitespace-only strings produce:

```text
ValueError
```

Status:

**FROZEN**

---

# TARGET_VERSION_REF CONTRACT

When present:

```text
target_version_ref
```

identifies the exact target version to which the Hold is asserted to apply.

The model does not verify:

* version existence
* target/version compatibility
* version currentness
* version admission

When absent:

```python
target_version_ref = None
```

means only:

```text
No exact target-version reference is established.
```

Status:

**FROZEN**

---

# BRANCH_REF CONTRACT

When present, `branch_ref` identifies declared branch context.

The model does not:

* verify branch existence
* infer root branch
* infer main branch
* infer all-branch applicability
* compare branch lineage

When absent:

```python
branch_ref = None
```

means only:

```text
No branch reference is established.
```

Status:

**FROZEN**

---

# CONTEXT_REF CONTRACT

When present, `context_ref` identifies declared runtime, operational, institutional, campaign, environment, or authority-domain context.

When absent:

```python
context_ref = None
```

does not mean universal context.

Status:

**FROZEN**

---

# TRIGGER_REF CONTRACT

When present, `trigger_ref` identifies the record, occurrence, result, request, or condition that triggered placement of the Hold.

The model does not:

* load the trigger
* validate trigger existence
* verify causal linkage
* equate trigger with reason
* equate trigger with basis

Boundary:

```text
Trigger Referenced
≠
Trigger Proven Causal
```

Status:

**FROZEN**

---

# BASIS_REF CONTRACT

When present, `basis_ref` identifies the principal supporting record or evidentiary basis for the Hold.

The model does not:

* load the basis
* verify evidence
* evaluate sufficiency
* infer admission
* infer authority

Boundary:

```text
Basis Referenced
≠
Hold Justified
```

Status:

**FROZEN**

---

# OWNER_REF CONTRACT

When present, `owner_ref` identifies the person, service, institution, or role responsible for coordinating review or resolution.

Owner does not establish:

* placement authority
* release authority
* target ownership
* evidence authority
* operational admission

Boundary:

```text
Hold Owner
≠
Hold Authority
```

Status:

**FROZEN**

---

# PLACED_BY_REF CONTRACT

When present, `placed_by_ref` identifies the actor, process, service, or institution that declared the Hold.

It does not establish that placement was authorized.

Boundary:

```text
Placed By
≠
Authorized to Place
```

Status:

**FROZEN**

---

# PLACEMENT_AUTHORITY_REF CONTRACT

When present, `placement_authority_ref` identifies the authority claim, role, rule, policy, or decision under which placement is asserted.

The model does not verify:

* authority validity
* authority scope
* actor binding
* temporal authority
* consequence authority

Boundary:

```text
Placement Authority Referenced
≠
Placement Authorized
```

Status:

**FROZEN**

---

# RELEASE_AUTHORITY_REF CONTRACT

When present, `release_authority_ref` identifies the authority claim, role, rule, policy, or decision expected to govern release.

The model does not:

* grant release authority
* evaluate release authority
* release the Hold
* prove resolution
* prove release eligibility

Boundary:

```text
Release Authority Referenced
≠
Release Authorized
```

Status:

**FROZEN**

---

# CROSS-FIELD REFERENCE RULES

The model must allow equal strings across reference fields.

Structurally permitted examples include:

```text
target_ref == target_version_ref
scope_ref == context_ref
reason_ref == trigger_ref
trigger_ref == basis_ref
owner_ref == placed_by_ref
placement_authority_ref == release_authority_ref
```

Equal syntax does not establish equal semantic identity.

No cross-field reference inequality rule is selected.

Status:

**FROZEN**

---

# TEMPORAL FIELD SET

Optional temporal fields:

```text
placed_at
effective_at
review_at
expires_at
```

Each accepts:

```python
datetime | None
```

Status:

**FROZEN**

---

# TEMPORAL TYPE CONTRACT

Wrong non-`None` types produce:

```text
TypeError
```

Invalid examples include:

* string timestamps
* integers
* floats
* Booleans
* dictionaries
* lists

The exception message must identify the field.

Status:

**FROZEN**

---

# TIMEZONE-AWARENESS CONTRACT

When present, each datetime must satisfy:

```python
value.tzinfo is not None
```

and:

```python
value.utcoffset() is not None
```

Naïve datetimes and timezone objects without a usable UTC offset are invalid.

Invalid value result:

```text
ValueError
```

Status:

**FROZEN**

---

# TEMPORAL PRESERVATION CONTRACT

The exact supplied datetime must be preserved.

The model must not call:

```text
datetime.now
datetime.utcnow
astimezone
replace
```

during construction.

The model must not:

* normalize to UTC
* change offsets
* access the system clock
* derive one timestamp from another

Status:

**FROZEN**

---

# PLACED_AT CONTRACT

`placed_at` identifies when the Hold decision is asserted to have been made.

When absent:

```python
placed_at = None
```

does not mean placement occurred at `header.recorded_at`.

Boundary:

```text
Recorded At
≠
Placed At
```

Status:

**FROZEN**

---

# EFFECTIVE_AT CONTRACT

`effective_at` identifies when the declared blocking effect is asserted to begin.

When absent:

```python
effective_at = None
```

does not mean:

* immediately effective
* effective at placement time
* effective at record time
* ineffective

Status:

**FROZEN**

---

# REVIEW_AT CONTRACT

`review_at` identifies when review is due or expected.

It does not establish:

* automatic review
* automatic escalation
* expiry
* resolution
* release

Boundary:

```text
Review Due
≠
Hold Expired
```

Status:

**FROZEN**

---

# EXPIRES_AT CONTRACT

`expires_at` identifies when expiry handling, escalation, review, or revalidation may become relevant.

It does not establish:

* automatic release
* automatic resolution
* automatic invalidation
* inactive status
* elapsed status during construction

Boundary:

```text
Expiry Reached
≠
Hold Released
```

Status:

**FROZEN**

---

# TEMPORAL ORDER CONTRACT

The model must not enforce ordering among:

```text
header.recorded_at
placed_at
effective_at
review_at
expires_at
```

Structurally representable cases include:

```text
placed_at < recorded_at
placed_at > recorded_at
effective_at < placed_at
review_at < effective_at
expires_at < review_at
expires_at < effective_at
```

These may later be evaluated as incoherent.

Boundary:

```text
Structurally Valid Times
≠
Temporally Coherent Hold
```

Status:

**FROZEN**

---

# RELEASE-FIELD ABSENCE CONTRACT

The model must not contain:

```text
released
release_status
released_at
released_by_ref
release_decision_ref
resolved
resolution_status
```

Release belongs to a later immutable record or Runtime Event.

The original Hold record must not be mutated.

Boundary:

```text
Resolution Condition Met
≠
Hold Released
```

Status:

**FROZEN**

---

# ACTIVE-STATE ABSENCE CONTRACT

The model must not contain:

```text
is_active
active
current
expired
inactive
```

Current Hold effect must be reconstructed later using:

* Hold record
* release records
* invalidations
* branch
* scope
* context
* time
* authority
* admission

Status:

**FROZEN**

---

# AUTOMATIC RELEASE PROHIBITION

Construction and import must not automatically release a Hold because:

* `expires_at` is in the past
* `review_at` is in the past
* resolution evidence exists
* owner is absent
* authority becomes available
* trigger disappears

Status:

**FROZEN**

---

# VALIDATION ORDER

Validation must occur in this conceptual order:

1. `header` type
2. header record category
3. `target_ref` type
4. `target_ref` value
5. `blocked_consequence_ref` type
6. `blocked_consequence_ref` value
7. `scope_ref` type
8. `scope_ref` value
9. `reason_ref` type
10. `reason_ref` value
11. `resolution_condition_ref` type
12. `resolution_condition_ref` value
13. `target_version_ref` type
14. `target_version_ref` value
15. `branch_ref` type
16. `branch_ref` value
17. `context_ref` type
18. `context_ref` value
19. `trigger_ref` type
20. `trigger_ref` value
21. `basis_ref` type
22. `basis_ref` value
23. `owner_ref` type
24. `owner_ref` value
25. `placed_by_ref` type
26. `placed_by_ref` value
27. `placement_authority_ref` type
28. `placement_authority_ref` value
29. `release_authority_ref` type
30. `release_authority_ref` value
31. `placed_at` type
32. `placed_at` timezone awareness
33. `effective_at` type
34. `effective_at` timezone awareness
35. `review_at` type
36. `review_at` timezone awareness
37. `expires_at` type
38. `expires_at` timezone awareness

Reason:

* immutable record identity first
* target and blocked consequence next
* required semantic boundaries before optional context
* trigger and basis before responsibility and authority
* temporal fields last
* type checks before value checks
* externally deterministic failure behavior

Status:

**FROZEN**

---

# POST-CONSTRUCTION VALIDATION

Validation must occur through:

```python
__post_init__()
```

The implementation may inspect but must not mutate fields.

Prohibited:

```python
object.__setattr__()
```

No construction-time normalization or default inference is permitted.

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

No custom exception hierarchy is permitted.

Future tests should assert:

* exception class
* meaningful field-name fragment

Complete punctuation should not be frozen unnecessarily.

Status:

**FROZEN**

---

# IMMUTABILITY CONTRACT

After construction, all nineteen fields are immutable.

Assignment attempts must raise standard frozen-dataclass behavior.

Expected exception:

```text
FrozenInstanceError
```

Release, review, expiry, resolution, and active-state changes must never mutate the original Hold record.

Status:

**FROZEN**

---

# EQUALITY CONTRACT

Equality is full structural equality across all nineteen fields.

Two Hold records compare equal only when every field compares equal.

Examples:

```text
Same Header + Different Target
→
NOT EQUAL
```

```text
Same Target + Different Blocked Consequence
→
NOT EQUAL
```

```text
Same Target and Consequence + Different Scope
→
NOT EQUAL
```

```text
Same Hold + Different Reason
→
NOT EQUAL
```

```text
Same Hold + Different Resolution Condition
→
NOT EQUAL
```

```text
Same Hold + Different Authority Reference
→
NOT EQUAL
```

```text
Same Hold + Different Temporal Field
→
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

* Hold authority
* Hold admission
* Hold uniqueness
* active-state equivalence
* duplicate control effect
* release eligibility
* semantic validity

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

* record ID
* recorded time
* placed time
* effective time
* review time
* expiry time
* target
* reason

Operations such as:

```python
hold_a < hold_b
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
* active-state display
* release-state display
* authority display
* blocking-summary logic

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
* Evaluation conversion
* progression conversion
* Runtime Event conversion
* persistence
* schema migration
* active-state projection

Status:

**DEFERRED**

---

# SIDE-EFFECT CONTRACT

Importing or constructing `HoldRecord` must not:

* read files
* write files
* create directories
* access the clock
* access environment variables
* access network resources
* query ObjectEngine
* resolve references
* load reason or basis records
* evaluate authority
* evaluate admission
* block operations
* refuse operations
* create Runtime Events
* create progression assertions
* schedule reviews
* release Holds
* calculate expiry
* determine active state
* emit logs
* modify application status
* mutate its composed header

Status:

**FROZEN**

---

# PRODUCTION MODULE CONTRACT

Production path:

```text
models/hold_record.py
```

The module should define only:

```text
HoldRecord
```

Private validation helpers are permitted.

The module must not define:

* Hold placement services
* Hold release services
* active-Hold projectors
* identity generators
* Runtime Event services
* progression services
* refusal services
* authority services
* persistence
* enums
* application adapters

Status:

**FROZEN**

---

# MODULE IMPORT CONTRACT

Future tests should import directly:

```python
from models.hold_record import HoldRecord
```

No package export modification is required.

Status:

**FROZEN**

---

# MINIMAL VALID CONSTRUCTION

The following must construct successfully:

```python
HoldRecord(
    header=valid_hold_header,
    target_ref="research_os",
    blocked_consequence_ref="release",
    scope_ref="SCOPE-000001",
    reason_ref="REASON-000001",
    resolution_condition_ref="RESOLUTION-000001",
)
```

Expected optional values:

```python
target_version_ref is None
branch_ref is None
context_ref is None
trigger_ref is None
basis_ref is None
owner_ref is None
placed_by_ref is None
placement_authority_ref is None
release_authority_ref is None
placed_at is None
effective_at is None
review_at is None
expires_at is None
```

Status:

**FROZEN**

---

# CONTEXT-RICH VALID CONSTRUCTION

The following must construct successfully when all values are structurally valid:

```python
HoldRecord(
    header=valid_hold_header,
    target_ref="research_os",
    blocked_consequence_ref="release",
    scope_ref="SCOPE-000001",
    reason_ref="REASON-000001",
    resolution_condition_ref="RESOLUTION-000001",
    target_version_ref="RR-000000202",
    branch_ref="BRANCH-000001",
    context_ref="CONTEXT-000001",
    trigger_ref="EVAL-000001",
    basis_ref="EVIDENCE-000001",
    owner_ref="OWNER-000001",
    placed_by_ref="ACTOR-000001",
    placement_authority_ref="AUTHORITY-000001",
    release_authority_ref="AUTHORITY-000002",
    placed_at=aware_placed_at,
    effective_at=aware_effective_at,
    review_at=aware_review_at,
    expires_at=aware_expires_at,
)
```

No authority, admission, blocking, expiry, release, or active-state check is performed.

Status:

**FROZEN**

---

# HEADER ACCEPTANCE CRITERIA

The model must:

1. accept a valid RuntimeRecordHeader with category `HOLD`
2. reject non-header values
3. reject headers belonging to another category
4. preserve the exact header instance
5. expose no `hold_id`
6. leave the header unchanged

Status:

**FROZEN**

---

# REQUIRED REFERENCE ACCEPTANCE CRITERIA

For:

```text
target_ref
blocked_consequence_ref
scope_ref
reason_ref
resolution_condition_ref
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

# OPTIONAL REFERENCE ACCEPTANCE CRITERIA

For:

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

For:

```text
placed_at
effective_at
review_at
expires_at
```

the model must:

1. accept `None`
2. accept timezone-aware datetime
3. accept non-UTC fixed offsets
4. reject naïve datetime
5. reject timezone objects with unusable offsets
6. reject non-datetime and non-`None` values
7. preserve exact supplied values
8. perform no UTC conversion
9. perform no defaulting
10. perform no ordering validation
11. perform no clock access

Status:

**FROZEN**

---

# TEMPORAL SEPARATION ACCEPTANCE CRITERIA

Future tests must prove:

1. `placed_at` does not default to `header.recorded_at`
2. `effective_at` does not default to `placed_at`
3. `review_at` does not default from effective time
4. `expires_at` does not default from review time
5. effective time may precede placement time
6. review time may precede effective time
7. expiry may precede review time
8. supplied offsets remain unchanged
9. past expiry does not mutate or reject the record solely because it is past

Status:

**FROZEN**

---

# RELEASE-ABSENCE ACCEPTANCE CRITERIA

Future tests must prove absence of:

```text
released
release_status
released_at
released_by_ref
release_decision_ref
resolved
resolution_status
```

Status:

**FROZEN**

---

# ACTIVE-STATE ABSENCE ACCEPTANCE CRITERIA

Future tests must prove absence of:

```text
is_active
active
current
expired
inactive
```

Status:

**FROZEN**

---

# EQUALITY ACCEPTANCE CRITERIA

Future tests must prove:

1. identical structures compare equal
2. different headers compare unequal
3. different targets compare unequal
4. different consequences compare unequal
5. different scopes compare unequal
6. different reasons compare unequal
7. different resolution conditions compare unequal
8. different target versions compare unequal
9. different branches compare unequal
10. different contexts compare unequal
11. different triggers compare unequal
12. different bases compare unequal
13. different owners compare unequal
14. different placement actors compare unequal
15. different placement authorities compare unequal
16. different release authorities compare unequal
17. different placement times compare unequal
18. different effective times compare unequal
19. different review times compare unequal
20. different expiry times compare unequal

Status:

**FROZEN**

---

# HASHING ACCEPTANCE CRITERIA

Future tests must prove:

1. equal Hold records have equal hashes
2. structurally different Hold records can coexist in a set
3. hashing does not mutate the Hold
4. hashing does not use target-only identity
5. hashing does not use header-only identity

Status:

**FROZEN**

---

# ORDERING ACCEPTANCE CRITERIA

Future tests must prove:

```python
hold_a < hold_b
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
3. target failure precedes blocked-consequence failure
4. blocked-consequence failure precedes scope failure
5. scope failure precedes reason failure
6. reason failure precedes resolution-condition failure
7. resolution-condition failure precedes target-version failure
8. target-version failure precedes branch failure
9. branch failure precedes context failure
10. context failure precedes trigger failure
11. trigger failure precedes basis failure
12. basis failure precedes owner failure
13. owner failure precedes placed-by failure
14. placed-by failure precedes placement-authority failure
15. placement-authority failure precedes release-authority failure
16. release-authority failure precedes placed-time failure
17. placed-time failure precedes effective-time failure
18. effective-time failure precedes review-time failure
19. review-time failure precedes expiry-time failure

Status:

**FROZEN**

---

# EXPLICIT NON-GOALS

The Hold Record foundation must not:

1. modify RuntimeRecordHeader
2. modify ProgressionAssertionRecord
3. modify application status
4. modify ObjectEngine
5. generate Hold identity
6. generate target identity
7. generate consequence identity
8. infer scope
9. normalize references
10. resolve references
11. validate target existence
12. validate target-version existence
13. validate target/version compatibility
14. validate reason truth
15. validate trigger causality
16. evaluate basis sufficiency
17. evaluate owner capability
18. evaluate placement authority
19. evaluate release authority
20. block operations
21. refuse operations
22. create progression `HELD`
23. create Evaluation `HOLD`
24. publish Runtime Events
25. calculate active Hold state
26. calculate expiry state
27. automatically release
28. mutate on release
29. persist records
30. serialize records
31. migrate application statuses
32. integrate with Platform Registry
33. integrate with Research Kernel services
34. reconstruct Hold history

---

# ADVERSARIAL CONTRACT TESTS

## Test 1 — Open Consequence Interpretation

Proposal:

Interpret known consequence names inside the model.

Finding:

Would introduce control behavior and service semantics.

Result:

**REJECTED**

---

## Test 2 — Optional Scope

Finding:

Would permit silent universal blocking.

Result:

**REJECTED**

---

## Test 3 — Free-Form Reason Payload

Finding:

Would introduce untyped content and serialization concerns.

Result:

**REJECTED**

---

## Test 4 — Require Owner

Finding:

Would prevent unresolved or imported Holds from being structurally represented.

Result:

**REJECTED AS CONSTRUCTION REQUIREMENT**

---

## Test 5 — Authorized Boolean

Finding:

Would collapse authority evaluation into record representation.

Result:

**REJECTED**

---

## Test 6 — Released Boolean

Finding:

Would collapse later release into the original placement record.

Result:

**REJECTED**

---

## Test 7 — Reject Past Expiry

Finding:

Would collapse structural representation and current-time evaluation.

Result:

**REJECTED**

---

## Test 8 — Enforce Temporal Ordering

Finding:

Would prevent disputed, imported, or historically inconsistent records from being represented for inspection.

Result:

**REJECTED**

---

## Test 9 — Infer Progression HELD

Finding:

Would collapse Hold control and progression assertion.

Result:

**REJECTED**

---

## Test 10 — Create Refusal

Finding:

Would collapse Hold representation and operation execution.

Result:

**REJECTED**

---

# CONTRACT INVARIANTS

## Invariant 1

Every Hold record composes one valid RuntimeRecordHeader.

## Invariant 2

The header category remains `HOLD`.

## Invariant 3

Hold-record identity remains `header.record_id`.

## Invariant 4

No separate `hold_id` is permitted.

## Invariant 5

Every Hold declares one exact target reference.

## Invariant 6

Every Hold declares one exact blocked-consequence reference.

## Invariant 7

Every Hold declares one exact scope reference.

## Invariant 8

Every Hold declares one exact reason reference.

## Invariant 9

Every Hold declares one exact resolution-condition reference.

## Invariant 10

Target-version reference remains optional and unresolved.

## Invariant 11

Branch remains optional and unresolved.

## Invariant 12

Context remains optional and unresolved.

## Invariant 13

Trigger remains optional and distinct from reason.

## Invariant 14

Basis remains optional and distinct from trigger.

## Invariant 15

Owner remains optional and does not establish authority.

## Invariant 16

Placement actor remains optional and does not establish authority.

## Invariant 17

Placement-authority reference does not prove placement authority.

## Invariant 18

Release-authority reference does not prove release authority.

## Invariant 19

Recorded, placed, effective, review, and expiry times remain distinct.

## Invariant 20

Temporal ordering remains outside the model.

## Invariant 21

Expiry does not automatically release the Hold.

## Invariant 22

Resolution-condition satisfaction does not automatically release the Hold.

## Invariant 23

Release fields remain absent.

## Invariant 24

Current active-state fields remain absent.

## Invariant 25

Release remains a separate immutable capability.

## Invariant 26

Multiple concurrent Holds remain representable.

## Invariant 27

Control Hold remains distinct from progression `HELD`.

## Invariant 28

Control Hold remains distinct from Evaluation `HOLD`.

## Invariant 29

Control Hold remains distinct from refusal and failure.

## Invariant 30

The model remains immutable and side-effect free.

## Invariant 31

Equality and hashing remain structural.

## Invariant 32

Ordering remains unsupported.

## Invariant 33

Serialization and persistence remain absent.

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

Constructor shape:
**FROZEN**

Dataclass configuration:
**FROZEN**

Header-category enforcement:
**FROZEN**

Required-reference validation:
**FROZEN**

Optional-reference validation:
**FROZEN**

Datetime validation:
**FROZEN**

Temporal separation:
**FROZEN**

Validation order:
**FROZEN**

Error behavior:
**FROZEN**

Release-field absence:
**FROZEN**

Active-state absence:
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

No Hold placement, blocking, refusal, authority, active-state, expiry, or release behavior was introduced.

---

# NEXT SESSION

Begin:

**HOLD RECORD FOUNDATION — TEST CONTRACT 001**

Primary question:

What exact tests must be written before implementation to prove header composition, target and blocked-consequence separation, required scope, reason and resolution conditions, optional target-version, branch, context, trigger, basis, owner and authority references, temporal separation, release-field absence, active-state absence, validation precedence, immutability, equality, hashing, ordering prohibition, service isolation, and preservation of all frozen Runtime Kernel foundations?

Required work:

1. define test file
2. define valid Hold header
3. define minimal Hold fixture
4. define context-rich Hold fixture
5. define header tests
6. define required-reference tests
7. define optional-reference tests
8. define temporal tests
9. define temporal-separation tests
10. define validation-precedence tests
11. define release-field absence tests
12. define active-state absence tests
13. define immutability tests
14. define equality and hashing tests
15. define ordering prohibition
16. define serialization absence
17. define service-isolation tests
18. preserve production implementation HOLD

**UNKNOWN → HOLD**
