# READ-ONLY RUNTIME RECORD INSPECTION EMBEDDED REPORT INTEGRITY VERIFICATION

# VOCABULARY, INPUT OWNERSHIP, PARTIAL RESULT, DIGEST, LENGTH, BOM, AND SCOPE REDUCTION 001

**Date:** 2026-07-17
**Project:** Research OS
**Development Version:** v2.0.0
**Authority:** VOCABULARY AND SCOPE REDUCTION ONLY
**Status:** COMPLETE
**Operating Posture:** SUBJECT-FIRST / FACT-FIRST / PARTIAL-RESULT-PRESERVING / NON-ADMITTING / UNKNOWN → HOLD

---

# PURPOSE

Freeze the vocabulary, exact inputs, ownership boundaries, measurable integrity facts, partial-result semantics, immutable result shape, derivation rules, validation order, mismatch meaning, codec exclusion, dependency direction, and prohibited expansion for the first Read-Only Runtime Record Inspection Embedded Report Integrity Verification capability.

This reduction follows:

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_EMBEDDED_REPORT_INTEGRITY_VERIFICATION_EXISTING_DIGEST_LENGTH_CODEC_BOM_PARTIAL_RESULT_SUBJECT_BINDING_ADMISSION_AND_AUTHORITY_BOUNDARY_INSPECTION_001.md
```

That inspection established:

1. the digest manifest carries validated digest, byte-length, codec, and BOM claims
2. those claims are not verified against supplied report bytes
3. no combined embedded report-integrity verification service exists
4. no partial-result model exists
5. exact report bytes and an exact digest manifest should be the inputs
6. SHA-256 digest equality is directly measurable
7. byte length is directly measurable
8. UTF-8 BOM-prefix presence is directly measurable
9. codec provenance is not directly measurable from arbitrary bytes
10. UTF-8 decodability does not prove UTF-8 origin
11. codec verification must remain outside the first capability
12. digest, length, and BOM checks can disagree independently
13. a Boolean-only result would erase partial evidence
14. an immutable result model is required
15. the overall integrity result must be derived
16. mismatches are valid outcomes
17. malformed runtime input remains distinct from mismatch
18. call-local pairing does not establish historical subject binding
19. full match does not establish provenance
20. full match does not establish identity
21. full match does not establish admission
22. full match does not establish trust
23. full match does not establish authority
24. persistence, events, export, and transport remain outside scope
25. frozen upstream components can remain unchanged

This document authorizes creation of immutable model and service contracts.

```text
Model implementation: HOLD
Tests: HOLD
Service implementation: HOLD
```

---

# ACCEPTED CAPABILITY NAME

```text
Read-Only Runtime Record Inspection Embedded Report Integrity Verification
```

The capability performs:

```text
one exact inspection-report bytes value
+
one exact RuntimeRecordInspectionDigestManifest
→
one immutable partial integrity-verification result
```

The first capability measures exactly:

```text
digest match
byte-length match
UTF-8 BOM-prefix match
```

---

# ACCEPTED SERVICE OWNER

```text
RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService
```

Accepted future location:

```text
services/runtime_record_inspection_embedded_report_integrity_verification_service.py
```

The service owns:

```text
exact input validation
SHA-256 measurement
constant-time digest comparison
byte-length comparison
UTF-8 BOM-prefix observation
result construction
```

It does not own:

```text
report construction
report representation
JSON encoding
UTF-8 encoding
manifest construction
manifest mutation
codec provenance
historical subject binding
admission
trust
authority
persistence
publication
```

---

# ACCEPTED RESULT OWNER

```text
RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult
```

Accepted future location:

```text
models/runtime_record_inspection_embedded_report_integrity_verification_result.py
```

The result owns immutable Boolean facts only.

Accepted stored fields:

```text
digest_matches
byte_length_matches
bom_matches
```

Accepted derived property:

```text
integrity_matches
```

---

# INPUT OWNERSHIP

The first input is:

```text
report_bytes
```

Meaning:

```text
the current byte sequence whose report-integrity facts
are being checked against the supplied digest manifest
```

The second input is:

```text
manifest
```

Meaning:

```text
the immutable validated integrity-claim container
against which the supplied bytes are measured
```

```text
Observed Byte Subject
≠
Expected Claim Container
```

---

# EXACT REPORT-BYTES TYPE

The accepted runtime type is exactly:

```text
bytes
```

Required rule:

```python
type(report_bytes) is bytes
```

The service must reject:

```text
None
bool
int
float
str
bytearray
memoryview
list
tuple
set
frozenset
dict
mapping
bytes subclass
path
file
stream
report model
primitive dictionary
JSON text
```

```text
Bytes Compatibility
≠
Exact Plain Bytes
```

Recommended exact error:

```text
TypeError
```

Recommended exact message:

```text
report_bytes must be an exact bytes
```

---

# EXACT MANIFEST TYPE

The accepted runtime type is exactly:

```text
RuntimeRecordInspectionDigestManifest
```

Required rule:

```python
type(manifest) is RuntimeRecordInspectionDigestManifest
```

The service must reject:

```text
None
dict
mapping
primitive manifest representation
JSON text
UTF-8 bytes
manifest subclass
unrelated dataclass
mock manifest
duck-typed object
```

```text
Manifest Compatibility
≠
Exact Manifest Ownership
```

Recommended exact error:

```text
TypeError
```

Recommended exact message:

```text
manifest must be an exact RuntimeRecordInspectionDigestManifest
```

---

# INPUT VALIDATION ORDER

The accepted validation order is:

```text
report_bytes runtime type
→
manifest runtime type
→
digest measurement
→
digest comparison
→
byte-length comparison
→
BOM-prefix observation
→
immutable result construction
```

No measurement occurs before both runtime types are valid.

---

# EMPTY BYTES

Exact empty bytes are accepted.

The capability does not require:

```text
non-empty bytes
valid JSON
valid UTF-8
valid report semantics
known schema
```

```text
Hashable Bytes
≠
Confirmed Inspection Report
```

---

# ARBITRARY BYTES

The service accepts arbitrary exact bytes, including:

```python
b""
b"abc"
b"\x00"
b"\xff"
b"\xef\xbb\xbf"
b"\xef\xbb\xbf{}"
```

The service verifies byte-level claims only.

It does not decode or parse the bytes.

---

# DIGEST MEASUREMENT

The computed digest is:

```python
hashlib.sha256(
    report_bytes
).hexdigest()
```

The service may import:

```python
import hashlib
```

This digest is an internal verification measurement.

It is not exposed as a new public digest-generation method.

```text
Internal Digest Measurement
≠
New Public Digest Capability
```

---

# DIGEST COMPARISON

The measured digest is compared with:

```text
manifest.sha256_digest
```

The accepted comparison operation is:

```python
hmac.compare_digest(
    computed_digest,
    manifest.sha256_digest,
)
```

The service may import:

```python
import hmac
```

Plain equality must not own the digest comparison.

```text
Digest Value Equality
≠
Constant-Time Digest Comparison
```

---

# DIGEST MATCH RESULT

```text
digest_matches
```

means only:

```text
SHA-256(report_bytes)
equals manifest.sha256_digest
under constant-time comparison
```

Exact runtime type:

```text
bool
```

A digest mismatch returns:

```text
digest_matches = False
```

It does not raise an exception.

---

# BYTE-LENGTH MEASUREMENT

The observed byte length is:

```python
len(report_bytes)
```

It is compared with:

```text
manifest.byte_length
```

Accepted operation:

```python
byte_length_matches = (
    len(report_bytes) == manifest.byte_length
)
```

Byte length is a direct property of the supplied bytes.

---

# BYTE-LENGTH MATCH RESULT

```text
byte_length_matches
```

means only:

```text
the number of supplied bytes equals
the manifest's declared byte_length
```

Exact runtime type:

```text
bool
```

A length mismatch returns:

```text
byte_length_matches = False
```

It does not raise an exception.

---

# UTF-8 BOM MARKER

The UTF-8 BOM marker is exactly:

```text
EF BB BF
```

Python literal:

```python
b"\xef\xbb\xbf"
```

Observed BOM presence:

```python
report_bytes.startswith(
    b"\xef\xbb\xbf"
)
```

---

# BOM MATCH MEASUREMENT

The manifest contract requires:

```text
manifest.bom_present is False
```

The bounded comparison is:

```python
observed_bom_present = report_bytes.startswith(
    b"\xef\xbb\xbf"
)

