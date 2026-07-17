# RESEARCH OS — RUNTIME PROGRESSION CONDITION REDUCTION 001

**Date:** 2026-07-16
**Project:** Research OS
**Development Version:** v2.0.0
**Status:** ACTIVE / CANDIDATE
**Implementation:** HOLD
**Authority:** NONE

**UNKNOWN → HOLD**

---

# PURPOSE

Determine the minimum progression-condition vocabulary required to represent whether a Runtime Object:

* has entered runtime progression
* may continue progressing
* is deliberately paused
* is awaiting admission
* has been interrupted
* is dormant
* has been abandoned
* has completed a scoped activity
* may re-enter progression

Primary question:

**Are ACTIVE and HELD sufficient, or are additional canonical progression conditions irreducible?**

No progression condition is promoted or frozen in this session.

---

# PREREQUISITE

Runtime State Dimension Reduction 001 established:

# Runtime Object core state

small progression condition only

Strong candidate values:

* ACTIVE
* HELD

Other conditions should remain grounded in:

* Runtime Events
* Runtime Relationships
* Evaluation objects
* Research Release objects
* representation maturity
* identity-integrity assertions
* branch topology
* authorization records
* epistemic inspection results

---

# OPERATING RULES

* Do not implement.
* Do not create state enumerations.
* Do not infer progression from object existence.
* Do not assume object creation implies admission.
* Do not collapse completion into permanent closure.
* Do not collapse interruption into HOLD.
* Do not collapse abandonment into deletion.
* Do not treat missing progression information as a state.
* Preserve scoped and branch-local progression.
* Preserve multiple concurrent control reasons.
* Preserve re-entry.
* Freeze only what survives reduction.

---

# PRIMARY DISTINCTIONS

Existence
≠
Admission

Admission
≠
Activation

Active
≠
Executing Now

Held
≠
Failed

Held
≠
Refused

Interrupted
≠
Held

Dormant
≠
Archived

Abandoned
≠
Deleted

Completed
≠
Closed Forever

Re-entry
≠
New Identity

Missing State
≠
Inactive

---

# CANDIDATE CONDITION — PENDING

## Candidate Meaning

A Runtime Object is PENDING when it exists but has not yet been admitted to active progression.

Possible reasons:

* awaiting review
* awaiting required provenance
* awaiting relationship admission
* awaiting authority
* awaiting branch placement
* awaiting identity resolution
* awaiting required metadata
* awaiting explicit activation

## Pressure Test

PENDING may combine several distinct conditions:

* not yet reviewed
* reviewed but not admitted
* authority unresolved
* evidence incomplete
* activation scheduled
* imported but not reconciled

These reasons may be represented through:

* admission decision objects
* HOLD conditions
* authorization records
* inspection results
* unresolved requirements

However, one distinction survives:

```text
Object exists
but
has not entered active progression
```

Boundary:

PENDING
≠
HELD

HELD presumes progression was admitted or explicitly considered and then paused.

PENDING may precede admission.

Status:

**STRONGLY SUPPORTED AS CANDIDATE**

---

# CANDIDATE CONDITION — ACTIVE

## Candidate Meaning

A Runtime Object is ACTIVE when it is admitted to runtime progression and may participate in valid runtime operations.

ACTIVE may include:

* current investigation
* revision
* evaluation
* relationship formation
* branch activity
* preparation for release
* reopening
* inspection-led continuation

ACTIVE does not require an operation to be executing at every moment.

Boundary:

ACTIVE
≠
CURRENTLY EXECUTING

ACTIVE
≠
VALID

ACTIVE
≠
AUTHORIZED FOR CONSEQUENCE

Candidate refinement:

**ACTIVE = admitted and available for runtime progression**

Status:

**STRONGLY SUPPORTED**

---

# CANDIDATE CONDITION — HELD

## Candidate Meaning

A Runtime Object is HELD when progression is deliberately suspended while the object remains preserved, addressable, and eligible for possible future continuation.

A HOLD must declare:

* hold identity
* target
* reason
* scope
* initiating event
* actor or process
* effective time
* required resolution conditions
* authority basis where applicable
* branch context
* release mechanism
* expiration rule if any

HELD does not mean:

* invalid
* failed
* rejected
* abandoned
* archived
* deleted
* permanently inactive

