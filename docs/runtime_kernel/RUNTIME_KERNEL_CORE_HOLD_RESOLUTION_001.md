# RESEARCH OS — RUNTIME KERNEL CORE HOLD RESOLUTION 001

**Date:** 2026-07-17
**Project:** Research OS
**Development Version:** v2.0.0
**Status:** ACTIVE / HOLD RESOLUTION
**Implementation:** HOLD
**Authority:** NONE

**UNKNOWN → HOLD**

---

# PURPOSE

Resolve the three core HOLD items identified during the consolidated architecture pressure test:

1. New-object identity threshold
2. Canonical treatment of unauthorized recorded events
3. Explicit control rule for conflicting progression assertions

Primary question:

**Can these three issues be resolved without weakening identity continuity, authority separation, conflict visibility, historical immutability, or reconstruction?**

This session does not authorize implementation or architecture freeze.

---

# PREREQUISITE

Runtime Kernel Consolidated Architecture Pressure Test 001 recorded:

* 52 PASS
* 5 PASS WITH QUALIFICATION
* 3 HOLD
* 3 prohibited architectural patterns confirmed as FAIL

The unresolved HOLD items were:

## HOLD 1

What semantic change requires a new Runtime Object identity rather than a new version?

## HOLD 2

How does an unauthorized but recorded event affect canonical projected state?

## HOLD 3

Under what explicit rule do conflicting progression assertions produce or preserve HOLD?

---

# OPERATING RULES

* Do not implement.
* Do not erase recorded events.
* Do not allow unauthorized events to establish canonical state.
* Do not treat every semantic change as a new object.
* Do not preserve identity when referent or semantic role has changed.
* Do not resolve conflict by silent ordering.
* Do not convert uncertainty into false precision.
* Preserve branch and scope.
* Preserve correction and invalidation history.
* Preserve explicit authority boundaries.
* Freeze only what survives adversarial testing.

---

# HOLD 1 — NEW-OBJECT IDENTITY THRESHOLD

## Primary Question

When does change preserve Runtime Object identity, and when must a new Runtime Object identity be created?

---

# IDENTITY CONTINUITY BASIS

Runtime Object identity may remain stable only when the following continuity basis remains established:

1. same enduring referent
2. same semantic object type
3. same declared object purpose
4. compatible semantic role
5. reconstructable predecessor lineage
6. explicit continuity declaration
7. no unresolved identity conflict
8. no prohibited identity transfer

Failure of one condition does not always force new identity.

Failure of the enduring referent or semantic role is stronger than failure of wording, metadata, or representation.

Status:

**STRONGLY SUPPORTED**

---

# IDENTITY-PRESERVING CHANGE

A change may preserve Runtime Object identity when:

* wording is corrected
* formatting changes
* metadata is repaired
* explanation is expanded
* provenance is strengthened
* evidence references are added
* uncertainty is clarified
* scope is narrowed without changing the enduring referent
* method detail is corrected without replacing the represented entity
* representation changes while the same semantic object remains addressable

Required response:

* preserve object identity
* create a new immutable version where representation changed
* record revision event
* preserve predecessor version
* record semantic-impact assessment

Status:

**STRONGLY SUPPORTED**

---

# NEW-OBJECT-REQUIRED CHANGE

A new Runtime Object identity is required when any of the following is established:

## Rule 1 — Referent Change

The object now refers to a different entity, phenomenon, question, claim, investigation, interpretation, or release target.

Example:

```text
Original:
Stability of System A

Changed:
Stability of System B
```

Result:

**NEW OBJECT REQUIRED**

---

## Rule 2 — Semantic Type Change

The object would need to become a different semantic object type.

Example:

```text
Observation
→
Interpretation
```

Result:

Create a new Interpretation object related to the Observation.

**NEW OBJECT REQUIRED**

---

## Rule 3 — Incompatible Claim Change

The revised assertion cannot coexist as a representation of the same proposition without creating contradiction inside one identity.

Example:

```text
The system remained stable.
```

changed to:

```text
The system did not remain stable.
```

Result:

Create a new Proposition identity.

Preserve an explicit relationship such as:

* contradicts
* corrects
* supersedes_within_scope
* arose_from_revision_of

**NEW OBJECT REQUIRED**

---

## Rule 4 — Purpose Replacement

