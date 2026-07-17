# RESEARCH OS — PROGRESSION ASSERTION RECORD FOUNDATION

# TARGET, CONDITION, SCOPE, AND BASIS SEPARATION 001

**Date:** 2026-07-17
**Project:** Research OS
**Development Version:** v2.0.0
**Status:** ACTIVE / SEMANTIC REDUCTION
**Architecture:** RUNTIME KERNEL CANDIDATE ARCHITECTURE FROZEN
**Implementation:** HOLD
**Authority:** VOCABULARY AND CONTRACT REDUCTION ONLY

**UNKNOWN → HOLD**

---

# PURPOSE

Define the minimum immutable semantic contract for a Progression Assertion record after separating:

1. assertion-record identity
2. target identity
3. target-version identity
4. asserted progression condition
5. prior progression condition
6. branch
7. scope
8. runtime context
9. assertion time
10. effective time
11. actor
12. source
13. basis
14. evidence
15. rationale
16. authority
17. admission
18. Hold control
19. canonical projection

This session does not authorize tests, implementation, persistence, services, migration, authority evaluation, Hold creation, or canonical progression projection.

---

# PREREQUISITE

Existing Progression and Status Boundary Inspection 001 established:

* application status is not Runtime progression
* application `UNKNOWN` is only a display fallback
* progression conditions are asserted rather than intrinsic object facts
* progression assertion is distinct from Runtime Event
* progression assertion is distinct from Runtime Object Version
* Evaluation result is distinct from progression condition
* control Hold is distinct from progression assertion
* conflicting assertions must remain visible
* latest recorded assertion is not automatically canonical
* progression remains scoped by target, branch, context, and time
* migration of existing application statuses is prohibited

---

# OPERATING RULES

* Do not implement.
* Do not create tests.
* Do not modify existing Runtime Kernel models.
* Do not modify application status fields.
* Do not modify ObjectEngine.
* Do not create Hold records.
* Do not create progression services.
* Do not calculate current progression.
* Do not infer authority.
* Do not infer admission.
* Do not infer truth.
* Do not embed generic evidence or rationale payloads.
* Freeze only the minimum contract that survives semantic reduction.

---

# PRIMARY QUESTION

What minimum information must an immutable Progression Assertion record contain to represent:

```text
Target T
is asserted to have progression condition C
within declared branch, scope, context, and time
with any available actor, source, and basis
```

without claiming:

* truth
* validity
* authority
* admission
* canonicality
* currentness
* successful transition
* complete lineage
* complete evidence
* Hold placement

---

# MODEL NAME CANDIDATES

## Candidate A — ProgressionAssertion

Advantages:

* concise
* directly names the semantic concept

Problems:

* may be confused with an in-memory claim rather than an immutable Runtime record
* does not emphasize durable record identity

Result:

**REJECTED**

---

## Candidate B — ProgressionAssertionRecord

Advantages:

* explicit immutable-record role
* separates assertion identity from target identity
* aligns with the capability name
* avoids unnecessary `Runtime` repetition while remaining inside Runtime Kernel models

Result:

**STRONGLY SUPPORTED**

---

## Candidate C — RuntimeProgressionAssertionRecord

Advantages:

* explicit Runtime Kernel ownership
* highly specific

Problems:

* longer than existing model naming pattern
* inconsistent with the planned roadmap wording
* `RuntimeRecordHeader` composition already establishes Runtime record context

Result:

**REJECTED**

---

# MODEL NAME DECISION

Selected model name:

```text
ProgressionAssertionRecord
```

Definition:

A `ProgressionAssertionRecord` is an immutable Runtime record declaring that a specified target has a specified progression condition within explicitly available branch, scope, context, and temporal dimensions.

It records an assertion.

It does not establish the assertion as canonical fact.

Status:

**SELECTED**

---

# PRODUCTION PATH

Selected future production path:

```text
models/progression_assertion_record.py
```

Selected future test path:

```text
tests/runtime/test_progression_assertion_record.py
```

Status:

**SELECTED**

---

# HEADER COMPOSITION

Every Progression Assertion record should compose:

```text
RuntimeRecordHeader
```

Selected field:

```text
header
```

Selected type:

```python
RuntimeRecordHeader
```

