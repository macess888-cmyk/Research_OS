# RESEARCH OS — RUNTIME OBJECT VERSION RECORD FOUNDATION

# IDENTITY, REPRESENTATION, AND LINEAGE SEPARATION 001

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

Define the minimum immutable semantic contract for a Runtime Object Version record after separating:

1. enduring Runtime Object identity
2. version-record identity
3. schema version
4. version label
5. representation reference
6. predecessor lineage
7. multiple-origin lineage
8. branch
9. scope
10. revision
11. supersession
12. currentness
13. persistence
14. canonical projection

This session does not authorize tests, implementation, migration, persistence, registry integration, or ObjectEngine modification.

---

# PREREQUISITE

Existing Object and Version Boundary Inspection 001 established:

* existing Research Objects are mutable heterogeneous JSON dictionaries
* `ObjectEngine` assumes one currently loaded dictionary per object ID
* no immutable version contract exists
* no version identity exists
* no predecessor lineage exists
* no current-version rule exists
* no migration is authorized
* `RuntimeRecordHeader` composition is strongly supported
* generic mutable payloads are prohibited
* ObjectEngine must remain unchanged

---

# OPERATING RULES

* Do not implement.
* Do not create tests.
* Do not modify ObjectEngine.
* Do not modify existing JSON objects.
* Do not migrate application objects.
* Do not introduce persistence.
* Do not introduce a registry.
* Do not infer currentness.
* Do not infer supersession.
* Do not infer lineage from record order.
* Do not embed generic mutable content.
* Keep identity dimensions explicit.
* Freeze only the minimum contract that survives reduction.

---

# PRIMARY QUESTION

What minimum information must an immutable Runtime Object Version record contain to represent one durable version of an enduring Runtime Object without claiming:

* currentness
* supersession
* validity
* admission
* authority
* completeness
* canonical priority
* semantic equivalence
* persistence
* lineage completeness

---

# MODEL NAME CANDIDATES

## Candidate A — RuntimeObjectVersion

Advantages:

* concise
* intuitive

Problems:

* may be confused with the represented version itself
* may imply current or operational version behavior
* does not emphasize immutable record status

Result:

**REJECTED**

---

## Candidate B — RuntimeObjectVersionRecord

Advantages:

* explicitly identifies an immutable record
* distinguishes record identity from enduring object identity
* distinguishes representation from currentness
* aligns with `RuntimeEventRecord`
* supports frozen record composition

Result:

**STRONGLY SUPPORTED**

---

## Candidate C — RuntimeVersionRecord

Problems:

* under-specifies what is being versioned
* may be confused with schema or software versions

Result:

**REJECTED**

---

# MODEL NAME DECISION

Selected model name:

```text
RuntimeObjectVersionRecord
```

Definition:

A `RuntimeObjectVersionRecord` is an immutable record identifying one declared representation version of an enduring Runtime Object within explicit lineage, branch, and scope context where available.

It does not establish:

* that the representation is current
* that the representation supersedes another
* that the representation is valid
* that the representation is admitted
* that lineage is complete

Status:

**SELECTED**

---

# HEADER COMPOSITION

Every Runtime Object Version record must compose:

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

* `record_id`
* `record_category`
* `recorded_at`
* `schema_version`
* `provenance_ref`
* `external_id`

Boundary:

```text
Runtime Object Version Record
COMPOSES
Runtime Record Header
```

not:

```text
Runtime Object Version Record
INHERITS
Runtime Record Header
```

Status:

**SELECTED**

---

# RECORD CATEGORY

The composed header must declare:

```text
record_category = VERSION
```

The model must reject any header whose category is not exactly:

```text
VERSION
```

Boundary:

```text
Record Category
≠
Object Type
```

```text
Record Category
≠
Version Label
```

Status:

**SELECTED**

---

# VERSION-RECORD IDENTITY

Runtime Object Version record identity is supplied by:

```text
header.record_id
```

Do not add:

```text
version_id
```

unless a later reduction proves a distinct identity requirement.

Boundary:

```text
Version Record Identity
≠
Enduring Object Identity
```

```text
Version Record Identity
≠
Version Label
```

