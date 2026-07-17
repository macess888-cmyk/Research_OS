# RESEARCH OS — HOLD RECORD FOUNDATION

# TARGET, SCOPE, REASON, OWNER, AND RELEASE SEPARATION 001

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

Define the minimum immutable semantic contract for a Hold record after separating:

1. Hold-record identity
2. target identity
3. target-version identity
4. blocked consequence
5. scope
6. branch
7. context
8. reason
9. triggering record
10. basis
11. owner
12. placement actor
13. placement authority
14. resolution condition
15. release authority
16. review time
17. expiry time
18. release decision
19. Runtime Events
20. progression condition
21. Evaluation result
22. refusal
23. failure

This session does not authorize tests, implementation, persistence, services, release behavior, authority evaluation, application migration, or automatic blocking.

---

# PREREQUISITE

Existing Hold, Refusal, and Control Boundary Inspection 001 established:

* a Hold is an explicit scoped control decision
* a triggering condition is not itself a Hold
* progression `HELD` is distinct from control Hold
* Evaluation `HOLD` is distinct from control Hold
* refusal is distinct from Hold
* failure is distinct from Hold
* pause, dormancy, and inactivity are distinct from Hold
* conflict may trigger a Hold but remains separately visible
* authority failure may trigger a Hold but remains separately represented
* every Hold requires target, scope, reason, and resolution conditions
* Hold owner is distinct from placement authority
* Hold owner is distinct from release authority
* resolution does not automatically release a Hold
* expiry does not automatically release a Hold
* release must be separately recorded
* multiple concurrent Holds must remain representable
* no application-status migration is permitted

---

# OPERATING RULES

* Do not implement.
* Do not create tests.
* Do not modify existing Runtime Kernel models.
* Do not modify application status fields.
* Do not create Hold placement services.
* Do not create release services.
* Do not calculate whether a Hold is currently active.
* Do not evaluate authority.
* Do not publish Runtime Events.
* Do not mutate existing records.
* Freeze only the minimum contract that survives semantic reduction.

---

# PRIMARY QUESTION

What minimum information must an immutable Hold record contain to represent:

```text
A declared control Hold applies to target T,
blocks consequence C,
within scope S,
for reason R,
pending resolution condition Q,
with any available branch, context, ownership,
placement, basis, authority, review, and expiry references.
```

without claiming:

* the Hold was authorized
* the Hold remains active
* the blocking condition is true
* resolution has occurred
* release is authorized
* release has occurred
* every consequence is blocked
* progression is universally `HELD`
* the target failed
* the target is invalid

---

# MODEL NAME CANDIDATES

## Candidate A — Hold

Problems:

* too broad
* may be confused with Evaluation `HOLD`
* may be confused with progression `HELD`
* does not explicitly identify immutable-record role

Result:

**REJECTED**

---

## Candidate B — HoldRecord

Advantages:

* concise
* explicit record semantics
* aligns with roadmap capability
* avoids unnecessary Runtime prefix

Result:

**SELECTED**

---

## Candidate C — RuntimeHoldRecord

Advantages:

* explicit Runtime ownership

Problems:

* inconsistent with `ProgressionAssertionRecord`
* Runtime context is already established through `RuntimeRecordHeader`

Result:

**REJECTED**

---

# MODEL NAME DECISION

Selected model name:

```text
HoldRecord
```

Definition:

A `HoldRecord` is an immutable Runtime control record declaring that a specified consequence is blocked for a specified target within a specified scope pending a declared resolution condition.

Status:

**SELECTED**

---

# PRODUCTION PATH

Selected future production path:

```text
models/hold_record.py
```

Selected future test path:

```text
tests/runtime/test_hold_record.py
```

Status:

**SELECTED**

---

# HEADER COMPOSITION

Every Hold record should compose:

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

Status:

**SELECTED**

---

# RECORD CATEGORY

The composed header must declare:

```text
HOLD
```

