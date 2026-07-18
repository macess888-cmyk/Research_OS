# READ-ONLY RUNTIME RECORD INSPECTION DIGEST MANIFEST DIGEST VERIFICATION

# VOCABULARY, INPUT ROLES, SYNTAX, CONSTANT-TIME BOOLEAN RESULT, MISMATCH, AND SCOPE REDUCTION 001

**Date:** 2026-07-17
**Project:** Research OS
**Development Version:** v2.0.0
**Authority:** VOCABULARY AND SCOPE REDUCTION ONLY
**Status:** COMPLETE
**Operating Posture:** COMPARISON-FIRST / SYNTAX-FIRST / CONSTANT-TIME / DETERMINISTIC / NON-ADMITTING / UNKNOWN → HOLD

---

# PURPOSE

Freeze the vocabulary, input roles, exact runtime types, SHA-256 hexadecimal syntax, validation order, constant-time comparison rule, Boolean result semantics, mismatch meaning, error boundaries, ownership boundaries, dependency direction, and prohibited expansion for the first Read-Only Runtime Record Inspection Digest Manifest Digest Verification capability.

This reduction follows:

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_DIGEST_MANIFEST_DIGEST_VERIFICATION_EXISTING_COMPARISON_CONSTANT_TIME_SYNTAX_RESULT_MISMATCH_ADMISSION_AND_AUTHORITY_BOUNDARY_INSPECTION_001.md
```

That inspection established:

1. no production digest-verification service exists
2. no verification-result model exists
3. the existing SHA-256 services generate digests only
4. verification requires a separate semantic owner
5. the service should accept one computed digest and one expected digest
6. both inputs should be exact plain strings
7. both values must satisfy frozen lowercase SHA-256 hexadecimal syntax
8. invalid runtime type and invalid digest syntax are distinct
9. valid mismatch should return `False`
10. valid match should return `True`
11. malformed digest syntax must not collapse into mismatch
12. a Boolean result is sufficient for the first capability
13. no result model is required
14. comparison should use `hmac.compare_digest`
15. digest generation remains upstream
16. verification must not accept bytes, manifests, JSON, or primitive dictionaries
17. verification does not verify the embedded inspection-report digest
18. verification does not establish subject binding
19. verification does not establish provenance
20. verification does not establish admission
21. verification does not establish trust
22. verification does not establish authority
23. persistence, events, export, transport, and orchestration remain separate
24. all frozen upstream services can remain unchanged

This document authorizes creation of an immutable service contract.

```text
Tests: HOLD
Implementation: HOLD
```

---

# ACCEPTED CAPABILITY NAME

The accepted capability name is:

```text
Read-Only Runtime Record Inspection Digest Manifest Digest Verification
```

The capability performs:

```text
one valid computed digest-manifest SHA-256 hexadecimal string
+
one valid expected digest-manifest SHA-256 hexadecimal string
→
one deterministic Boolean comparison result
```

The capability does not perform:

```text
digest generation
byte encoding
JSON encoding
manifest construction
manifest inspection
manifest mutation
embedded report-digest verification
byte-length verification
codec verification
BOM verification
provenance verification
subject binding
identity verification
content addressing
admission
trust evaluation
governance
execution
persistence
export
transport
publication
```

---

# ACCEPTED OWNER

The accepted service name is:

```text
RuntimeRecordInspectionDigestManifestDigestVerificationService
```

The accepted future production location is:

```text
services/runtime_record_inspection_digest_manifest_digest_verification_service.py
```

The service owns:

```text
valid computed digest string
+
valid expected digest string
→
constant-time Boolean comparison
```

It does not own:

```text
digest calculation
manifest reconstruction
expected-digest retrieval
expected-digest trust
verification evidence persistence
admission decisions
authority decisions
```

---

# OWNERSHIP SEPARATION

Digest generation remains owned by:

```text
RuntimeRecordInspectionDigestManifestSha256DigestService
```

Digest verification becomes owned by:

```text
RuntimeRecordInspectionDigestManifestDigestVerificationService
```

Required separation:

```text
Digest Generation
≠
Digest Verification
```

```text
Digest Availability
≠
Comparison Authority
```

```text
Comparison Result
≠
Admission Decision
```

---

# REJECTED OWNER OPTIONS

The following ownership choices are rejected:

```text
add verify_digest to RuntimeRecordInspectionDigestManifestSha256DigestService
add digest comparison to RuntimeRecordInspectionDigestManifest
add verification to RuntimeRecordInspectionDigestManifestService
add verification to the representation service
add verification to the JSON encoder
add verification to the UTF-8 byte encoder
create a generic integrity service
create an admission service
create a trust service
create an orchestration service
```

Reasons:

```text
hasher-owned verification collapses generation and comparison
model-owned verification adds behavior to immutable evidence
manifest-service verification collapses construction and checking
representation-owned verification collapses representation and integrity
generic integrity ownership exceeds the narrow first subject
admission and trust exceed Boolean comparison authority
orchestration composes capabilities not yet authorized
```

---

# ACCEPTED PUBLIC METHOD

The accepted public method is:

```text
verify_digest
```

The accepted conceptual signature is:

```python
def verify_digest(
    self,
    computed_digest: str,
    expected_digest: str,
) -> bool:
```

No optional arguments are authorized.

No algorithm argument is authorized.

No normalization argument is authorized.

No subject argument is authorized.

No provenance argument is authorized.

No admission argument is authorized.

No authority argument is authorized.

---

# INPUT ROLE VOCABULARY

The first input is:

```text
computed_digest
```

Meaning:

```text
the digest calculated from the current digest-manifest UTF-8 bytes
```

The second input is:

```text
expected_digest
```

Meaning:

```text
the caller-supplied digest value against which the computed digest is checked
```

These roles must remain explicit.

Although equality comparison is mathematically symmetric:

```text
computed_digest == expected_digest
```

the evidence roles are not semantically interchangeable.

```text
Comparison Symmetry
≠
Semantic Role Equivalence
```

---

# COMPUTED DIGEST OWNERSHIP

The computed digest is expected to originate from:

```text
RuntimeRecordInspectionDigestManifestSha256DigestService
```

Expected upstream flow:

```text
digest-manifest UTF-8 bytes
→
RuntimeRecordInspectionDigestManifestSha256DigestService
→
computed_digest
```

The verification service must not:

```text
accept manifest bytes
calculate the digest
import hashlib
instantiate the SHA-256 service
delegate digest generation
```

The caller owns composition.

---

# EXPECTED DIGEST OWNERSHIP

The expected digest is caller-supplied.

The service does not establish whether that value came from:

```text
trusted storage
a registry
a sidecar
an earlier receipt
a transport header
operator input
another runtime
another repository
an external authority
```

The source remains outside the first capability.

```text
Expected Digest Supplied
≠
Expected Digest Trusted
```

```text
Expected Digest Available
≠
Expected Digest Provenance Established
```

---

# EXACT RUNTIME INPUT TYPES

Both inputs must be exact plain Python strings.

Required runtime rules:

```python
type(computed_digest) is str
```

```python
type(expected_digest) is str
```

The service must reject:

```text
None
bool
int
float
bytes
bytearray
memoryview
list
tuple
set
frozenset
dict
mapping
string subclass
hash object
manifest model
manifest primitive dictionary
manifest JSON text wrapper
manifest UTF-8 bytes
path
file
stream
```

---

# STRING-SUBCLASS REJECTION

String subclasses are rejected.

```text
String Compatibility
≠
Exact Plain String
```

The service must not use:

```python
isinstance(value, str)
```

for accepted-input validation.

It should use exact runtime-type checks.

---

# COMPUTED DIGEST TYPE ERROR

If `computed_digest` is not an exact plain string, the service should raise:

```text
TypeError
```

Recommended exact message:

```text
computed_digest must be an exact str
```

---

# EXPECTED DIGEST TYPE ERROR

If `expected_digest` is not an exact plain string, the service should raise:

```text
TypeError
```

Recommended exact message:

```text
expected_digest must be an exact str
```

The two roles should retain role-specific error wording.

---

# TYPE VALIDATION ORDER

The accepted validation order begins with:

```text
computed digest runtime type
→
expected digest runtime type
```

No syntax validation should occur for a value whose runtime type is invalid.

No comparison should occur until both runtime types are valid.

---

# SHA-256 HEXADECIMAL SYNTAX

Both values must independently satisfy:

```text
exact length: 64 characters
allowed characters: 0-9 and a-f
lowercase only
no prefix
no whitespace
no separators
no newline
no carriage return
```

Valid syntax:

```text
ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
```

Invalid syntax includes:

```text
empty string
short digest
long digest
uppercase hexadecimal
mixed-case hexadecimal
sha256: prefix
SHA256: prefix
0x prefix
spaces
tabs
newline
carriage return
colon separators
hyphen separators
non-hexadecimal characters
Unicode lookalike characters
```

---

# COMPUTED DIGEST VALUE ERROR

If `computed_digest` is an exact string but does not satisfy the frozen syntax, the service should raise:

```text
ValueError
```

Recommended exact message:

```text
computed_digest must be a lowercase 64-character SHA-256 hexadecimal string
```

---

# EXPECTED DIGEST VALUE ERROR

If `expected_digest` is an exact string but does not satisfy the frozen syntax, the service should raise:

```text
ValueError
```

Recommended exact message:

```text
expected_digest must be a lowercase 64-character SHA-256 hexadecimal string
```

---

# TYPE INVALIDITY VERSUS VALUE INVALIDITY

Required distinction:

```text
Wrong Runtime Type
→
TypeError
```

```text
Correct Runtime Type With Invalid Digest Syntax
→
ValueError
```

```text
Type Invalidity
≠
Value Invalidity
```

---

# INVALID SYNTAX VERSUS MISMATCH

Malformed input and valid disagreement are separate states.

```text
Invalid Digest Syntax
≠
Digest Mismatch
```

Invalid syntax means:

```text
one or both supplied strings are not valid frozen SHA-256 hexadecimal values
```

Mismatch means:

```text
both supplied strings are valid
+
their values differ
```

Invalid syntax raises an exception.

Valid mismatch returns:

```text
False
```

---

# VALID MATCH RESULT

For two valid equal digest strings:

```python
service.verify_digest(
    computed_digest,
    expected_digest,
)
```

returns exactly:

```text
True
```

Required relation:

```text
Valid Equal Digest Strings
→
True
```

---

# VALID MISMATCH RESULT

For two valid unequal digest strings:

```python
service.verify_digest(
    computed_digest,
    expected_digest,
)
```

returns exactly:

```text
False
```

Required relation:

```text
Valid Unequal Digest Strings
→
False
```

A valid mismatch must not raise an exception.

```text
Mismatch
≠
Verification Execution Failure
```

---

# ACCEPTED RESULT TYPE

The accepted result is exactly:

```text
bool
```

Required concrete types:

```python
type(True) is bool
type(False) is bool
```

The service must not return:

```text
integer
string
tuple
dictionary
status enum
verification model
receipt
manifest
exception for mismatch
None
```

---

# BOOLEAN RESULT MEANING

The result means only:

```text
True
=
the two supplied valid digest strings compare equal
```

```text
False
=
the two supplied valid digest strings compare unequal
```

It does not mean:

```text
artifact admitted
artifact trusted
artifact authentic
artifact current
artifact safe
artifact complete
source proven
provenance verified
authority granted
```

---

# RESULT MODEL DECISION

No result model is authorized for the first capability.

The first capability must not create:

```text
RuntimeRecordInspectionDigestManifestVerificationResult
verification receipt
verification evidence object
comparison artifact
status model
reason model
```

A later evidence model would require separate inspection of:

```text
subject binding
computed digest retention
expected digest retention
provenance
timestamp
identity
persistence
admission
authority
```

---

# CONSTANT-TIME COMPARISON

The accepted comparison mechanism is:

```python
hmac.compare_digest(
    computed_digest,
    expected_digest,
)
```

The service should import exactly:

```python
import hmac
```

The comparison must occur only after:

```text
both runtime types are valid
both digest syntaxes are valid
```

---

# PLAIN EQUALITY PROHIBITION

The production comparison should not use:

```python
computed_digest == expected_digest
```

The first capability adopts the standard-library constant-time comparison primitive.

```text
Value Equality
≠
Constant-Time Digest Comparison
```

---

# HMAC MODULE BOUNDARY

Using:

```python
hmac.compare_digest
```

does not authorize:

```text
HMAC generation
keyed hashing
secret-key handling
message authentication codes
signature behavior
```

The service must not use:

```text
hmac.new
hmac.digest
digestmod
key
secret
nonce
salt
```

```text
hmac.compare_digest
≠
HMAC Generation
```

---

# DIGEST NORMALIZATION PROHIBITION

The service must not normalize digest values.

It must not:

```text
convert uppercase to lowercase
trim whitespace
remove prefixes
remove line endings
remove separators
pad short digests
truncate long digests
decode bytes
coerce objects to strings
```

Malformed syntax must remain malformed.

```text
Input Normalization
≠
Verification
```

---

# SYNTAX VALIDATION MECHANICS

The syntax rule may be implemented through a deterministic condition equivalent to:

```python
len(value) == 64
and all(
    character in "0123456789abcdef"
    for character in value
)
```

A compiled regular expression may also satisfy the semantic contract if separately frozen.

The first implementation should prefer the smallest transparent mechanism.

---

# VALIDATION ORDER

The accepted complete validation order is:

```text
computed digest runtime type
→
expected digest runtime type
→
computed digest syntax
→
expected digest syntax
→
constant-time comparison
→
Boolean result
```

No later stage may occur if an earlier stage fails.

---

# DIGEST GENERATION PROHIBITION

The verification service must not:

```text
import hashlib
accept bytes
calculate SHA-256
call hexdigest
instantiate RuntimeRecordInspectionDigestManifestSha256DigestService
derive computed_digest from a manifest
derive expected_digest from storage
```

```text
Digest Generation
≠
Digest Verification
```

---

# SUBJECT INPUT BOUNDARY

The service compares digest strings only.

It must not accept:

```text
RuntimeRecordInspectionDigestManifest
manifest primitive dictionary
manifest JSON string as artifact input
manifest UTF-8 bytes
inspection-report bytes
file
path
stream
registry entry
```

```text
Digest Comparison
≠
Artifact Comparison
```

---

# EMBEDDED REPORT-DIGEST BOUNDARY

The digest manifest contains an upstream inspection-report digest.

The new service compares the external digest of the manifest itself.

It does not verify:

```text
the embedded inspection-report digest
inspection-report bytes
inspection-report byte length
inspection-report codec
inspection-report BOM declaration
inspection-report provenance
```

```text
Manifest-Digest Verification
≠
Embedded Report-Digest Verification
```

---

# SUBJECT-BINDING BOUNDARY

The service does not prove that either supplied digest belongs to:

```text
a specific digest manifest
a specific inspection report
a specific runtime record
a specific registry
a specific execution
a specific timestamp
a specific authority
```

```text
Digest Match
≠
Subject Binding
```

Subject binding remains:

```text
HOLD
```

---

# PROVENANCE BOUNDARY

The service does not prove:

```text
who generated the expected digest
when it was generated
where it was stored
whether it was altered
whether it belongs to the current manifest
whether it belongs to the current repository
whether it belongs to the current runtime
```

```text
Digest Equality
≠
Provenance Equality
```

---

# TRUST BOUNDARY

A `True` result means only that two valid supplied strings compare equal.

It does not establish:

```text
expected digest trustworthiness
source authenticity
artifact legitimacy
artifact safety
artifact completeness
artifact freshness
registry admission
governance approval
```

```text
Digest Match
≠
Trust
```

---

# ADMISSION BOUNDARY

The service must not:

```text
admit the manifest
approve the manifest
register the manifest
promote evidence
change lifecycle state
authorize execution
mark an artifact verified in storage
```

```text
Digest Match
≠
Integrity Admission
```

Admission remains:

```text
HOLD
```

---

# MISMATCH MEANING

A `False` result means:

```text
the two valid digest strings differ
```

It does not identify:

```text
which digest is correct
which digest is stale
which artifact changed
when a change occurred
who caused a change
whether corruption occurred
whether tampering occurred
whether the expected digest belongs to another subject
```

```text
Digest Mismatch
≠
Tampering Proof
```

```text
Digest Mismatch
≠
Cause Attribution
```

---

# COMPLETE INTEGRITY BOUNDARY

Digest equality is one comparison fact.

It is not a complete integrity proof.

Complete integrity may additionally require:

```text
trusted expected digest
subject binding
provenance
byte reconstruction
algorithm agreement
artifact identity
time context
admission rules
authority rules
```

```text
Digest Equality
≠
Complete Integrity Proof
```

---

# DETERMINISM

For unchanged valid inputs:

```python
service.verify_digest(
    computed_digest,
    expected_digest,
)
```

must always return the same Boolean value.

The service introduces no:

```text
timestamp
identifier
random value
salt
nonce
key
environment dependency
filesystem dependency
network dependency
registry dependency
cache
counter
global state
```

---

# SERVICE STATE

The service requires no constructor arguments.

It retains no:

```text
last computed digest
last expected digest
last result
call count
cache
verification history
clock
registry
path
authority state
```

The service is stateless.

---

# IMPORT BOUNDARY

The future service should import exactly:

```python
import hmac
```

It must not import:

```text
hashlib
models
other services
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
database libraries
network libraries
event engines
third-party libraries
```

---

# FROZEN HASHER PRESERVATION

The frozen digest-manifest hasher remains:

```text
services/runtime_record_inspection_digest_manifest_sha256_digest_service.py
```

It must remain unchanged and verification-unaware.

It must not gain:

```text
verify_digest
compare_digest
expected_digest
matches
is_valid
```

---

# INSPECTION-REPORT HASHER PRESERVATION

The frozen inspection-report hasher remains:

```text
services/runtime_record_inspection_sha256_digest_service.py
```

It remains unchanged and generation-only.

---

# DIGEST-MANIFEST MODEL PRESERVATION

The frozen model remains:

```text
models/runtime_record_inspection_digest_manifest.py
```

It must remain unchanged.

It must not gain:

```text
computed_digest
expected_digest
verified
matches
verification_status
verification_reason
verify
```

---

# DIGEST-MANIFEST PIPELINE PRESERVATION

The following frozen components remain unchanged:

```text
RuntimeRecordInspectionDigestManifest
RuntimeRecordInspectionDigestManifestService
RuntimeRecordInspectionDigestManifestRepresentationService
RuntimeRecordInspectionDigestManifestJsonEncodingService
RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService
RuntimeRecordInspectionDigestManifestSha256DigestService
```

The caller owns composition.

---

# FILESYSTEM SCOPE

Filesystem behavior remains:

```text
HOLD
```

The service must not:

```text
open files
read expected digests from files
write results
create directories
read sidecars
write receipts
accept paths
return paths
```

The capability ends when the Boolean result is returned.

---

# PERSISTENCE SCOPE

Persistence remains:

```text
HOLD
```

The service must not:

```text
save verification results
load expected digest records
persist comparison evidence
register outcomes
create audit records
write databases
```

```text
Boolean Verification Result
≠
Persisted Verification Evidence
```

---

# EVENT AND LOGGING SCOPE

Event publication and logging remain:

```text
HOLD
```

The service must not publish:

```text
verification events
mismatch events
audit events
notifications
alerts
logs
```

```text
Comparison Result
≠
Event Publication
```

---

# EXPORT AND TRANSPORT SCOPE

Export and transport remain:

```text
HOLD
```

The service must not:

```text
export results
publish results
upload results
send results
stream results
transmit digests
```

It accepts no destination or transport configuration.

---

# COLLECTION SCOPE

The service compares one digest pair only.

It must reject:

```text
list of computed digests
list of expected digests
tuple of digest pairs
digest map
manifest collection
registry snapshot
batch verification request
```

```text
Single Digest-Pair Verification
≠
Batch Verification
```

---

# MERKLE AND HASH-CHAIN SCOPE

The service must not verify:

```text
Merkle roots
Merkle proofs
hash chains
digest chains
aggregate digests
collection digests
```

These remain separate capabilities.

---

# SIGNATURE SCOPE

The service does not verify signatures.

It must not:

```text
load keys
verify signatures
inspect certificates
verify attestations
establish signer identity
```

```text
Digest Match
≠
Signature Validity
```

---

# PUBLIC DISCLOSURE SCOPE

Public disclosure remains:

```text
HOLD
```

The service grants no permission to disclose:

```text
the digest manifest
the digest values
the verification result
the inspection report
the registry state
```

```text
Digest Match
≠
Publicly Disclosable
```

---

# AUTHORITY SCOPE

The Boolean result does not establish:

```text
authorization
governance authority
execution permission
publication permission
export permission
admission authority
trust authority
corrective authority
```

```text
Verification True
≠
Authority Granted
```

```text
Verification False
≠
Authority Revoked
```

---

# PROHIBITED PUBLIC METHODS

The first service must not expose:

```text
compare
compare_digests
matches
is_valid
validate
hash
digest
to_sha256_hexdigest
verify_manifest
verify_bytes
verify_report_digest
verify_signature
save
load
persist
export
publish
register
inspect
health
status
verify_collection
```

The only capability-specific public method is:

```text
verify_digest
```

---

# ACCEPTED PRODUCTION LOCATION

The accepted future production location is:

```text
services/runtime_record_inspection_digest_manifest_digest_verification_service.py
```

No alternative location is authorized.

---

# ACCEPTED TEST LOCATION

The accepted future test location is:

```text
tests/runtime/test_runtime_record_inspection_digest_manifest_digest_verification_service.py
```

Tests remain HOLD until the immutable service contract is frozen.

---

# MINIMUM IMPLEMENTATION SHAPE

The future minimum implementation is expected to be structurally equivalent to:

```python
import hmac