```text
Version Record Identity
≠
Schema Version
```

Status:

**SELECTED**

---

# ENDURING OBJECT IDENTITY

Selected field name:

```text
object_ref
```

Definition:

A local reference identifying the enduring Runtime Object to which this immutable version belongs.

Boundary:

```text
object_ref
≠
header.record_id
```

```text
object_ref
≠
representation_ref
```

```text
object_ref
≠
predecessor_ref
```

Status:

**REQUIRED**

---

# OBJECT_REF REPRESENTATION

Selected type:

```python
str
```

Requirements:

* non-empty
* not whitespace-only
* exact value preserved
* no automatic normalization
* no prefix validation
* no existence check
* no ObjectEngine lookup
* no identity migration
* no object-type inference

Reason:

No universal Runtime Object identity syntax is frozen yet.

Status:

**SELECTED**

---

# VERSION LABEL

Primary pressure:

Does every Runtime Object Version need a human-readable or sequential version label?

Possible examples:

```text
1
2
v1
draft-2
branch-a-3
```

Problems:

* labels may be branch-local
* labels may be external
* labels may imply false chronology
* labels may be confused with schema version
* imported versions may have no local label

---

# VERSION LABEL DECISION

Selected field name:

```text
version_label
```

Selected representation:

```python
str | None
```

When present:

* non-empty
* not whitespace-only
* exact value preserved
* no normalization
* no semantic-version parsing
* no ordering inference
* no uniqueness inference

When absent:

No local version label is established.

Absence does not mean:

* first version
* unversioned representation
* invalid version
* missing record identity

Status:

**OPTIONAL**

---

# SCHEMA VERSION SEPARATION

The composed header already contains:

```text
schema_version
```

This identifies the structural contract used to construct the record.

It must remain distinct from:

```text
version_label
```

and from the represented Runtime Object Version itself.

Boundary:

```text
Header Schema Version
≠
Object Version Label
```

```text
Header Schema Version
≠
Version Record Identity
```

Status:

**FROZEN SEPARATION**

---

# REPRESENTATION REQUIREMENT

A Runtime Object Version record must identify the immutable representation it describes.

Embedding a generic content dictionary is prohibited.

The foundation therefore requires an explicit representation reference.

Selected field name:

```text
representation_ref
```

Definition:

A reference identifying the immutable or independently addressable representation associated with this version record.

Status:

**REQUIRED**

---

# REPRESENTATION_REF TYPE

Selected type:

```python
str
```

Requirements:

* non-empty
* not whitespace-only
* exact value preserved
* no path interpretation
* no URI validation
* no existence check
* no persistence behavior
* no content loading
* no content hashing
* no trust inference

Boundary:

```text
representation_ref
≠
File Path Automatically
```

```text
representation_ref
≠
Content Hash
```

```text
representation_ref
≠
Object Identity
```

Status:

**SELECTED**

---

# GENERIC CONTENT PAYLOAD

Do not include:

```text
content
payload
data
metadata
representation
```

as a generic dictionary or mutable container.

Reason:

* heterogeneous object content remains outside the first foundation
* serialization remains deferred
* representation contracts may vary by object type
* generic payloads weaken reconstruction and validation

Status:

**PROHIBITED**

---

# PREDECESSOR LINEAGE

Selected field name:

```text
predecessor_ref
```

Definition:

An optional local reference identifying one directly declared predecessor Runtime Object Version record.

Selected type:

```python
str | None
```

Status:

**OPTIONAL**

---

# PREDECESSOR ABSENCE

```python
predecessor_ref = None
```

means only:

```text
No direct predecessor reference is established in this record.
```

It does not mean:

* this is the first historical version
* no predecessor exists
* lineage is complete
* the version is a root
* the version was independently created

Status:

**FROZEN**

---

# PREDECESSOR REFERENCE RULE

When present:

* must be string
* must not be empty
* must not be whitespace-only
* exact value preserved
* no existence check
* no ordering inference
* no same-object validation
* no cycle detection
* no supersession inference

Boundary:

```text
predecessor_ref
≠
superseded_version_ref
```