Boundary:

```text
Record Category HOLD
≠
Evaluation Result HOLD
```

```text
Record Category HOLD
≠
Progression Condition HELD
```

Status:

**SELECTED**

---

# HOLD-RECORD IDENTITY

Local Hold-record identity is:

```text
header.record_id
```

Do not add:

```text
hold_id
```

Boundary:

```text
Hold Record Identity
≠
Target Identity
```

```text
Hold Record Identity
≠
Trigger Identity
```

```text
Hold Record Identity
≠
Resolution Condition Identity
```

Status:

**SELECTED**

---

# TARGET FIELD

Selected field:

```text
target_ref
```

Selected type:

```python
str
```

Meaning:

A reference identifying the Runtime entity, operation, relationship, release, branch, execution request, or other consequence-bearing subject to which the Hold applies.

Status:

**REQUIRED**

---

# TARGET-VERSION FIELD

A Hold may apply:

* to an enduring target
* to one exact version
* to a version-unresolved historical target

Selected field:

```text
target_version_ref
```

Selected type:

```python
str | None
```

When absent:

No exact target version is established.

Absence does not mean:

* all versions
* current version
* no version exists
* version is irrelevant

Status:

**OPTIONAL / SELECTED**

---

# BLOCKED CONSEQUENCE FIELD

A Hold must declare what consequence is blocked.

Selected field:

```text
blocked_consequence_ref
```

Selected type:

```python
str
```

Possible references may identify:

* progression
* release
* execution
* merge
* revision
* admission
* authorization
* relationship activation
* publication
* deployment

The model does not interpret the consequence.

Status:

**REQUIRED**

---

# TARGET AND CONSEQUENCE SEPARATION

```text
target_ref
≠
blocked_consequence_ref
```

The target identifies what the Hold concerns.

The blocked consequence identifies what may not proceed.

Example:

```text
target_ref = OBJ-000001
blocked_consequence_ref = RELEASE
```

The Hold does not automatically block:

* editing
* inspection
* evidence collection
* unrelated branch progression
* unrelated operations

Status:

**FROZEN SEMANTIC SEPARATION**

---

# SCOPE FIELD

Selected field:

```text
scope_ref
```

Selected type:

```python
str
```

Every Hold must declare one scope.

Reason:

A Hold without scope could silently broaden into universal blocking.

Boundary:

```text
Hold in Scope A
≠
Hold Universally
```

Status:

**REQUIRED / SELECTED**

---

# BRANCH FIELD

Selected field:

```text
branch_ref
```

Selected type:

```python
str | None
```

Branch-local Holds must remain representable.

When absent:

No branch reference is established.

Absence does not mean:

* root branch
* main branch
* all branches
* branch-independent Hold

Status:

**OPTIONAL / SELECTED**

---

# CONTEXT FIELD

Selected field:

```text
context_ref
```

Selected type:

```python
str | None
```

Meaning:

An optional reference identifying the runtime, environment, campaign, operation, institution, or authority domain in which the Hold applies.

Status:

**OPTIONAL / SELECTED**

---

# REASON FIELD

Every Hold must declare why it exists.

Selected field:

```text
reason_ref
```

Selected type:

```python
str
```

The first foundation uses a reference rather than free-form reason text.

Potential reason references may identify:

* identity ambiguity
* unresolved conflict
* missing authority
* insufficient evidence
* provenance insufficiency
* temporal inconsistency
* relationship conflict
* reconstruction failure
* unavailable dependency
* safety concern

Status:

**REQUIRED / SELECTED**

---

# TRIGGER FIELD

Selected field:

```text
trigger_ref
```

Selected type:

```python
str | None
```

Meaning:

An optional reference identifying the record, event, Evaluation, conflict result, request, or condition that directly triggered placement of the Hold.

Boundary:

```text
reason_ref
≠
trigger_ref
```

Reason classifies or explains why.

