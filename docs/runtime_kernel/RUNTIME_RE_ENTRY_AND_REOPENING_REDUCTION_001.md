# RESEARCH OS — RUNTIME RE-ENTRY AND REOPENING REDUCTION 001

**Date:** 2026-07-17
**Project:** Research OS
**Development Version:** v2.0.0
**Status:** ACTIVE / CANDIDATE
**Implementation:** HOLD
**Authority:** NONE

**UNKNOWN → HOLD**

---

# PURPOSE

Determine the minimum semantics required to distinguish:

* re-entry
* reopening
* resumption
* reactivation
* continuation
* branch-local return
* release challenge
* abandoned-object return
* new inquiry creation

Primary question:

**When may an existing Runtime Object or lineage return to progression without losing identity, and when must the return create a new object, branch, version, or inquiry?**

No re-entry model, reopening rule, transition rule, or identity threshold is promoted or frozen in this session.

---

# PREREQUISITE

Runtime Progression Condition Reduction 001 established candidate progression conditions:

* PENDING
* ACTIVE
* HELD
* DORMANT
* ABANDONED

Runtime Object Identity and Continuity Separation 001 established:

Runtime Object Identity
= stable durable addressability

Object Continuity
= preserved lineage through change

Runtime Revision and Supersession Reduction 001 established that material semantic change may require a new Runtime Object identity.

---

# OPERATING RULES

* Do not implement.
* Do not silently reactivate objects.
* Do not treat re-entry as a new identity automatically.
* Do not treat reopening as continuation without record.
* Do not erase prior releases or dispositions.
* Do not assume prior authority remains valid.
* Do not assume prior Evaluations remain applicable.
* Preserve branch context.
* Preserve triggers and reasons.
* Preserve continuity inspection.
* Preserve reconstruction.
* Freeze only what survives reduction.

---

# PRIMARY DISTINCTIONS

Re-entry
≠
Reopening

Re-entry
≠
New Inquiry

Re-entry
≠
New Identity Automatically

Reopening
≠
Unrecorded Continuation

Resumption
≠
Reconstruction

Dormant
≠
Held

Abandoned
≠
Irreversible

Released
≠
Closed Forever

Prior Validation
≠
Current Validation

Prior Authority
≠
Current Authority

Same Topic
≠
Same Runtime Object

---

# CANDIDATE DEFINITION — RE-ENTRY

Re-entry is a declared runtime transition by which an existing Runtime Object or lineage returns to active progression after previously not participating within the declared scope.

Possible prior conditions:

* PENDING
* HELD
* DORMANT
* ABANDONED
* released but inactive
* branch-non-selected
* archived but still addressable

Re-entry must preserve:

* target identity
* prior condition
* resulting condition
* trigger
* reason
* branch
* scope
* actor or process
* event
* authority where required
* continuity basis
* provenance

Status:

**CANDIDATE**

---

# CANDIDATE DEFINITION — REOPENING

Reopening is a specific form of re-entry in which previously released, apparently completed, abandoned, dormant, or inactive research becomes active again because a new condition requires renewed inquiry or progression.

Possible triggers:

* new evidence
* contradiction
* replication result
* method failure
* environmental change
* policy change
* source correction
* external challenge
* release dispute
* new technology
* reconstruction failure

Boundary:

Reopening
≠
Proof Prior Work Was Improper

Status:

**CANDIDATE**

---

# RE-ENTRY IDENTITY

Every re-entry occurrence should possess a stable identity.

Candidate form:

```text
REN-000000001
```

Re-entry identity supports:

* event association
* authority inspection
* continuity review
* branch comparison
* trigger reconstruction
* correction
* invalidation

Boundary:

Re-entry Identity
≠
Target Identity

Re-entry Identity
≠
Reopening Event Identity

Status:

**STRONGLY SUPPORTED**

---

# RE-ENTRY EVENT

Every re-entry must be recorded through an immutable Runtime Event.

