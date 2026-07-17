# RESEARCH OS — APPEND-ONLY RUNTIME RECORD REGISTRY

# IDENTITY, DUPLICATE, COLLISION, AND REGISTRATION RESULT SEPARATION 001

**Date:** 2026-07-17
**Project:** Research OS
**Development Version:** v2.0.0
**Status:** ACTIVE / SEMANTIC REDUCTION
**Architecture:** RUNTIME KERNEL CANDIDATE ARCHITECTURE FROZEN
**Implementation:** HOLD
**Persistence:** HOLD
**Platform Registry Integration:** HOLD
**Authority:** VOCABULARY AND CONTRACT REDUCTION ONLY

**UNKNOWN → HOLD**

---

# PURPOSE

Define the minimum semantic contract for an in-memory append-only Runtime Record Registry after separating:

1. registry identity
2. Runtime record identity
3. supported record families
4. bare-header acceptance
5. successful registration
6. exact duplicate attempts
7. identity collisions
8. unsupported record types
9. registration results
10. missing-record lookup
11. append position
12. append-order snapshots
13. category filtering
14. registration from admission
15. registration from persistence
16. registration from canonical projection
17. registry mutation from record mutation
18. structural inspection from history reconstruction

This session does not authorize tests, implementation, persistence, serialization, application migration, Platform Registry integration, admission, authority evaluation, or canonical projection.

---

# PREREQUISITE

Existing Registry, Admission, and Storage Boundary Inspection 001 established:

* no architectural Runtime Record Registry currently exists
* Platform Registry is a service-inspection registry
* ObjectEngine loads heterogeneous application objects
* EventEngine manages mutable application event JSON
* application content storage is not a Runtime Record ledger
* registration is distinct from construction
* registration is distinct from admission
* registration is distinct from persistence
* registration is distinct from canonical projection
* registry identity uses `header.record_id`
* local identity uniqueness belongs to the registry
* exact duplicate attempts are distinct from identity collisions
* registration order is distinct from recorded-time order
* registration order is distinct from semantic order
* the first registry should remain in memory
* no existing application behavior may change

---

# OPERATING RULES

* Do not implement.
* Do not create tests.
* Do not create persistent storage.
* Do not modify Platform Registry.
* Do not modify ObjectEngine.
* Do not modify EventEngine.
* Do not migrate application content.
* Do not serialize records.
* Do not calculate admission.
* Do not calculate canonical state.
* Do not calculate active Holds.
* Do not calculate current versions.
* Do not reconstruct progression.
* Do not mutate registered records.
* Freeze only the minimum registry semantics.

---

# PRIMARY QUESTION

What minimum in-memory registry contract must support:

```text
register one supported immutable Runtime record
```

while distinguishing:

```text
new identity
exact duplicate attempt
identity collision
unsupported record type
missing lookup
append position
append-order inspection
```

without claiming:

* semantic truth
* authority
* admission
* persistence
* canonicality
* currentness
* causality
* progression
* release
* operational consequence

---

# REGISTRY CLASS NAME CANDIDATES

## Candidate A — RuntimeRegistry

Problems:

* too broad
* may imply objects, services, relationships, or application state
* may collide conceptually with Platform Registry

Result:

**REJECTED**

---

## Candidate B — RuntimeRecordRegistry

Advantages:

* explicit Runtime ownership
* explicit record ownership
* distinguishes it from Platform Registry
* broad enough to contain multiple Runtime record families

Result:

**SELECTED**

---

## Candidate C — AppendOnlyRuntimeRecordRegistry

Advantages:

* explicit append-only semantics

Problems:

* unnecessarily long
* append-only behavior belongs to the class contract
* name may become awkward in imports and tests

Result:

**REJECTED**

---

# CLASS NAME DECISION

Selected class name:

```text
RuntimeRecordRegistry
```

Definition:

A mutable in-memory container that append-registers supported immutable Runtime records under locally unique `header.record_id` values while prohibiting replacement, deletion, and semantic interpretation.

Status:

**SELECTED**

---

# PRODUCTION PATH

Selected future production path:

```text
services/runtime_record_registry.py
```

Reason:

The registry owns mutable operational behavior around immutable records.

It is not itself an immutable record model.

Status:

**SELECTED**

---

# TEST PATH

Selected future test path:

```text
tests/runtime/test_runtime_record_registry.py
```

Status:

**SELECTED**

---

# MODULE OWNERSHIP

The registry belongs under:

```text
services/
```

not:

```text
models/
```

Reason:

* it changes over time through registration
* it owns lookup behavior
* it enforces registry-level uniqueness
* it preserves append order
* it exposes read operations
* it is not an immutable value object

Boundary:

```text
Immutable Runtime Record
≠
Mutable Registry Service
```

Status:

**FROZEN DIRECTION**

---

# REGISTRY INSTANCE IDENTITY

Question:

Should each registry instance possess a separate registry identifier?

Candidate fields:

```text
registry_id
name
namespace
scope_ref
```

Finding:

The minimum in-memory capability does not require registry-instance identity.

Adding identity would introduce:

* namespace semantics
* cross-registry coordination
* persistence identity
* merge semantics
* distributed uniqueness questions

Decision:

Do not include registry-instance identity in the first capability.

Boundary:

```text
Registry Instance
≠
Registered Runtime Record
```

Status:

**DEFERRED**

---

# RECORD IDENTITY EXTRACTION

Every supported Runtime record composes:

```text
RuntimeRecordHeader
```

Registry key:

```python
record.header.record_id
```

The registry must not:

* generate record identity
* normalize record identity
* parse identity into another key
* derive identity from record content
* use object identity as registry identity
* use append position as identity

Status:

**SELECTED**

---

# REGISTRY KEY CONTRACT

Registry membership is keyed by:

```text
header.record_id
```

Boundary:

```text
Registry Key
=
Runtime Record Local Identity
```

The registry must not introduce:

* `registry_entry_id`
* `registry_record_id`
* `event_id`
* `version_id`
* `assertion_id`
* `hold_id`

Status:

**SELECTED**

---

# SUPPORTED RECORD FAMILIES

Currently implemented immutable Runtime record families:

```text
RuntimeEventRecord
RuntimeObjectVersionRecord
ProgressionAssertionRecord
HoldRecord
```

All compose one valid RuntimeRecordHeader.

Selected first supported family set:

```python
(
    RuntimeEventRecord,
    RuntimeObjectVersionRecord,
    ProgressionAssertionRecord,
    HoldRecord,
)
```

Status:

**SELECTED**

---

# CLOSED FAMILY SET

The first registry must use explicit supported classes.

It must not accept arbitrary objects based only on:

```text
hasattr(record, "header")
```

Reason:

Duck typing could admit:

* mutable objects
* application objects
* accidental wrappers
* incomplete structures
* unsupported future record families
* forged header containers

Boundary:

```text
Has Header Attribute
≠
Supported Runtime Record
```

Status:

**FROZEN**

---

# SUBCLASS ACCEPTANCE

Question:

Should subclasses of supported record classes be accepted through `isinstance`?

Risks:

* subclasses may add mutable behavior
* subclasses may alter equality
* subclasses may add side effects
* subclasses may weaken frozen semantics
* subclasses may represent unreviewed record families

Preferred first-capability direction:

```text
Exact Supported Type
Required
```

Candidate check:

```python
type(record) in SUPPORTED_RECORD_TYPES
```

rather than:

```python
isinstance(record, SUPPORTED_RECORD_TYPES)
```

Status:

**STRONGLY SUPPORTED**

---

# BARE HEADER ACCEPTANCE

Candidate:

```text
RuntimeRecordHeader
```

Finding:

A bare header establishes identity and attribution only.

It does not identify a complete semantic Runtime record family.

Accepting it would occupy an identity without a declared record payload.

Decision:

```text
Bare RuntimeRecordHeader
IS NOT
a registrable Runtime record
```

Status:

**REJECTED**

---

# APPLICATION OBJECT ACCEPTANCE

The registry must reject:

* dictionaries
* lists
* JSON objects
* application project objects
* application event dictionaries
* graph objects
* strings
* raw RuntimeRecordHeader values
* arbitrary dataclasses
* mutable wrappers

Boundary:

```text
Application Object
≠
Supported Runtime Record
```

Status:

**FROZEN**

---

# REGISTRATION OPERATION NAME

Candidate names:

```text
add
append
register
store
insert
```

## `add`

Too generic.

## `append`

Describes container mechanics but not identity occupation.

## `store`

May imply persistence.

## `insert`

May imply arbitrary position.

## `register`

Best expresses local identity occupation and retrievability.

Selected method:

```python
register(record)
```

Status:

**SELECTED**

---

# SUCCESSFUL REGISTRATION

A successful registration requires:

1. exact supported record type
2. valid immutable record already constructed
3. extractable `header.record_id`
4. record ID not already occupied
5. append to internal order
6. add to identity lookup
7. no mutation of the supplied record
8. no admission or authority evaluation
9. no persistence

Resulting facts:

* identity is occupied in this registry
* record is retrievable
* record appears once in append order
* count increases by one

Status:

**SELECTED**

---

# REGISTRATION RETURN CANDIDATES

## Candidate A — Return None

Advantages:

* minimal

Problems:

* provides no direct access to append position
* provides no explicit success representation
* duplicate and collision handling become exception-only

Result:

**REJECTED**

---

## Candidate B — Return the Registered Record

Advantages:

* simple
* confirms preserved record

Problems:

* does not expose append position
* does not distinguish a future idempotent duplicate result
* adds little value because caller already has the record

Result:

**REJECTED**

---

## Candidate C — Return Integer Append Position

Advantages:

* minimal append evidence

Problems:

* position alone does not identify the record
* position indexing semantics must be frozen
* poor extensibility

Result:

**REJECTED**

---

## Candidate D — Return Immutable Registration Result

Advantages:

* explicit outcome
* preserves record ID
* preserves append position
* can remain separate from admission
* can distinguish successful registration from later behaviors

Result:

**SELECTED**

---

# REGISTRATION RESULT MODEL NAME

Candidate names:

```text
RegistrationResult
RuntimeRecordRegistration
RuntimeRecordRegistrationResult
```

Selected:

```text
RuntimeRecordRegistrationResult
```

Status:

**SELECTED**

---

# REGISTRATION RESULT PATH

Selected future path:

```text
models/runtime_record_registration_result.py
```

Reason:

The result is an immutable structural value returned by the registry service.

Status:

**SELECTED**

---

# REGISTRATION RESULT MINIMUM FIELDS

Selected minimum fields:

```python
record_id: str
append_position: int
```

Question:

Should it also contain:

* status
* record
* category
* timestamp
* registry reference

Finding:

Successful construction already implies success.

Additional status would be redundant.

Returning the record duplicates caller ownership.

Category remains available from registry lookup.

Timestamp would require clock access.

Registry reference introduces identity concerns.

Selected minimum:

```python
record_id: str
append_position: int
```

Status:

**STRONGLY SUPPORTED**

---

# APPEND POSITION INDEXING

Candidate conventions:

## Zero-Based

First successful registration:

```text
0
```

Advantages:

* native Python indexing
* direct tuple/list position
* deterministic

## One-Based

First successful registration:

```text
1
```

Advantages:

* human-readable ordinal

Problems:

* differs from Python indexing
* requires conversion for snapshots

Selected:

```text
ZERO-BASED
```

Status:

**SELECTED**

---

# APPEND POSITION MEANING

`append_position` means:

```text
The zero-based location assigned by this registry instance when the record was successfully registered.
```

It does not mean:

* semantic order
* event sequence
* recorded-time order
* causal order
* authority order
* persistent offset
* global ledger position

Boundary:

```text
Append Position
≠
Semantic Sequence
```

Status:

**FROZEN**

---

# REGISTRATION RESULT IMMUTABILITY

The future result should be:

```python
@dataclass(frozen=True)
```

It must not:

* mutate registry contents
* expose registry internals
* contain admission status
* contain authority status
* contain canonical status
* contain persistence status

Status:

**SELECTED**

---

# EXACT DUPLICATE DEFINITION

Exact duplicate attempt:

```text
incoming.header.record_id
==
existing.header.record_id
```

and:

```text
incoming
==
existing
```

using full structural equality.

Boundary:

```text
Same Identity + Same Structure
=
Exact Duplicate Attempt
```

Status:

**FROZEN**

---

# EXACT DUPLICATE BEHAVIOR CANDIDATES

## Candidate A — Append Again

Violates identity uniqueness.

Result:

**REJECTED**

## Candidate B — Idempotent Success

Would make repeated registration appear successful.

Could conceal duplicate calls and weaken append evidence.

Result:

**REJECTED**

## Candidate C — Return Existing Result

Still conceals that no append occurred unless a separate status is added.

Result:

**REJECTED**

## Candidate D — Raise Explicit Exception

Advantages:

* deterministic
* no append
* caller must acknowledge duplicate attempt
* preserves uniqueness
* preserves observability

Result:

**SELECTED**

---

# EXACT DUPLICATE EXCEPTION

Candidate:

```text
RuntimeRecordDuplicateError
```

Selected future path:

```text
services/runtime_record_registry.py
```