bom_matches = (
    observed_bom_present
    is manifest.bom_present
)
```

Because the manifest requires `False`, this returns `True` only when the supplied bytes do not begin with the UTF-8 BOM marker.

---

# BOM MATCH RESULT

```text
bom_matches
```

means only:

```text
the observed UTF-8 BOM-prefix state of the supplied bytes
matches the manifest's bom_present declaration
```

It does not mean:

```text
the bytes are valid UTF-8
the bytes came from the frozen UTF-8 encoder
the bytes are valid JSON
the bytes are a valid report
```

```text
No UTF-8 BOM Prefix
≠
UTF-8 Provenance
```

---

# CODEC EXCLUSION

The first result must not contain:

```text
codec_matches
```

Reason:

```text
arbitrary bytes do not prove encoding provenance
successful UTF-8 decoding proves decodability only
manifest.codec is already fixed by model validation
```

The service must not call:

```python
report_bytes.decode("utf-8")
```

for codec verification.

```text
UTF-8 Decodable
≠
Created By UTF-8 Encoder
```

Codec provenance remains:

```text
HOLD
```

---

# PARTIAL RESULT REQUIREMENT

The authorized checks may disagree independently.

Examples:

```text
digest_matches = False
byte_length_matches = True
bom_matches = True
```

```text
digest_matches = False
byte_length_matches = False
bom_matches = True
```

```text
digest_matches = False
byte_length_matches = False
bom_matches = False
```

Therefore, a single stored Boolean is insufficient.

```text
Combined Verification Bool
≠
Preserved Partial Evidence
```

---

# RESULT MODEL FIELDS

The immutable result stores exactly:

```python
digest_matches: bool
byte_length_matches: bool
bom_matches: bool
```

No fourth stored Boolean is authorized.

---

# DERIVED OVERALL RESULT

The result exposes:

```text
integrity_matches
```

as a derived property.

Required derivation:

```python
return (
    self.digest_matches
    and self.byte_length_matches
    and self.bom_matches
)
```

```text
integrity_matches
=
all authorized component checks match
```

The value must not be caller-supplied.

---

# CONTRADICTORY-STATE PROHIBITION

The result must not permit:

```text
digest_matches = False
byte_length_matches = True
bom_matches = True
integrity_matches = True
```

Derivation prevents contradictory aggregate state.

```text
Derived Aggregate
≠
Caller-Supplied Aggregate
```

---

# RESULT FIELD TYPES

Each stored field must be exact:

```text
bool
```

Required validation rules:

```python
type(digest_matches) is bool
type(byte_length_matches) is bool
type(bom_matches) is bool
```

Invalid values raise:

```text
TypeError
```

Recommended exact messages:

```text
digest_matches must be an exact bool
byte_length_matches must be an exact bool
bom_matches must be an exact bool
```

---

# RESULT VALIDATION ORDER

The accepted result-model validation order is:

```text
digest_matches runtime type
→
byte_length_matches runtime type
→
bom_matches runtime type
```

---

# RESULT IMMUTABILITY

The result model must be:

```python
@dataclass(frozen=True)
```

Stored fields cannot be reassigned.

The result owns no mutable collection.

---

# RESULT PUBLIC SURFACE

Accepted public facts:

```text
digest_matches
byte_length_matches
bom_matches
integrity_matches
```

The result must not expose behavior including:

```text
save
load
persist
publish
admit
approve
trust
authorize
verify_again
recalculate
to_json
to_bytes
```

---

# RESULT CONTENT PROHIBITIONS

The result must not store:

```text
report_bytes
manifest
computed_digest
expected_digest
observed_byte_length
expected_byte_length
observed_bom_present
codec
timestamp
identifier
subject_id
record_id
registry_ref
provenance
path
authority
```

The first result preserves only bounded comparison facts.

---

# VALID FULL MATCH

A full match is:

```text
digest_matches = True
byte_length_matches = True
bom_matches = True
integrity_matches = True
```

This means all authorized byte-level checks agree.

It does not establish complete artifact integrity.

---

# VALID PARTIAL MISMATCH

A partial mismatch is any result where at least one component is `False` and at least one component is `True`.

It is a valid result.

It is not an exception.

```text
Partial Mismatch
≠
Verification Execution Failure
```

---

# VALID COMPLETE MISMATCH

A result may contain:

```text
digest_matches = False
byte_length_matches = False
bom_matches = False
integrity_matches = False
```

This remains a valid result.

It does not prove tampering or cause.

---

# MALFORMED INPUT VERSUS MISMATCH

Invalid runtime input raises an exception.

Valid inputs with disagreeing facts return a result.

```text
Invalid Runtime Input
≠
Integrity Mismatch
```

---

# DIGEST MISMATCH MEANING

A digest mismatch means only:

```text
the SHA-256 digest measured from report_bytes
differs from manifest.sha256_digest
```

It does not establish:

```text
tampering
corruption
malice
which side is wrong
which artifact is current
which artifact is authoritative
```

```text
Digest Mismatch
≠
Tampering Proof
```

---

# LENGTH MISMATCH MEANING

A byte-length mismatch means only:

```text
len(report_bytes)
differs from manifest.byte_length
```

It does not establish:

```text
truncation
appending
transport failure
encoding failure
tampering
```

```text
Length Mismatch
≠
Cause Attribution
```

---

# BOM MISMATCH MEANING

A BOM mismatch means only:

```text
the observed BOM-prefix state differs
from manifest.bom_present
```

It does not establish:

```text
invalid UTF-8
invalid JSON
unsafe content
malicious modification
```

---

# CALL-LOCAL PAIRING

The service directly compares one supplied byte value with one supplied manifest.

This establishes:

```text
call-local comparison pairing
```

It does not establish:

```text
historical subject binding
original creation relationship
shared custody
registry relationship
```

```text
Call-Local Pairing
≠
Historical Subject Binding
```

---

# PROVENANCE BOUNDARY

The capability does not establish:

```text
who created the bytes
who created the manifest
when either was created
where either was stored
whether either was previously altered
whether they share a custody chain
```

---

# IDENTITY BOUNDARY

The result does not establish:

```text
report identity
manifest identity
artifact identity
record identity
registry identity
execution identity
```

```text
Integrity Facts Match
≠
Identity Established
```

---

# ADMISSION BOUNDARY

A full match does not:

```text
admit evidence
register evidence
approve artifacts
promote evidence
change lifecycle state
authorize use
```

```text
Integrity Match
≠
Integrity Admission
```

Admission remains:

```text
HOLD
```

---

# TRUST BOUNDARY

A full match does not establish:

```text
source authenticity
manifest authority
report correctness
report completeness
artifact safety
expected-claim trustworthiness
```

```text
Integrity Match
≠
Trust
```

---

# AUTHORITY BOUNDARY

The result grants no:

```text
execution authority
governance authority
publication permission
export permission
corrective authority
admission authority
```

```text
Integrity Match
≠
Authority Granted
```

---

# PERSISTENCE BOUNDARY

The model and service must not:

```text
save results
load artifacts
write files
create receipts
update registries
write databases
```

---

# EVENT AND LOGGING BOUNDARY

The capability publishes no:

```text
verification event
mismatch event
audit event
notification
alert
log
```

---

# EXPORT AND TRANSPORT BOUNDARY

The capability performs no:

```text
export
upload
download
streaming
transmission
network request
```

---

# COLLECTION BOUNDARY

The first service accepts exactly one pair:

```text
one report_bytes
+
one manifest
```

It does not support:

```text
batch verification
report collections
manifest collections
registry snapshots
Merkle verification
hash chains
```

---

# SIGNATURE BOUNDARY

The capability does not verify:

```text
signatures
certificates
attestations
signer identity
keys
```

---

# SERVICE STATE

The service requires no constructor arguments.

It retains no:

```text
last bytes
last manifest
last computed digest
last result
call count
cache
history
```

The service is stateless.

---

# DETERMINISM

For unchanged exact inputs, the service must return an equal immutable result.

The result does not depend on:

```text
time
randomness
identifiers
environment variables
filesystem state
network state
registry state
service instance identity
process identity
```

---

# ACCEPTED MODEL IMPORT

The result model should import exactly:

```python
from dataclasses import dataclass
```

No other import should be required.

---

# ACCEPTED SERVICE IMPORTS

The service should import:

```python
import hashlib
import hmac
```

and:

```python
from models.runtime_record_inspection_digest_manifest import (
    RuntimeRecordInspectionDigestManifest,
)
```

```python
from models.runtime_record_inspection_embedded_report_integrity_verification_result import (
    RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult,
)
```

No other dependency should be required.

---

# FROZEN UPSTREAM PRESERVATION

The following components must remain unchanged:

```text
models/runtime_record_inspection_digest_manifest.py
services/runtime_record_inspection_digest_manifest_service.py
services/runtime_record_inspection_representation_service.py
services/runtime_record_inspection_json_encoding_service.py
services/runtime_record_inspection_utf8_byte_encoding_service.py
services/runtime_record_inspection_sha256_digest_service.py
services/runtime_record_inspection_digest_manifest_digest_verification_service.py
```

---

# ACCEPTED FUTURE MODEL SHAPE

The future model is expected to be structurally equivalent to:

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult:
    digest_matches: bool
    byte_length_matches: bool
    bom_matches: bool

    def __post_init__(self) -> None:
        if type(self.digest_matches) is not bool:
            raise TypeError(
                "digest_matches must be an exact bool"
            )

        if type(self.byte_length_matches) is not bool:
            raise TypeError(
                "byte_length_matches must be an exact bool"
            )

        if type(self.bom_matches) is not bool:
            raise TypeError(
                "bom_matches must be an exact bool"
            )

    @property
    def integrity_matches(self) -> bool:
        return (
            self.digest_matches
            and self.byte_length_matches
            and self.bom_matches
        )
```

