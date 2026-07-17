# RESEARCH OS — RUNTIME OBJECT TYPE AND STATE SEPARATION 001

**Date:** 2026-07-16
**Project:** Research OS
**Development Version:** v2.0.0
**Status:** ACTIVE / CANDIDATE
**Implementation:** HOLD
**Authority:** NONE

**UNKNOWN → HOLD**

---

# PURPOSE

Determine how Runtime Object Type must remain distinct from:

* runtime state
* evaluation result
* lifecycle position
* relationship status
* identity-integrity condition
* release condition
* archival condition
* branch condition
* validation status
* supersession status

Primary question:

**What kind of object is this, and what is currently true of it?**

No type or state vocabulary is promoted or frozen in this session.

---

# PREREQUISITE

Runtime Object Identity and Continuity Separation 001 established the candidate distinctions:

Runtime Object Identity
= stable durable addressability

Object Version
= immutable representation within object history

Object State
= current declared condition

Object Continuity
= preserved lineage through change

This session isolates semantic type from state and other changing conditions.

---

# OPERATING RULES

* Do not implement.
* Do not infer type from state.
* Do not infer state from type.
* Do not use lifecycle stage as object state.
* Do not collapse validation result into universal object state.
* Do not collapse identity integrity into object state.
* Do not collapse relationship status into object state.
* Do not assume one state dimension is sufficient.
* Preserve object-local state.
* Preserve historical state transitions.
* Pressure test every candidate state.
* Freeze only what survives reduction.

---

# PRIMARY DISTINCTIONS

Object Type
≠
Object State

Object State
≠
Lifecycle Stage

Object State
≠
Evaluation Result

Object State
≠
Relationship Status

Object State
≠
Identity Integrity

Object State
≠
Storage Condition

Object State
≠
Release Event

Object State
≠
Authority

Object State
≠
Truth

Object State
≠
Validity Everywhere

---

# CANDIDATE DEFINITION — RUNTIME OBJECT TYPE

Runtime Object Type is the declared semantic category that identifies what kind of research-relevant entity a Runtime Object represents.

Candidate examples:

* Inquiry
* Investigation
* Observation
* Proposition
* Evidence Assignment
* Analysis
* Evaluation
* Interpretation
* Research Release

A Runtime Object Type should remain stable unless the object was misclassified or must be replaced by a differently typed object.

Type answers:

**What kind of entity is this?**

Type does not answer:

* whether the object is active
* whether it is valid
* whether it has been released
* whether it has been archived
* whether it has been superseded
* whether it is trusted
* whether it is complete
* whether it is authoritative
* whether it is true

Status:

**CANDIDATE**

---

# CANDIDATE DEFINITION — RUNTIME OBJECT STATE

Runtime Object State is a declared representation of what is currently true about a Runtime Object within a defined state dimension and runtime context.

State answers:

**What is currently true of this object in this dimension?**

A state must be:

* object-local
* explicitly declared
* historically inspectable
* attributable to a runtime event
* reconstructable
* scoped to a defined state dimension

Candidate finding:

A single undifferentiated state field may be insufficient.

Status:

**STRONGLY SUPPORTED**

---

# TYPE STABILITY

Candidate principle:

Object type should not change merely because:

* content changes
* state changes
* validation occurs
* invalidation occurs
* release occurs
* archival occurs
* supersession occurs
* branch membership changes
* new relationships are created
* an evaluation result changes

Example:

```text
OBS-000001
Type: Observation
```

The object may become:

* active
* held
* invalidated
* released
* archived
* superseded

It remains an Observation.

Boundary:

State Transition
≠
Type Transition

Status:

**STRONGLY SUPPORTED**

---

# TYPE CORRECTION

An object may be discovered to have been misclassified.

Example:

```text
ANL-000003
Declared Type: Analysis

later determined to be:

Interpretation
```

Possible responses:

## Model A — Change Type In Place

Risk:

Historical classification becomes difficult to reconstruct.

## Model B — Record Type-Correction Event