```text
predecessor_ref
≠
revision_authority
```

Status:

**SELECTED**

---

# MULTIPLE-ORIGIN LINEAGE

Some versions may result from:

* merge
* reconciliation
* imported composite history
* multi-source derivation

A single `predecessor_ref` cannot represent every case.

Candidate options:

1. tuple of predecessor references
2. separate lineage-origin record
3. merge record
4. specialized version subtype

---

# MULTIPLE-ORIGIN DECISION

The first foundation preserves one optional direct predecessor reference only.

Multiple-origin lineage must be represented later through:

* a dedicated merge record
* additional lineage relationships
* specialized typed records

The foundation must not introduce a generic list of predecessors.

Reason:

A tuple would prematurely freeze lineage semantics and ordering.

Status:

**SAFE DEFERRAL**

---

# DERIVATION REFERENCE

Question:

Should the record contain a separate:

```text
derived_from_ref
```

Finding:

This may overlap with predecessor, source, evidence, or merge lineage.

Status:

**DEFERRED**

---

# BRANCH REFERENCE

Selected field name:

```text
branch_ref
```

Selected type:

```python
str | None
```

Meaning:

An optional reference identifying the branch or lineage context in which this version exists.

When present:

* non-empty
* not whitespace-only
* exact value preserved
* no branch lookup
* no branch creation
* no root inference

When absent:

The record does not establish branch context.

Absence does not mean:

* root branch
* branch independence
* universal lineage

Status:

**OPTIONAL / SELECTED**

---

# SCOPE REFERENCE

Selected field name:

```text
scope_ref
```

Selected type:

```python
str | None
```

Meaning:

An optional reference identifying the scope within which the representation or lineage claim applies.

When absent:

No explicit local scope reference is established.

Absence does not imply universal scope.

Status:

**OPTIONAL / SELECTED**

---

# REVISION BOUNDARY

The version record may be produced by a revision, but it does not perform revision.

Do not include:

* `revision_number`
* `revision_action`
* `revised`
* `revision_status`

unless separately reduced.

Boundary:

```text
Runtime Object Version Record
≠
Revision Operation
```

Status:

**FROZEN**

---

# SUPERSESSION BOUNDARY

Do not include:

* `supersedes`
* `superseded_by`
* `is_superseded`
* `supersession_status`

in the first foundation.

Reason:

Supersession is scoped, typed, and separately recorded.

A later-recorded version does not automatically supersede its predecessor.

Boundary:

```text
Predecessor
≠
Superseded Version Automatically
```

Status:

**PROHIBITED FOR FOUNDATION**

---

# CURRENTNESS BOUNDARY

Do not include:

* `is_current`
* `current`
* `latest`
* `active_version`
* `canonical`
* `selected`

Currentness must be derived through later projection using:

* branch
* scope
* supersession
* invalidation
* admission
* authority
* temporal context
* reconstruction completeness

Boundary:

```text
Version Exists
≠
Version Is Current
```

Status:

**PROHIBITED**

---

# VALIDITY AND ADMISSION BOUNDARY

Do not include:

* `valid`
* `admitted`
* `approved`
* `authorized`
* `released`

These are separate Evaluation, authority, or release semantics.

Status:

**PROHIBITED**

---

# TEMPORAL DIMENSIONS

The version record already receives:

```text
header.recorded_at
```

No additional timestamp is universally required for the minimum foundation.

Possible future fields:

* authored_at
* represented_at
* effective_at
* imported_at

remain deferred.

Reason:

The first foundation records representation identity and lineage, not all temporal semantics.

Status:

**DEFERRED**

---

# MINIMUM REQUIRED FIELD SET

Selected required fields:

```python
header: RuntimeRecordHeader
object_ref: str
representation_ref: str
```

Optional fields:

```python
version_label: str | None = None
predecessor_ref: str | None = None
branch_ref: str | None = None
scope_ref: str | None = None
```

Status:

**STRONGLY SUPPORTED**

---

# FIELD ORDER

Selected field declaration order:

1. `header`
2. `object_ref`
3. `representation_ref`
4. `version_label`
5. `predecessor_ref`
6. `branch_ref`
7. `scope_ref`