The model must not duplicate:

* record ID
* record category
* recorded time
* schema version
* provenance reference
* external identity

Status:

**SELECTED**

---

# RECORD CATEGORY

The composed header must declare:

```text
PROGRESSION_ASSERTION
```

Boundary:

```text
Record Category
≠
Progression Condition
```

```text
Record Category
≠
Event Type
```

```text
Record Category
≠
Hold Type
```

Status:

**SELECTED**

---

# ASSERTION-RECORD IDENTITY

Local assertion-record identity is:

```text
header.record_id
```

Do not add:

```text
assertion_id
```

unless a later reduction proves a separate identity requirement.

Boundary:

```text
Assertion Record Identity
≠
Target Identity
```

```text
Assertion Record Identity
≠
Basis Identity
```

```text
Assertion Record Identity
≠
Source Identity
```

Status:

**SELECTED**

---

# TARGET FIELD

Selected field name:

```text
target_ref
```

Definition:

A local reference identifying the primary Runtime entity to which the progression assertion applies.

Selected type:

```python
str
```

Status:

**REQUIRED**

---

# TARGET_REF CONTRACT DIRECTION

`target_ref` must later be:

* non-empty
* not whitespace-only
* exact
* unresolved by the model
* free from prefix assumptions
* free from automatic ObjectEngine lookup
* free from target-type inference

The target may refer to:

* enduring Runtime Object
* Runtime Object Version
* Branch
* Relationship
* another separately addressable Runtime entity

The first foundation must not restrict target category.

Status:

**SELECTED**

---

# TARGET VERSION FIELD

Question:

Must every assertion identify an exact Runtime Object Version?

Pressure:

* some progression claims apply to an enduring object
* some apply only to a specific version
* some imported claims lack resolved version identity
* some branch-local claims may later resolve to a version

Selected field:

```text
target_version_ref
```

Selected type:

```python
str | None
```

Meaning:

An optional reference identifying the exact Runtime Object Version to which the assertion applies.

When absent:

The record does not establish exact version targeting.

Absence does not mean:

* all versions
* current version
* no version exists
* version identity is irrelevant

Status:

**OPTIONAL / SELECTED**

---

# TARGET AND TARGET VERSION SEPARATION

```text
target_ref
≠
target_version_ref
```

`target_ref` identifies the primary target entity.

`target_version_ref` optionally narrows the assertion to a specific version.

The model must not verify:

* that the version belongs to the target
* that the version exists
* that the version is current
* that the version is admitted

Status:

**FROZEN SEMANTIC SEPARATION**

---

# ASSERTED CONDITION FIELD

Selected field name:

```text
asserted_condition
```

Definition:

The progression condition declared by the assertion.

Status:

**REQUIRED**

---

# CONDITION VOCABULARY

Frozen candidate values:

```text
PENDING
ACTIVE
HELD
DORMANT
ABANDONED
```

These represent progression participation conditions.

They do not represent:

* Evaluation results
* inspection results
* authority decisions
* release conditions
* current-version state
* canonical projection state

Status:

**SELECTED CLOSED FOUNDATION VOCABULARY**

---

# CONDITION REPRESENTATION OPTIONS

## Option A — Open Uppercase String

Advantages:

* extensible
* avoids enum dependency

Problems:

* permits accidental semantic drift
* weakens the frozen candidate vocabulary
* may admit `UNKNOWN`, `CONFLICTING`, or `PASS`

Result:

**REJECTED**

---

## Option B — Python Enum

Advantages:

* strong vocabulary closure
* explicit type
* protects semantic boundaries

Problems:

* adds a second production model
* may complicate first-capability test scope
* previous architecture warned against premature progression enums

Result:

**DEFERRED**

---

## Option C — String with Explicit Accepted Values

Advantages:

* simple immutable model
* standard-library only
* closes foundation vocabulary
* avoids separate enum capability
* preserves future migration path to enum if justified

Result:

**SELECTED**

---

# ASSERTED CONDITION REPRESENTATION

Selected type:

```python
str
```

Accepted values only:

```text
PENDING
ACTIVE
HELD
DORMANT
ABANDONED
```

No normalization is permitted.

Invalid examples include:

```text
UNKNOWN
CONFLICTING
PASS
FAIL
ACTIVE 
active
```

Status:

**SELECTED**

---

# PRIOR CONDITION FIELD

Selected field name:

```text
prior_condition
```

Selected type:

```python
str | None
```

Meaning:

An optional progression condition believed or declared to apply before the asserted condition.

Status:

**OPTIONAL / SELECTED**

---

# PRIOR CONDITION VOCABULARY

When present, `prior_condition` must use the same accepted vocabulary:

```text
PENDING
ACTIVE
HELD
DORMANT
ABANDONED
```

It remains a declared prior condition.

Boundary:

```text
Declared Prior Condition
≠
Verified Prior Condition
```

Status:

**SELECTED**

---

# SAME PRIOR AND ASSERTED CONDITION

Question:

Should the model reject:

```text
prior_condition == asserted_condition
```

Finding:

No.

A Progression Assertion may reaffirm or restate a condition without declaring a transition.

Examples:

* repeated external assertion
* imported duplicate claim
* continued-condition assertion
* correction of surrounding context without changing condition

Boundary:

```text
Prior Condition Equals Asserted Condition
≠
Invalid Assertion
```

Status:

**ALLOWED**

---

# TRANSITION BOUNDARY

The model must not claim that a transition occurred merely because both fields exist.

Boundary:

```text
Prior Condition + Asserted Condition
≠
Verified Transition
```

A transition may require:

* event
* temporal ordering
* authority
* admissibility
* prior-state reconstruction

Status:

**FROZEN**

---

# BRANCH FIELD

Selected field name:

```text
branch_ref
```

Selected type:

```python
str | None
```

Branch-local progression must remain representable.

When present:

* identifies declared branch context
* remains unresolved
* carries no branch-validity inference

When absent:

No branch reference is established.

Absence does not mean:

* root branch
* main branch
* universal branch
* branch-independent assertion

Status:

**OPTIONAL / SELECTED**

---

# BRANCH REQUIREDNESS DECISION

Architecture requires branch scope where progression is branch-local.

However, universal field requiredness would make these cases unrepresentable:

* imported assertion with unresolved branch
* assertion made before branch resolution
* non-branch-specific target
* incomplete historical record

Therefore:

```text
branch_ref
```

remains optional structurally.

Later admission rules may require it for branch-sensitive operations.

Boundary:

```text
Structural Validity
≠
Branch-Sufficient Admission
```

Status:

**SELECTED**

---

# SCOPE FIELD

Selected field name:

```text
scope_ref
```

Selected type:

```python
str
```

Meaning:

A reference identifying the declared scope within which the progression assertion applies.

Status:

**REQUIRED**

---

# SCOPE REQUIREDNESS DECISION

A progression assertion without scope risks silent universalization.

The frozen architecture requires:

```text
No runtime assertion may silently broaden the scope of its supporting record.
```

Therefore, every Progression Assertion must declare one scope reference.

The first model does not interpret scope.

It only requires an explicit non-empty reference.

Status:

**REQUIRED / SELECTED**

---

# CONTEXT FIELD

Selected field name:

```text
context_ref
```

Selected type:

```python
str | None
```

Meaning:

An optional reference identifying the runtime, operational, institutional, campaign, or environmental context in which the assertion applies.

When absent:

No explicit context reference is established.

Absence does not imply universal context.

Status:

**OPTIONAL / SELECTED**

---

# SCOPE AND CONTEXT SEPARATION

```text
scope_ref
≠
context_ref
```

Scope defines where the assertion’s semantic applicability is bounded.

Context identifies the surrounding operational or environmental setting.

Equal strings may be permitted because equal syntax does not prove equal semantics.

Status:

**SELECTED**

---

# RECORDED TIME

Recorded time remains:

```text
header.recorded_at
```

It identifies when the record entered the local Runtime Kernel.

The model must not duplicate:

```text
recorded_at
```

Status:

**FROZEN**

---

# ASSERTED_AT FIELD

Question:

Must the model separately record when the assertion was made?

Cases:

* external assertion made before import
* locally recorded assertion made at record time
* historical assertion with unknown assertion time
* machine-generated assertion with explicit time

Selected field:

```text
asserted_at
```

Selected type:

```python
datetime | None
```

Status:

**OPTIONAL / SELECTED**

---

# ASSERTED_AT SEMANTICS

When present:

* identifies when the assertion is declared to have been made
* must be timezone-aware
* preserves exact value
* carries no truth or authority inference

When absent:

No separate assertion time is established.

Absence does not mean:

* assertion time equals recorded time
* assertion was made immediately
* assertion time is unknown globally

Status:

**SELECTED**

---

# EFFECTIVE_AT FIELD

Selected field:

```text
effective_at
```

Selected type:

```python
datetime | None
```

Meaning:

The time at which the asserted progression condition is claimed to apply.

Status:

**OPTIONAL / SELECTED**

---

# TEMPORAL ORDERING

The model must not enforce ordering among:

```text
header.recorded_at
asserted_at
effective_at
```

These may legitimately differ because of:

* delayed recording
* historical import
* retroactive assertion
* future-effective assertion
* incomplete chronology

Boundary:

```text
Valid Temporal Fields
≠
Temporally Coherent Assertion
```

Status:

**SELECTED**

---

# OBSERVED_AT FIELD

Question:

Should the model include:

```text
observed_at
```

Finding:

Observation and assertion are distinct, but not every progression assertion is observational.

Adding this field would broaden the first model.

Status:

**DEFERRED**

---

# ACTOR FIELD

Selected field:

```text
actor_ref
```

Selected type:

```python
str | None
```

Meaning:

An optional reference identifying the person, service, controller, institution, or agent declaring the assertion.

Actor does not imply authority.

Boundary:

```text
Actor
≠
Authority
```

Status:

**OPTIONAL / SELECTED**

---

# SOURCE FIELD

Selected field:

```text
source_ref
```

Selected type:

```python
str | None
```

Meaning:

An optional reference identifying the source system, record, dataset, process, or external origin from which the assertion was obtained.

Source remains distinct from actor.

Boundary:

```text
Source
≠
Actor
```

```text
Source
≠
Provenance Automatically
```

Status:

**OPTIONAL / SELECTED**

---

# BASIS FIELD

Selected field:

```text
basis_ref
```

Selected type:

```python
str | None
```

Meaning:

An optional reference identifying the primary record, Evaluation, event, evidence object, decision, or other basis supporting the assertion.

Status:

**OPTIONAL / SELECTED**

---

# BASIS REQUIREDNESS DECISION

Ideally, every progression assertion would include a basis.

However, requiring it would make these cases unrepresentable:

* imported assertion with incomplete source history
* unresolved historical assertion
* human declaration awaiting evidence linkage
* initial structural capture before basis reconciliation

Therefore:

```text
basis_ref
```

remains optional structurally.

Later admission may require it.

Boundary:

```text
Basis Missing
≠
Assertion False
```

```text
Basis Missing
≠
Assertion Admissible
```

Status:

**SELECTED**

---

# EVIDENCE FIELD

Do not include:

```text
evidence
evidence_refs
```

as a generic list or payload.

Evidence may be represented through:

* `basis_ref`
* separate relationships
* Evaluation records
* future evidence-binding capability

Status:

**PROHIBITED FOR FOUNDATION**

---

# RATIONALE FIELD

Question:

Should the model include free-form:

```text
rationale
```

Finding:

A free-form string introduces content, authorship, localization, and serialization concerns.

Candidate alternative:

```text
rationale_ref
```

However, a primary basis reference is sufficient for the first foundation.

Status:

**DEFERRED**

---

# AUTHORITY FIELDS

Do not include:

```text
authorized
authority_ref
authority_status
permission
approved
```

Authority remains separately evaluated.

Status:

**PROHIBITED**

---

# ADMISSION FIELDS

Do not include:

```text
admitted
valid
accepted
rejected
```

Structural construction remains distinct from admission.

Status:

**PROHIBITED**

---

# CANONICAL PROJECTION FIELDS

Do not include:

```text
is_current
canonical
selected
effective_condition
current_condition
```

Canonical progression is later reconstructed.

Status:

**PROHIBITED**

---

# HOLD CONTROL FIELDS

Do not include:

```text
hold_ref
is_blocked
blocked
control_status
```

A Hold record is a separate capability.