```text
ANL-000003
Type:
Analysis → Interpretation
```

Risk:

A stable semantic type becomes mutable.

## Model C — Create Replacement Object

```text
INT-000009
--replaces_misclassified→
ANL-000003
```

Benefit:

Historical classification and correction remain explicit.

Initial finding:

Type correction must preserve the original classification history.

Whether correction changes type or creates a replacement object remains unresolved.

Status:

**HOLD**

---

# STATE VS LIFECYCLE STAGE

Lifecycle stage asks:

**Where is an assumed process?**

Object state asks:

**What is currently true of this object?**

Example:

A research program may simultaneously contain:

* a DRAFT proposition
* an ACTIVE investigation
* a HELD evaluation
* a RELEASED interpretation
* an ARCHIVED observation
* a SUPERSEDED analysis

One global stage cannot represent this condition.

Boundary:

One Global Runtime Stage
≠
Research State

Candidate decision:

State must remain object-local.

Status:

**STRONGLY SUPPORTED**

---

# SINGLE STATE VS MULTIPLE STATE DIMENSIONS

Candidate object:

```text
PROP-000004
```

Possible simultaneous conditions:

```text
Progression State: ACTIVE
Evaluation Condition: VALIDATED
Release Condition: UNRELEASED
Archival Condition: AVAILABLE
Identity Integrity: PRESERVED
Supersession Condition: CURRENT
```

A single state field such as:

```text
State: VALIDATED
```

cannot express the other dimensions.

Candidate finding:

Runtime objects may require multiple orthogonal condition dimensions rather than one universal state enumeration.

Boundary:

Concurrent Conditions
≠
Conflicting States

Status:

**STRONGLY SUPPORTED**

---

# CANDIDATE STATE DIMENSIONS

## 1. Progression State

Describes whether the object is currently participating in active runtime progression.

Candidate values:

* DRAFT
* ACTIVE
* HELD
* INACTIVE
* CLOSED

Pressure:

`CLOSED` may incorrectly imply permanent closure.

Status:

**CANDIDATE**

---

## 2. Evaluation Condition

Describes the current relationship between an object and one or more evaluations.

Candidate values:

* NOT_EVALUATED
* EVALUATION_PENDING
* EVALUATED
* VALIDATED
* INVALIDATED
* INCONCLUSIVE
* INSUFFICIENT_EVIDENCE

Pressure:

An object may have multiple evaluations with different scopes and results.

A universal object-level evaluation condition may collapse scoped disagreement.

Status:

**HOLD**

---

## 3. Release Condition

Describes whether an object or representation has participated in a release.

Candidate values:

* UNRELEASED
* RELEASE_CANDIDATE
* RELEASED
* WITHDRAWN

Pressure:

Release may apply to a specific version or package rather than the whole object.

Status:

**CANDIDATE**

---

## 4. Archival Condition

Describes storage or active-access disposition.

Candidate values:

* AVAILABLE
* ARCHIVED
* RESTRICTED
* TOMBSTONED
* IRRETRIEVABLE

Pressure:

Archival may be a repository condition rather than a semantic Runtime Object state.

Status:

**HOLD**

---

## 5. Supersession Condition

Describes whether another object has formally replaced the object for a declared scope.

Candidate values:

* CURRENT
* PARTIALLY_SUPERSEDED
* SUPERSEDED

Pressure:

Supersession is fundamentally a relationship with scope and provenance.

A derived condition may be useful, but the relationship is primary.

Status:

**STRONGLY SUPPORTED AS DERIVED CONDITION**

---

## 6. Identity-Integrity Condition

Describes whether identity continuity and reconstruction remain reliable.

Candidate values:

* ESTABLISHED
* PRESERVED
* AMBIGUOUS
* CONFLICTING
* DUPLICATED
* ORPHANED
* CORRUPTED
* PARTIALLY_RECONSTRUCTABLE
* TOMBSTONED
* IRRETRIEVABLE

Boundary:

Identity Integrity
≠
Runtime Progression State

Status:

**CANDIDATE SEPARATE DIMENSION**

---

## 7. Branch Condition

Describes branch participation or branch-local continuity.

Candidate values:

* UNBRANCHED
* SHARED
* BRANCH_LOCAL
* MERGED
* DIVERGED

Pressure:

Branch membership may be better represented through explicit relationships rather than state.

Status:

**HOLD**

---

# VALIDATION AS STATE OR RELATIONSHIP

Claim:

“A validated object should have state VALIDATED.”

Pressure:

Validation requires:

* target
* criteria
* evidence
* scope
* method
* evaluator
* result
* limitations
* time

An object may be:

* validated for one scope
* invalidated for another
* unevaluated for a third
* validated by one evaluator
* held by another evaluator

Therefore:

```text
State: VALIDATED
```

may be too broad.

Candidate structure:

```text
EVAL-000010
--evaluates→
PROP-000004

EVAL-000010
Result: PASS

Scope:
specified operational conditions
```

Derived inspection view:

```text
PROP-000004
Validated within scope X
```

Boundary:

Validation Relationship Exists
≠
Object Universally Validated

Candidate decision:

Validation should be represented primarily through Evaluation objects, results, scope, and typed relationships.

A validation condition may be derived for inspection.

Status:

**STRONGLY SUPPORTED**

---

# INVALIDATION AS STATE OR RELATIONSHIP

Invalidation may target:

* an object
* a version
* a relationship
* an evaluation
* a release
* a method
* a scoped claim

Candidate form:

```text
EVAL-000015
--invalidates_within_scope→
PROP-000004
```

The target may remain active or historically relevant outside that scope.

Boundary:

Invalidated Within Scope
≠
Globally Invalid

Candidate decision:

Invalidation must remain scoped and evidentially grounded.

A universal `INVALIDATED` state is unsafe unless its scope is explicit.

Status:

**STRONGLY SUPPORTED**

---

# SUPERSESSION AS STATE OR RELATIONSHIP

Supersession requires:

* predecessor
* successor
* declared scope
* reason
* effective time
* provenance

Primary representation:

```text
PROP-000005
--supersedes_within_scope→
PROP-000004
```

Derived condition:

```text
PROP-000004
Supersession Condition:
SUPERSEDED within scope X
```

Boundary:

Superseded Condition
≠
Supersession Relationship

Candidate decision:

Supersession is primarily a typed relationship.

Object-level supersession condition should be derived.

Status:

**STRONGLY SUPPORTED**

---

# RELEASE AS STATE OR EVENT

Release may be represented by:

* a release event
* a Research Release object
* a relationship between release and included objects
* a release condition projected onto included versions

Candidate example:

```text
REL-000003
Type: Research Release

REL-000003
--includes_version→
PROP-000004/VER-000002
```

Runtime event:

```text
EVT-000041
Type: RELEASE_ISSUED
Target: REL-000003
```

Derived object condition:

```text
PROP-000004/VER-000002
Release Condition: RELEASED
```

Boundary:

Release Event
≠
Research Release Object

Research Release Object
≠
Released Object Identity

Release Condition
≠
Object Type

Status:

**STRONGLY SUPPORTED**

---

# WITHDRAWAL AS STATE OR EVENT

Withdrawal may apply to:

* release
* version
* interpretation
* proposition
* relationship
* evaluation

A withdrawal event records the occurrence.

A withdrawal condition describes current effect.

The underlying identity remains preserved.

Boundary:

Withdrawn
≠
Deleted

Withdrawal Event
≠
Withdrawal Condition

Status:

**CANDIDATE**

---

# ARCHIVAL AS STATE OR STORAGE CONDITION

Archival may mean:

* removed from active workflow
* stored for long-term preservation
* unavailable in the primary interface
* access restricted
* physically relocated
* logically inactive

These meanings are not identical.

Candidate reduction:

Archival should not automatically be treated as semantic object state.

It may instead be:

* repository condition
* availability condition
* progression condition
* explicit archival event

Boundary:

Archived
≠
Semantically Inactive

Archived
≠
Invalid

Archived
≠
Deleted

Status:

**HOLD**

---

# HELD STATE

`HELD` appears useful as a progression-control state.

Candidate meaning:

The object remains preserved and addressable, but progression or promotion is paused because required conditions are unresolved, insufficient, conflicting, or unsafe.

HELD does not mean:

* false
* invalid
* rejected
* deleted
* inactive forever
* unauthorized in all contexts

Boundary:

HELD
≠
FAIL

HELD
≠
INVALIDATED

HELD
≠
ARCHIVED

HELD
≠
WITHDRAWN

Status:

**STRONGLY SUPPORTED**

---

# ACTIVE STATE

`ACTIVE` appears useful as a progression state.

Candidate meaning:

The object is currently participating in runtime activity, review, revision, evaluation, investigation, or relationship formation.

ACTIVE does not mean:

* valid
* accepted
* released
* complete
* authoritative
* correct

Boundary:

Active
≠
Valid

Active
≠
Approved

Status:

**CANDIDATE**

---

# DRAFT STATE

`DRAFT` appears useful for an object whose representation or admission remains incomplete.

Pressure:

A draft object may still be:

* actively evaluated
* released internally
* archived
* referenced
* branched

Therefore DRAFT may describe maturity rather than progression.

Candidate concern:

`DRAFT` may belong to a representation-maturity dimension rather than the primary Runtime Object state.

Status:

**HOLD**

---

# CLOSED STATE

Claim:

“Completed research objects should become CLOSED.”

Pressure:

Research may reopen after:

* new evidence
* contradiction
* replication
* external change
* method failure
* reinterpretation
* release challenge

Boundary:

Closed
≠
Permanently Closed

Candidate alternatives:

* INACTIVE
* RELEASED
* ARCHIVED
* DORMANT
* COMPLETE_WITHIN_SCOPE

No candidate survives yet.

Status:

**HOLD**

---

# COMPLETION CONDITION

Completion may apply to:

* an investigation
* an analysis execution
* an evaluation
* a release package
* a branch
* a task

Completion must be scoped.

Example:

```text
Investigation:
completed

Research Question:
still open
```

Boundary:

Component Complete
≠
Research Complete

Status:

**STRONGLY SUPPORTED**

---

# RELATIONSHIP STATUS VS OBJECT STATE

A relationship may be:

* proposed
* active
* held
* invalidated
* superseded
* withdrawn
* archived

This condition belongs to the relationship.

It must not automatically alter the states of source and target objects.

Example:

```text
OBS-000001 --supports→ PROP-000004
Relationship Status: INVALIDATED
```

The Observation and Proposition remain independently addressable.

Boundary:

Relationship Invalidated
≠
Source Object Invalidated

Relationship Invalidated
≠
Target Object Invalidated

Status:

**STRONGLY SUPPORTED**

---

# EVENT STATUS VS OBJECT STATE

An event record may possess conditions such as:

* recorded
* verified
* disputed
* invalidated
* superseded
* corrupted

These conditions describe the event record or its integrity.

They do not directly describe the affected object.

Boundary:

Event Integrity
≠
Object State

Status:

**STRONGLY SUPPORTED**

---

# TYPE-SPECIFIC STATE

Different Runtime Object Types may require different state semantics.

Examples:

## Investigation

* PLANNED
* ACTIVE
* INTERRUPTED
* COMPLETED
* ABANDONED

## Evaluation

* PENDING
* ACTIVE
* COMPLETED
* INCONCLUSIVE
* WITHDRAWN

## Research Release

* DRAFT
* ISSUED
* WITHDRAWN
* SUPERSEDED
* ARCHIVED

Pressure:

A universal state vocabulary may erase type-specific meaning.

Candidate architecture:

* small cross-type progression vocabulary
* type-specific condition vocabularies
* explicit derived inspection views

Status:

**CANDIDATE**

---

# CROSS-TYPE STATE VOCABULARY

Potential cross-type progression conditions:

* ACTIVE
* HELD
* INACTIVE

Potential problems:

`INACTIVE` may combine:

* completed
* paused
* archived
* abandoned
* withdrawn

Candidate finding:

Even a small universal progression vocabulary may be too coarse without reason and context.

Status:

**HOLD**

---

# STATE TRANSITION REQUIREMENTS

Every state transition candidate should declare:

* target object
* state dimension
* prior value
* new value
* triggering event
* actor or process
* timestamp
* reason
* authority where applicable
* evidence where applicable
* branch context
* scope

Boundary:

Recorded Transition
≠
Authorized Transition

State Change
≠
Valid State Change

Status:

**STRONGLY SUPPORTED**

---

# CONCURRENT STATE PRESSURE TEST

Candidate object:

```text
PROP-000004
```

Simultaneous conditions:

```text
Progression: HELD
Evaluation: PASS within scope A
Evaluation: FAIL within scope B
Release: RELEASED as version 2
Supersession: CURRENT within scope A
Supersession: SUPERSEDED within scope B
Identity Integrity: PRESERVED
Availability: ARCHIVED
```

Result:

These conditions are not necessarily contradictory.

They occupy different dimensions and scopes.

Boundary:

Multiple Conditions
≠
Incoherent State

Status:

**STRONGLY SUPPORTED**

---

# DERIVED STATE VIEWS

An inspection surface may provide simplified views such as:

```text
Overall Condition:
HELD
```

However, this must be derived from explicit underlying conditions and must disclose:

* derivation rule
* included dimensions
* excluded dimensions
* scope
* time
* uncertainty
* conflicts

Boundary:

Derived Summary
≠
Canonical State

Status:

**STRONGLY SUPPORTED**

---

# MINIMUM TYPE INVARIANTS

## Invariant 1

Every Runtime Object must declare one semantic object type.

## Invariant 2

Object type must remain distinct from object state.

## Invariant 3

State transitions must not silently change object type.

## Invariant 4

Type correction must remain historically reconstructable.

## Invariant 5

Type must not imply validity, truth, authority, release, or completion.

## Invariant 6

Equivalent state does not imply equivalent type.

## Invariant 7

Equivalent type does not imply equivalent state.

Status:

**STRONGLY SUPPORTED**

**NOT YET FROZEN**

---

# MINIMUM STATE INVARIANTS

## Invariant 1

State must be object-local.

## Invariant 2

Every state assertion must identify its state dimension.

## Invariant 3

Every state transition must be recorded through an immutable Runtime Event.

## Invariant 4

State history must remain reconstructable.

## Invariant 5

Validation must not be represented as universal object truth.

## Invariant 6

Supersession must remain grounded in an explicit typed relationship.

## Invariant 7

Relationship status must remain distinct from source and target object states.

## Invariant 8

Identity-integrity condition must remain distinct from runtime progression state.

## Invariant 9

Release condition must identify the released object, version, branch, or package.

## Invariant 10

Archival must not erase identity, provenance, relationships, or event history.

## Invariant 11

Derived state summaries must not replace canonical underlying conditions.

## Invariant 12

Conflicting scoped evaluations must remain representable.

## Invariant 13

One global runtime stage must not govern all Runtime Objects.

## Invariant 14

State must not imply authority.

Status:

**STRONGLY SUPPORTED**

**NOT YET FROZEN**

---

# ADVERSARIAL TESTS

## Test 1 — Validated Observation

Claim:

```text
OBS-000001
State: VALIDATED
```

Pressure:

Validated against what criteria, evidence, method, and scope?

Result:

Unsafe without explicit Evaluation and scope.

**FAIL AS UNIVERSAL STATE**

---

## Test 2 — Superseded Proposition

Claim:

```text
PROP-000004
State: SUPERSEDED
```

Pressure:

Superseded by what, for which purpose, and within what scope?

Result:

Useful only as a derived condition grounded in a typed relationship.

**PASS AS DERIVED CONDITION**

---

## Test 3 — Released Analysis