Reason:

* shared record structure first
* enduring object binding second
* immutable representation third
* optional human label next
* lineage before branch and scope context

Status:

**SELECTED**

---

# MINIMUM STRUCTURAL SUFFICIENCY

The following is structurally complete:

```python
RuntimeObjectVersionRecord(
    header=valid_version_header,
    object_ref="research_os",
    representation_ref="REP-000001",
)
```

It may remain:

* unlabeled
* predecessor-unresolved
* branch-unresolved
* scope-unresolved
* not current
* not admitted
* not validated
* not persisted

Boundary:

```text
Structural Completeness
≠
Lineage Completeness
```

```text
Structural Completeness
≠
Canonical Currentness
```

Status:

**SELECTED**

---

# OBJECT AND REPRESENTATION IDENTITY COLLISION

Question:

May `object_ref` equal `representation_ref`?

Finding:

The two fields represent different semantic dimensions.

However, no universal syntax or registry exists to prove a collision.

The model should not reject equal strings automatically.

Boundary:

```text
Equal Reference Strings
≠
Proven Semantic Identity
```

Status:

**NO CROSS-FIELD EQUALITY RULE**

---

# SELF-PREDECESSOR PRESSURE TEST

Question:

Should the model reject:

```text
predecessor_ref == header.record_id
```

Finding:

Yes.

A version record cannot directly declare itself as its own predecessor without violating minimal lineage coherence.

This comparison is locally testable.

Selected rule:

```text
predecessor_ref must not equal header.record_id
```

Wrong value result:

```text
ValueError
```

Status:

**SELECTED**

---

# CROSS-OBJECT PREDECESSOR PRESSURE

Question:

Should the model verify that a predecessor belongs to the same `object_ref`?

Finding:

No registry or lookup is available.

This belongs to later lineage validation.

Status:

**DEFERRED**

---

# VERSION LABEL ORDERING

The model must not compare or order version labels.

Examples:

```text
2
10
v1
v2
draft
final
```

must remain opaque strings.

Boundary:

```text
Version Label
≠
Version Order
```

Status:

**SELECTED**

---

# REFERENCE STRUCTURAL RULE

The following fields use a non-empty exact-string rule:

* `object_ref`
* `representation_ref`
* `version_label` when present
* `predecessor_ref` when present
* `branch_ref` when present
* `scope_ref` when present

Required references:

```text
object_ref
representation_ref
```

must reject `None`.

Optional references may accept `None`.

No field is normalized.

Status:

**SELECTED**

---

# EQUALITY

Candidate rule:

Use full structural equality across all seven fields.

Same header with different representation reference:

```text
NOT EQUAL
```

Same object and representation with a different header:

```text
NOT EQUAL
```

Same header and representation with a different lineage context:

```text
NOT EQUAL
```

Status:

**SELECTED**

---

# HASHING

Use standard frozen-dataclass structural hashing.

Hashing must not establish:

* version uniqueness
* representation integrity
* semantic equivalence
* currentness
* lineage validity

Status:

**SELECTED**

---

# ORDERING

Do not support ordering.

The following must not create automatic ordering:

* header record ID
* version label
* recorded time
* predecessor reference

Boundary:

```text
Version Label Present
≠
Versions Ordered
```

Status:

**SELECTED**

---

# SERIALIZATION

Do not implement:

* `to_dict`
* `from_dict`
* JSON encoding
* content loading
* file persistence
* ObjectEngine conversion
* migration helpers

Status:

**DEFERRED**

---

# IMMUTABILITY

The future model should use:

```python
@dataclass(frozen=True)
```

No mutation methods are permitted.

Status:

**STRONGLY SUPPORTED**

---

# PRODUCTION PATH

Selected production path:

```text
models/runtime_object_version_record.py
```

Selected test path:

```text
tests/runtime/test_runtime_object_version_record.py
```

Status:

**SELECTED**

---

# IMPORT BOUNDARY

Likely permitted imports:

```python
from dataclasses import dataclass

from models.runtime_record_identity import RuntimeRecordHeader
```

