# ESS–TTM STAGE 0 — PREDEFINED CRITERIA 001

**Experiment Identifier:** ESS-TTM-STAGE-0-001
**Date:** 2026-07-18
**Status:** PREDEFINED CRITERIA DRAFT
**Operating Posture:** FALSIFICATION-FIRST / PRECOMMITTED / NON-ADMITTING / UNKNOWN → HOLD

---

# 1. PURPOSE

This document freezes the measurable conditions for classifying the Stage 0 Pilot Calibration outcome.

The criteria must be established before experiment execution begins.

No criterion may be altered after execution begins without a documented protocol deviation.

---

# 2. CLASSIFICATION STATES

The Stage 0 outcome must be classified as exactly one of:

```text
PASS
PARTIAL
FAIL
HOLD
```

These classifications apply only to the calibration instruments and procedure.

They do not classify TTM or ESS as valid or invalid.

---

# 3. PASS

Stage 0 may be classified as PASS only if every required condition below is satisfied.

## 3.1 Temporal Event Separation

The instruments must record separately:

```text
creation_time
verification_time
condition_change_time
expiry_time
execution_time
revalidation_time
```

PASS requires:

```text
all six fields exist
all six meanings are distinguishable
no event is silently substituted for another
unknown events remain explicitly unknown
```

## 3.2 Trust-Dimension Separation

The instruments must assess separately:

```text
evidence
authority
context
scope
sufficiency
```

PASS requires:

```text
all five dimensions are represented independently
no single aggregate score replaces them
a change in one dimension does not automatically alter the others
```

## 3.3 Knowledge-Unit Identity

PASS requires both reviewers to identify the same bounded knowledge unit from the experiment record.

The knowledge unit must not change during execution without a protocol deviation.

## 3.4 Event-Sequence Reconstruction

PASS requires both reviewers to reconstruct the controlled event sequence in the same order from the preserved records.

Permitted differences:

```text
wording
formatting
non-material interpretation
```

Material differences must be recorded and resolved.

## 3.5 Historical Integrity Versus Current Standing

PASS requires reviewers to distinguish:

```text
historical evidence remains intact
```

from:

```text
current use remains sufficiently supported
```

Historical integrity must not automatically produce current admissibility.

## 3.6 Verification Versus Execution-Time Use

PASS requires reviewers to distinguish:

```text
prior verification
```

from:

```text
standing at the proposed execution time
```

A prior successful verification must not be treated as execution authority.

## 3.7 Renewal Semantics

PASS requires revalidation to document:

```text
what was revalidated
who performed it
under what authority
for which scope
until what time or condition
```

A timestamp reset alone is insufficient.

## 3.8 Unknown Preservation

PASS requires every unresolved condition to remain visible.

No unknown may be silently converted into:

```text
valid
invalid
approved
rejected
trusted
authorized
```

## 3.9 Protocol-Deviation Visibility

PASS requires all deviations to be recorded with:

```text
time
description
reason
affected artifact
effect on interpretation
```

## 3.10 Role Separation

PASS requires:

```text
framework owner identified
Research OS operator identified
methodological reviewer identified
independent outcome reviewer assigned
conflicts declared
```

The independent reviewer must not be the framework owner or Research OS operator.

## 3.11 Reproducibility

PASS requires an independent reviewer to follow the same documented procedure and reach a materially comparable classification of the instrument behavior.

Exact wording need not match.

The evidence basis must be traceable.

## 3.12 Claim Discipline

PASS requires the final result to avoid claims that Stage 0 proves:

```text
TTM validity
ESS validity
causal independence
truth
authority
production readiness
```

---

# 4. PARTIAL

Stage 0 may be classified as PARTIAL when:

```text
the core procedure executes
most required observations are preserved
one or more non-fatal deficiencies remain
the deficiencies are visible and bounded
```

Examples:

```text
one optional temporal event remains unobserved
one Python or document instrument requires manual interpretation
reviewers agree on the sequence but disagree on one dimension
revalidation fields are complete but difficult to use consistently
a procedural weakness exists without invalidating all observations
```

PARTIAL requires:

```text
no hidden deviation
no collapsed unknown
no false validation claim
a documented correction path
```

PARTIAL does not authorize progression automatically.

---

# 5. FAIL

Stage 0 must be classified as FAIL if any critical failure occurs.

Critical failures include:

```text
temporal events cannot be separated
trust dimensions collapse into one score
reviewers cannot identify the same knowledge unit
the event sequence cannot be reconstructed
historical integrity is treated as current sufficiency
prior verification is treated as execution authority
renewal is represented only by resetting time
unknowns are silently resolved
protocol deviations are omitted
experiment data is altered without record
criteria are changed after execution without deviation
the independent reviewer is not independent
the result claims TTM or ESS was validated
```

A FAIL result must be preserved.

It must not be rewritten as PARTIAL for convenience.

---

# 6. HOLD

Stage 0 must be classified as HOLD when the outcome cannot yet be responsibly classified.

HOLD conditions include:

```text
independent reviewer remains unassigned
required evidence is missing
experiment records are incomplete
conflicts of interest are unresolved
reviewer disagreement remains undisposed
repository or artifact identity is uncertain
protocol deviation impact is unknown
execution sequence is interrupted materially
```

HOLD is not failure.

HOLD means evidence is insufficient for classification.

---

# 7. REQUIRED EVIDENCE FOR CLASSIFICATION

No final classification may be issued without:

```text
PROTOCOL.md
ROLE_DECLARATIONS.md
PREDEFINED_CRITERIA.md
KNOWLEDGE_UNIT.md
EVENT_TIMELINE.md
EXECUTION_RECORD.md
OBSERVATIONS.md
PROTOCOL_DEVIATIONS.md
INDEPENDENT_REVIEW.md
STAGE_0_CALIBRATION_RESULT.md
```

Missing required artifacts force HOLD.

---

# 8. MATERIAL AGREEMENT

Two reviewers materially agree when they independently identify the same:

```text
knowledge unit
event order
dimension changes
unknowns
deviations
classification basis
```

They may use different language.

Agreement of conclusion without agreement of evidence basis is insufficient.

---

# 9. DISAGREEMENT HANDLING

A reviewer disagreement must record:

```text
disputed point
each reviewer’s interpretation
supporting evidence
whether the dispute affects classification
proposed disposition
```

If the disagreement affects classification and remains unresolved:

```text
final state = HOLD
```

---

# 10. NO MAJORITY OVERRIDE

The experiment does not use majority voting to resolve evidence disputes.

```text
More reviewers agreeing
≠
Evidence resolved
```

The evidence basis must be inspected directly.

---

# 11. NO AGGREGATE TRUST SCORE

No Stage 0 instrument may produce one combined trust score as the authoritative result.

The five dimensions must remain separately visible.

A combined display may be explored later, but it cannot replace partial evidence.

---

# 12. NO AUTOMATIC ADMISSION

No PASS classification means the knowledge unit is:

```text
admitted
approved
trusted
authorized
executable
```

Boundary:

```text
Calibration PASS
≠
Execution Permission
```

---

# 13. NO CAUSAL-INDEPENDENCE CLAIM

Stage 0 may observe source declarations and lineage information.

It cannot prove causal independence merely through:

```text
multiple records
multiple reviewers
external review
agreement
temporal alignment
```

Boundary:

```text
Observed Separation
≠
Causal Independence Proven
```

---

# 14. CHANGE CONTROL

After execution begins, any criterion change requires:

```text
protocol deviation identifier
original criterion
revised criterion
reason
author
time
impact assessment
reviewer acknowledgment
```

The original criterion remains preserved.

---

# 15. INITIAL CLASSIFICATION POSTURE

Before execution:

```text
classification: HOLD
reason: execution not begun and independent reviewer unassigned
```

---

# 16. AUTHORIZED NEXT ARTIFACT

```text
KNOWLEDGE_UNIT.md
```

That document must freeze:

```text
the exact synthetic knowledge unit
its declared use
its evidence
its authority source
its context
its scope
its sufficiency conditions
its temporal fields
its exclusion boundaries
```

---

# 17. FINAL STATUS

```text
PASS criteria: PREDEFINED
PARTIAL criteria: PREDEFINED
FAIL criteria: PREDEFINED
HOLD criteria: PREDEFINED
Required evidence: PREDEFINED
Reviewer agreement rule: PREDEFINED
Disagreement rule: PREDEFINED
Aggregate trust score: PROHIBITED
Automatic admission: PROHIBITED
Causal independence claim: PROHIBITED
Execution: HOLD
Current classification: HOLD
UNKNOWN → HOLD
```