or a dedicated exception module.

Question remains whether exceptions should be defined beside the service or separately.

Status:

**NAME SELECTED / LOCATION HOLD**

---

# IDENTITY COLLISION DEFINITION

Identity collision:

```text
incoming.header.record_id
==
existing.header.record_id
```

and:

```text
incoming
!=
existing
```

Boundary:

```text
Same Identity + Different Structure
=
Identity Collision
```

Status:

**FROZEN**

---

# IDENTITY COLLISION BEHAVIOR

The registry must:

* refuse registration
* preserve the existing record
* preserve append order
* preserve count
* avoid overwrite
* avoid merge
* avoid replacement
* avoid automatic identity reassignment

Selected exception:

```text
RuntimeRecordIdentityCollisionError
```

Status:

**SELECTED**

---

# DUPLICATE VERSUS COLLISION EXCEPTIONS

Exact duplicate:

```text
RuntimeRecordDuplicateError
```

Identity collision:

```text
RuntimeRecordIdentityCollisionError
```

They must remain separate.

Boundary:

```text
Duplicate Attempt
≠
Identity Collision
```

Status:

**SELECTED**

---

# EXCEPTION PAYLOAD

Question:

Should custom exceptions expose:

* `record_id`
* existing record
* incoming record
* append position

The minimum first capability may include the record ID in the message.

Storing full records on exceptions may:

* retain references unnecessarily
* expose internal state
* complicate equality and testing
* encourage semantic comparison outside the registry

Preferred minimum:

```text
Exception message includes record_id.
```

Status:

**STRONGLY SUPPORTED**

---

# UNSUPPORTED RECORD TYPE

Unsupported values include:

* `None`
* RuntimeRecordHeader
* dictionaries
* lists
* strings
* arbitrary dataclasses
* subclasses if exact-type enforcement is frozen
* unsupported future record families

Selected behavior:

```text
TypeError
```

Required message fragment:

```text
record
```

or:

```text
supported Runtime record
```

Boundary:

```text
Unsupported Type
≠
Identity Collision
```

Status:

**SELECTED**

---

# VALID RECORD WITH UNSUPPORTED CATEGORY

Current supported record classes already enforce category alignment.

A forged unsupported object with a valid header remains unsupported by type.

The registry must not accept it based only on category.

Boundary:

```text
Recognized record_category
≠
Supported Record Type
```

Status:

**FROZEN**

---

# INTERNAL STORAGE CANDIDATES

The registry needs:

1. identity lookup
2. append-order preservation

Candidate internal structures:

```python
_records_by_id: dict[str, RuntimeRecord]
_records_in_order: list[RuntimeRecord]
```

Advantages:

* constant-time identity lookup
* deterministic append-order snapshot
* simple duplicate and collision handling

Risk:

* dual structure must remain synchronized

Alternative:

```python
_records_by_id: dict[str, RuntimeRecord]
```

Python dictionaries preserve insertion order.

Advantages:

* one structure

Risks:

* append position requires enumeration or separate calculation
* dictionary semantics may obscure explicit append-order ownership

Preferred direction:

```text
ONE INSERTION-ORDERED DICTIONARY
OR
EXPLICIT DICTIONARY + ORDER LIST
```

Status:

**IMPLEMENTATION DETAIL HOLD**

---

# REGISTER ATOMICITY

Registration must be atomic at the service-method level:

Either:

```text
record absent
→
identity and append order both updated
→
success result returned
```

or:

```text
failure
→
registry unchanged
```

No partial registration is permitted.

Boundary:

```text
Failed Registration
≠
Partial Membership
```

Status:

**FROZEN**

---

# RECORD INSTANCE PRESERVATION

Question:

Should the registry preserve:

* the exact record instance
* an equal copy
* serialized reconstruction

The first in-memory registry should preserve the exact supplied immutable instance.

Expected:

```python
registry.get(record_id) is record
```

Advantages:

* no copying
* no serialization
* no reconstruction drift
* preserves caller-supplied immutable value

Status:

**SELECTED**

---

# LOOKUP METHOD NAME

Candidate names:

```text
get
lookup
retrieve
record
```

Selected:

```python
get(record_id)
```

Reason:

* standard mapping-style behavior
* concise
* clear

Status:

**SELECTED**

---

# RECORD ID LOOKUP INPUT

Lookup input:

```python
record_id: str
```

Question:

Should lookup validate full `RR-#########` syntax?

The registry owns registered identities but should not duplicate RuntimeRecordHeader syntax rules unnecessarily.

