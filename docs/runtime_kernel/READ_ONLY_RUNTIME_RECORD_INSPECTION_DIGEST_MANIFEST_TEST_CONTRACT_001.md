# READ-ONLY RUNTIME RECORD INSPECTION DIGEST MANIFEST

# TEST CONTRACT 001

**Date:** 2026-07-17
**Project:** Research OS
**Development Version:** v2.0.0
**Authority:** TEST CONTRACT
**Status:** TESTS AUTHORIZED / IMPLEMENTATION HOLD
**Operating Posture:** TEST-FIRST / IMMUTABLE / DETERMINISTIC / IN-MEMORY / UNKNOWN → HOLD

---

# PURPOSE

Freeze the executable test contract for:

```text
RuntimeRecordInspectionDigestManifest
```

and:

```text
RuntimeRecordInspectionDigestManifestService
```

The capability performs:

```text
exact caller-supplied manifest facts
→
one immutable validated in-memory digest manifest
```

This test contract follows:

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_DIGEST_MANIFEST_EXISTING_METADATA_SCHEMA_IDENTITY_PERSISTENCE_AND_AUTHORITY_BOUNDARY_INSPECTION_001.md
```

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_DIGEST_MANIFEST_VOCABULARY_MODEL_FIELD_OWNERSHIP_SCHEMA_AND_SCOPE_REDUCTION_001.md
```

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_DIGEST_MANIFEST_IMMUTABLE_MODEL_AND_SERVICE_CONTRACT_001.md
```

Production implementation remains:

```text
HOLD
```

until:

1. this test contract exists
2. both test modules exist
3. the expected missing-module failure is observed
4. the test-first checkpoint is committed

---

# AUTHORIZED TEST FILES

Exact model test location:

```text
tests/runtime/test_runtime_record_inspection_digest_manifest.py
```

Exact service test location:

```text
tests/runtime/test_runtime_record_inspection_digest_manifest_service.py
```

Exact future production model:

```text
models/runtime_record_inspection_digest_manifest.py
```

Exact future production service:

```text
services/runtime_record_inspection_digest_manifest_service.py
```

The production files must remain absent until the expected import failure is recorded.

---

# EXPECTED FIRST FAILURE

Run:

```powershell
python -m pytest tests\runtime\test_runtime_record_inspection_digest_manifest.py tests\runtime\test_runtime_record_inspection_digest_manifest_service.py -q
```

Expected collection failure:

```text
ModuleNotFoundError:
No module named 'models.runtime_record_inspection_digest_manifest'
```

Depending on import order, absence of the service module may also be reported.

This proves:

```text
test contract present
+
production model absent
+
production service absent
```

No placeholder production module is permitted before observing this failure.

---

# EXACT MODEL SHAPE

The tests must prove that the model is:

```python
@dataclass(frozen=True)
class RuntimeRecordInspectionDigestManifest:
    manifest_schema_version: str
    digest_algorithm: str
    sha256_digest: str
    byte_length: int
    codec: str
    bom_present: bool
