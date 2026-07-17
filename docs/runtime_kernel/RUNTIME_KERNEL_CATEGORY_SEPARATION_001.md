# RESEARCH OS — RUNTIME KERNEL CATEGORY SEPARATION 001

**Date:** 2026-07-16
**Project:** Research OS
**Development Version:** v2.0.0
**Status:** ACTIVE / CANDIDATE
**Implementation:** HOLD
**Authority:** NONE

**UNKNOWN → HOLD**

---

# PURPOSE

Separate the minimum runtime categories required to distinguish:

* what exists
* what happened
* how existing things are meaningfully connected

Primary candidates:

1. Runtime Object
2. Runtime Event
3. Runtime Relationship

No candidate is promoted or frozen in this session.

---

# OPERATING RULES

* Do not implement.
* Do not infer a global lifecycle.
* Do not collapse events into objects.
* Do not collapse relationships into object fields.
* Do not permit runtime operations to bypass canonical semantic relationships.
* Pressure test every distinction.
* Preserve reconstructability.
* Preserve backward compatibility.

---

# CATEGORY 1 — RUNTIME OBJECT

## Candidate Definition

A Runtime Object is a uniquely identifiable, durable, research-relevant entity that may possess type, state, provenance, and typed relationships and may participate in runtime progression.

A Runtime Object represents something that can remain addressable through time.

Candidate examples:

* Inquiry
* Investigation
* Observation
* Proposition
* Analysis
* Evaluation
* Interpretation
* Research Release

## Required Characteristics

A Runtime Object should be:

* uniquely identifiable
* independently addressable
* inspectable
* state-bearing
* provenance-bearing
* relationship-capable
* historically reconstructable

## Boundary

Runtime Object
≠
Runtime Event

Runtime Object
≠
Runtime Relationship

Runtime Object
≠
Arbitrary Data Structure

Runtime Object
≠
Operation

Runtime Object
≠
Current Inspection View

## Pressure Test

A Runtime Object may survive multiple events.

Example:

Observation `OBS-000001`

may be:

* created
* revised
* evaluated
* related to a proposition
* invalidated
* superseded
* archived

The Observation remains the addressed object.

The events do not become the Observation.

## Candidate Reduction

An entity should qualify as a Runtime Object only when stable identity and durable addressability are required.

Status:

**CANDIDATE**

---

# CATEGORY 2 — RUNTIME EVENT

## Candidate Definition

A Runtime Event is an immutable record that a runtime-relevant occurrence happened at a specific point or interval in runtime history.

A Runtime Event records change, action, or occurrence.

Candidate examples:

* object created
* state changed
* relationship established
* relationship withdrawn
* revision declared
* evaluation completed
* branch created
* merge attempted
* release issued
* research reopened

## Required Characteristics

A Runtime Event should declare:

* event identity
* event type
* timestamp or temporal interval
* actor or process
* affected target
* prior condition where applicable
* resulting condition where applicable
* provenance
* branch or lineage context
* declared outcome

## Boundary

Runtime Event
≠
Runtime Object

Runtime Event
≠
Current State

Runtime Event
≠
Relationship

Runtime Event
≠
Command

Runtime Event
≠
Authorization

Runtime Event
≠
Proof That Change Was Valid

## Pressure Test

An event may record:

```text
OBS-000001
ACTIVE
→
HELD
```

The event establishes that a state transition was recorded.

The event does not itself become:

* the Observation
* the ACTIVE state
* the HELD state
* the reason the transition was valid

## Immutability Candidate

A Runtime Event should not be edited after recording.

Correction should occur through:

* a new corrective event
* an invalidation event
* a superseding event
* an annotation relationship

Boundary:

Correcting History
≠
Rewriting History

## Candidate Reduction

Runtime Events preserve runtime history.

They should not serve as mutable containers for current truth.

Status:

**CANDIDATE**

---

# CATEGORY 3 — RUNTIME RELATIONSHIP

## Candidate Definition

A Runtime Relationship is a typed, directed, provenance-bearing semantic connection between two addressable entities.

A Runtime Relationship represents meaning between entities.

Candidate examples:

* supports
* supported_by
* derived_from
* revises
* supersedes
* evaluates
* validates
* invalidates
* belongs_to_branch
* released_as
* responds_to
* contradicts

## Required Characteristics

A Runtime Relationship should declare:

* relationship identity
* source
* relationship type
* target
* direction
* provenance
* creation event
* status
* scope where applicable
* validity interval where applicable

## Boundary

Runtime Relationship
≠
Runtime Object

Runtime Relationship
≠
Runtime Event

Runtime Relationship
≠
Undeclared Object Field

Runtime Relationship
≠
Temporal Sequence

Runtime Relationship
≠
Causation

Runtime Relationship
≠
Symmetric Meaning

## Directionality Pressure Test

Evidence
--supports→
Proposition

Inverse navigation may expose:

Proposition
--supported_by→
Evidence

However:

supports
≠
supported_by

They are inverse navigation forms, not semantically interchangeable directions.

Boundary:

Bidirectional Navigation
≠
Semantic Symmetry

## Relationship History

A relationship may be:

* proposed
* active
* held
* invalidated
* superseded
* withdrawn
* archived

The event that creates or changes the relationship is not the relationship itself.

Example:

```text
Runtime Event:
RELATIONSHIP_ESTABLISHED

Runtime Relationship:
OBS-000001 --supports→ PROP-000004
```

## Candidate Reduction

Runtime Relationships should represent explicit semantic topology.

They must not be hidden inside untyped metadata where reconstruction and inspection become unreliable.

Status:

**CANDIDATE**

---

# THREE-CATEGORY SEPARATION

## Runtime Object

Answers:

**What durable entity is being addressed?**

## Runtime Event

Answers:

**What happened?**

## Runtime Relationship

Answers:

**How are addressable entities meaningfully connected?**

---

# MINIMUM EXAMPLE

Runtime Object:

```text
PROP-000004
Type: Proposition
State: ACTIVE
```

Runtime Object:

```text
OBS-000001
Type: Observation
State: ACTIVE
```

Runtime Relationship:

```text
OBS-000001 --supports→ PROP-000004
```

Runtime Event:

```text
EVT-000019
Type: RELATIONSHIP_ESTABLISHED
Source: OBS-000001
Target: PROP-000004
Relationship: supports
```

Reduction:

* `OBS-000001` is not the event.
* `PROP-000004` is not the relationship.
* `supports` is not proof that the proposition is valid.
* `EVT-000019` records that the relationship was established.
* The Platform Kernel preserves the canonical relationship.
* The Runtime Kernel records the progression that produced it.

---

# PLATFORM / RUNTIME RESPONSIBILITY

## Platform Kernel

Responsible for representing:

* object identity
* object type
* current object state
* canonical semantic relationships
* durable provenance references
* inspectable graph topology

## Runtime Kernel

Responsible for representing:

* runtime occurrences
* progression
* transition attempts
* branch operations
* revision operations
* evaluation operations
* release and reopening operations
* event history

Boundary:

Runtime Kernel
≠
Canonical Semantic Graph Owner

Platform Kernel
≠
Runtime Progression Controller

---

# INITIAL INVARIANTS

## Invariant 1

Every Runtime Event must possess a distinct identity from every affected Runtime Object.

## Invariant 2

No Runtime Relationship may exist without explicit source, type, and target.

## Invariant 3

No event record may be treated as the current state of an object without reconstruction or projection.

## Invariant 4

No relationship may be inferred solely from temporal ordering.

## Invariant 5

Inverse navigation must not collapse semantic direction.

## Invariant 6

Runtime progression must not bypass canonical Platform Kernel relationship services.

## Invariant 7

Historical events must remain inspectable after state changes, invalidation, supersession, withdrawal, or archival.

## Invariant 8

Deleting or rewriting historical events is not an acceptable correction mechanism.

Status:

**CANDIDATE INVARIANTS**

**NOT FROZEN**

---

# ADVERSARIAL TESTS

## Test 1 — Object Mistaken for Event

Claim:

“Validation is a Runtime Event.”

Pressure:

Validation may also require a durable Evaluation object containing target, criteria, evidence, scope, method, result, and limitations.

Result:

Validation may produce an event, but the complete evaluation record may require an object.

**HOLD**

## Test 2 — Event Mistaken for State

Claim:

“The latest state-change event is the object state.”

Pressure:

Events may be missing, duplicated, invalidated, unordered, imported, or only partially reconstructed.

Result:

Event history may derive or support state, but event existence alone is not sufficient to assert current state.

**HOLD**

## Test 3 — Relationship Mistaken for Metadata

Claim:

“Evidence IDs can simply be stored in a proposition field.”

Pressure:

This weakens directionality, provenance, relationship status, inverse navigation, scope, and historical reconstruction.

Result:

Research-significant semantic relationships should remain explicit and typed.

**STRONGLY SUPPORTED**

## Test 4 — Event Mistaken for Relationship

Claim:

“A relationship-established event is the relationship.”

Pressure:

The event records establishment. The relationship may persist, become invalidated, be superseded, or be withdrawn through later events.

Result:

Event and relationship remain distinct.

**STRONGLY SUPPORTED**

## Test 5 — Relationship Mistaken for Causation

Claim:

“If Analysis B followed Observation A, then A caused B.”

Pressure:

Temporal sequence alone does not establish semantic derivation or causation.

Result:

Temporal Order
≠
Causation

**STRONGLY SUPPORTED**

---

# SESSION FINDINGS

The following separation currently survives:

```text
Runtime Object
= durable addressable entity

Runtime Event
= immutable record of occurrence

Runtime Relationship
= typed semantic connection
```

This separation supports:

* graph-native representation
* object-local state
* runtime history
* reverse reconstruction
* branching
* revision
* supersession
* explicit semantic topology
* inspection

Status:

**STRONGLY SUPPORTED**

**NOT YET FROZEN**

---

# UNRESOLVED QUESTIONS

1. Must every Runtime Event reference at least one Runtime Object?
2. Can Runtime Events relate directly to other Runtime Events?
3. Are Runtime Relationships themselves Runtime Objects?
4. Should relationships possess independent durable identities?
5. Can relationships carry their own state?
6. Is relationship removal represented as deletion, withdrawal, invalidation, or supersession?
7. Is current object state stored directly or derived from event history?
8. Which layer owns relationship status?
9. Can one event affect multiple branches?
10. Can an event exist before its target object is admitted?
11. Can imported events be trusted without verified provenance?
12. What minimum event data is required for backward reconstruction?

---

# IMPLEMENTATION DECISION

Do not create models.

Do not create services.

Do not encode event types.

Do not encode relationship types.

Do not encode object-state transitions.

Do not alter the frozen Platform Kernel.

Implementation remains:

**HOLD**

---

# NEXT SESSION

Begin:

**RUNTIME OBJECT IDENTITY AND CONTINUITY SEPARATION 001**

Primary question:

What must remain stable for a Runtime Object to preserve identity across revision, state change, branching, invalidation, supersession, release, and reopening?

Required pressure points:

* identity vs version
* identity vs content
* revision vs replacement
* branch-local identity
* cross-branch identity
* imported identity
* superseded identity
* invalidated identity
* archived identity
* reconstruction continuity

**UNKNOWN → HOLD**