Claim:

```text
ANL-000003
State: RELEASED
```

Pressure:

Was the object released, a version released, or a package containing it released?

Result:

Release target must be explicit.

**HOLD**

---

## Test 4 — Archived Observation

Claim:

```text
OBS-000001
State: ARCHIVED
```

Pressure:

Does this describe semantic condition, storage, availability, or progression?

Result:

Term is overloaded.

**HOLD**

---

## Test 5 — Active Invalidated Proposition

Claim:

A proposition is both ACTIVE and invalidated within one evaluation scope.

Result:

Possible. ACTIVE describes progression; invalidation describes scoped evaluation condition.

**PASS**

---

## Test 6 — Multiple Validation Results

Claim:

One object cannot be both validated and invalidated.

Pressure:

Different evaluations may use different criteria, scopes, evidence, or times.

Result:

Both conditions may coexist when scope remains explicit.

**PASS**

---

## Test 7 — Type Changed by Release

Claim:

A Proposition becomes a Publication after release.

Result:

Release creates or uses a Research Release object. It does not change the Proposition’s type.

**FAIL**

---

## Test 8 — Relationship Invalidated

Claim:

Invalidating a `supports` relationship invalidates both connected objects.

Result:

Unsupported. Relationship condition remains distinct.

**FAIL**

---

# SESSION FINDINGS

The following separation currently survives:

```text
Runtime Object Type
= what kind of entity the object is

Runtime Object State
= what is currently true within a declared state dimension

Evaluation Result
= outcome of a scoped assessment

Relationship Status
= current condition of a typed semantic connection

Identity Integrity
= condition of identity continuity and reconstructability

Release Condition
= participation of an object, version, branch, or package in a release
```

Strong findings:

* type and state must remain distinct
* state must be object-local
* one global lifecycle stage is unsafe
* one universal state field is probably insufficient
* validation must remain scoped
* supersession is primarily a relationship
* release requires an explicit target
* archival remains semantically overloaded
* derived summaries must not replace canonical conditions

Status:

**STRONGLY SUPPORTED**

**NOT YET FROZEN**

---

# UNRESOLVED QUESTIONS

1. Which state dimensions are irreducible?
2. Is there any safe universal progression-state vocabulary?
3. Is DRAFT a progression condition or maturity condition?
4. Is ACTIVE meaningful across every Runtime Object Type?
5. Is HELD universal or type-specific?
6. Should INACTIVE exist?
7. How should completion be represented?
8. Is archival part of Runtime Kernel state or repository state?
9. Should release condition apply to objects or only versions and packages?
10. Can one Runtime Object have multiple current branch-local states?
11. How should contradictory evaluation results be summarized?
12. Which derived state views are safe?
13. Can type ever change without new object identity?
14. What distinguishes type correction from object replacement?
15. Which states require explicit authority?
16. Which state transitions may occur automatically?
17. How should state uncertainty be represented?
18. How should absent state information be represented?
19. Is UNKNOWN a state, inspection result, or epistemic condition?
20. Is HOLD a state, control decision, or both at different layers?

---

# IMPLEMENTATION DECISION

Do not create type models.

Do not create state enumerations.

Do not create transition services.

Do not encode validation as a universal object state.

Do not encode supersession as a standalone state without relationship scope.

Do not encode archival semantics.

Do not create global lifecycle stages.

Do not modify the frozen Platform Kernel.

Implementation remains:

**HOLD**

---

# NEXT SESSION

Begin:

**RUNTIME STATE DIMENSION REDUCTION 001**

Primary question:

What is the minimum set of irreducible state dimensions required to represent runtime progression without collapsing evaluation, release, identity integrity, relationship condition, archival, or authority?

Required pressure points:

* progression condition
* representation maturity
* evaluation condition
* release condition
* availability condition
* identity-integrity condition
* relationship condition
* branch-local condition
* scoped and concurrent states
* unknown state
* absent state
* derived summary state
* HOLD semantics
* authority-bound transitions

**UNKNOWN → HOLD**