No datetime import is required unless later contract expansion adds temporal fields.

No service imports are permitted.

Status:

**SELECTED**

---

# OBJECTENGINE BOUNDARY

The Runtime Object Version foundation must not:

* import ObjectEngine
* call ObjectEngine
* load JSON objects
* write JSON objects
* alter existing application IDs
* determine current application representation
* create migration adapters
* change graph construction

Status:

**FROZEN**

---

# PROHIBITED FIELDS

The first foundation must not include:

* `version_id`
* `content`
* `payload`
* `metadata`
* `data`
* `is_current`
* `latest`
* `active`
* `valid`
* `admitted`
* `approved`
* `authorized`
* `released`
* `supersedes`
* `superseded_by`
* `revision_number`
* `revision_status`
* `current_version`
* `content_hash`
* `file_path`
* `created_at`
* `modified_at`

Some may become valid through later separately reduced capabilities.

---

# CANDIDATE CONTRACT SUMMARY

## Model

```text
RuntimeObjectVersionRecord
```

## Required Fields

```python
header: RuntimeRecordHeader
object_ref: str
representation_ref: str
```

## Optional Fields

```python
version_label: str | None = None
predecessor_ref: str | None = None
branch_ref: str | None = None
scope_ref: str | None = None
```

## Header Requirement

```text
header.record_category == VERSION
```

## Version Record Identity

```text
header.record_id
```

## Generic Content

```text
PROHIBITED
```

## Currentness

```text
PROHIBITED
```

## Supersession

```text
DEFERRED
```

## Persistence

```text
DEFERRED
```

---

# SEMANTIC BOUNDARIES

```text
Version Record Identity
≠
Enduring Object Identity
```

```text
Enduring Object Identity
≠
Representation Reference
```

```text
Header Schema Version
≠
Object Version Label
```

```text
Version Label
≠
Version Order
```

```text
Predecessor
≠
Superseded Version Automatically
```

```text
Recorded Later
≠
Semantically Newer
```

```text
Version Exists
≠
Version Is Current
```

```text
Version Exists
≠
Version Is Valid
```

```text
Version Exists
≠
Version Is Admitted
```

```text
Representation Reference
≠
Representation Content
```

```text
File Path
≠
Version Identity
```

```text
Structural Reference Valid
≠
Reference Resolved
```

---

# ADVERSARIAL TEST 1 — EMBED JSON CONTENT

Finding:

Recreates mutable heterogeneous object storage.

Result:

**REJECTED**

---

# ADVERSARIAL TEST 2 — VERSION NUMBER REQUIRED

Finding:

Imported, branch-local, and externally labeled versions may not have a universal numeric sequence.

Result:

**REJECTED**

---

# ADVERSARIAL TEST 3 — PREDECESSOR REQUIRED

Finding:

Root, imported, and unresolved-lineage versions would become unrepresentable.

Result:

**REJECTED**

---

# ADVERSARIAL TEST 4 — MULTIPLE PREDECESSORS TUPLE

Finding:

Prematurely freezes merge-lineage semantics.

Result:

**DEFERRED**

---

# ADVERSARIAL TEST 5 — CURRENT BOOLEAN

Finding:

Collapses a derived scoped projection into an immutable record field.

Result:

**REJECTED**

---

# ADVERSARIAL TEST 6 — SUPERSEDES FIELD

Finding:

Supersession requires typed, scoped, separately reconstructable semantics.

Result:

**DEFERRED**

---

# ADVERSARIAL TEST 7 — CONTENT HASH REQUIRED

Finding:

Requires frozen serialization and hashing semantics not yet available.

Result:

**DEFERRED**

---

# ADVERSARIAL TEST 8 — VERSION ID FIELD

Finding:

Duplicates `header.record_id`.

Result:

**REJECTED**

---

# ADVERSARIAL TEST 9 — OBJECTENGINE LOOKUP

Finding:

Introduces service coupling and side effects.

Result:

**REJECTED**

---

# ADVERSARIAL TEST 10 — SELF PREDECESSOR

Finding:

Creates an immediate local lineage contradiction.

Result:

**REJECTED BY CONTRACT**