Trigger identifies the specific initiating record or occurrence.

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

An optional reference identifying the principal supporting record or evidentiary basis for the Hold.

Boundary:

```text
Trigger
≠
Basis
```

A trigger may initiate placement.

A basis may support the decision.

Status:

**OPTIONAL / SELECTED**

---

# OWNER FIELD

Selected field:

```text
owner_ref
```

Selected type:

```python
str | None
```

Meaning:

An optional reference identifying the person, service, institution, or role responsible for coordinating review or resolution.

Owner does not imply authority.

Boundary:

```text
Hold Owner
≠
Placement Authority
```

```text
Hold Owner
≠
Release Authority
```

```text
Responsible for Resolution
≠
Authorized to Release
```

Status:

**OPTIONAL / SELECTED**

---

# PLACED-BY FIELD

Selected field:

```text
placed_by_ref
```

Selected type:

```python
str | None
```

Meaning:

An optional reference identifying the actor, service, institution, or process that declared the Hold.

Placement actor does not establish placement authority.

Boundary:

```text
Placed By
≠
Authorized to Place
```

Status:

**OPTIONAL / SELECTED**

---

# PLACEMENT AUTHORITY FIELD

Question:

Should the Hold directly store:

```text
placement_authority_ref
```

Finding:

A reference may preserve declared authority context, but construction must not prove authority validity.

Selected field:

```text
placement_authority_ref
```

Selected type:

```python
str | None
```

Meaning:

An optional reference identifying the authority claim, role, rule, or decision under which placement is asserted.

Boundary:

```text
Placement Authority Reference Present
≠
Placement Authorized
```

Status:

**OPTIONAL / SELECTED**

---

# RESOLUTION CONDITION FIELD

Every Hold must declare what must be resolved before release may be considered.

Selected field:

```text
resolution_condition_ref
```

Selected type:

```python
str
```

Meaning:

A reference identifying the declared resolution requirement or condition.

Examples may include:

* evidence supplied
* conflict reconciled
* authority established
* identity repaired
* provenance reconstructed
* Evaluation completed
* dependency restored
* review performed

Status:

**REQUIRED / SELECTED**

---

# RELEASE AUTHORITY FIELD

Selected field:

```text
release_authority_ref
```

Selected type:

```python
str | None
```

Meaning:

An optional reference identifying the authority claim, role, rule, or decision expected to govern release.

Boundary:

```text
Release Authority Reference Present
≠
Release Authorized
```

```text
Release Authority
≠
Hold Owner
```

```text
Release Authority
≠
Placement Actor
```

Status:

**OPTIONAL / SELECTED**

---

# RELEASE DECISION FIELD

Do not include:

```text
released
release_status
released_at
released_by_ref
release_decision_ref
```

in the original Hold record.

Release must be represented separately.

Reasons:

* the Hold record is immutable
* release may occur later
* release may require separate authority
* release may be refused
* release conditions may be disputed
* historical reconstruction requires both records

Status:

**PROHIBITED FOR FOUNDATION**

---

# RESOLUTION CONDITION VERSUS RELEASE

```text
Resolution Condition Met
≠
Hold Released
```

```text
Release Authorized
≠
Release Recorded
```

```text
Hold Expired
≠
Hold Released
```

The original Hold record records placement only.

Status:

**FROZEN**

---

# REVIEW TIME FIELD

Selected field:

```text
review_at
```

Selected type:

```python
datetime | None
```

Meaning:

An optional timezone-aware datetime indicating when Hold review is due or expected.

Review does not imply:

* expiry
* automatic escalation
* release
* resolution

Status:

**OPTIONAL / SELECTED**

---

# EXPIRY TIME FIELD

Selected field:

```text
expires_at
```

Selected type:

```python
datetime | None
```

Meaning:

An optional timezone-aware datetime after which expiry handling, escalation, revalidation, or review may become relevant.

Expiry does not automatically release the Hold.