Candidate event:

```text
EVT-000140
Type:
OBJECT_REENTERED

Target:
PROP-000004

Prior Condition:
DORMANT

Resulting Condition:
ACTIVE
```

Boundary:

Re-entry Event
≠
Re-entry Record

The event records the occurrence.

The re-entry record preserves the full transition semantics.

Status:

**STRONGLY SUPPORTED**

---

# TARGET

Re-entry may target:

* Runtime Object
* version
* Branch
* Investigation
* Inquiry
* Evaluation
* Research Release lineage
* imported lineage

The exact target must be explicit.

Boundary:

Topic Revisited
≠
Same Target Re-entered

Status:

**STRONGLY SUPPORTED**

---

# PRIOR CONDITION

Re-entry must declare the prior progression or disposition condition where known.

Possible prior conditions:

* PENDING
* HELD
* DORMANT
* ABANDONED
* NOT_ESTABLISHED
* CONFLICTING
* PARTIALLY_RECONSTRUCTABLE

Inspection conditions such as `NOT_ESTABLISHED` must remain distinct from progression conditions.

Boundary:

Declared Prior Condition
≠
Verified Prior Condition

Status:

**STRONGLY SUPPORTED**

---

# RESULTING CONDITION

Most re-entry transitions appear to result in:

```text
ACTIVE
```

Possible exceptions:

* return to PENDING for review
* return to HELD while continuity is inspected
* branch creation before activation

Candidate decision:

Re-entry does not necessarily imply immediate ACTIVE status.

Status:

**STRONGLY SUPPORTED**

---

# TRIGGER

Every reopening should declare what caused renewed progression.

Candidate trigger categories:

* NEW_EVIDENCE
* CONTRADICTION
* REPLICATION_RESULT
* METHOD_FAILURE
* EXTERNAL_CHANGE
* RELEASE_CHALLENGE
* PROVENANCE_CORRECTION
* IDENTITY_CONFLICT
* AUTHORITY_CHANGE
* NEW_REQUIREMENT
* REINTERPRETATION
* RECONSTRUCTION_FAILURE

Trigger vocabulary remains unfrozen.

Boundary:

Trigger
≠
Reason

Status:

**TYPE REQUIRED / VALUES HOLD**

---

# REASON

Reason explains why re-entry is appropriate after the triggering condition was observed.

Example:

```text
Trigger:
NEW_EVIDENCE

Reason:
The new evidence directly challenges the released interpretation.
```

Boundary:

Trigger
≠
Rationale

Trigger identifies what happened.

Reason explains why progression should resume.

Status:

**STRONGLY SUPPORTED**

---

# CONTINUITY VALIDATION

Before preserving the same target identity, re-entry should inspect whether continuity remains legitimate.

Continuity pressure points:

* same referent
* same semantic role
* same object purpose
* same lineage
* compatible branch
* reconstructable prior versions
* preserved identity
* unresolved supersession
* prior invalidation
* prior release scope

Possible results:

* CONTINUITY_PRESERVED
* CONTINUITY_PARTIAL
* CONTINUITY_CONFLICTING
* NEW_OBJECT_REQUIRED
* UNKNOWN

These remain candidate inspection results.

Boundary:

Same Label
≠
Continuity Preserved

Status:

**STRONGLY SUPPORTED**

---

# DORMANT TO ACTIVE

Candidate transition:

```text
DORMANT
→
ACTIVE
```

Use when:

* the same object remains legitimate
* no blocking condition remains
* work is intentionally resumed
* continuity is preserved

Status:

**STRONGLY SUPPORTED**

---

# HELD TO ACTIVE

Candidate transition:

```text
HELD
→
ACTIVE
```

This requires:

* relevant Holds resolved
* unresolved Holds identified
* release event
* evidence
* authority where required
* branch and scope

Boundary:

One Hold Released
≠
All Holds Resolved

Status:

**STRONGLY SUPPORTED**

---

# ABANDONED TO ACTIVE

Candidate transition:

```text
ABANDONED
→
ACTIVE
```

Required:

* responsible re-entry decision
* prior abandonment reason
* new reason for return
* unresolved work
* continuity inspection
* branch context
* authority where required

Boundary:

Abandoned
≠
Terminal

Status:

**STRONGLY SUPPORTED**

---

# PENDING TO ACTIVE

This is admission rather than reopening when the object never previously entered active progression.

Boundary:

Initial Admission
≠
Re-entry

Status:

**STRONGLY SUPPORTED**

---

# RELEASED RESEARCH REOPENING

A released object or lineage may be reopened because of:

* contradiction
* replication failure
* correction
* new evidence
* changed environment
* challenge to method
* invalid provenance
* external policy change

Reopening must preserve:

* original release
* released versions
* release scope
* release time
* prior Evaluations
* challenge evidence
* new branch or continued lineage
* public or institutional impact

Boundary:

Reopened Release
≠
Original Release Erased

Status:

**STRONGLY SUPPORTED**

---

# RELEASE CHALLENGE

A challenge to a release should not silently alter released content.

Candidate structure:

```text
CHL-000001
--challenges→
REL-000003
```

The challenge may trigger reopening.

Boundary:

Challenge Exists
≠
Release Invalidated

Status:

**STRONGLY SUPPORTED**

---

# PRIOR EVALUATIONS

Re-entry must inspect whether prior Evaluations remain applicable.

Reasons they may not:

* target version changed
* criteria changed
* evidence changed
* environment changed
* evaluation expired
* scope changed
* provenance failed

Boundary:

Previously Passed
≠
Currently Passed

Status:

**STRONGLY SUPPORTED**

---

# PRIOR AUTHORITY

Prior authority may have:

* expired
* been revoked
* changed scope
* applied to a prior version
* applied to another branch
* depended on old conditions

Boundary:

Previously Authorized
≠
Currently Authorized

Re-entry must not inherit authority automatically.

Status:

**STRONGLY SUPPORTED**

---

# BRANCH-LOCAL REOPENING

A Runtime Object may be reopened in one branch while remaining dormant or abandoned in another.

Example:

```text
Branch A:
DORMANT

Branch B:
ACTIVE
```

Every re-entry must declare branch scope.

Boundary:

Object Reopened
≠
All Branches Reopened

Status:

**STRONGLY SUPPORTED**

---

# NEW BRANCH ON REOPENING

Reopening may create a new Branch when:

* prior released lineage must remain stable
* alternative interpretation is being explored
* prior branch must not be modified
* authority differs
* new methods create divergence
* unresolved contradictions must be preserved

Example:

```text
BR-000009
branched_from
BR-000004

Reason:
release challenge
```

Boundary:

Reopening
≠
New Branch Required

Status:

**CANDIDATE**

---

# SAME OBJECT VS NEW VERSION

Re-entry may preserve the same object identity while creating a new version.

Example:

```text
PROP-000004
VER-000003
→ reopening →
VER-000004
```

Use when:

* same referent
* same semantic role
* continuity preserved
* representation revised

Status:

**STRONGLY SUPPORTED**

---

# SAME OBJECT VS NEW OBJECT

A new Runtime Object may be required when reopening creates:

* a different claim
* a changed referent
* incompatible purpose
* different evaluation target
* independently addressable successor
* contradiction to prior object
* distinct inquiry

Example:

```text
PROP-000008
--arose_from_reopening_of→
PROP-000004
```

Boundary:

Reopened Topic
≠
Same Object Automatically

Status:

**STRONGLY SUPPORTED**

---

# REOPENING VS NEW INQUIRY

A new inquiry should be created when the new question cannot be represented as continuation of the prior inquiry without semantic distortion.

Example:

Prior inquiry:

```text
Does the system remain stable under condition A?
```

