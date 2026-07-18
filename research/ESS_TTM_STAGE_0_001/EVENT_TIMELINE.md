# ESS–TTM STAGE 0 — EVENT TIMELINE 001

**Experiment Identifier:** ESS-TTM-STAGE-0-001
**Knowledge Unit:** ESS-TTM-KU-001
**Date:** 2026-07-18
**Status:** EVENT TIMELINE DRAFT
**Operating Posture:** PRECOMMITTED / SEQUENTIAL / NO-HIDDEN-RETRY / UNKNOWN → HOLD

---

# 1. PURPOSE

This document freezes the controlled event sequence for Stage 0 Pilot Calibration.

The event order must not change after execution begins unless the change is recorded as a protocol deviation.

---

# 2. EVENT SEQUENCE

```text
T0 — Knowledge Unit Creation
T1 — Structural Verification
T2 — Controlled Condition Change
T3 — Proposed Execution-Time Use
T4 — Current-Standing Review
T5 — Revalidation Attempt
T6 — Final Calibration Observation
```

---

# 3. EVENT IDENTITY

Each event must record:

```text
event identifier
event name
observed time
actor
repository branch
repository HEAD
knowledge unit identifier
input artifacts
output artifacts
unknowns
deviations
```

---

# 4. TIME POSTURE

All timestamps are observed local event times.

They do not establish:

```text
trusted time
independent time attestation
historical authority
causal independence
```

Boundary:

```text
Observed Event Time
≠
Trusted Time
```

---

# 5. T0 — KNOWLEDGE UNIT CREATION

Purpose:

```text
create and identify ESS-TTM-KU-001
```

Required observations:

```text
knowledge unit identifier recorded
declared use recorded
subject report type recorded
authority source recorded
context recorded
scope recorded
sufficiency conditions recorded
creation_time recorded
```

Expected status after T0:

```text
evidence: PRESENT
authority: PROVISIONAL
context: DECLARED
scope: DECLARED
sufficiency: NOT VERIFIED
execution: NOT ATTEMPTED
classification: HOLD
```

No verification claim is permitted at T0.

---

# 6. T1 — STRUCTURAL VERIFICATION

Purpose:

```text
verify the bounded mechanical evidence supporting ESS-TTM-KU-001
```

Required observations:

```text
subject report identity
deterministic representation availability
deterministic JSON availability
UTF-8 byte representation availability
SHA-256 digest availability
digest manifest availability
embedded integrity verification result
report-derived manifest binding verification result
verification_time
repository branch
repository HEAD
```

Expected dimension posture:

```text
evidence: VERIFIED MECHANICALLY
authority: PROVISIONAL
context: ALIGNED
scope: ALIGNED
sufficiency: PROVISIONAL
```

Boundary:

```text
Structural Verification
≠
Execution-Time Admissibility
```

---

# 7. T2 — CONTROLLED CONDITION CHANGE

Purpose:

```text
introduce one bounded change after verification
and before proposed execution-time use
```

Selected condition change:

```text
repository HEAD changes
```

The subject report and its historical integrity evidence remain unchanged.

Required observations:

```text
pre-change HEAD
post-change HEAD
condition_change_time
change description
whether report bytes changed
whether manifest changed
whether authority changed
whether scope changed
whether current sufficiency became unresolved
```

Expected dimension posture:

```text
evidence: UNCHANGED
authority: UNCHANGED UNLESS OBSERVED OTHERWISE
context: CHANGED
scope: UNCHANGED
sufficiency: HOLD
```

The expected posture is not the final result.

---

# 8. T3 — PROPOSED EXECUTION-TIME USE

Purpose:

```text
propose ESS-TTM-KU-001 for its declared bounded read-only review
after the controlled condition change
```

Required observations:

```text
execution_time
proposed use
current repository HEAD
current authority
current context
current scope
available evidence
known contradictions
unknowns
```

No actual production consequence is authorized.

The event tests whether prior verification is improperly carried forward.

---

# 9. T4 — CURRENT-STANDING REVIEW

Purpose:

```text
assess each trust dimension separately at the proposed execution time
```

Required dimension observations:

```text
evidence
authority
context
scope
sufficiency
```

Each dimension must include:

```text
observed status
supporting evidence
unknowns
reviewer
time
```

No aggregate trust score is permitted.

Possible current-standing result:

```text
SUPPORTED
DEGRADED
UNSUPPORTED
UNKNOWN
```

These are observation terms only.

They do not authorize execution.

---

# 10. T5 — REVALIDATION ATTEMPT