The object’s declared research purpose changes so substantially that it becomes independently addressable.

Example:

```text
Evaluation of safety criteria
```

changed to:

```text
Authorization decision for deployment
```

Result:

Evaluation and Authorization remain distinct objects.

**NEW OBJECT REQUIRED**

---

## Rule 5 — Independent Addressability

The changed result must be cited, evaluated, related, released, or superseded independently from the predecessor.

Result:

**NEW OBJECT REQUIRED**

---

## Rule 6 — Branch-Incompatible Continuity

A branch-local change creates an independently progressing semantic entity with its own state, relationships, Evaluations, or release history.

Result:

Create a new branch-local Runtime Object identity and preserve:

```text
branched_from
```

or:

```text
derived_from
```

**NEW OBJECT REQUIRED**

---

## Rule 7 — Explicit Replacement

The actor or process declares that the new entity replaces rather than revises the predecessor.

Result:

New identity plus explicit replacement or supersession relationship.

**NEW OBJECT REQUIRED**

---

# IDENTITY-PRESERVING DEFAULT

Where the change does not trigger a new-object-required rule, preserve Runtime Object identity and create a new immutable version.

Candidate default:

```text
Same enduring referent
+
same semantic type
+
same object purpose
+
compatible semantic role
=
identity preserved
```

Boundary:

Identity Preserved
≠
No Material Change

Status:

**STRONGLY SUPPORTED**

---

# IDENTITY UNCERTAINTY

Where the continuity basis cannot be established, the system must not choose silently.

Candidate inspection result:

```text
Identity Continuity:
UNRESOLVED
```

Candidate progression response:

```text
Progression Decision:
HOLD
```

The HOLD must identify:

* disputed continuity dimensions
* predecessor
* candidate successor
* branch
* scope
* evidence required
* responsible resolver
* authority where required

Boundary:

Continuity Unknown
≠
Identity Preserved

Continuity Unknown
≠
New Identity Automatically

Status:

**STRONGLY SUPPORTED**

---

# IDENTITY RESOLUTION RULE

Candidate decision:

A new Runtime Object identity is mandatory when:

```text
referent changes
OR
semantic type changes
OR
claim becomes incompatible
OR
purpose is replaced
OR
independent addressability is required
OR
branch continuity becomes semantically incompatible
OR
replacement is explicitly declared
```

Otherwise:

```text
preserve identity
+
create immutable version
+
record revision
```

Where uncertain:

```text
UNKNOWN → HOLD
```

Status:

**RESOLVED CANDIDATE**

---

# HOLD 1 ADVERSARIAL TESTS

## Test 1 — Typographical Correction

Same identity, new version.

**PASS**

## Test 2 — Narrowed Scope

Same referent and purpose remain.

Same identity may be preserved with new version and explicit scope change.

**PASS WITH QUALIFICATION**

## Test 3 — Meaning Reversal

Incompatible claim.

New object required.

**PASS**

## Test 4 — Observation Recast as Interpretation

Semantic type changed.

New object required.

**PASS**

## Test 5 — Branch Alternative with Independent Evaluation

Independent addressability and branch-local progression required.

New object required.

**PASS**

## Test 6 — Missing Continuity Evidence

Neither preservation nor replacement may be asserted.

HOLD.

**PASS**

## Test 7 — Explicit Successor

New identity plus supersession relationship.

**PASS**

---

# HOLD 1 RESOLUTION

Identity threshold status:

**RESOLVED AS CANDIDATE RULE**

Remaining qualification:

The semantic-impact assessor and authority for declaring continuity remain unfrozen.

Implementation remains:

**HOLD**

---

# HOLD 2 — UNAUTHORIZED RECORDED EVENT EFFECT

## Primary Question

How should a recorded event affect canonical projected state when the event lacks required authority?

---

# EVENT RECORDING BOUNDARY

A Runtime Event may be historically valid as a record even when the asserted operation was unauthorized.

Example:

```text
EVT-000210

Type:
PROGRESSION_TRANSITIONED

Target:
PROP-000004

Asserted Transition:
HELD → ACTIVE

Authority:
NOT ESTABLISHED
```

The event establishes:

* the transition was attempted or asserted
* the record exists
* the actor or process acted
* authority was absent or unresolved

The event does not establish:

* canonical transition validity
* current canonical progression
* permission
* admissibility
* lawful consequence

Boundary:

Event Recorded
≠
Transition Admitted

Status:

**STRONGLY SUPPORTED**

---

# EVENT EFFECT CLASSIFICATION

Every authority-relevant event should distinguish:

## Recorded Occurrence

What was attempted, asserted, or observed.

## Admissibility Result

Whether the event satisfies structural and semantic admission requirements.

## Authority Result

Whether required authority was valid and applicable.

## Canonical Effect

Whether the event changes canonical projected state.

These must remain separately inspectable.

Status:

**STRONGLY SUPPORTED**

---

# UNAUTHORIZED EVENT CANONICAL RULE

Candidate rule:

An event requiring authority must not alter canonical projected state unless authority is established within the required scope, target, environment, and effective time.

Therefore:

```text
Recorded Event
+
Authority Not Established
=
Historical Record Preserved
+
Canonical Effect Denied
```

Status:

**STRONGLY SUPPORTED**

---

# UNAUTHORIZED EVENT RESULT

Candidate authority result:

* AUTHORIZED
* UNAUTHORIZED
* AUTHORITY_UNRESOLVED
* AUTHORITY_EXPIRED
* AUTHORITY_REVOKED
* AUTHORITY_OUT_OF_SCOPE
* AUTHORITY_NOT_REQUIRED

Exact vocabulary remains unfrozen.

Canonical treatment:

## AUTHORIZED

Event may be admitted subject to all other rules.

## UNAUTHORIZED

Event remains recorded but has no canonical state-changing effect.

## AUTHORITY_UNRESOLVED

Event remains recorded.

Canonical effect remains HOLD.

## AUTHORITY_EXPIRED

Event remains recorded.

Canonical effect denied.

## AUTHORITY_REVOKED

Event remains recorded.

Canonical effect denied unless revocation was not effective at event time.

## AUTHORITY_OUT_OF_SCOPE

Event remains recorded.

Canonical effect denied for the asserted scope.

Status:

**STRONGLY SUPPORTED**

---

# ATTEMPTED EFFECT VS CANONICAL EFFECT

An unauthorized event may still have real-world consequences outside the runtime.

Example:

An actor releases material without authority.

The runtime should represent:

* release attempt
* external occurrence
* unauthorized status
* canonical release not established
* possible consequence record
* corrective or containment response

Boundary:

Canonical Effect Denied
≠
No External Consequence Occurred

Status:

**STRONGLY SUPPORTED**

---

# UNAUTHORIZED EVENT AND CURRENT STATE

Canonical current state must be derived only from events that are:

* structurally admissible
* semantically applicable
* not invalidated
* correctly scoped
* authority-valid where authority is required
* temporally applicable
* branch-applicable

Unauthorized events remain visible in event history but are excluded from canonical state projection.

Status:

**STRONGLY SUPPORTED**

---

# AUTHORITY-UNRESOLVED EVENT

Where authority cannot yet be determined:

```text
Authority Result:
UNRESOLVED
```

The event must not alter canonical projected state.

Candidate control response:

```text
Authority Review:
HOLD
```

The object progression condition does not necessarily become HELD automatically unless a separate control decision establishes that effect.

Boundary:

Authority HOLD
≠
Object Progression HOLD Automatically

Status:

**STRONGLY SUPPORTED**

---

# UNAUTHORIZED EVENT CORRECTION

If authority evidence is later discovered:

* do not edit the original event
* create an authority-resolution event or Evaluation
* preserve the authority evidence
* recompute canonical projection
* preserve prior unresolved state

If the authority later becomes valid retroactively, the effective-time rule must be explicit.

Boundary:

Later Authority Evidence
≠
Silent Historical Rewrite

Status:

**STRONGLY SUPPORTED**

---

# RETROACTIVE AUTHORITY

Pressure:

Can authority be granted after an event and retroactively admit its effect?

Candidate rule:

Retroactive authority is not assumed.

It must explicitly declare:

* target event
* permitted retroactive effect
* effective-from time
* scope
* issuing authority
* legal or institutional basis
* consequences
* limitations

Without explicit retroactive authority:

```text
later authorization
≠
earlier event authorized
```

Status:

**STRONGLY SUPPORTED**

---

# UNAUTHORIZED EVENT INVALIDATION