Boundary:

HELD
≠
FAIL

HELD
≠
REFUSAL

HELD
≠
ABANDONED

HELD
≠
COMPLETED

Status:

**STRONGLY SUPPORTED**

---

# MULTIPLE HOLDS

A Runtime Object may be held for several independent reasons.

Example:

```text
HOLD-000001
Reason: identity conflict

HOLD-000002
Reason: authority unresolved

HOLD-000003
Reason: insufficient evidence
```

A single field:

```text
Progression Condition: HELD
```

does not preserve the full control topology.

Candidate architecture:

* progression summary: HELD
* one or more explicit Hold records
* each Hold independently releasable
* progression resumes only when required holds are resolved

Boundary:

HELD Summary
≠
Hold Record

Status:

**STRONGLY SUPPORTED**

---

# HOLD RELEASE

A HOLD must not disappear through silent field replacement.

Candidate release requirements:

* hold identity
* releasing actor or process
* release event
* satisfied resolution conditions
* evidence
* effective time
* scope
* resulting progression condition
* unresolved remaining holds

Boundary:

Hold Removed
≠
Hold Resolved

Status:

**STRONGLY SUPPORTED**

---

# CANDIDATE CONDITION — INTERRUPTED

## Candidate Meaning

A Runtime Object is INTERRUPTED when an active runtime operation or progression path stops before its intended scoped completion.

Possible causes:

* system failure
* actor withdrawal
* lost dependency
* environment failure
* timeout
* safety control
* external disruption
* resource loss

## Pressure Test

Interruption may apply more accurately to:

* operation execution
* investigation
* analysis run
* evaluation run
* branch activity

The Runtime Object itself may remain ACTIVE or become HELD after interruption.

Example:

```text
Analysis operation: INTERRUPTED
Analysis object: ACTIVE
```

or:

```text
Investigation operation: INTERRUPTED
Investigation object: HELD
```

Boundary:

Interrupted Operation
≠
Held Object

Candidate decision:

INTERRUPTED should remain primarily an operation or execution outcome.

It should not be a universal Runtime Object progression condition.

Status:

**REJECTED AS UNIVERSAL OBJECT CONDITION**

---

# CANDIDATE CONDITION — DORMANT

## Candidate Meaning

A Runtime Object is DORMANT when it is not presently progressing but remains eligible for future re-entry without requiring defect resolution.

Possible examples:

* no current investigator
* no current priority
* waiting for future technology
* waiting for external conditions
* intentionally deferred
* preserved for later continuation

## Pressure Test

DORMANT differs from HELD:

* HELD has unresolved blocking conditions.
* DORMANT may have no defect or block.
* DORMANT reflects deliberate non-activity.

DORMANT differs from PENDING:

* PENDING has not yet entered progression.
* DORMANT previously entered or was explicitly deferred.

DORMANT differs from ARCHIVED:

* archival concerns storage or access.
* dormancy concerns progression.

Status:

**STRONGLY SUPPORTED AS CANDIDATE**

---

# CANDIDATE CONDITION — ABANDONED

## Candidate Meaning

A Runtime Object is ABANDONED when responsible progression has been intentionally discontinued without claiming successful scoped completion.

Abandonment should declare:

* target
* reason
* actor or process
* effective time
* scope
* unresolved work
* known consequences
* re-entry conditions
* branch context

ABANDONED does not mean:

* invalid
* erased
* valueless
* permanently unreopenable
* failed in every sense

Boundary:

Abandoned
≠
Deleted

Abandoned
≠
Failed

Abandoned
≠
Completed

## Pressure Test

Abandonment may be:

* an event
* a progression disposition
* a type-specific outcome

A universal object-level condition may still be useful because it distinguishes deliberate discontinuation from passive dormancy and unresolved HOLD.

Status:

**SUPPORTED AS CANDIDATE**

---

# CANDIDATE CONDITION — COMPLETED

## Candidate Meaning

A Runtime Object is COMPLETED when a declared scoped objective has been satisfied.

Pressure:

Completion may apply to:

* one investigation
* one analysis
* one evaluation
* one version
* one branch activity
* one release preparation task

An object may be complete within one scope and active within another.

Example:

```text
Investigation objective A:
COMPLETED

Investigation extension B:
ACTIVE
```

A universal object condition `COMPLETED` may collapse scope.

Candidate safer form:

```text
Completion Record
Target: INV-000003
Scope: Objective A
Result: COMPLETED
```

Derived progression decision may then become:

* DORMANT
* ACTIVE
* ABANDONED
* HELD

Boundary:

Scoped Completion
≠
Universal Object Completion

Status:

**REJECTED AS UNIVERSAL PROGRESSION CONDITION**

---

# CANDIDATE CONDITION — INACTIVE

## Candidate Meaning

The object is not presently participating in runtime progression.

Pressure:

INACTIVE may describe:

* pending
* held
* dormant
* abandoned
* completed within scope
* restricted
* archived
* superseded
* withdrawn

The term erases the reason for non-progression.

Candidate decision:

Do not use INACTIVE as a canonical progression condition.

It may be a derived binary inspection summary.

Boundary:

Not Active
≠
One Canonical State

Status:

**REJECTED AS CANONICAL CONDITION**

---

# CANDIDATE CONDITION — CLOSED

## Candidate Meaning

Progression is considered finished.

Pressure:

Research may reopen because of:

* new evidence
* contradiction
* replication
* reinterpretation
* environmental change
* method failure
* release challenge

CLOSED is easily misread as permanent finality.

Candidate decision:

Do not use CLOSED as a canonical Runtime Object progression condition.

Use explicit scoped completion, dormancy, abandonment, release, or archival records instead.

Status:

**REJECTED**

---

# CANDIDATE CONDITION — REFUSED

## Candidate Meaning

A requested progression operation was not admitted.

Pressure:

Refusal is an outcome of:

* authorization
* admissibility
* policy
* safety control
* operation validation

The target object may remain:

* PENDING
* ACTIVE
* HELD
* DORMANT

Boundary:

Refused Operation
≠
Refused Object State

Status:

**REJECTED AS OBJECT PROGRESSION CONDITION**

---

# CANDIDATE CONDITION — FAILED

## Candidate Meaning

An attempted operation or evaluation did not satisfy declared success criteria.

Pressure:

Failure may apply to:

* execution
* evaluation
* validation
* investigation
* replication
* import
* reconstruction

The object itself may remain ACTIVE, become HELD, become DORMANT, or be ABANDONED.

Boundary:

Failed Operation
≠
Failed Object

Status:

**REJECTED AS UNIVERSAL OBJECT PROGRESSION CONDITION**

---

# OBJECT CREATION

Question:

Does object creation imply PENDING or ACTIVE?

Pressure:

An object may be created:

* as an imported record
* as a draft representation
* as an admitted observation
* as a branch-local successor
* as an automatically generated candidate
* as an archived historical object
* before authority review

Candidate decision:

Creation must not imply ACTIVE.

Object creation should record:

* identity
* type
* provenance
* creation event
* initial progression condition where established

If no progression condition is established, inspection must report:

```text
Progression Condition:
NOT_ESTABLISHED
```

`NOT_ESTABLISHED` is an inspection result, not a progression condition.

Status:

**STRONGLY SUPPORTED**

---

# ADMISSION TO PROGRESSION

Admission is the transition by which a Runtime Object becomes eligible for runtime progression.

Candidate transition:

```text
PENDING
→
ACTIVE
```

Admission should declare:

* target
* admission event
* actor or process
* admission basis
* authority where required
* branch
* effective time
* unresolved conditions
* admitted scope

Boundary:

Object Exists
≠
Object Admitted

Status:

**STRONGLY SUPPORTED**

---

# ACTIVE TO HELD

Candidate transition:

```text
ACTIVE
→
HELD
```

Required record:

* target
* hold record
* reason
* scope
* event
* actor or process
* effective time
* resolution conditions

The object remains preserved and addressable.

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

This transition is valid only when all required blocking Holds within the relevant scope have been resolved or explicitly overridden by valid authority.

Boundary:

One Hold Released
≠
Object Fully Released

Status:

**STRONGLY SUPPORTED**

---

# ACTIVE TO DORMANT

Candidate transition:

```text
ACTIVE
→
DORMANT
```

Possible reasons:

* deliberate deferral
* priority change
* external dependency timing
* no current work required
* future condition awaited without defect