Boundary:

```text
expires_at Reached
≠
Hold Released
```

```text
expires_at Reached
≠
Resolution Condition Satisfied
```

Status:

**OPTIONAL / SELECTED**

---

# PLACED-AT FIELD

Recorded time already exists as:

```text
header.recorded_at
```

Question:

Should a distinct placement time be supported for delayed import or historical recording?

Selected field:

```text
placed_at
```

Selected type:

```python
datetime | None
```

Meaning:

The time at which the Hold decision is asserted to have been made.

When absent:

No distinct placement time is established.

Absence does not mean placement time equals record time.

Status:

**OPTIONAL / SELECTED**

---

# EFFECTIVE-AT FIELD

A Hold may become effective at a time different from placement or recording.

Selected field:

```text
effective_at
```

Selected type:

```python
datetime | None
```

Meaning:

The time at which the Hold is asserted to begin blocking the declared consequence.

Status:

**OPTIONAL / SELECTED**

---

# TEMPORAL SEPARATION

The following remain distinct:

```text
header.recorded_at
placed_at
effective_at
review_at
expires_at
```

The first model must not enforce temporal order.

Structurally representable cases include:

```text
placed_at < recorded_at
placed_at > recorded_at
effective_at < placed_at
review_at < effective_at
expires_at < review_at
```

These may later be judged incoherent, but structural representation must preserve imported or disputed records.

Boundary:

```text
Structurally Valid Hold Times
≠
Temporally Coherent Hold
```

Status:

**SELECTED**

---

# AUTOMATIC RELEASE

The model must not perform automatic release when:

* `expires_at` is reached
* `review_at` is reached
* resolution evidence exists
* owner changes
* authority becomes available
* blocking condition disappears

Automatic release requires a later explicit capability.

Status:

**PROHIBITED**

---

# CURRENT-ACTIVE FIELD

Do not include:

```text
is_active
active
current
expired
resolved
```

Whether a Hold remains active must be reconstructed from:

* Hold record
* release records
* invalidations
* authority
* temporal conditions
* scope
* branch
* context

Status:

**PROHIBITED**

---

# MULTIPLE HOLDS

The model must permit multiple Hold records with:

* same target
* same consequence
* same scope
* different reasons
* different branches
* different contexts
* different authorities
* different resolution conditions

No uniqueness or supersession rule is selected.

Boundary:

```text
New Hold
≠
Prior Hold Replaced
```

Status:

**FROZEN**

---

# EVENT COUPLING

The first Hold model must not require:

* RuntimeEventRecord composition
* automatic `HOLD_CREATED`
* automatic `HOLD_RELEASED`
* EventEngine
* event publication

A later service may create related Runtime Events.

Boundary:

```text
Hold Record
≠
Hold Event
```

Status:

**FROZEN**

---

# PROGRESSION COUPLING

The Hold record must not:

* create ProgressionAssertionRecord
* mutate progression condition
* infer progression `HELD`
* overwrite progression assertions

A later service may produce a separate progression assertion based on an admitted Hold.

Status:

**FROZEN**

---

# EVALUATION COUPLING

The Hold record must not:

* require an Evaluation
* convert Evaluation `HOLD`
* infer failure
* infer validity
* evaluate basis sufficiency

An Evaluation may be referenced through `trigger_ref` or `basis_ref`.

Status:

**FROZEN**

---

# REFUSAL COUPLING

The Hold record must not:

* create refusal outcomes
* reject operations directly
* contain `refused`
* contain `refusal_reason`

A later control service may refuse a blocked consequence by consulting admitted Hold records.

Status:

**FROZEN**

---

# GENERIC PAYLOAD PROHIBITION

Do not include:

```text
reason
resolution_conditions
evidence
metadata
payload
details
```

as mutable strings, lists, or dictionaries.

The first foundation uses typed reference fields.

Status:

**FROZEN**

---