A progression assertion may assert `HELD`, but this remains distinct from a control Hold.

Boundary:

```text
asserted_condition = HELD
≠
Explicit Hold Record
```

Status:

**PROHIBITED**

---

# CONFLICT FIELDS

Do not include:

```text
conflicting
conflict_status
```

Conflict is detected by comparing multiple assertions.

It is not intrinsic to one assertion record.

Status:

**PROHIBITED**

---

# MINIMUM REQUIRED FIELD SET

Selected required fields:

```python
header: RuntimeRecordHeader
target_ref: str
asserted_condition: str
scope_ref: str
```

Optional fields:

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

Status:

**STRONGLY SUPPORTED**

---

# FIELD ORDER

Selected declaration order:

1. `header`
2. `target_ref`
3. `asserted_condition`
4. `scope_ref`
5. `target_version_ref`
6. `prior_condition`
7. `branch_ref`
8. `context_ref`
9. `asserted_at`
10. `effective_at`
11. `actor_ref`
12. `source_ref`
13. `basis_ref`

Reason:

* common record identity first
* target binding second
* primary semantic assertion third
* required scope fourth
* optional target refinement and prior condition next
* branch and context before temporal dimensions
* actor, source, and basis last

Status:

**SELECTED**

---

# MINIMUM STRUCTURAL SUFFICIENCY

The following is structurally complete:

```python
ProgressionAssertionRecord(
    header=valid_progression_assertion_header,
    target_ref="research_os",
    asserted_condition="ACTIVE",
    scope_ref="SCOPE-000001",
)
```

It may remain:

* version-unresolved
* prior-condition unresolved
* branch-unresolved
* context-unresolved
* assertion-time unresolved
* effective-time unresolved
* actor-unresolved
* source-unresolved
* basis-unresolved
* unauthorized
* inadmissible
* non-canonical
* conflicting with other assertions

Boundary:

```text
Structural Completeness
≠
Admission Sufficiency
```

Status:

**SELECTED**

---

# CONTEXT-RICH STRUCTURE

A context-rich assertion may contain:

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

This remains an assertion record only.

Status:

**SELECTED**

---

# CROSS-FIELD RULES

The model should not reject equal strings among:

```text
target_ref
target_version_ref
branch_ref
scope_ref
context_ref
actor_ref
source_ref
basis_ref
```

Equal syntax does not prove equal semantic identity.

No cross-field reference equality rule is selected.

Status:

**SELECTED**

---

# CONDITION CROSS-FIELD RULES

The model should allow:

```text
prior_condition == asserted_condition
```

The model should reject any condition value outside the closed foundation vocabulary.

No transition-validity rule is selected.

Status:

**SELECTED**

---

# EQUALITY

Candidate rule:

Use full structural equality across all thirteen fields.

Same header with different asserted condition:

```text
NOT EQUAL
```

Same target and condition with different scope:

```text
NOT EQUAL
```

Same target, condition, and scope with different basis:

```text
NOT EQUAL
```

Status:

**SELECTED**

---

# HASHING

Use standard frozen-dataclass structural hashing.

Hashing must not establish:

* assertion truth
* semantic equivalence
* canonicality
* authority
* admission
* progression order

Status:

**SELECTED**

---

# ORDERING

Do not support ordering.

The following must not imply ordering:

* record ID
* recorded time
* asserted time
* effective time
* condition value
* prior condition

Status:

**SELECTED**

---

# IMMUTABILITY

The future model should use:

```python
@dataclass(frozen=True)
```

No mutation methods are permitted.

Status:

**SELECTED**

---

# SERIALIZATION

Do not implement:

* `to_dict`
* `from_dict`
* JSON serialization
* persistence
* event conversion
* application-status conversion
* canonical projection

Status:

**DEFERRED**

---

# SIDE-EFFECT BOUNDARY

Importing or constructing the model must not:

* access files
* access services
* access the clock
* create events
* create Holds
* resolve references
* evaluate authority
* evaluate admission
* project current progression
* modify existing objects

Status:

**SELECTED**

---

# IMPORT BOUNDARY

Likely permitted imports:

```python
from dataclasses import dataclass
from datetime import datetime

from models.runtime_record_identity import RuntimeRecordHeader
```