New inquiry:

```text
Why does the system fail under condition B?
```

The second may arise from the first but remain independently addressable.

Relationship:

```text
INQ-000009
--arose_from→
INQ-000002
```

Boundary:

Question Emerged From Prior Research
≠
Same Inquiry

Status:

**STRONGLY SUPPORTED**

---

# RESUMPTION

Resumption describes continuation of previously paused active work without material change to purpose, scope, identity, or branch.

Candidate use:

* HELD → ACTIVE
* DORMANT → ACTIVE

Pressure:

Resumption may be an interface term rather than an irreducible runtime primitive.

Candidate decision:

Use Re-entry as the broader runtime semantic.

Resumption may remain a qualified re-entry type.

Status:

**SUPPORTED AS SPECIALIZATION**

---

# REACTIVATION

Reactivation describes restoring ACTIVE progression status.

Pressure:

It says little about why, from what prior condition, or whether continuity remains valid.

Candidate decision:

Reactivation may describe the resulting transition but is insufficient as the full runtime semantic.

Status:

**REJECTED AS PRIMARY TERM**

---

# CONTINUATION

Continuation may occur without a prior transition out of ACTIVE.

Therefore:

Continuation
≠
Re-entry

Status:

**STRONGLY SUPPORTED**

---

# RECONSTRUCTION FAILURE

A lineage may appear reopenable but lack sufficient history.

Possible failures:

* missing target version
* missing release
* missing branch origin
* conflicting identity
* absent provenance
* unresolved supersession
* incomplete event history

Candidate response:

```text
Continuity:
PARTIALLY_RECONSTRUCTABLE

Progression Decision:
HOLD
```

Boundary:

Reconstruction Failure
≠
New Identity Automatically

Status:

**STRONGLY SUPPORTED**

---

# INVALIDATED OBJECT RE-ENTRY

An invalidated object may re-enter progression for:

* correction
* re-evaluation
* historical analysis
* method repair
* replacement development
* scope reassessment

Re-entry does not erase invalidation.

Boundary:

Re-entered
≠
Revalidated

Status:

**STRONGLY SUPPORTED**

---

# SUPERSEDED OBJECT RE-ENTRY

A superseded object may re-enter progression:

* outside supersession scope
* because successor failed
* for historical comparison
* for branch exploration
* after supersession expiration
* after authority change

Boundary:

Superseded
≠
Unusable Forever

Status:

**STRONGLY SUPPORTED**

---

# WITHDRAWN RELEASE REOPENING

A withdrawn release may be reopened for:

* correction
* replacement
* reissuance
* historical review
* challenge response

The withdrawn release identity remains preserved.

A new release identity is likely required for reissuance.

Boundary:

Reopened Release Work
≠
Original Release Reissued Automatically

Status:

**STRONGLY SUPPORTED**

---

# RE-ENTRY AUTHORITY

Some re-entry transitions may require authority when they affect:

* released research
* canonical relationships
* public claims
* institutional records
* operational artifacts
* regulated research
* consequential decisions

Authority must bind to:

* target
* transition
* branch
* scope
* environment
* time
* permitted consequences

Boundary:

Re-entry Recorded
≠
Re-entry Authorized

Status:

**STRONGLY SUPPORTED**

---

# AUTOMATIC RE-ENTRY

Potential automatic triggers:

* scheduled review date
* Hold resolution
* new imported evidence
* replication result
* authority restoration
* environmental threshold

Pressure:

Automatic re-entry may activate research without responsible continuity review.

Candidate decision:

Automatic trigger detection may propose re-entry.

Actual progression transition should require:

* declared rule
* event
* continuity inspection
* authority where required
* visible decision

Boundary:

Trigger Detected
≠
Re-entry Admitted

Status:

**STRONGLY SUPPORTED**

---

# RE-ENTRY CORRECTION

A re-entry record may be incorrect.

Correction must preserve:

* original re-entry
* corrective event
* corrected target, branch, trigger, scope, or condition
* reason
* evidence
* actor or process
* downstream impact

Boundary:

Correction
≠
Deletion

Status:

**STRONGLY SUPPORTED**

---

# RE-ENTRY INVALIDATION

A re-entry may be invalidated when:

* continuity was falsely declared
* authority was absent
* wrong branch was activated
* target identity was incorrect
* trigger evidence was inadmissible
* prior Holds remained unresolved

Invalidation of re-entry does not erase the attempt.

Status:

**STRONGLY SUPPORTED**

---

# RE-ENTRY RECONSTRUCTION

A re-entry must be reconstructable sufficiently to answer:

* what returned to progression
* from which prior condition
* within which branch and scope
* what triggered the return
* why the return was admitted
* who or what initiated it
* what authority applied
* whether continuity was preserved
* whether a new version, object, or branch was created
* which prior Evaluations and releases remain relevant

Status:

**STRONGLY SUPPORTED**

---

# CANDIDATE MINIMUM RE-ENTRY CONTRACT

Every re-entry currently appears to require:

1. re-entry identity
2. target identity
3. prior progression or disposition condition
4. resulting progression condition
5. trigger
6. reason
7. branch or runtime context
8. scope
9. initiating actor or process
10. recorded time
11. provenance
12. creation event
13. continuity assessment

Conditionally required:

14. prior release reference
15. prior Evaluation references
16. authority basis
17. resulting version
18. resulting object
19. resulting branch
20. Hold-release references
21. external trigger identity
22. integrity evidence
23. correction references
24. invalidation references
25. unresolved conditions

Status:

**STRONGLY SUPPORTED**

**NOT YET FROZEN**

---

# MINIMUM RE-ENTRY INVARIANTS

## Invariant 1

Every re-entry must possess stable local identity.

## Invariant 2

Every re-entry must identify an exact target.

## Invariant 3

Every re-entry must declare prior and resulting progression conditions where established.

## Invariant 4

Every re-entry must declare branch and scope.

## Invariant 5

Every re-entry must preserve trigger and rationale.

## Invariant 6

Re-entry must be recorded through an immutable Runtime Event.

## Invariant 7

Re-entry must not erase prior states, releases, Evaluations, Holds, invalidations, or supersession.

## Invariant 8

Re-entry must not imply revalidation.

## Invariant 9

Re-entry must not inherit prior authority automatically.

## Invariant 10

Continuity must be inspected before preserving object identity where semantic change is material.

## Invariant 11

Branch-local re-entry must remain representable.

## Invariant 12

Reopening may create a new version, object, branch, or inquiry without collapsing predecessor identity.

## Invariant 13

Automatic triggers must not silently activate progression.

## Invariant 14

Re-entry correction must not rewrite history.

## Invariant 15

Invalidated re-entry attempts must remain inspectable.

## Invariant 16

Where continuity cannot be established, progression remains HOLD.

Status:

**STRONGLY SUPPORTED**

**NOT YET FROZEN**

---

# ADVERSARIAL TESTS

## Test 1 — Dormant Return

Claim:

A dormant object can become ACTIVE without an event.

Result:

Destroys transition reconstruction.

**REJECTED**

---

## Test 2 — Abandonment Is Terminal

Claim:

An abandoned object cannot return.

Result:

Explicit re-entry may legitimately reopen it.

**REJECTED**

---

## Test 3 — Released Means Closed

Claim:

Released research cannot be reopened.

Result:

New evidence, contradiction, or replication may require reopening.

**REJECTED**

---

## Test 4 — Same Topic Means Same Object

Claim:

Research on the same topic should reuse the same identity.

Result:

Semantic referent, purpose, and claim may differ.

**REJECTED**

---

## Test 5 — Prior PASS Remains Valid

Claim:

Previously validated research remains validated after reopening.

Result:

Version, scope, evidence, criteria, or environment may have changed.