# MINIMUM REQUIRED FIELD SET

Selected required fields:

```python
header: RuntimeRecordHeader
target_ref: str
blocked_consequence_ref: str
scope_ref: str
reason_ref: str
resolution_condition_ref: str
```

Optional fields:

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

Status:

**STRONGLY SUPPORTED**

---

# FIELD ORDER

Selected declaration order:

1. `header`
2. `target_ref`
3. `blocked_consequence_ref`
4. `scope_ref`
5. `reason_ref`
6. `resolution_condition_ref`
7. `target_version_ref`
8. `branch_ref`
9. `context_ref`
10. `trigger_ref`
11. `basis_ref`
12. `owner_ref`
13. `placed_by_ref`
14. `placement_authority_ref`
15. `release_authority_ref`
16. `placed_at`
17. `effective_at`
18. `review_at`
19. `expires_at`

Reason:

* record identity first
* target and blocked consequence next
* required semantic boundaries before optional context
* trigger and basis before responsibility and authority
* temporal dimensions last

Status:

**SELECTED**

---

# MINIMUM STRUCTURAL SUFFICIENCY

The following is structurally complete:

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

It may remain:

* target-version unresolved
* branch unresolved
* context unresolved
* trigger unresolved
* basis unresolved
* owner unresolved
* placement actor unresolved
* placement authority unresolved
* release authority unresolved
* placement time unresolved
* effective time unresolved
* review time absent
* expiry absent
* unauthorized
* inadmissible
* inactive
* already released by another record

Boundary:

```text
Structural Completeness
≠
Operational Admission
```

Status:

**SELECTED**

---

# CONTEXT-RICH STRUCTURE

A context-rich Hold may contain:

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

This remains a structural Hold record only.

Status:

**SELECTED**

---

# CROSS-FIELD EQUALITY RULES

The model should not reject equal strings among reference fields.

Examples structurally permitted:

```text
target_ref == target_version_ref
reason_ref == trigger_ref
trigger_ref == basis_ref
owner_ref == placed_by_ref
placement_authority_ref == release_authority_ref
scope_ref == context_ref
```

Equal syntax does not prove equal semantic identity.

Status:

**SELECTED**

---

# EQUALITY

Use full structural equality across all nineteen fields.

Same header with different reason:

```text
NOT EQUAL
```

Same target and consequence with different scope:

```text
NOT EQUAL
```

Same Hold with different resolution condition:

```text
NOT EQUAL
```

Same Hold with different authority reference:

```text
NOT EQUAL
```

Status:

**SELECTED**

---

# HASHING

Use standard frozen-dataclass structural hashing.

Hashing must not establish:

* Hold authority
* Hold admission
* current active status
* semantic equivalence
* duplicate control effect
* release eligibility

Status:

**SELECTED**

---

# ORDERING

Do not support ordering.

The following must not imply ordering:

* record ID
* recorded time
* placed time
* effective time
* review time
* expiry time

Status:

**SELECTED**

---

# IMMUTABILITY

The future model should use:

```python
@dataclass(frozen=True)
```

Release, expiry, review, and resolution must not mutate the original record.

Status:

**SELECTED**

---

# SIDE-EFFECT BOUNDARY

Importing or constructing the model must not:

* access files
* access services
* access the clock
* resolve references
* evaluate authority
* evaluate admission
* block operations
* refuse operations
* publish Runtime Events
* create progression assertions
* schedule reviews
* release Holds
* determine active status
* mutate application state

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

* ProgressionAssertionRecord
* RuntimeEventRecord
* RuntimeObjectVersionRecord
* ObjectEngine
* Evaluation services
* authority services
* release services
* projection services
* Streamlit
* persistence services

Status:

**SELECTED**

---

# PROHIBITED FIELDS

The first Hold foundation must not include:

* `hold_id`
* `status`
* `is_active`
* `active`
* `current`
* `resolved`
* `released`
* `released_at`
* `released_by_ref`
* `release_decision_ref`
* `expired`
* `failed`
* `refused`
* `progression_condition`
* `evaluation_result`
* `evidence`
* `metadata`
* `payload`

---

# CANDIDATE CONTRACT SUMMARY

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

## Header Requirement

```text
header.record_category == HOLD
```

## Release

```text
SEPARATE IMMUTABLE RECORD OR EVENT
```

## Automatic Expiry Release

```text
PROHIBITED
```

## Active-State Projection

```text
DEFERRED
```

---

# SEMANTIC BOUNDARIES

```text
Hold Record Identity
≠
Target Identity
```

```text
Target
≠
Blocked Consequence
```

```text
Reason
≠
Trigger
```

```text
Trigger
≠
Basis
```

```text
Owner
≠
Placement Actor
```

```text
Placement Actor
≠
Placement Authority
```

```text
Owner
≠
Release Authority
```

```text
Resolution Condition Met
≠
Hold Released
```

```text
Expiry Reached
≠
Hold Released
```

```text
Control Hold
≠
Progression HELD
```

```text
Control Hold
≠
Evaluation HOLD
```

```text
Control Hold
≠
Refusal
```

```text
Control Hold
≠
Failure
```

```text
Structural Validity
≠
Authority
```

```text
Structural Validity
≠
Admission
```

---

# ADVERSARIAL TEST 1 — TARGET ONLY

Proposal:

Store only a target.

Finding:

Does not identify what consequence is blocked.

Result:

**REJECTED**

---

# ADVERSARIAL TEST 2 — OPTIONAL SCOPE

Finding:

Permits silent universal blocking.

Result:

**REJECTED**

---

# ADVERSARIAL TEST 3 — FREE-FORM REASON

Finding:

Introduces content, authorship, localization, and serialization concerns.

Result:

**REJECTED FOR FOUNDATION**

---

# ADVERSARIAL TEST 4 — OWNER REQUIRED

Finding:

Would make imported or unresolved historical Holds structurally unrepresentable.

Result:

**REJECTED AS STRUCTURAL REQUIREMENT**

---

# ADVERSARIAL TEST 5 — AUTHORITY BOOLEAN

Proposal:

Add `authorized`.

Finding:

Collapses authority evaluation into record representation.

Result:

**REJECTED**

---

# ADVERSARIAL TEST 6 — RELEASED BOOLEAN

Finding:

Requires mutation or collapses later release into original placement record.

Result:

**REJECTED**

---

# ADVERSARIAL TEST 7 — AUTOMATIC EXPIRY RELEASE

Finding:

Expiry does not prove resolution or authority.

Result:

**REJECTED**

---

# ADVERSARIAL TEST 8 — REQUIRE BRANCH

Finding:

Would make non-branch-specific and unresolved historical Holds unrepresentable.

Result:

**REJECTED AS STRUCTURAL REQUIREMENT**

---

# ADVERSARIAL TEST 9 — EMBED PROGRESSION HELD

Finding:

Collapses control decision and progression assertion.

Result:

**REJECTED**

---

# ADVERSARIAL TEST 10 — EMBED EVALUATION HOLD

Finding:

Collapses Evaluation result and control decision.

Result:

**REJECTED**

---

# CANDIDATE INVARIANTS

## Invariant 1

Every Hold record composes one valid RuntimeRecordHeader.

## Invariant 2

The header category must equal `HOLD`.

## Invariant 3

Hold-record identity remains `header.record_id`.

## Invariant 4

No separate `hold_id` is permitted.

## Invariant 5

Every Hold identifies one exact target reference.

## Invariant 6

Every Hold identifies one exact blocked-consequence reference.

## Invariant 7

Every Hold declares one explicit scope reference.

## Invariant 8

Every Hold declares one reason reference.

## Invariant 9

Every Hold declares one resolution-condition reference.

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

Placement authority reference does not prove placement authority.