```

The model must contain exactly six fields in that exact order.

No defaults are authorized.

No additional fields are authorized.

---

# MANIFEST SCHEMA VERSION TESTS

The model must accept only:

```python
"1.0"
```

Invalid type must raise:

```text
TypeError
```

Exact message:

```text
manifest_schema_version must be an exact str
```

Invalid value must raise:

```text
ValueError
```

Exact message:

```text
manifest_schema_version must be exactly '1.0'
```

Rejected values include:

```text
None
integer
float
empty string
1
1.1
2.0
v1.0
str subclass
```

---

# DIGEST ALGORITHM TESTS

The model must accept only:

```python
"sha256"
```

Invalid type must raise:

```text
TypeError
```

Exact message:

```text
digest_algorithm must be an exact str
```

Invalid value must raise:

```text
ValueError
```

Exact message:

```text
digest_algorithm must be exactly 'sha256'
```

Rejected values include:

```text
None
empty string
SHA-256
sha-256
SHA256
sha1
sha512
md5
str subclass
```

---

# SHA-256 DIGEST TESTS

The model must accept exactly:

```text
64 lowercase hexadecimal characters
```

Allowed alphabet:

```text
0123456789abcdef
```

Invalid type must raise:

```text
TypeError
```

Exact message:

```text
sha256_digest must be an exact str
```

Invalid format must raise:

```text
ValueError
```

Exact message:

```text
sha256_digest must be exactly 64 lowercase hexadecimal characters
```

The tests must reject:

```text
empty string
short digest
long digest
uppercase digest
mixed-case digest
non-hexadecimal characters
0x prefix
sha256 prefix
sha-256 prefix
spaces
tabs
newlines
str subclass
```

The model must not normalize or repair invalid values.

---

# BYTE-LENGTH TESTS

The model must accept:

```text
exact non-negative Python int
```

Zero is accepted.

Invalid type must raise:

```text
TypeError
```

Exact message:

```text
byte_length must be an exact int
```

Negative values must raise:

```text
ValueError
```

Exact message:

```text
byte_length must be non-negative
```

The tests must reject:

```text
None
False
True
float
string
negative integer
integer subclass
```

Frozen separation:

```text
Byte-Length Metadata
≠
Source-Byte Inspection
```

---

# CODEC TESTS

The model must accept only:

```python
"utf-8"
```

Invalid type must raise:

```text
TypeError
```

Exact message:

```text
codec must be an exact str
```

Invalid value must raise:

```text
ValueError
```

Exact message:

```text
codec must be exactly 'utf-8'
```

Rejected values include:

```text
None
empty string
UTF-8
utf8
utf-8-sig
ascii
utf-16
str subclass
```

Frozen separation:

```text
Codec Declared
≠
Codec Proven
```

---

# BOM TESTS

The model must accept only:

```python
False
```

Invalid type must raise:

```text
TypeError
```

Exact message:

```text
bom_present must be an exact bool
```

A value of `True` must raise:

```text
ValueError
```

Exact message:

```text
bom_present must be False
```

The tests must reject:

```text
None
0
1
"false"
"False"
True
```

Frozen separation:

```text
BOM Metadata
≠
BOM Verification
```

---

# VALIDATION ORDER TESTS

Validation order must be:

```text
manifest_schema_version
→
digest_algorithm
→
sha256_digest
→
byte_length
→
codec
→
bom_present
```

When multiple fields are invalid, the first invalid field in this order must determine the raised error.

The model must not aggregate errors.

The model must not return a partial object.

---

# IMMUTABILITY TESTS

The model must be a frozen dataclass.

Assignment to any field must raise:

```text
dataclasses.FrozenInstanceError
```

The model must expose no mutation methods.

Prohibited methods include:

```text
set_digest
set_byte_length
set_codec
set_bom
update
replace_fields
mutate
clear
append
```

Frozen separation:

```text
Manifest Construction
≠
Manifest Mutation
```

---

# STRUCTURAL EQUALITY TESTS

Two manifests with equal field values must compare equal.

Two manifests with different field values must compare unequal.

Object identity is not part of the contract.

Frozen separation:

```text
Manifest Structural Equality
≠
Manifest Object Identity
```

---

# PROHIBITED MODEL FIELD TESTS

The model must not contain:

```text
manifest_id
artifact_id
record_id
report_id
external_id
provenance_ref
schema_version
source_commit
created_at
generated_at
manifested_at
file_name
path
content_type
manifest_digest
signature
verified
trusted
authorized
public
exported
persisted
```

---

# SERVICE CONSTRUCTION TESTS

The service must:

1. construct without arguments
2. retain no state
3. require no upstream service
4. retain no cache
5. retain no last manifest
6. retain no clock
7. retain no registry
8. retain no defaults

Accepted construction:

```python
service = RuntimeRecordInspectionDigestManifestService()
```

---

# SERVICE METHOD TESTS

The exact public method is:

```text
create_manifest
```

Exact signature:

```python
def create_manifest(
    self,
    *,
    manifest_schema_version: str,
    digest_algorithm: str,
    sha256_digest: str,
    byte_length: int,
    codec: str,
    bom_present: bool,
) -> RuntimeRecordInspectionDigestManifest:
    ...