The model must not import:

* RuntimeEventRecord
* RuntimeObjectVersionRecord
* ObjectEngine
* Evaluation services
* Hold services
* authority services
* projection services
* persistence services
* Streamlit

Status:

**SELECTED**

---

# PROHIBITED FIELDS

The first foundation must not include:

* `assertion_id`
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
* `result`
* `status`
* `transitioned`
* `supersedes`
* `superseded_by`

---

# CANDIDATE CONTRACT SUMMARY

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

## Header Requirement

```text
header.record_category == PROGRESSION_ASSERTION
```

## Accepted Conditions

```text
PENDING
ACTIVE
HELD
DORMANT
ABANDONED
```

## Authority

```text
PROHIBITED
```

## Canonical Projection

```text
PROHIBITED
```

## Hold Control

```text
SEPARATE CAPABILITY
```

---

# SEMANTIC BOUNDARIES

```text
Assertion Record Identity
≠
Target Identity
```

```text
Target Identity
≠
Target Version Identity
```

```text
Progression Assertion
≠
Progression Fact
```

```text
Asserted Condition
≠
Canonical Current Condition
```

```text
Prior Condition
≠
Verified Prior Condition
```

```text
Prior + Asserted Condition
≠
Verified Transition
```

```text
Progression HELD
≠
Control Hold Record
```

```text
Evaluation HOLD
≠
Progression HELD
```

```text
CONFLICTING
≠
Progression Condition
```

```text
Actor
≠
Authority
```

```text
Source
≠
Actor
```

```text
Basis
≠
Truth
```

```text
Recorded At
≠
Asserted At
```

```text
Asserted At
≠
Effective At
```

```text
Structural Validity
≠
Admission
```

---

# ADVERSARIAL TEST 1 — APPLICATION STATUS FIELD

Proposal:

Use one `status` field.

Finding:

Would collapse application display state, progression condition, Evaluation result, and control state.

Result:

**REJECTED**

---

# ADVERSARIAL TEST 2 — UNKNOWN CONDITION

Proposal:

Allow `UNKNOWN` as asserted progression condition.

Finding:

Missing knowledge must not become a negative or state assertion.

Result:

**REJECTED**

---

# ADVERSARIAL TEST 3 — CONFLICTING CONDITION

Proposal:

Allow `CONFLICTING` as asserted condition.

Finding:

Conflict is reconstructed from multiple assertions.

Result:

**REJECTED**

---

# ADVERSARIAL TEST 4 — BRANCH REQUIRED

Finding:

Would make unresolved and non-branch-specific assertions unrepresentable.

Result:

**REJECTED AS STRUCTURAL REQUIREMENT**

---

# ADVERSARIAL TEST 5 — SCOPE OPTIONAL

Finding:

Would permit silent universalization.

Result:

**REJECTED**

---

# ADVERSARIAL TEST 6 — BASIS REQUIRED

Finding:

Would make incomplete imported assertions unrepresentable.

Result:

**REJECTED AS STRUCTURAL REQUIREMENT**

---

# ADVERSARIAL TEST 7 — AUTHORIZED BOOLEAN

Finding:

Collapses authority evaluation into assertion representation.

Result:

**REJECTED**

---

# ADVERSARIAL TEST 8 — HOLD REFERENCE

Finding:

Couples progression assertion to a separate control capability.

Result:

**REJECTED**

---

# ADVERSARIAL TEST 9 — CURRENT BOOLEAN

Finding:

Collapses canonical projection into one record.

Result:

**REJECTED**

---

# ADVERSARIAL TEST 10 — REQUIRE TRANSITION

Proposal:

Require prior condition to differ from asserted condition.

Finding:

Would prevent reaffirmation and non-transition assertions.

Result:

**REJECTED**

---

# CANDIDATE INVARIANTS

## Invariant 1

Every Progression Assertion record composes one valid `RuntimeRecordHeader`.

## Invariant 2

The header category must equal `PROGRESSION_ASSERTION`.

## Invariant 3

Assertion-record identity remains `header.record_id`.

## Invariant 4

No separate `assertion_id` is permitted.

## Invariant 5

Every assertion declares one non-empty target reference.

## Invariant 6