Dormancy should declare:

* target
* reason
* actor or process
* effective time
* re-entry trigger if known
* scope
* branch

Status:

**SUPPORTED AS CANDIDATE**

---

# DORMANT TO ACTIVE

Candidate transition:

```text
DORMANT
→
ACTIVE
```

Re-entry must be recorded through an immutable event.

Re-entry does not imply:

* new object identity
* new branch
* invalidity of prior work
* erasure of dormancy history

Status:

**STRONGLY SUPPORTED**

---

# ACTIVE TO ABANDONED

Candidate transition:

```text
ACTIVE
→
ABANDONED
```

This transition must preserve:

* incomplete work
* reasons
* provenance
* unresolved questions
* branch history
* possible re-entry conditions

Status:

**SUPPORTED AS CANDIDATE**

---

# ABANDONED TO ACTIVE

An abandoned object may be reopened.

Candidate transition:

```text
ABANDONED
→
ACTIVE
```

Required:

* re-entry event
* actor or process
* reason
* scope
* branch
* continuity validation
* unresolved prior conditions

Boundary:

Abandoned
≠
Irreversible

Status:

**SUPPORTED AS CANDIDATE**

---

# PENDING TO HELD

Question:

Can an object be HELD before admission?

Example:

An imported object has conflicting identity and cannot be admitted.

Possible models:

## Model A

```text
PENDING
with unresolved admission conditions
```

## Model B

```text
HELD
before activation
```

Concern:

HELD may imply prior admission.

Candidate decision:

Pre-admission blockage should remain PENDING with explicit unresolved admission conditions.

HELD should apply after admission or after an explicit progression decision.

Status:

**STRONGLY SUPPORTED AS CANDIDATE**

---

# PENDING TO ABANDONED

An object may never be admitted and later be intentionally discontinued.

Candidate transition:

```text
PENDING
→
ABANDONED
```

This preserves the object and records that admission did not occur.

Status:

**SUPPORTED**

---

# BRANCH-LOCAL PROGRESSION

One object may be:

```text
Branch A:
ACTIVE

Branch B:
HELD
```

Question:

Can one object possess different progression conditions by branch?

If branch-local operations can diverge while sharing identity, then progression must be scoped to:

* object
* branch
* possibly version

Candidate form:

```text
Target: PROP-000004
Branch: BR-A
Condition: ACTIVE
```

and:

```text
Target: PROP-000004
Branch: BR-B
Condition: HELD
```

Boundary:

Object-Local
Does Not Necessarily Mean
Branch-Global

Status:

**STRONGLY SUPPORTED**

---

# MULTIPLE CONCURRENT PROGRESSION SCOPES

An object may be:

* ACTIVE for revision
* HELD for release
* DORMANT for one branch
* PENDING for admission into another program

This suggests progression may be scoped to a declared activity or runtime context.

Risk:

If every activity receives its own progression condition, the object-level progression summary may become derived rather than canonical.

Candidate reduction:

Canonical progression assertions must declare:

* target
* runtime context
* branch
* scope

Object-level summary may be derived.

Status:

**HOLD**

---

# AUTHORITY-BOUND TRANSITIONS

Some transitions may require explicit authority:

* PENDING → ACTIVE
* ACTIVE → HELD
* HELD → ACTIVE
* ACTIVE → ABANDONED
* ABANDONED → ACTIVE

Authority requirements may vary by:

* object type
* branch
* institutional policy
* consequence level
* operation
* environment

Boundary:

State Transition Recorded
≠
State Transition Authorized

Candidate decision:

Progression transition records must preserve authority basis where authority is required.

Status:

**STRONGLY SUPPORTED**

---

# AUTOMATIC TRANSITIONS

Potential automatic transitions:

* scheduled dormancy
* hold expiration
* inactivity timeout
* failed integrity check causing HOLD
* completed operation producing DORMANT
* authority expiry causing HOLD

Pressure:

Automatic transitions may silently change research progression without responsible review.

Candidate decision:

No automatic transition should occur without:

* declared rule
* triggering evidence
* event record
* scope
* responsible authority or policy
* inspection visibility

Status:

**STRONGLY SUPPORTED**

---

# HOLD EXPIRATION