Potential behavior:

* require string
* require non-empty string
* do exact dictionary lookup
* allow structurally invalid but absent strings to resolve as missing

Preferred direction:

```text
Type-check as string;
perform exact lookup;
do not duplicate record ID syntax validation.
```

Status:

**STRONGLY SUPPORTED**

---

# MISSING LOOKUP BEHAVIOR CANDIDATES

## Candidate A — Return None

Advantages:

* convenient

Problems:

* may conceal missing identity
* conflates absent record with nullable return handling

## Candidate B — Raise KeyError

Advantages:

* standard mapping semantics
* explicit absence
* no new result type required

## Candidate C — Custom Missing Error

Advantages:

* explicit domain language

Problems:

* unnecessary custom exception for standard lookup behavior

Selected:

```text
KeyError
```

Status:

**SELECTED**

---

# CONTAINS METHOD

Candidate:

```python
contains(record_id) -> bool
```

Alternative:

```python
record_id in registry
```

Dunder membership introduces additional interface design.

Selected minimum explicit method:

```python
contains(record_id) -> bool
```

Status:

**SELECTED**

---

# COUNT METHOD

Candidate:

```python
count() -> int
```

Alternative:

```python
len(registry)
```

Dunder length is conventional but adds protocol surface.

Preferred minimum:

```python
count() -> int
```

Whether `__len__` is also supported remains deferred.

Status:

**SELECTED**

---

# SNAPSHOT METHOD

Selected method:

```python
records() -> tuple[SupportedRuntimeRecord, ...]
```

Meaning:

Return registered records in successful append order.

The returned tuple must not permit registry mutation.

Status:

**SELECTED**

---

# SNAPSHOT IDENTITY

The snapshot may contain the exact immutable record instances.

Expected:

```python
registry.records()[0] is first_record
```

Snapshot creation does not copy records.

Status:

**SELECTED**

---

# SNAPSHOT STABILITY

A previously returned tuple remains unchanged after later registrations.

Example:

```text
snapshot_1 = (A,)
register B
snapshot_1 remains (A,)
new snapshot = (A, B)
```

Boundary:

```text
Read Snapshot
≠
Live Mutable View
```

Status:

**SELECTED**

---

# CATEGORY FILTERING

Candidate method:

```python
records_by_category(record_category: str)
```

Question:

Should category filtering be in the minimum registry?

Advantages:

* structural query
* no semantic interpretation
* useful for inspection
* supported by every RuntimeRecordHeader

Risks:

* category validation semantics
* future unsupported category questions
* duplicate method surface

Preferred minimum:

```python
records_by_category(record_category) -> tuple
```

Status:

**SELECTED**

---

# CATEGORY FILTER INPUT

Preferred behavior:

* require string
* require non-empty, non-whitespace string
* exact case-sensitive match
* no normalization
* no requirement that category is currently supported
* unknown category returns empty tuple

Boundary:

```text
No Records for Category
≠
Invalid Category
```

Status:

**STRONGLY SUPPORTED**

---

# CATEGORY FILTER ORDER

Filtered records must preserve original append order.

Boundary:

```text
Category Filter
≠
Category Reordering
```

Status:

**SELECTED**

---

# RECORD ID SNAPSHOT

Candidate method:

```python
record_ids() -> tuple[str, ...]
```

Advantages:

* structural inspection
* avoids extracting headers repeatedly
* deterministic append-order identity view

Question:

Is it necessary in the minimum contract?

It may be redundant with `records()`.

Decision:

**DEFERRED**

---

# APPEND POSITION LOOKUP

Candidate:

```python
position_of(record_id) -> int
```

Advantages:

* exposes registry placement

Problems:

* additional method
* may encourage semantic misuse
* result already returned at registration time

Decision:

**DEFERRED**

---

# REMOVE OPERATION

Do not expose:

```python
remove(record_id)
```

Status:

**PROHIBITED**

---

# REPLACE OPERATION

Do not expose:

```python
replace(record)
```

Status:

**PROHIBITED**

---

# UPDATE OPERATION

Do not expose:

```python
update(record_id, record)
```

Status:

**PROHIBITED**

---

# UPSERT OPERATION

Do not expose:

```python
upsert(record)
```

Reason:

Upsert silently collapses append and replacement.

Status:

**PROHIBITED**

---

# CLEAR OR RESET

Do not expose:

```python
clear()
reset()
```

Reason:

These erase append history.

Tests may create a fresh registry instance instead.