An unauthorized event need not be invalidated merely because it lacked authority.

The event may accurately record an unauthorized occurrence.

Invalidation is appropriate only when the event record itself is false, malformed, inadmissible, corrupted, or incorrectly scoped.

Boundary:

Unauthorized Occurrence
≠
Invalid Event Record

Status:

**STRONGLY SUPPORTED**

---

# HOLD 2 ADVERSARIAL TESTS

## Test 1 — Unauthorized ACTIVE Transition

Event recorded.

Canonical state remains unchanged.

**PASS**

## Test 2 — Authority Unknown

Event recorded.

Canonical projection excludes the asserted effect pending review.

**PASS**

## Test 3 — Authority Expired Before Event

Canonical effect denied.

**PASS**

## Test 4 — Valid Authority Discovered Later

Authority-resolution event recorded.

Projection may be recomputed according to explicit effective-time rules.

**PASS WITH QUALIFICATION**

## Test 5 — Unauthorized External Release

External occurrence preserved.

Canonical Research Release remains unestablished.

**PASS**

## Test 6 — Unauthorized Event Deleted

Rejected.

Historical record must remain.

**PASS**

## Test 7 — Unauthorized Event Automatically Invalidated

Rejected unless the event record itself is invalid.

**PASS**

---

# HOLD 2 RESOLUTION

Candidate canonical rule:

```text
Unauthorized or authority-unresolved events
remain immutable historical records
but do not alter canonical projected state.
```

A separate authority-resolution record may later change projection eligibility.

Status:

**RESOLVED AS CANDIDATE RULE**

Implementation remains:

**HOLD**

---

# HOLD 3 — CONFLICTING PROGRESSION ASSERTION RULE

## Primary Question

When conflicting progression assertions exist within the same target, branch, scope, and runtime context, what control response is required?

---

# PROGRESSION CONFLICT DEFINITION

A progression conflict exists when two or more admissible progression assertions:

* address the same target
* apply to overlapping branch and scope
* apply within overlapping effective time
* assert incompatible progression conditions
* cannot be ordered or reconciled through valid correction, invalidation, or supersession

Example:

```text
Assertion A:
ACTIVE

Assertion B:
HELD
```

Status:

**STRONGLY SUPPORTED**

---

# NON-CONFLICTING DIFFERENCE

Different progression assertions are not conflicting when they differ by:

* branch
* runtime context
* scope
* activity
* effective time
* version
* authority domain

Example:

```text
Branch A:
ACTIVE

Branch B:
HELD
```

Result:

No conflict.

Status:

**STRONGLY SUPPORTED**

---

# CONFLICT DETECTION REQUIREMENTS

A conflict assessment must compare:

1. target
2. branch
3. scope
4. runtime context
5. effective interval
6. progression condition
7. event admissibility
8. authority validity
9. invalidation status
10. correction or supersession history

Boundary:

Different Values
≠
Conflict Automatically

Status:

**STRONGLY SUPPORTED**

---

# CONFLICTED PROJECTION

Where an unresolved progression conflict exists, the runtime must not project one conflicting condition as canonical.

Candidate inspection result:

```text
Progression Reconstruction:
CONFLICTING
```

`CONFLICTING` remains an inspection or reconstruction result.

It is not a progression condition.

Status:

**STRONGLY SUPPORTED**

---

# CONTROL RESPONSE

Candidate rule:

An unresolved progression conflict blocks consequential progression within the affected scope.

The control result is:

```text
Control Decision:
HOLD
```

This HOLD must be represented through an explicit Hold record.

It must not silently overwrite the conflicting progression assertions.

Boundary:

Conflict Detected
≠
Progression Condition HELD Automatically

Conflict Detected
→
Explicit Control HOLD Required

Status:

**STRONGLY SUPPORTED**

---

# CONFLICT HOLD RECORD

The conflict Hold should declare:

* hold identity
* target
* branch
* scope
* conflicting assertions
* conflicting events
* conflict basis
* detected time
* detector
* blocked operations
* resolution requirements
* authority
* release conditions
* expiration rule if any

The conflicting assertions remain preserved.

Status:

**STRONGLY SUPPORTED**

---

# EFFECT OF CONFLICT HOLD

The conflict Hold blocks:

* promotion
* release
* canonical transition dependent on progression
* authority-dependent consequence
* merge selection where progression is material
* automatic re-entry