A Hold may include an expiration time.

Expiration must not automatically imply resolution.

Possible outcomes:

* remain HELD
* require review
* become PENDING
* escalate
* be released by declared rule

Boundary:

Hold Expired
≠
Hold Resolved

Status:

**STRONGLY SUPPORTED**

---

# MISSING PROGRESSION CONDITION

Possible inspection results:

* NOT_ESTABLISHED
* NOT_RECORDED
* UNAVAILABLE
* CONFLICTING
* PARTIALLY_RECONSTRUCTABLE
* OUT_OF_SCOPE
* UNKNOWN

These are not progression conditions.

Boundary:

Missing Progression Record
≠
PENDING

Missing Progression Record
≠
DORMANT

Missing Progression Record
≠
INACTIVE

Status:

**STRONGLY SUPPORTED**

---

# CANDIDATE MINIMUM VOCABULARY

The strongest surviving progression candidates are:

1. PENDING
2. ACTIVE
3. HELD
4. DORMANT
5. ABANDONED

Rejected as universal progression conditions:

* INTERRUPTED
* COMPLETED
* INACTIVE
* CLOSED
* REFUSED
* FAILED
* ARCHIVED
* RELEASED
* VALIDATED
* INVALIDATED
* SUPERSEDED
* UNKNOWN

---

# CANDIDATE SEMANTIC DEFINITIONS

## PENDING

The object exists but has not yet been admitted to active progression within the declared scope.

## ACTIVE

The object is admitted and available for runtime progression within the declared scope.

## HELD

Progression is deliberately suspended within the declared scope pending resolution of explicit blocking conditions.

## DORMANT

The object is deliberately not progressing within the declared scope, without an unresolved blocking condition preventing future re-entry.

## ABANDONED

Responsible progression has been intentionally discontinued within the declared scope without claiming scoped completion.

Status:

**STRONGLY SUPPORTED**

**NOT YET FROZEN**

---

# MINIMUM PROGRESSION TRANSITIONS

Candidate transitions:

```text
PENDING → ACTIVE
PENDING → ABANDONED

ACTIVE → HELD
ACTIVE → DORMANT
ACTIVE → ABANDONED

HELD → ACTIVE
HELD → DORMANT
HELD → ABANDONED

DORMANT → ACTIVE
DORMANT → ABANDONED

ABANDONED → ACTIVE
ABANDONED → DORMANT
```

No transition is yet mandatory or universally authorized.

No transition should erase prior history.

Status:

**CANDIDATE**

---

# PROGRESSION INVARIANTS

## Invariant 1

Object existence must remain distinct from progression admission.

## Invariant 2

Creation must not automatically imply ACTIVE.

## Invariant 3

Every progression assertion must declare target and scope.

## Invariant 4

Branch-local progression must remain representable.

## Invariant 5

Every transition must be recorded through an immutable Runtime Event.

## Invariant 6

Every transition must preserve prior progression history.

## Invariant 7

Every HOLD must be grounded in one or more explicit Hold records.

## Invariant 8

A Hold expiration must not be treated as Hold resolution.

## Invariant 9

DORMANT must remain distinct from HELD.

## Invariant 10

ABANDONED must remain distinct from FAILED and DELETED.

## Invariant 11

Scoped completion must not become a universal object progression condition.

## Invariant 12

INTERRUPTED must remain an operation or execution outcome unless a type-specific object contract requires otherwise.

## Invariant 13

Missing progression information must not be converted into a progression condition.

## Invariant 14

Authority requirements must remain explicit for authority-bound transitions.

## Invariant 15

Automatic transitions must remain rule-bound, attributable, and inspectable.

## Invariant 16

Re-entry must preserve object identity and historical continuity.

Status:

**STRONGLY SUPPORTED**

**NOT YET FROZEN**

---

# ADVERSARIAL TESTS

## Test 1 — Newly Created Object

Claim:

Every new Runtime Object is ACTIVE.

Result:

Fails because imported, provisional, unresolved, and unadmitted objects may exist.

**REJECTED**

---

## Test 2 — Pending Object

Claim:

PENDING is unnecessary because HELD covers non-progression.

Result:

Fails because HELD implies deliberate suspension, while PENDING describes non-admission.

**PENDING SURVIVES**