Status:

**PROHIBITED**

---

# DIRECT INTERNAL ACCESS

The registry must not expose a public mutable dictionary or list.

Prohibited public fields:

```text
records_by_id
records_list
entries
storage
```

if they expose mutable internals directly.

Private internal attributes remain an implementation detail.

Status:

**FROZEN**

---

# REGISTRY MUTABILITY

The registry object itself changes only through successful `register`.

Allowed mutation:

```text
append new unique record
```

Prohibited mutation:

```text
replace existing record
delete existing record
edit existing record
reorder existing records
clear registry
```

Boundary:

```text
Registry Growth
≠
Registry Rewrite
```

Status:

**FROZEN**

---

# RECORD MUTABILITY

Registered records are already frozen dataclasses.

The registry must not:

* call `object.__setattr__`
* modify headers
* normalize references
* assign append position into records
* assign admission status
* assign persistence status
* wrap records in mutable proxies

Status:

**FROZEN**

---

# ADMISSION FIELDS

The registry and registration result must not include:

```text
admitted
accepted
approved
authorized
valid
canonical
current
active
```

Boundary:

```text
Registration Result
≠
Admission Result
```

Status:

**PROHIBITED**

---

# PERSISTENCE FIELDS

The registry result must not include:

```text
persisted
storage_path
database_id
file_offset
durable
committed
```

Boundary:

```text
Registered
≠
Persisted
```

Status:

**PROHIBITED**

---

# TIMESTAMP FIELDS

Do not add:

```text
registered_at
appended_at
```

to the first result.

Reason:

* would require clock access
* duplicates timing questions
* introduces deterministic-test complexity
* registration time is not yet architecturally required

Status:

**DEFERRED**

---

# REGISTRATION EVENT

Do not automatically create a RuntimeEventRecord when registration succeeds.

Boundary:

```text
Record Registered
≠
Registration Event Automatically Created
```

Status:

**PROHIBITED**

---

# COLLISION EVENT

Do not automatically create an event when collision occurs.

The failed operation must leave the registry unchanged.

Status:

**PROHIBITED**

---

# DUPLICATE ATTEMPT ACCOUNTING

Question:

Should the registry count duplicate or collision attempts?

Potential fields:

```text
duplicate_attempt_count
collision_count
failed_registration_count
```

These introduce mutable operational telemetry.

Decision:

**DEFERRED**

---

# STRUCTURAL INSPECTION

Minimum structural inspection may be satisfied by:

```text
count()
contains(record_id)
get(record_id)
records()
records_by_category(record_category)
```

No dedicated `inspect()` method is selected yet.

Platform inspection integration remains separate.

Status:

**SELECTED MINIMUM READ SURFACE**

---

# REGISTRY PROTOCOL SURFACE

Selected candidate public methods:

```python
register(record) -> RuntimeRecordRegistrationResult
get(record_id: str) -> SupportedRuntimeRecord
contains(record_id: str) -> bool
count() -> int
records() -> tuple[SupportedRuntimeRecord, ...]
records_by_category(record_category: str) -> tuple[SupportedRuntimeRecord, ...]
```

Status:

**STRONGLY SUPPORTED**

---

# TYPE ALIAS

The service may define an internal or public type alias:

```python
SupportedRuntimeRecord = (
    RuntimeEventRecord
    | RuntimeObjectVersionRecord
    | ProgressionAssertionRecord
    | HoldRecord
)
```

Question:

Should this alias be publicly exported?

Public export may help tests and typing but expands module API.

Status:

**HOLD**

---

# INITIAL REGISTRY STATE

A newly constructed registry must:

* contain zero records
* return count zero
* return empty tuple from `records()`
* return empty tuple for any valid category filter
* report `contains(record_id)` false
* raise `KeyError` from `get(record_id)`

Status:

**SELECTED**

---

# CONSTRUCTOR ARGUMENTS

The minimum registry constructor should accept no initial records.

Reason:

Constructor preload would introduce:

* bulk registration semantics
* partial failure questions
* collision handling during construction
* ordering ambiguity
* bypass risk around `register`

Selected constructor:

```python
RuntimeRecordRegistry()
```

Status:

**SELECTED**

---

# BULK REGISTRATION

Do not include:

```python
register_many(records)
```

in the first capability.

Bulk registration requires:

* atomicity policy
* partial-success policy
* collision rollback
* result ordering
* duplicate handling across the batch

Status:

**DEFERRED**

---

# ITERATION

Question:

Should the registry implement:

```python
__iter__
```

Potentially convenient, but it expands protocol behavior and may encourage assumptions about live views.

Decision:

**DEFERRED**

---

# LENGTH

Question:

Should the registry implement:

```python
__len__
```

`count()` is sufficient for the first capability.

Decision:

**DEFERRED**

---

# MEMBERSHIP OPERATOR

Question:

Should the registry implement:

```python
record_id in registry
```

`contains()` is sufficient.

Decision:

**DEFERRED**

---

# EQUALITY

Registry instances should not use structural equality over their contents in the first capability.

Two independent registry instances containing equal records should not automatically be treated as the same registry.

Default object identity equality is preferred.

Boundary:

```text
Equal Contents
≠
Same Registry Instance
```

Status:

**SELECTED**

---

# HASHING

Registry instances should remain unhashable or use default object behavior depending on class implementation.

No semantic registry hashing is selected.

Status:

**DEFERRED TO IMPLEMENTATION CONTRACT**

---

# THREAD SAFETY

The first in-memory registry does not establish thread safety.

Do not add:

* locks
* async methods
* concurrent append semantics
* transaction isolation

Status:

**DEFERRED**

---

# PERSISTENCE

The first registry must not:

* write files
* append logs
* create directories
* use databases
* serialize records
* load records
* restore snapshots
* migrate application content

Status:

**HOLD**

---

# PLATFORM REGISTRY INTEGRATION

Do not:

* register RuntimeRecordRegistry with PlatformRegistry
* change service counts
* alter ResearchKernel
* alter Mission Control
* alter Platform Registry page
* add Streamlit dependencies

Status:

**HOLD**

---

# ADMISSION

Do not:

* approve records
* reject semantic content
* validate authority
* validate provenance sufficiency
* calculate progression
* determine current version
* determine active Hold
* determine canonical event history

Status:

**HOLD**

---

# CANONICAL PROJECTION

The registry preserves all successfully registered records, including records that may later be:

* superseded
* invalidated
* contradicted
* released
* abandoned
* noncanonical
* inadmissible

Boundary:

```text
Preserved in Registry
≠
Canonically Relied Upon
```

Status:

**FROZEN**

---

# ADVERSARIAL TEST 1 — DUCK-TYPED OBJECT

Proposal:

Accept any object with `.header.record_id`.

Finding:

Could admit mutable or unsupported objects.

Result:

**REJECTED**

---

# ADVERSARIAL TEST 2 — BARE HEADER

Proposal:

Register RuntimeRecordHeader directly.

Finding:

Occupies identity without a complete record family.

Result:

**REJECTED**

---

# ADVERSARIAL TEST 3 — DUPLICATE AS IDEMPOTENT SUCCESS

Finding:

Conceals repeated registration attempts and weakens append evidence.

Result:

**REJECTED**

---

# ADVERSARIAL TEST 4 — COLLISION OVERWRITE

Finding:

Destroys append-only history and identity integrity.

Result:

**REJECTED**

---

# ADVERSARIAL TEST 5 — UPSERT

Finding:

Collapses append and replacement.

Result:

**REJECTED**

---

# ADVERSARIAL TEST 6 — SORT BY RECORDED TIME

Finding:

Destroys registration-order evidence and assumes chronology.

Result:

**REJECTED**

---

# ADVERSARIAL TEST 7 — REGISTERED MEANS ADMITTED

Finding:

Collapses storage membership and semantic permission.

Result:

**REJECTED**

---

# ADVERSARIAL TEST 8 — REGISTRATION WRITES JSON

Finding:

Couples semantic registry behavior to persistence technology before the contract is proven.

Result:

**REJECTED FOR FIRST CAPABILITY**

---

# ADVERSARIAL TEST 9 — RETURN INTERNAL LIST

Finding:

Permits external mutation and reordering.

Result:

**REJECTED**

---

# ADVERSARIAL TEST 10 — AUTO-CREATE REGISTRATION EVENT

Finding:

Introduces event recursion and unapproved side effects.

Result:

**REJECTED**

---

# MINIMUM CANDIDATE ARCHITECTURE

## Service

```text
RuntimeRecordRegistry
```

## Service Path

```text
services/runtime_record_registry.py
```

## Result Model

```text
RuntimeRecordRegistrationResult
```

## Result Path

```text
models/runtime_record_registration_result.py
```

## Supported Exact Types

```text
RuntimeEventRecord
RuntimeObjectVersionRecord
ProgressionAssertionRecord
HoldRecord
```