class RuntimeRecordInspectionDigestManifestDigestVerificationService:
    def verify_digest(
        self,
        computed_digest: str,
        expected_digest: str,
    ) -> bool:
        if type(computed_digest) is not str:
            raise TypeError(
                "computed_digest must be an exact str"
            )

        if type(expected_digest) is not str:
            raise TypeError(
                "expected_digest must be an exact str"
            )

        allowed = "0123456789abcdef"

        if (
            len(computed_digest) != 64
            or any(
                character not in allowed
                for character in computed_digest
            )
        ):
            raise ValueError(
                "computed_digest must be a lowercase "
                "64-character SHA-256 hexadecimal string"
            )

        if (
            len(expected_digest) != 64
            or any(
                character not in allowed
                for character in expected_digest
            )
        ):
            raise ValueError(
                "expected_digest must be a lowercase "
                "64-character SHA-256 hexadecimal string"
            )

        return hmac.compare_digest(
            computed_digest,
            expected_digest,
        )
```

This code is a vocabulary reference only.

It does not authorize implementation.

---

# PROHIBITED FIRST-CAPABILITY EXPANSION

The first capability must not include:

```text
digest generation
manifest input
bytes input
JSON input
primitive-dictionary input
string-subclass acceptance
input normalization
case folding
prefix removal
generic algorithm support
batch verification
verification result model
verification receipt
timestamps
identifiers
subject binding
provenance verification
embedded report-digest verification
byte-length verification
codec verification
BOM verification
identity verification
content addressing
persistence
audit records
events
logging
alerts
export
transport
registry integration
admission
trust evaluation
signing
attestation
public disclosure
governance authority
execution authority
```

---

# OWNERSHIP MAP

```text
RuntimeRecordInspectionDigestManifestSha256DigestService
→
owns digest-manifest UTF-8-byte-to-SHA-256-hexdigest generation
```

```text
RuntimeRecordInspectionDigestManifestDigestVerificationService
→
owns valid digest-string syntax checking and constant-time pair comparison
```

Future ownership remains unresolved for:

```text
expected-digest provenance
subject binding
verification evidence modeling
verification persistence
embedded inspection-report digest verification
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