---

# CANDIDATE INVARIANTS

## Invariant 1

Every Runtime Object Version record composes one valid `RuntimeRecordHeader`.

## Invariant 2

The composed header category must equal `VERSION`.

## Invariant 3

Version-record identity remains `header.record_id`.

## Invariant 4

No duplicate `version_id` is permitted.

## Invariant 5

Every version record declares one enduring `object_ref`.

## Invariant 6

Every version record declares one `representation_ref`.

## Invariant 7

Object identity remains distinct from representation reference.

## Invariant 8

Version label remains optional and opaque.

## Invariant 9

Version label does not establish ordering.

## Invariant 10

Predecessor reference remains optional.

## Invariant 11

Predecessor absence does not imply historical root.

## Invariant 12

A version record must not reference itself as predecessor.

## Invariant 13

Multiple-origin lineage remains deferred.

## Invariant 14

Branch and scope remain optional and distinct.

## Invariant 15

Missing branch does not imply root branch.

## Invariant 16

Missing scope does not imply universal scope.

## Invariant 17

The model contains no generic representation payload.

## Invariant 18

The model does not determine currentness.

## Invariant 19

The model does not determine supersession.

## Invariant 20

The model does not perform revision.

## Invariant 21

The model does not infer validity, admission, authority, or release.

## Invariant 22

The model remains immutable and side-effect free.

## Invariant 23

Equality and hashing remain structural.

## Invariant 24

Ordering remains unsupported.

## Invariant 25

ObjectEngine and existing JSON objects remain unchanged.

Status:

**STRONGLY SUPPORTED**

**NOT YET FROZEN AS IMPLEMENTATION CONTRACT**

---

# UNRESOLVED QUESTIONS

The following remain open:

1. exact dataclass configuration
2. exact constructor validation order
3. exact error-message fragments
4. whether `object_ref` and `representation_ref` may be identical strings
5. whether `predecessor_ref` should require a specific Runtime Record ID syntax
6. whether `branch_ref` and `scope_ref` should use generic reference validation
7. whether version labels should accept surrounding whitespace
8. whether a representation reference may equal the header external identity
9. whether header subclasses are accepted
10. whether representation references eventually require integrity records
11. whether lineage validation should become a separate capability
12. whether specialized object-version records compose this foundation

All remain:

**HOLD**

---

# REDUCTION DECISION

Model name:
**SELECTED**

Header composition:
**SELECTED**

Record-category enforcement:
**SELECTED**

Enduring object reference:
**REQUIRED / SELECTED**

Representation reference:
**REQUIRED / SELECTED**

Version label:
**OPTIONAL / SELECTED**

Predecessor reference:
**OPTIONAL / SELECTED**

Self-predecessor prohibition:
**SELECTED**

Branch reference:
**OPTIONAL / SELECTED**

Scope reference:
**OPTIONAL / SELECTED**

Generic payload:
**PROHIBITED**

Currentness fields:
**PROHIBITED**

Supersession fields:
**DEFERRED**

Persistence:
**DEFERRED**

Implementation:
**HOLD**

---

# READINESS CHECKPOINT 2

Identity, Representation, and Lineage Separation:

**COMPLETE**

No production model was created.

No tests were created.

No ObjectEngine or JSON object behavior was changed.

No migration was performed.

No implementation authority was granted.

---

# NEXT SESSION

Begin:

**RUNTIME OBJECT VERSION RECORD FOUNDATION — IMMUTABLE CONTRACT 001**

Primary question:

What exact field types, validation order, error rules, header-category enforcement, reference validation, self-predecessor refusal, immutability, equality, hashing, and acceptance criteria must define `RuntimeObjectVersionRecord` before tests are written?

Required work:

1. freeze exact field types
2. freeze constructor shape
3. freeze dataclass configuration
4. define required-reference validation
5. define optional-reference validation
6. define header-category enforcement
7. define self-predecessor refusal
8. define validation order
9. define error behavior
10. define equality and hashing
11. define ordering prohibition
12. define explicit non-goals
13. define acceptance criteria
14. preserve implementation HOLD

**UNKNOWN → HOLD**