**REJECTED**

---

## Test 6 — Prior Authority Persists

Claim:

Original authority covers reopening.

Result:

Authority may have expired or applied only to prior scope.

**REJECTED**

---

## Test 7 — Trigger Automatically Reopens

Claim:

New evidence should automatically activate the object.

Result:

Trigger detection does not establish continuity, authority, or admission.

**REJECTED**

---

## Test 8 — Invalidated Object Cannot Re-enter

Claim:

Invalidated objects must remain inactive permanently.

Result:

They may re-enter for correction, reassessment, or replacement development.

**REJECTED**

---

## Test 9 — Reopening Erases Release

Claim:

Reopening replaces the prior release.

Result:

The prior release remains historically preserved.

**REJECTED**

---

## Test 10 — Re-entry Requires Same Branch

Claim:

An object must reopen in its prior branch.

Result:

A new branch may be required to preserve released or alternative lineage.

**REJECTED**

---

# SESSION FINDINGS

The following definitions survive:

```text
Re-entry
=
declared transition by which an existing
Runtime Object or lineage returns to progression
within a declared branch and scope
```

```text
Reopening
=
re-entry caused by a new condition that requires
renewed inquiry or progression after prior release,
dormancy, abandonment, or apparent completion
```

Strong boundaries:

Re-entry
≠
New Identity Automatically

Reopening
≠
Unrecorded Continuation

Initial Admission
≠
Re-entry

Prior Validation
≠
Current Validation

Prior Authority
≠
Current Authority

Re-entered
≠
Revalidated

Released
≠
Closed Forever

Trigger Detected
≠
Re-entry Admitted

Same Topic
≠
Same Runtime Object

Status:

**STRONGLY SUPPORTED**

**NOT YET FROZEN**

---

# UNRESOLVED QUESTIONS

1. Is re-entry an object, operation, event family, or composite record?
2. Must every re-entry identify a prior progression condition?
3. Is ACTIVE the only valid resulting condition?
4. Can a re-entry result in PENDING?
5. Which trigger categories are irreducible?
6. Is continuity assessment an Evaluation?
7. Who may establish continuity?
8. Which continuity failures force new identity?
9. When must reopening create a new branch?
10. When must reopening create a new inquiry?
11. Can one re-entry target several objects?
12. Can one trigger reopen several branches?
13. Which re-entry transitions require authority?
14. Can Hold resolution automatically propose re-entry?
15. How should expired prior Evaluations be represented?
16. Can superseded objects become current again?
17. Can withdrawn releases be reissued under the same release identity?
18. What minimum history is required for reopening reconstruction?
19. How should conflicting re-entry attempts be resolved?
20. Which re-entry failures force HOLD?

---

# IMPLEMENTATION DECISION

Do not create re-entry models.

Do not create reopening models.

Do not create trigger enumerations.

Do not create continuity-assessment services.

Do not create automatic re-entry rules.

Do not create reactivation services.

Do not inherit prior Evaluations or authority.

Do not encode new-identity thresholds.

Do not modify the frozen Platform Kernel.

Implementation remains:

**HOLD**

---

# NEXT SESSION

Begin:

**RUNTIME INSPECTION AND RECONSTRUCTION REDUCTION 001**

Primary question:

What minimum read-only inspection and reconstruction contract is required to expose current conditions, historical events, relationships, provenance, versions, branches, Evaluations, releases, uncertainty, conflicts, and missing information without mutating the runtime or presenting derived summaries as canonical truth?

Required pressure points:

* inspection target
* inspection scope
* inspection time
* current representation
* event history
* relationship history
* provenance chain
* version lineage
* branch lineage
* Evaluation history
* release history
* reconstruction completeness
* conflict reporting
* uncertainty
* missing records
* derived summaries
* authority boundary
* read-only guarantees
* partial reconstruction
* reverse traversal

**UNKNOWN → HOLD**