This is a vocabulary reference only.

Model implementation remains:

```text
HOLD
```

---

# ACCEPTED FUTURE SERVICE SHAPE

The future service is expected to be structurally equivalent to:

```python
import hashlib
import hmac

from models.runtime_record_inspection_digest_manifest import (
    RuntimeRecordInspectionDigestManifest,
)
from models.runtime_record_inspection_embedded_report_integrity_verification_result import (
    RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult,
)


class RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService:
    def verify_integrity(
        self,
        report_bytes: bytes,
        manifest: RuntimeRecordInspectionDigestManifest,
    ) -> RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult:
        if type(report_bytes) is not bytes:
            raise TypeError(
                "report_bytes must be an exact bytes"
            )

        if type(manifest) is not RuntimeRecordInspectionDigestManifest:
            raise TypeError(
                "manifest must be an exact "
                "RuntimeRecordInspectionDigestManifest"
            )

        computed_digest = hashlib.sha256(
            report_bytes
        ).hexdigest()

        digest_matches = hmac.compare_digest(
            computed_digest,
            manifest.sha256_digest,
        )

        byte_length_matches = (
            len(report_bytes)
            == manifest.byte_length
        )

        observed_bom_present = report_bytes.startswith(
            b"\xef\xbb\xbf"
        )

        bom_matches = (
            observed_bom_present
            is manifest.bom_present
        )

        return RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult(
            digest_matches=digest_matches,
            byte_length_matches=byte_length_matches,
            bom_matches=bom_matches,
        )
```