Every assertion declares one accepted progression condition.

## Invariant 7

Every assertion declares one non-empty scope reference.

## Invariant 8

Target version remains optional and unresolved.

## Invariant 9

Prior condition remains optional and declarative.

## Invariant 10

Equal prior and asserted conditions remain representable.

## Invariant 11

Prior and asserted conditions do not establish a verified transition.

## Invariant 12

Branch remains optional and unresolved.

## Invariant 13

Missing branch does not imply root or universal branch.

## Invariant 14

Context remains optional and unresolved.

## Invariant 15

Missing context does not imply universal context.

## Invariant 16

Recorded, asserted, and effective times remain distinct.

## Invariant 17

Temporal order remains outside the model.

## Invariant 18

Actor remains optional and does not imply authority.

## Invariant 19

Source remains optional and distinct from actor.

## Invariant 20

Basis remains optional and does not establish truth.

## Invariant 21

No generic evidence or rationale payload is permitted.

## Invariant 22

The record does not create or represent a control Hold.

## Invariant 23

The record does not determine conflict.

## Invariant 24

The record does not determine authority, admission, validity, truth, or canonical progression.

## Invariant 25

The model remains immutable, structurally comparable, unordered, and side-effect free.

Status:

**STRONGLY SUPPORTED**

**NOT YET FROZEN AS IMPLEMENTATION CONTRACT**

---

# UNRESOLVED QUESTIONS

The following remain open:

1. exact dataclass configuration
2. exact constructor validation order
3. exact condition validation implementation
4. exact datetime validation
5. exact error-message fragments
6. whether header subclasses are accepted
7. whether target and target-version references may match
8. whether asserted time should default to recorded time
9. whether effective time may precede asserted time
10. whether scope and context may match
11. whether basis may equal source
12. whether target-version syntax should be constrained
13. whether accepted condition vocabulary should become an enum later
14. whether a specialized transition assertion should follow this capability
15. whether basis sufficiency belongs to admission or Evaluation

All remain:

**HOLD**

---

# REDUCTION DECISION

Model name:
**SELECTED**

Production path:
**SELECTED**

Header composition:
**SELECTED**

Record category:
**SELECTED**

Target reference:
**REQUIRED / SELECTED**

Target-version reference:
**OPTIONAL / SELECTED**

Asserted condition:
**REQUIRED / SELECTED**

Condition vocabulary:
**CLOSED / SELECTED**

Prior condition:
**OPTIONAL / SELECTED**

Branch reference:
**OPTIONAL / SELECTED**

Scope reference:
**REQUIRED / SELECTED**

Context reference:
**OPTIONAL / SELECTED**

Asserted time:
**OPTIONAL / SELECTED**

Effective time:
**OPTIONAL / SELECTED**

Actor reference:
**OPTIONAL / SELECTED**

Source reference:
**OPTIONAL / SELECTED**

Basis reference:
**OPTIONAL / SELECTED**

Authority fields:
**PROHIBITED**

Admission fields:
**PROHIBITED**

Canonical fields:
**PROHIBITED**

Hold fields:
**PROHIBITED**

Implementation:
**HOLD**

---

# READINESS CHECKPOINT 2

Target, Condition, Scope, and Basis Separation:

**COMPLETE**

No production model was created.

No tests were created.

No application status behavior was changed.

No Hold capability was created.

No authority or projection behavior was introduced.

---

# NEXT SESSION

Begin:

**PROGRESSION ASSERTION RECORD FOUNDATION — IMMUTABLE CONTRACT 001**

Primary question:

What exact field types, condition vocabulary, validation order, datetime rules, scope enforcement, error behavior, immutability, equality, hashing, ordering prohibition, and acceptance criteria must define `ProgressionAssertionRecord` before tests are written?

Required work:

1. freeze exact field types
2. freeze field declaration order
3. freeze constructor shape
4. freeze dataclass configuration
5. define header-category enforcement
6. define required-reference validation
7. define optional-reference validation
8. define condition validation
9. define datetime validation
10. define validation precedence
11. define error behavior
12. define equality and hashing
13. define ordering prohibition
14. define side-effect boundary
15. define acceptance criteria
16. preserve implementation HOLD

**UNKNOWN → HOLD**