---

## Test 3 — Dormant Object

Claim:

DORMANT is equivalent to HELD.

Result:

Fails because dormancy need not involve a blocking condition.

**DORMANT SURVIVES**

---

## Test 4 — Interrupted Analysis

Claim:

The Analysis object must become INTERRUPTED.

Result:

The operation may be interrupted while the object remains ACTIVE or becomes HELD.

**INTERRUPTED REJECTED AS UNIVERSAL OBJECT CONDITION**

---

## Test 5 — Completed Investigation

Claim:

The Investigation object becomes permanently COMPLETED.

Result:

Completion must remain scoped and may generate further inquiry or re-entry.

**COMPLETED REJECTED AS UNIVERSAL CONDITION**

---

## Test 6 — Abandoned Research

Claim:

Abandoned objects should be deleted.

Result:

Deletion destroys provenance, negative results, and reconstruction history.

**REJECTED**

---

## Test 7 — Multiple Holds

Claim:

One HELD value is sufficient.

Result:

The summary is insufficient without separate Hold identities and resolution conditions.

**FAIL**

---

## Test 8 — Branch Divergence

Claim:

One object must have one global progression condition.

Result:

Different branches may legitimately progress differently.

**REJECTED**

---

## Test 9 — Hold Expiration

Claim:

An expired Hold automatically returns the object to ACTIVE.

Result:

Expiration does not establish resolution.

**REJECTED**

---

## Test 10 — Abandoned Re-entry

Claim:

ABANDONED is terminal.

Result:

Research may be reopened with explicit continuity and re-entry records.

**REJECTED**

---

# SESSION FINDINGS

The following candidate progression vocabulary survives:

```text
PENDING
ACTIVE
HELD
DORMANT
ABANDONED
```

Primary distinctions:

PENDING
≠
HELD

HELD
≠
DORMANT

DORMANT
≠
ABANDONED

ABANDONED
≠
FAILED

INTERRUPTED
≠
Object Progression Condition

COMPLETED
≠
Universal Object Condition

Missing Progression Information
≠
Any Declared Progression Condition

Strong finding:

Progression must be scoped.

A single global condition attached to an object may be insufficient where branch, activity, or runtime-context progression diverges.

Status:

**STRONGLY SUPPORTED**

**NOT YET FROZEN**

---

# UNRESOLVED QUESTIONS

1. Is PENDING required for every Runtime Object Type?
2. Can an object remain permanently without a progression condition?
3. Is ACTIVE a canonical condition or a derived admission view?
4. Should progression scope be branch, activity, program, or all three?
5. Can one scope contain multiple simultaneous progression assertions?
6. Which assertion controls the object-level summary?
7. Is DORMANT universally distinguishable from PENDING?
8. Can an object move directly from PENDING to DORMANT?
9. Does ABANDONED require a responsible owner?
10. Can ABANDONED be declared automatically?
11. Are Hold records Runtime Objects?
12. Can Holds depend on other Holds?
13. Can a Hold be partially resolved?
14. Can an object remain ACTIVE while one operation is refused?
15. Which transitions require authority?
16. What minimum authority evidence is required?
17. How should unauthorized transitions be represented?
18. What happens when progression records conflict?
19. Should progression transitions be append-only events with derived current condition?
20. What minimum event history is required to reconstruct progression?

---

# IMPLEMENTATION DECISION

Do not create progression enums.

Do not create Hold models.

Do not create transition services.

Do not encode transition rules.

Do not encode default progression conditions.

Do not encode automatic transitions.

Do not encode object-level progression summaries.

Do not modify the frozen Platform Kernel.

Implementation remains:

**HOLD**

---

# NEXT SESSION

Begin:

**RUNTIME EVENT FOUNDATION REDUCTION 001**

Primary question:

What is the minimum immutable Runtime Event contract required to reconstruct object creation, progression transitions, relationship changes, revision, branching, evaluation, release, and reopening?

Required pressure points:

* event identity
* event type
* target
* actor or process
* time
* prior condition
* resulting condition
* scope
* branch context
* authority basis
* provenance
* outcome
* event correction
* event invalidation
* event ordering
* concurrent events
* imported events
* incomplete events
* reconstruction sufficiency

**UNKNOWN → HOLD**