This is a vocabulary reference only.

Service implementation remains:

```text
HOLD
```

---

# ACCEPTED FUTURE MODEL CONTRACT

The next model contract must freeze:

```text
exact model location
exact class declaration
frozen dataclass behavior
three stored fields
exact Boolean validation
validation order
derived integrity_matches property
immutability
equality
representation
prohibited fields
side-effect absence
```

---

# ACCEPTED FUTURE SERVICE CONTRACT

The later service contract must freeze:

```text
exact service location
exact public method
exact input types
exact error messages
validation order
hashlib.sha256 measurement
hmac.compare_digest comparison
len-based byte-length comparison
UTF-8 BOM-prefix observation
result construction
statelessness
dependency restrictions
upstream preservation
```

---

# PROHIBITED FIRST-CAPABILITY EXPANSION

The first capability must not include:

```text
codec_matches
UTF-8 decoding
JSON parsing
report reconstruction
manifest construction
manifest mutation
digest-manifest digest verification
expected manifest-digest retrieval
result timestamps
result identifiers
computed digest retention
byte retention
manifest retention
subject identifiers
historical subject binding
provenance verification
artifact identity
integrity admission
trust evaluation
registry integration
persistence
receipts
events
logging
alerts
export
transport
batch verification
Merkle verification
hash-chain verification
signature verification
attestation
public disclosure
governance authority
execution authority
```

