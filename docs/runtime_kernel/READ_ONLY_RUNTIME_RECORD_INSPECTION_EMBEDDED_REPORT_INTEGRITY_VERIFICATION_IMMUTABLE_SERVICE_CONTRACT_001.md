# READ-ONLY RUNTIME RECORD INSPECTION EMBEDDED REPORT INTEGRITY VERIFICATION

# IMMUTABLE SERVICE CONTRACT 001

**Date:** 2026-07-17
**Project:** Research OS
**Development Version:** v2.0.0
**Authority:** IMMUTABLE SERVICE CONTRACT
**Status:** COMPLETE
**Operating Posture:** SUBJECT-FIRST / MEASUREMENT-FIRST / PARTIAL-RESULT-PRESERVING / CONSTANT-TIME / DETERMINISTIC / NON-ADMITTING / UNKNOWN → HOLD

---

# PURPOSE

Freeze the exact production location, service declaration, public method, input roles, runtime types, validation order, SHA-256 measurement, constant-time digest comparison, byte-length comparison, UTF-8 BOM-prefix observation, result construction, dependency boundary, service state, side-effect prohibition, upstream preservation, and test authorization for the first Read-Only Runtime Record Inspection Embedded Report Integrity Verification capability.

This contract follows:

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_EMBEDDED_REPORT_INTEGRITY_VERIFICATION_EXISTING_DIGEST_LENGTH_CODEC_BOM_PARTIAL_RESULT_SUBJECT_BINDING_ADMISSION_AND_AUTHORITY_BOUNDARY_INSPECTION_001.md
```

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_EMBEDDED_REPORT_INTEGRITY_VERIFICATION_VOCABULARY_INPUT_OWNERSHIP_PARTIAL_RESULT_DIGEST_LENGTH_BOM_AND_SCOPE_REDUCTION_001.md
```

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_EMBEDDED_REPORT_INTEGRITY_VERIFICATION_RESULT_IMMUTABLE_MODEL_CONTRACT_001.md
```

The following result model is already implemented and frozen:

```text
RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult
```

Production implementation remains:

```text
HOLD
```

until the service test contract exists, the authorized test module exists, the expected missing-module failure is observed, and the test-first checkpoint is committed and synchronized.

---

# CAPABILITY NAME

The frozen capability name is:

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

The authorized checks are:

```text
SHA-256 digest match
byte-length match
UTF-8 BOM-prefix match
```

---

# PRODUCTION LOCATION

The exact future production file is:

```text
services/runtime_record_inspection_embedded_report_integrity_verification_service.py
```

No alternative location is authorized.

---

# SERVICE DECLARATION

The exact service declaration is:

```python
class RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService:
```

No inheritance is required.

The service must not inherit from:

```text
Inspectable
ABC
Protocol
verification base class
integrity base class
admission service
trust service
artifact model
```

---

# REQUIRED IMPORTS

The production service imports exactly:

```python
import hashlib
import hmac

from models.runtime_record_inspection_digest_manifest import (
    RuntimeRecordInspectionDigestManifest,
)
from models.runtime_record_inspection_embedded_report_integrity_verification_result import (
    RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult,
)
```

No other import is authorized.

---

# CONSTRUCTOR CONTRACT

The service requires no constructor arguments.

Accepted construction:

```python
service = RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService()
```

No explicit `__init__` method is required.

The service owns no mutable state.

The constructor must not:

```text
accept a hasher
accept a digest verifier
accept a manifest service
accept a registry
accept a path
accept configuration
accept a clock
accept an identifier generator
create files
create directories
read environment variables
publish events
register itself
cache results
```

---

# PUBLIC METHOD CONTRACT

The exact public method name is:

```text
verify_integrity
```

The exact declaration is:

```python
def verify_integrity(
    self,
    report_bytes: bytes,
    manifest: RuntimeRecordInspectionDigestManifest,
) -> RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult:
```

No optional argument is authorized.

No algorithm argument is authorized.

No codec argument is authorized.

No subject identifier is authorized.

No provenance argument is authorized.

No admission argument is authorized.

No authority argument is authorized.

---

# EXACT PUBLIC SURFACE

The only capability-specific public method is:

```text
verify_integrity
```

The service must not expose:

```text
verify
verify_report
verify_digest
verify_manifest
verify_bytes
compare
compare_digest
calculate_digest
calculate_length
inspect_bom
decode
parse
save
load
persist
export
write
read
publish
upload
download
register
inspect
health
status
verify_collection
create_receipt
admit
approve
trust
authorize
```

Standard Python object dunder behavior is outside this restriction.

---

# REPORT-BYTES INPUT ROLE

The first input is:

```text
report_bytes
```

Meaning:

```text
the current byte sequence whose report-integrity facts
are measured against the supplied digest manifest
```

The service must not construct these bytes internally.

---

# MANIFEST INPUT ROLE

The second input is:

```text
manifest
```

Meaning:

```text
the immutable validated expected-claim container
against which the supplied report bytes are measured
```

```text
Observed Byte Subject
≠
Expected Claim Container
```

---

# EXACT REPORT-BYTES TYPE

The accepted runtime type is exact plain Python:

```text
bytes
```

The exact validation rule is:

```python
if type(report_bytes) is not bytes:
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