The first digest-manifest verification capability is reduced to:

```text
exact computed digest string
+
exact expected digest string
→
constant-time Boolean comparison
```

The service owns:

```text
exact string-type acceptance
role-specific TypeError behavior
frozen lowercase SHA-256 syntax validation
role-specific ValueError behavior
valid match → True
valid mismatch → False
hmac.compare_digest comparison
deterministic result
stateless behavior
```

Everything else remains outside scope.

The next authorized artifact is:

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_DIGEST_MANIFEST_DIGEST_VERIFICATION_IMMUTABLE_SERVICE_CONTRACT_001.md
```

```text
Tests: HOLD
Implementation: HOLD
```

---

# FINAL REDUCTIONS

```text
Digest Generation
≠
Digest Verification
```

```text
Wrong Runtime Type
≠
Invalid Digest Syntax
```

```text
Invalid Digest Syntax
≠
Digest Mismatch
```

```text
Digest Match
≠
Integrity Admission
```

```text
Digest Match
≠
Trust
```

```text
Digest Match
≠
Subject Binding
```

```text
Digest Equality
≠
Complete Integrity Proof
```

```text
Digest Mismatch
≠
Tampering Proof
```

```text
Verification True
≠
Authority Granted
```

```text
Digest Match
≠
Publicly Disclosable
```

```text
No proof → No bind → No side effect.
```

**UNKNOWN → HOLD**