It does not necessarily block:

* inspection
* reconstruction
* Evaluation
* provenance repair
* conflict analysis
* branch creation
* corrective events

Boundary:

Progression HOLD
≠
Total System Halt

Status:

**STRONGLY SUPPORTED**

---

# CONFLICT HOLD RELEASE

A conflict Hold may be released only when:

* conflicting assertion is invalidated
* correction establishes one assertion
* scope distinction removes overlap
* effective-time ordering is established
* valid supersession resolves the conflict
* authority decision selects one assertion within scope
* merge creates an explicit resulting progression assertion
* conflict is accepted as branch divergence through new branch separation

Release must preserve:

* resolution basis
* evidence
* actor or process
* authority
* release event
* resulting projection
* remaining unresolved conflicts

Status:

**STRONGLY SUPPORTED**

---

# CONFLICT AND BRANCH CREATION

A same-scope conflict may be resolved by separating incompatible progression paths into different branches.

Example:

```text
Original Scope:
CONFLICTING

Resolution:
Create Branch A → ACTIVE
Create Branch B → HELD
```

This does not erase the original conflict.

It records a topology change that makes both assertions independently coherent.

Status:

**STRONGLY SUPPORTED**

---

# CONFLICT AND AUTHORITY

An authority decision may select one progression assertion for a declared operational scope.

This does not prove the other assertion false.

Boundary:

Operational Selection
≠
Semantic Resolution

Status:

**STRONGLY SUPPORTED**

---

# CONFLICT AND EVENT ORDER

A later recorded event does not resolve conflict unless:

* effective ordering is established
* earlier assertion is superseded, corrected, or invalidated
* scope remains the same
* authority is valid
* the transition is admissible

Boundary:

Later Recorded
≠
Conflict Resolved

Status:

**STRONGLY SUPPORTED**

---

# CONFLICT AND MISSING HISTORY

Where conflict may result from incomplete history:

```text
Reconstruction:
PARTIAL

Progression:
CONFLICTING

Control:
HOLD
```

The Hold remains until sufficient history establishes a safe projection or an authorized scoped decision is made.

Status:

**STRONGLY SUPPORTED**

---

# HOLD 3 ADVERSARIAL TESTS

## Test 1 — Different Branches

No conflict Hold required.

**PASS**

## Test 2 — Same Scope, ACTIVE and HELD

Conflict Hold required.

**PASS**

## Test 3 — Latest Event Recorded Later

No automatic resolution.

**PASS**

## Test 4 — One Event Invalidated

Conflict may resolve after projection recomputation.

**PASS**

## Test 5 — Authority Selects ACTIVE Operationally

Operational projection may become ACTIVE within authority scope.

The other assertion remains historically visible.

**PASS WITH QUALIFICATION**

## Test 6 — Branch Split

Conflict preserved and separated into branch-local assertions.

**PASS**

## Test 7 — Missing Event History

Conflict Hold remains.

**PASS**

## Test 8 — Conflict Automatically Changes Object State to HELD

Rejected.

An explicit Hold record is required.

**PASS**

---

# HOLD 3 RESOLUTION

Candidate rule:

```text
Unresolved same-target, same-branch,
overlapping-scope progression conflict
=
canonical projection CONFLICTING
+
explicit control HOLD
+
no silent state overwrite
```

Status:

**RESOLVED AS CANDIDATE RULE**

Implementation remains:

**HOLD**

---

# CROSS-RESOLUTION CONSISTENCY TEST

## Identity Uncertain

```text
Identity Continuity:
UNRESOLVED
```

Result:

Explicit progression or admission HOLD may be created.

## Unauthorized Event

```text
Authority:
UNRESOLVED or UNAUTHORIZED
```

Result:

Event preserved.

Canonical effect excluded.

A separate authority-review HOLD may exist.

## Conflicting Progression

```text
Progression Reconstruction:
CONFLICTING
```

Result:

Explicit conflict Hold blocks consequential progression.

Finding:

The three rules preserve distinct semantics:

* identity uncertainty
* authority failure
* progression conflict

They may all trigger HOLD without becoming one state or result.

Status:

**PASS**

---

# CONSOLIDATED RESOLUTION RULES

## Rule 1 — Identity