## Registry Key

```text
record.header.record_id
```

## Successful Operation

```python
register(record)
```

## Successful Result

```python
RuntimeRecordRegistrationResult(
    record_id=record.header.record_id,
    append_position=zero_based_position,
)
```

## Exact Duplicate

```text
RuntimeRecordDuplicateError
```

## Identity Collision

```text
RuntimeRecordIdentityCollisionError
```

## Unsupported Type

```text
TypeError
```

## Missing Lookup

```text
KeyError
```

## Snapshot

```text
tuple in append order
```

Status:

**STRONGLY SUPPORTED**

---

# UNRESOLVED QUESTIONS

The following remain open:

1. exact exception module location
2. exact exception inheritance
3. exact exception messages
4. exact registration result field validation
5. whether the result should validate `RR-#########` syntax
6. whether exact supported types or subclasses are accepted
7. exact internal storage representation
8. exact lookup input validation
9. exact category filter input validation
10. whether `records_by_category` belongs in the first implementation
11. whether `count()` or `__len__` should be primary
12. whether `contains()` or `__contains__` should be primary
13. whether registry snapshots contain exact instances
14. whether a public SupportedRuntimeRecord alias is exported
15. whether service equality should remain identity-based
16. whether custom exceptions store `record_id`
17. exact deterministic validation order
18. exact side-effect import boundary
19. whether the registration result belongs in `models`
20. whether structural inspection requires `inspect()`

All remain:

**HOLD**

---

# REDUCTION DECISION

Registry class name:
**SELECTED**

Service path:
**SELECTED**

Test path:
**SELECTED**

Registration result model:
**SELECTED**

Registration result path:
**SELECTED**

Registry-instance identity:
**DEFERRED**

Registry key:
**SELECTED**

Supported record families:
**SELECTED**

Bare-header acceptance:
**REJECTED**

Duck typing:
**REJECTED**

Subclass acceptance:
**STRONGLY SUPPORTED FOR REJECTION**

Registration method:
**SELECTED**

Registration result fields:
**STRONGLY SUPPORTED**

Zero-based append position:
**SELECTED**

Exact duplicate exception:
**SELECTED**

Identity collision exception:
**SELECTED**

Unsupported type behavior:
**SELECTED**

Missing lookup behavior:
**SELECTED**

Exact instance preservation:
**SELECTED**

Count method:
**SELECTED**

Contains method:
**SELECTED**

Snapshot method:
**SELECTED**

Category filtering:
**SELECTED**

Remove operation:
**PROHIBITED**

Replace operation:
**PROHIBITED**

Update operation:
**PROHIBITED**

Upsert operation:
**PROHIBITED**

Clear/reset operation:
**PROHIBITED**

Bulk registration:
**DEFERRED**

Persistence:
**HOLD**

Platform Registry integration:
**HOLD**

Admission:
**HOLD**

Canonical projection:
**HOLD**

Implementation:
**HOLD**

---

# READINESS CHECKPOINT 2

Identity, Duplicate, Collision, and Registration Result Separation:

**COMPLETE**

No service was created.

No result model was created.

No exceptions were created.

No tests were created.

No persistence was introduced.

No Platform Registry integration was introduced.

No application behavior changed.

No admission or canonical projection behavior was introduced.

---

# NEXT SESSION

Begin:

**APPEND-ONLY RUNTIME RECORD REGISTRY — IMMUTABLE RESULT AND SERVICE CONTRACT 001**

Primary question:

What exact field, exception, constructor, method, validation-order, atomicity, snapshot, identity, type-acceptance, lookup, equality, mutation-prohibition, and side-effect rules must define `RuntimeRecordRegistrationResult` and `RuntimeRecordRegistry` before tests are written?

Required work:

1. freeze registration-result field types
2. freeze registration-result validation
3. freeze result immutability and equality
4. freeze supported exact record types
5. freeze registry constructor
6. freeze internal behavioral invariants
7. freeze registration validation order
8. freeze duplicate behavior
9. freeze collision behavior
10. freeze exception definitions
11. freeze lookup validation
12. freeze missing lookup behavior
13. freeze count and contains behavior
14. freeze snapshot behavior
15. freeze category-filter behavior
16. freeze mutation prohibitions
17. freeze service equality behavior
18. freeze import and side-effect boundaries
19. preserve persistence HOLD
20. preserve Platform Registry integration HOLD
21. preserve implementation HOLD

**UNKNOWN → HOLD**