---

# REPORT-BYTES TYPE ERROR

Invalid report-bytes runtime type raises exactly:

```text
TypeError
```

with the exact message:

```text
report_bytes must be an exact bytes
```

---

# EXACT MANIFEST TYPE

The accepted runtime type is exactly:

```text
RuntimeRecordInspectionDigestManifest
```

The exact validation rule is:

```python
if type(manifest) is not RuntimeRecordInspectionDigestManifest:
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

---

# MANIFEST TYPE ERROR

Invalid manifest runtime type raises exactly:

```text
TypeError
```

with the exact message:

```text
manifest must be an exact RuntimeRecordInspectionDigestManifest
```

---

# INPUT VALIDATION ORDER

The exact validation order is:

```text
report_bytes runtime type
→
manifest runtime type
→
SHA-256 measurement
→
constant-time digest comparison
→
byte-length comparison
→
UTF-8 BOM-prefix observation
→
immutable result construction
```

No measurement may occur before both runtime types are valid.

---

# EMPTY-BYTES CONTRACT

Exact empty bytes are accepted.

The service must not require:

```text
non-empty content
valid UTF-8
valid JSON
valid report semantics
known report schema
```

```text
Hashable Bytes
≠
Confirmed Inspection Report
```

---

# ARBITRARY-BYTES CONTRACT

The service accepts arbitrary exact bytes, including:

```python
b""
b"abc"
b"\x00"
b"\xff"
b"\xef\xbb\xbf"
b"\xef\xbb\xbf{}"
```

It performs byte-level integrity checks only.

It must not decode or parse the bytes.

---

# SHA-256 MEASUREMENT CONTRACT

The exact digest measurement is:

```python
computed_digest = hashlib.sha256(
    report_bytes
).hexdigest()
```

The measurement is internal to verification.

The service must not expose a public digest-generation method.

```text
Internal Digest Measurement
≠
New Public Digest Capability
```

---

# DIGEST COMPARISON CONTRACT

The measured digest is compared with:

```text
manifest.sha256_digest
```

using exactly:

```python
digest_matches = hmac.compare_digest(
    computed_digest,
    manifest.sha256_digest,
)
```

Plain equality must not own digest comparison.

```text
Digest Value Equality
≠
Constant-Time Digest Comparison
```

---

# DIGEST RESULT CONTRACT

The computed `digest_matches` value must be exact:

```text
bool
```

A digest mismatch is a valid result.

It must not raise an exception.

```text
Digest Mismatch
≠
Verification Execution Failure
```

---

# BYTE-LENGTH COMPARISON CONTRACT

The exact comparison is:

```python
byte_length_matches = (
    len(report_bytes)
    == manifest.byte_length
)
```

The result must be exact:

```text
bool
```

A length mismatch is a valid result.

It must not raise an exception.

---

# UTF-8 BOM MARKER

The exact UTF-8 BOM prefix is:

```python
b"\xef\xbb\xbf"
```

Observed BOM presence is:

```python
observed_bom_present = report_bytes.startswith(
    b"\xef\xbb\xbf"
)
```

---

# BOM COMPARISON CONTRACT

The exact comparison is:

```python
bom_matches = (
    observed_bom_present
    is manifest.bom_present
)
```

Because the manifest contract requires:

```text
bom_present is False
```

the result is true only when the supplied bytes do not begin with the UTF-8 BOM marker.

---

# BOM RESULT CONTRACT

The computed `bom_matches` value must be exact:

```text
bool
```

A BOM mismatch is a valid result.

It must not raise an exception.

---

# CODEC EXCLUSION

The service must not produce:

```text
codec_matches
```

The service must not decode:

```python
report_bytes.decode("utf-8")
```

The service makes no encoding-provenance claim.

```text
UTF-8 Decodable
≠
Created By UTF-8 Encoder
```

Codec verification remains:

```text
HOLD
```

---

# RESULT CONSTRUCTION CONTRACT

The service returns exactly:

```text
RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult
```

The exact construction is:

```python
return RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult(
    digest_matches=digest_matches,
    byte_length_matches=byte_length_matches,
    bom_matches=bom_matches,
)
```

The service must not pass:

```text
integrity_matches
```

to the constructor.

The aggregate result remains derived by the result model.

---

# RESULT OUTPUT TYPE

The exact output runtime type is:

```text
RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult
```

The service must not return:

```text
bool
dict
tuple
list
string
enum
receipt
manifest
None
```

---

# PARTIAL RESULT PRESERVATION

The service must preserve independent component outcomes.

Valid results include:

```text
False, True, True
True, False, True
True, True, False
False, False, True
False, True, False
True, False, False
False, False, False
```

No partial mismatch may be collapsed into a single Boolean return.

```text
Combined Verification Bool
≠
Preserved Partial Evidence
```

---

# FULL MATCH

A full match produces:

```text
digest_matches = True
byte_length_matches = True
bom_matches = True
integrity_matches = True
```

This means only that all authorized checks matched.

---

# PARTIAL MISMATCH

A partial mismatch remains a valid immutable result.

It is not:

```text
invalid input
exception
complete integrity
complete failure
tampering proof
```

```text
Partial Mismatch
≠
Verification Execution Failure
```

---

# COMPLETE MISMATCH

A complete mismatch may produce:

```text
digest_matches = False
byte_length_matches = False
bom_matches = False
integrity_matches = False
```

This remains a valid result.

It does not prove tampering, corruption, malice, or cause.

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

# DIGEST-MISMATCH BOUNDARY

A digest mismatch proves only:

```text
SHA-256(report_bytes)
differs from
manifest.sha256_digest
```

It does not prove:

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

# LENGTH-MISMATCH BOUNDARY

A byte-length mismatch proves only:

```text
len(report_bytes)
differs from
manifest.byte_length
```

It does not prove:

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

# BOM-MISMATCH BOUNDARY

A BOM mismatch proves only:

```text
the observed UTF-8 BOM-prefix state differs
from manifest.bom_present
```

It does not prove:

```text
invalid UTF-8
invalid JSON
unsafe content
malicious modification
```

---

# SUBJECT-BINDING BOUNDARY

The service compares one supplied byte value with one supplied manifest.

This establishes call-local pairing only.

It does not establish:

```text
historical subject binding
original creation relationship
shared custody
registry relationship
artifact identity
```

```text
Call-Local Pairing
≠
Historical Subject Binding
```

---

# PROVENANCE BOUNDARY

The service does not establish:

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

# SERVICE STATE CONTRACT

The service is stateless.

It retains no:

```text
last report bytes
last manifest
last computed digest
last result
call count
cache
history
clock
registry
path
authority state
```

Calling `verify_integrity` must not add mutable instance state.

Multiple service instances must behave equivalently.

---

# DETERMINISM CONTRACT

For unchanged exact inputs, the service must return an equal immutable result.

The result must not depend on:

```text
current time
randomness
identifier generation
environment variables
filesystem state
network state
registry state
service instance identity
process identity
locale
timezone
```

---

# FILESYSTEM BOUNDARY

The service must not:

```text
open files
read files
write files
create directories
accept paths
return paths
```

The capability ends when the result is returned.

---

# PERSISTENCE BOUNDARY

The service must not:

```text
save results
load artifacts
create receipts
write databases
update registries
```

---

# EVENT AND LOGGING BOUNDARY

The service must publish no:

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

The service must perform no:

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

The service accepts exactly one pair:

```text
one report_bytes
+
one manifest
```

It must not support:

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

The service does not verify:

```text
signatures
certificates
attestations
signer identity
keys
```

---

# FROZEN RESULT-MODEL PRESERVATION

The implemented model remains:

```text
models/runtime_record_inspection_embedded_report_integrity_verification_result.py
```

The service must use it without modification.

The model remains measurement-unaware.

It must not gain:

```text
hashlib
hmac
report_bytes
manifest
computed_digest
len(
startswith(
verify_integrity
```

---

# FROZEN MANIFEST-MODEL PRESERVATION

The existing manifest remains:

```text
models/runtime_record_inspection_digest_manifest.py
```

It must remain unchanged.

It must not gain:

```text
verify_integrity
digest_matches
byte_length_matches
bom_matches
integrity_matches
report_bytes
```

---

# FROZEN UPSTREAM PRESERVATION

The following components remain unchanged:

```text
models/runtime_record_inspection_digest_manifest.py
models/runtime_record_inspection_embedded_report_integrity_verification_result.py
services/runtime_record_inspection_digest_manifest_service.py
services/runtime_record_inspection_representation_service.py
services/runtime_record_inspection_json_encoding_service.py
services/runtime_record_inspection_utf8_byte_encoding_service.py
services/runtime_record_inspection_sha256_digest_service.py
services/runtime_record_inspection_digest_manifest_digest_verification_service.py
```

---

# PROHIBITED IMPORTS

The production service must not import:

```text
pathlib
os
sys
tempfile
datetime
time
uuid
random
secrets
json
codecs
io
sqlite3
requests
urllib
socket
event engines
registries
third-party libraries
```

Only the frozen imports are authorized.

---

# SOURCE RESTRICTIONS

Production source must not contain prohibited behavior fragments including:

```text
open(
Path(
write_text
write_bytes
mkdir
touch(
unlink(
rename(
datetime.now
datetime.utcnow
time.time
uuid
random
secrets
report_bytes.decode(
json.loads
json.dumps
codec_matches
verify_collection
verify_batch
merkle
hash_chain
signature
certificate
attestation
publish
emit
logger
notification
alert
save
load
persist
export
upload
download
stream
send
transfer
```

---

# REQUIRED SERVICE TEST SURFACE

The future service test contract must cover at minimum:

1. exact production-file location
2. exact service class name
3. constructor requires no arguments
4. independent service instances
5. exact public method
6. prohibited public methods absent
7. exact report-bytes type validation
8. report-bytes subclass rejection
9. exact manifest type validation
10. manifest subclass rejection
11. exact TypeError messages
12. validation order
13. empty bytes accepted
14. arbitrary bytes accepted
15. SHA-256 measurement
16. exact digest subject
17. constant-time digest comparison
18. no plain-equality digest comparison
19. byte-length comparison
20. BOM-prefix observation
21. BOM comparison against manifest fact
22. no codec check
23. no UTF-8 decoding
24. exact result type
25. exact result component propagation
26. aggregate not supplied
27. full match
28. digest-only mismatch
29. length-only mismatch
30. BOM-only mismatch
31. multiple partial mismatches
32. complete mismatch
33. mismatch does not raise
34. malformed input distinguished from mismatch
35. deterministic repeated output
36. cross-instance determinism
37. statelessness
38. no filesystem effects
39. no persistence
40. no events or logging
41. no export or transport
42. no collection verification
43. no Merkle or hash-chain verification
44. no signature verification
45. frozen result-model preservation
46. frozen manifest-model preservation
47. frozen upstream preservation
48. exact import boundary
49. prohibited dependency checks
50. authorized production-file existence

---

# AUTHORIZED SERVICE TEST FILE

The exact future test location is:

```text
tests/runtime/test_runtime_record_inspection_embedded_report_integrity_verification_service.py
```

No service implementation is authorized until:

1. the service test contract document exists
2. the authorized service test module exists
3. the expected missing-module failure is observed
4. the service test-first checkpoint is committed and pushed

---

# EXPECTED TEST-FIRST FAILURE

Before the service exists, running:

```powershell
python -m pytest tests\runtime\test_runtime_record_inspection_embedded_report_integrity_verification_service.py -q
```

must fail during collection with an error equivalent to:

```text
ModuleNotFoundError:
No module named 'services.runtime_record_inspection_embedded_report_integrity_verification_service'
```

---

# ACCEPTED MINIMUM IMPLEMENTATION SHAPE

The future minimum implementation is structurally equivalent to:

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
                "manifest must be an exact RuntimeRecordInspectionDigestManifest"
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

This code is contractual reference only.

Production implementation remains:

```text
HOLD
```

---

# OWNERSHIP MAP

```text
RuntimeRecordInspectionDigestManifest
→
owns immutable validated expected claims
```

```text
RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService
→
owns call-local byte measurement and comparison
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

# CONTRACT CONCLUSION

The immutable service contract is frozen as:

```text
exact report bytes
+
exact digest manifest
→
SHA-256 measurement
→
constant-time digest comparison
+
byte-length comparison
+
UTF-8 BOM-prefix comparison
→
immutable partial result
```

with:

```text
exact runtime types
exact TypeError behavior
fixed validation order
empty bytes accepted
arbitrary bytes accepted
no decoding
no parsing
no codec claim
partial mismatch preservation
derived aggregate ownership
stateless behavior
deterministic output
no persistence
no admission
no trust
no authority
```

The next authorized artifact is:

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_EMBEDDED_REPORT_INTEGRITY_VERIFICATION_TEST_CONTRACT_001.md
```

Service tests are now authorized.

Production implementation remains:

```text
HOLD
```

---

# FINAL CONTRACT

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
Digest Value Equality
≠
Constant-Time Digest Comparison
```

```text
Combined Verification Bool
≠
Preserved Partial Evidence
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
UTF-8 Decodable
≠
Created By UTF-8 Encoder
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