Preserve identity when enduring referent, semantic type, object purpose, and compatible semantic role remain established.

Create new identity when referent, type, incompatible claim, purpose, independent addressability, branch continuity, or explicit replacement requires it.

Where uncertain:

**HOLD**

---

## Rule 2 — Unauthorized Events

Preserve every recorded event.

Exclude unauthorized or authority-unresolved event effects from canonical state projection.

Do not erase or automatically invalidate the event.

---

## Rule 3 — Progression Conflict

Preserve every conflicting assertion.

Project the progression condition as `CONFLICTING` in inspection.

Create an explicit control Hold blocking consequential progression within the affected scope.

Do not overwrite assertions with HELD.

---

# RESOLUTION INVARIANTS

## Invariant 1

Identity must not be preserved when the enduring referent changes.

## Invariant 2

Semantic type change requires a new object.

## Invariant 3

Incompatible claims require distinct object identities.

## Invariant 4

Identity uncertainty must not be resolved silently.

## Invariant 5

Unauthorized events remain immutable historical records.

## Invariant 6

Unauthorized events must not alter canonical projected state.

## Invariant 7

Authority resolution must remain explicit and historically recorded.

## Invariant 8

Progression conflict must remain visible.

## Invariant 9

Conflict must not be resolved through record ordering alone.

## Invariant 10

Conflict-triggered HOLD requires an explicit Hold record.

## Invariant 11

A Hold must not erase the assertions that triggered it.

## Invariant 12

Operational authority selection must not be represented as semantic truth.

## Invariant 13

Branch separation may preserve incompatible progression paths.

## Invariant 14

Every resolution must remain reconstructable.

Status:

**STRONGLY SUPPORTED**

**NOT YET FROZEN**

---

# REMAINING QUALIFICATIONS

The three core HOLD items are resolved at the architectural level.

The following implementation-neutral details remain unfrozen:

1. semantic-impact classification vocabulary
2. continuity-assessment procedure
3. actor authorized to declare continuity
4. authority-result vocabulary
5. canonical projection algorithm
6. Hold record object category
7. conflict-detection service design
8. exact blocked-operation vocabulary
9. retroactive-authority policy
10. branch-splitting authority

These may be deferred if the final invariant review confirms that the architecture remains coherent without implementation detail.

---

# HOLD RESOLUTION STATUS

New-object identity threshold:
**RESOLVED AS CANDIDATE RULE**

Unauthorized recorded event effect:
**RESOLVED AS CANDIDATE RULE**

Conflicting progression assertion rule:
**RESOLVED AS CANDIDATE RULE**

Core architecture HOLD items remaining:
**NONE**

Implementation-detail questions remaining:
**YES**

Implementation authorization:
**NONE**

---

# FREEZE READINESS RECOMMENDATION

The consolidated Runtime Kernel architecture is now ready for a final invariant consistency review.

Architecture freeze should occur only if the final review confirms:

* no rule conflicts with prior reductions
* Platform Kernel ownership remains intact
* Runtime Kernel responsibility remains bounded
* authority remains separate
* inspection remains read-only
* history remains immutable
* conflicts remain visible
* partial reconstruction remains representable
* no mandatory lifecycle has been introduced
* implementation details can be deferred safely

Recommendation:

**PROCEED TO FINAL INVARIANT CONSISTENCY REVIEW**

Implementation remains:

**HOLD**

---

# NEXT SESSION

Begin:

**RUNTIME KERNEL FINAL INVARIANT CONSISTENCY REVIEW 001**

Primary question:

Do the consolidated primitives, composite semantics, ownership boundaries, pressure-test findings, and resolved HOLD rules form one coherent and non-contradictory architecture suitable for candidate freeze?

Required work:

1. Review all core primitives.
2. Review all composite semantics.
3. Review Platform Kernel ownership.
4. Review Runtime Kernel responsibility.
5. Review identity-resolution rule.
6. Review unauthorized-event rule.
7. Review progression-conflict rule.
8. Test invariant collisions.
9. Identify redundant invariants.
10. Identify missing invariants.
11. Classify safely deferred details.
12. Issue one result:

* FREEZE RECOMMENDED
* FREEZE WITH EXPLICIT DEFERRALS
* CONTINUE HOLD
* ARCHITECTURE FAIL

**UNKNOWN → HOLD**