## Invariant 18

Release authority reference does not authorize or record release.

## Invariant 19

Recorded, placed, effective, review, and expiry times remain distinct.

## Invariant 20

Temporal ordering remains outside the model.

## Invariant 21

Expiry does not automatically release the Hold.

## Invariant 22

Resolution-condition satisfaction does not automatically release the Hold.

## Invariant 23

Release remains a separate immutable capability.

## Invariant 24

Current active Hold status remains derived.

## Invariant 25

Multiple concurrent Holds remain representable.

## Invariant 26

Control Hold remains distinct from progression `HELD`.

## Invariant 27

Control Hold remains distinct from Evaluation `HOLD`.

## Invariant 28

Control Hold remains distinct from refusal and failure.

## Invariant 29

The model remains immutable, structurally comparable, unordered, and side-effect free.

Status:

**STRONGLY SUPPORTED**

**NOT YET FROZEN AS IMPLEMENTATION CONTRACT**

---

# UNRESOLVED QUESTIONS

The following remain open:

1. exact constructor validation order
2. exact datetime validation rules
3. whether blocked consequence requires a closed vocabulary
4. whether reason references require type prefixes
5. whether resolution condition may equal reason
6. whether trigger may equal basis
7. whether owner and placed-by may match
8. whether placement and release authority may match
9. whether expiry before effective time is structurally valid
10. whether review time should be required for expiry-bearing Holds
11. whether `placed_at` is necessary for all locally created Holds
12. whether release requires a dedicated record or Event foundation
13. whether active-Hold reconstruction belongs to registry or inspection
14. whether multiple resolution conditions require a separate typed object
15. whether blocked consequence should later become a typed vocabulary

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

Blocked-consequence reference:
**REQUIRED / SELECTED**

Scope reference:
**REQUIRED / SELECTED**

Branch reference:
**OPTIONAL / SELECTED**

Context reference:
**OPTIONAL / SELECTED**

Reason reference:
**REQUIRED / SELECTED**

Trigger reference:
**OPTIONAL / SELECTED**

Basis reference:
**OPTIONAL / SELECTED**

Owner reference:
**OPTIONAL / SELECTED**

Placed-by reference:
**OPTIONAL / SELECTED**

Placement-authority reference:
**OPTIONAL / SELECTED**

Release-authority reference:
**OPTIONAL / SELECTED**

Resolution-condition reference:
**REQUIRED / SELECTED**

Placed time:
**OPTIONAL / SELECTED**

Effective time:
**OPTIONAL / SELECTED**

Review time:
**OPTIONAL / SELECTED**

Expiry time:
**OPTIONAL / SELECTED**

Release fields:
**PROHIBITED**

Current-active fields:
**PROHIBITED**

Automatic expiry release:
**PROHIBITED**

Implementation:
**HOLD**

---

# READINESS CHECKPOINT 2

Target, Scope, Reason, Owner, and Release Separation:

**COMPLETE**

No production model was created.

No tests were created.

No Hold placement or release service was created.

No Runtime Events were created.

No application behavior was changed.

No authority or active-Hold projection was introduced.

---

# NEXT SESSION

Begin:

**HOLD RECORD FOUNDATION — IMMUTABLE CONTRACT 001**

Primary question:

What exact field types, validation order, datetime rules, reference rules, immutability, equality, hashing, ordering prohibition, release separation, and acceptance criteria must define `HoldRecord` before tests are written?

Required work:

1. freeze exact field types
2. freeze field declaration order
3. freeze constructor shape
4. freeze dataclass configuration
5. define header-category enforcement
6. define required-reference validation
7. define optional-reference validation
8. define datetime validation
9. define validation precedence
10. define error behavior
11. define equality and hashing
12. define ordering prohibition
13. define release-field absence
14. define service and side-effect isolation
15. define acceptance criteria
16. preserve implementation HOLD

**UNKNOWN → HOLD**