---

# OWNERSHIP MAP

```text
RuntimeRecordInspectionDigestManifest
→
owns immutable validated expected report-integrity claims
```

```text
RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService
→
owns call-local measurement and comparison of digest, length, and BOM facts
```

```text
RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult
→
owns immutable component outcomes and derived aggregate outcome
```

Future ownership remains unresolved for:

```text
codec provenance
historical subject binding
verification evidence receipts
verification persistence
artifact identity
integrity admission
trust evaluation
registry integration
end-to-end orchestration
```

All remain:

```text
HOLD
```

---

# REDUCTION CONCLUSION

The first embedded report-integrity capability is reduced to:

```text
exact report bytes
+
exact digest manifest
→
digest match
+
byte-length match
+
BOM match
→
immutable partial result
→
derived integrity_matches
```

The service owns measurement and comparison.

The result owns immutable outcomes.

Codec provenance remains outside scope.

The next authorized artifacts are:

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_EMBEDDED_REPORT_INTEGRITY_VERIFICATION_RESULT_IMMUTABLE_MODEL_CONTRACT_001.md
```

followed by:

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_EMBEDDED_REPORT_INTEGRITY_VERIFICATION_IMMUTABLE_SERVICE_CONTRACT_001.md
```

```text
Model implementation: HOLD
Tests: HOLD
Service implementation: HOLD
```

---

# FINAL REDUCTIONS

```text
Valid Manifest
≠
Verified Report Facts
```

```text
Observed Byte Subject
≠
Expected Claim Container
```

```text
Internal Digest Measurement
≠
New Public Digest Capability
```

```text
UTF-8 Decodable
≠
Created By UTF-8 Encoder
```

```text
Combined Verification Bool
≠
Preserved Partial Evidence
```

```text
Derived Aggregate
≠
Caller-Supplied Aggregate
```

```text
Invalid Runtime Input
≠
Integrity Mismatch
```

```text
Partial Mismatch
≠
Verification Execution Failure
```

```text
Digest Mismatch
≠
Tampering Proof
```

```text
Length Mismatch
≠
Cause Attribution
```

```text
Call-Local Pairing
≠
Historical Subject Binding
```

```text
Integrity Facts Match
≠
Identity Established
```

```text
Integrity Match
≠
Integrity Admission
```

```text
Integrity Match
≠
Trust
```

```text
Integrity Match
≠
Authority Granted
```

```text
No proof → No bind → No side effect.
```

**UNKNOWN → HOLD**