```

All six arguments are required.

All six arguments are keyword-only.

No defaults are authorized.

No extra arguments are authorized.

---

# POSITIONAL INVOCATION TESTS

Supplying positional field values must raise:

```text
TypeError
```

The exact interpreter-generated message is not frozen.

---

# MISSING ARGUMENT TESTS

Omitting any required argument must raise:

```text
TypeError
```

The service must not supply defaults.

---

# EXTRA ARGUMENT TESTS

Supplying any unknown keyword must raise:

```text
TypeError
```

Examples include:

```text
manifest_id
artifact_id
record_id
created_at
source_commit
verified
authorized
public
```

---

# SERVICE RETURN TESTS

The service must return exactly:

```text
RuntimeRecordInspectionDigestManifest
```

The runtime type must not be:

```text
dict
list
tuple
mapping proxy
JSON text
bytes
path
file
status wrapper
result wrapper
```

---

# FIELD PROPAGATION TESTS

The service must propagate every caller-supplied field unchanged.

It must not:

```text
lowercase values
strip values
coerce values
replace values
generate values
calculate values
supply defaults
```

Frozen separation:

```text
Model Validation
≠
Service Derivation
```

---

# MODEL ERROR PROPAGATION TESTS

Invalid field values passed through the service must raise the model’s exact exception type and exact message.

The service must not:

```text
catch and replace errors
wrap errors
return status objects
return partial manifests
```

---

# DIGEST RECOMPUTATION BOUNDARY TESTS

The model and service must not import:

```text
hashlib
RuntimeRecordInspectionSha256DigestService
```

They must not accept source bytes.

They must not call:

```text
sha256
hexdigest
digest
```

Frozen separation:

```text
Manifest Construction
≠
Digest Generation
```

---

# BYTE-LENGTH CALCULATION BOUNDARY TESTS

The model and service must not accept source bytes.

They must not calculate:

```python
len(content_bytes)
```

The caller supplies byte length explicitly.

Frozen separation:

```text
Manifest Records Byte Length
≠
Manifest Calculates Byte Length
```

---

# BYTE ENCODING BOUNDARY TESTS

The model and service must not import:

```text
RuntimeRecordInspectionUtf8ByteEncodingService
```

They must not call:

```python
.encode("utf-8")
```

They must not accept JSON text.

---

# JSON AND REPRESENTATION BOUNDARY TESTS

The model and service must not import:

```text
json
RuntimeRecordInspectionJsonEncodingService
RuntimeRecordInspectionRepresentationService
```

They must not create:

```text
primitive dictionary
JSON text
UTF-8 bytes
```

---

# REPORT AND REGISTRY BOUNDARY TESTS

The model and service must not import:

```text
RuntimeRecordInspectionReport
RuntimeRecordInspector
RuntimeRecordRegistry
```

They must not inspect records or establish registry membership.

Frozen separation:

```text
Manifest Metadata
≠
Live Registry Inspection
```

---

# GENERATED IDENTIFIER TESTS

The model and service must not create:

```text
manifest_id
artifact_id
record_id
UUID
counter-based identifier
digest-derived identifier
```

The source must not import:

```text
uuid
random
```

---

# TIMESTAMP TESTS

The model and service must not create:

```text
created_at
generated_at
manifested_at
```

The source must not import:

```text
datetime
time
```

Frozen separation:

```text
Manifest Construction
≠
Timestamp Generation
```

---

# VERIFICATION BOUNDARY TESTS

The service must not expose:

```text
verify
verify_digest
verify_byte_length
matches
compare
validate_source
```

The manifest validates field shape only.

It does not prove the facts correspond to source bytes.

Frozen separation:

```text
Manifest Field Validation
≠
Manifest Evidence Verification
```

---

# SERIALIZATION BOUNDARY TESTS

The model and service must not expose:

```text
to_dict
to_primitive
to_json
to_json_text
to_bytes
serialize
encode
```

They must not create JSON, bytes, files, or streams.

Frozen separation:

```text
Manifest Model
≠
Manifest Serialization
```

---

# MANIFEST HASHING BOUNDARY TESTS

The model must contain no:

```text
manifest_digest
```

The model and service must not hash the manifest.

Frozen separation:

```text
Source Content Digest
≠
Manifest Digest
```

---

# SIGNING BOUNDARY TESTS

The model must contain no signature field.

The model and service must not expose:

```text
sign
verify_signature
```

They must not import:

```text
hmac
secrets
cryptography
```

---

# FILE-SYSTEM AND PERSISTENCE TESTS

The model and service must not import:

```text
pathlib
os
tempfile
```

Construction must create no files.

They must not expose:

```text
save
load
persist
write
read
store
```

Frozen separation:

```text
Manifest Exists
≠
Manifest Persisted
```

---

# EXPORT BOUNDARY TESTS

The service must not expose:

```text
export
upload
download
publish
transfer
```

It accepts no path, stream, URL, repository, or destination.

Frozen separation:

```text
Manifest Exists
≠
Export Authority
```

---

# REGISTRY BOUNDARY TESTS

The model and service must not integrate with:

```text
RuntimeRecordRegistry
PlatformRegistry
MissionControl
ResearchKernel
```

They must not expose:

```text
register
admit
append
```

Frozen separation:

```text
Manifest Constructed
≠
Manifest Registered
```

---

# COLLECTION BOUNDARY TESTS

The model must not contain:

```text
items
records
digests
children
entries
collection_digest
merkle_root
```

The service must not expose:

```text
create_collection_manifest
create_batch_manifest
create_snapshot_manifest
```

Frozen separation:

```text
Single Content Digest Manifest
≠
Collection Manifest
```

---

# PUBLIC DISCLOSURE AND AUTHORITY TESTS

The model must not contain:

```text
public
publishable
disclosure_authorized
sharing_allowed
authorized
approved
admitted
trusted
verified
authentic
```

The manifest creates no disclosure or governance authority.

Frozen separations:

```text
Manifest Exists
≠
Publicly Disclosable
```

```text
Manifest Metadata
≠
Authority
```

```text
Integrity Evidence
≠
Governance Authority
```

---

# PLATFORM AND EVENT TESTS

The model and service must not inherit:

```text
src.services.inspectable.Inspectable
```

They must not expose:

```text
inspect
health
status
```

The service must publish no events, logs, notifications, or audit records.

---

# PROHIBITED SERVICE METHODS

The service must not expose:

```text
build
generate
derive
calculate
calculate_digest
calculate_byte_length
verify
verify_digest
verify_byte_length
matches
compare
serialize
to_dict
to_json
encode
hash_manifest
sign
save
load
persist
export
write
read
register
publish
inspect
health
status
```

The only capability-specific public method is:

```text
create_manifest
```

---

# TEST-FIRST COMMIT BOUNDARY

The test-first commit must contain only:

```text
docs/runtime_kernel/READ_ONLY_RUNTIME_RECORD_INSPECTION_DIGEST_MANIFEST_TEST_CONTRACT_001.md
tests/runtime/test_runtime_record_inspection_digest_manifest.py
tests/runtime/test_runtime_record_inspection_digest_manifest_service.py
```

It must not contain:

```text
models/runtime_record_inspection_digest_manifest.py
services/runtime_record_inspection_digest_manifest_service.py
```

Suggested commit message:

```text
Add runtime inspection digest manifest test contract
```

---

# REQUIRED SEQUENCE

```text
test contract
→
model tests
→
service tests
→
missing-module failure
→
test-first commit
→
minimum model implementation
→
minimum service implementation
→
isolated validation
→
full-suite validation
→
production commit
→
foundation freeze
```

---

# CURRENT BASELINE

Current full-suite baseline:

```text
2097 passed
```

No existing test may regress.

---

# TEST CONTRACT STATUS

Frozen dataclass:

```text
REQUIRED
```

Exact six-field order:

```text
REQUIRED
```

Exact validation rules:

```text
REQUIRED
```

Exact error messages:

```text
REQUIRED
```

Structural equality:

```text
REQUIRED
```

Mutation:

```text
PROHIBITED
```

Keyword-only service construction:

```text
REQUIRED
```

Generated values:

```text
PROHIBITED
```

Digest recomputation:

```text
PROHIBITED
```

Byte-length calculation:

```text
PROHIBITED
```

Verification:

```text
HOLD
```

Serialization:

```text
HOLD
```

Manifest hashing:

```text
HOLD
```

Signing:

```text
HOLD
```

Persistence:

```text
HOLD
```

Export:

```text
HOLD
```

Registry integration:

```text
HOLD
```

Collection manifests:

```text
HOLD
```

Public disclosure:

```text
HOLD
```

Authority:

```text
HOLD
```

Production implementation:

```text
HOLD PENDING EXPECTED FAILURE AND TEST-FIRST COMMIT
```

---

# CONCLUSION

This test contract authorizes executable tests for:

```text
exact caller-supplied manifest facts
→
immutable validated digest manifest
```

All derivation, verification, serialization, persistence, export, disclosure, and authority remain separate and on HOLD.

**No proof → No bind → No side effect.**

**UNKNOWN → HOLD**