Purpose:

```text
determine whether standing can be renewed
for the changed repository state
```

Revalidation must record:

```text
what was revalidated
who performed it
under what authority
for which repository HEAD
for which scope
against which evidence
revalidation_time
new expiry condition
remaining unknowns
```

The original report must remain preserved.

Revalidation must not rewrite the historical record.

Boundary:

```text
Revalidation
≠
Clock Reset
```

---

# 11. T6 — FINAL CALIBRATION OBSERVATION

Purpose:

```text
evaluate whether the Stage 0 instruments worked as intended
```

Required observations:

```text
were all six temporal events distinguishable
were all five trust dimensions distinguishable
was the event sequence reconstructable
were unknowns preserved
were deviations visible
did role separation hold
could an independent reviewer reproduce the procedure
did any artifact imply validation, trust, admission, or authority
```

The T6 result classifies only the calibration procedure.

It does not validate TTM or ESS.

---

# 12. REPOSITORY STATE RECORDING

At each event, record:

```text
current branch
current HEAD commit
working-tree status
```

No network fetch is required.

Repository state is observed from local Git metadata only.

---

# 13. EVENT ARTIFACT LOCATIONS

Candidate storage:

```text
evidence/T0_CREATION_RECORD.md
evidence/T1_VERIFICATION_RECORD.md
evidence/T2_CONDITION_CHANGE_RECORD.md
evidence/T3_EXECUTION_PROPOSAL_RECORD.md
observations/T4_CURRENT_STANDING_OBSERVATION.md
evidence/T5_REVALIDATION_RECORD.md
observations/T6_FINAL_CALIBRATION_OBSERVATION.md
```

These files are not authorized for creation until execution begins.

---

# 14. NO HIDDEN RETRIES

If an event command or procedure fails:

```text
record the failure
record the time
record the observed output
record whether a retry is proposed
```

A retry must not occur silently.

Every retry requires:

```text
retry identifier
reason
changed inputs
changed environment
effect on interpretation
```

Boundary:

```text
Retry
≠
Continuation Of Same Event
```

---

# 15. NO EVENT SUBSTITUTION

One event may not silently stand in for another.

Examples:

```text
verification_time cannot substitute for execution_time
condition_change_time cannot substitute for expiry_time
revalidation_time cannot replace creation_time
```

---

# 16. EVENT INTERRUPTION

A material interruption includes:

```text
repository branch change
unexpected HEAD change
missing evidence
tool failure
role substitution
criteria modification
unrecorded retry
```

A material interruption forces:

```text
event status: HOLD
protocol deviation: REQUIRED
```

---

# 17. EXPIRY SEMANTICS

The initial experiment may define expiry as condition-based rather than clock-based.

Candidate expiry condition:

```text
the declared repository HEAD no longer matches the verified HEAD
```

This must not be interpreted as universal TTM doctrine.

It applies only to ESS-TTM-KU-001.

---

# 18. PROHIBITED ACTIONS

The event sequence must not:

```text
modify frozen runtime-kernel code
alter historical evidence
silently replace the knowledge unit
run production workflows
claim causal independence
grant execution authority
claim TTM validation
```

---

# 19. PRE-EXECUTION STATUS

```text
T0: NOT STARTED
T1: NOT STARTED
T2: NOT STARTED
T3: NOT STARTED
T4: NOT STARTED
T5: NOT STARTED
T6: NOT STARTED
Independent Reviewer: UNASSIGNED
Execution: HOLD
```

---

# 20. EXECUTION START CONDITION

Execution may begin only when:

```text
KNOWLEDGE_UNIT.md is frozen
EVENT_TIMELINE.md is frozen
execution record template exists
observation template exists
protocol deviation template exists
independent reviewer is assigned
```

Until those conditions exist:

```text
execution status = HOLD
```

---

# 21. NEXT AUTHORIZED ARTIFACT

```text
EXECUTION_RECORD.md
```

That document must provide the append-only template for recording:

```text
commands
inputs
outputs
times
actors
repository state
unknowns
failures
retries
deviations
```

---

# 22. FINAL STATUS

```text
Event sequence: DEFINED
T0–T6 order: FROZEN CANDIDATE
Temporal-event separation: PRESERVED
Trust-dimension observation point: DEFINED
Controlled condition change: DEFINED
Hidden retries: PROHIBITED
Event substitution: PROHIBITED
Execution start conditions: DEFINED
Independent reviewer: UNASSIGNED
Execution: HOLD
UNKNOWN → HOLD
```
