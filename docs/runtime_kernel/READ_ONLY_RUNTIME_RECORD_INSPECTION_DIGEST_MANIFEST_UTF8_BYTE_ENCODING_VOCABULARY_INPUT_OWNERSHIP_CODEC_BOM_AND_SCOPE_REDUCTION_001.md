# READ-ONLY RUNTIME RECORD INSPECTION DIGEST MANIFEST UTF-8 BYTE ENCODING

# VOCABULARY, INPUT OWNERSHIP, CODEC, BOM, AND SCOPE REDUCTION 001

**Date:** 2026-07-17
**Project:** Research OS
**Development Version:** v2.0.0
**Authority:** VOCABULARY AND SCOPE REDUCTION ONLY
**Status:** COMPLETE
**Operating Posture:** BYTE-FIRST / DETERMINISTIC / IMMUTABLE / IN-MEMORY / UNKNOWN → HOLD

---

# PURPOSE

Freeze the vocabulary, service ownership, accepted input, semantic input boundary, output type, codec, BOM policy, deterministic behavior, exact-text preservation, dependency direction, and prohibited expansion for the first Read-Only Runtime Record Inspection Digest Manifest UTF-8 Byte Encoding capability.

This reduction follows:

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_DIGEST_MANIFEST_UTF8_BYTE_ENCODING_EXISTING_ENCODER_REUSE_CODEC_BOM_CANONICALIZATION_HASH_PERSISTENCE_AND_AUTHORITY_BOUNDARY_INSPECTION_001.md
```

That inspection established:

1. no digest-manifest-specific UTF-8 byte encoder currently exists
2. the existing inspection-report UTF-8 encoder accepts exact strings mechanically
3. the existing encoder is semantically frozen around inspection-report JSON text
4. exact-string compatibility does not authorize semantic ownership expansion
5. direct reuse would widen a frozen capability
6. the existing encoder must remain unchanged
7. identical `.encode("utf-8")` mechanics may be adopted independently
8. a separate digest-manifest UTF-8 byte encoder is required
9. the future service should accept one exact plain string
10. the semantic input must be digest-manifest JSON text
11. the codec must be exactly `utf-8`
12. UTF-8-SIG must be prohibited
13. output must contain no BOM
14. the supplied string must be encoded exactly
15. JSON validity remains upstream
16. output must be immutable `bytes`
17. decoding remains separate
18. deterministic bytes do not establish canonical-byte authority
19. hashing and verification remain separate
20. persistence, export, transport, framing, and compression remain separate
21. byte availability establishes no identity, disclosure permission, or governance authority

This document resolves the narrowest first digest-manifest byte capability.

It authorizes creation of an immutable service contract.

```text
Tests: HOLD
Implementation: HOLD
```

---

# ACCEPTED CAPABILITY NAME

The accepted capability name is:

```text
Read-Only Runtime Record Inspection Digest Manifest UTF-8 Byte Encoding
```

The capability performs:

```text
one exact digest-manifest JSON string
→
one immutable UTF-8 bytes value without BOM
```

The capability does not perform:

```text
manifest construction
manifest validation
primitive representation creation
JSON creation
JSON validation
codec selection
UTF-8-SIG encoding
BOM insertion
Unicode normalization
newline generation
decoding
canonicalization authority
hashing
verification
byte-length verification
identity generation
timestamp generation
persistence
export
transport
framing
compression
collection encoding
redaction
publication
governance
execution
```

---

# ACCEPTED OWNER

The accepted service name is:

```text
RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService
```

The accepted production location is:

```text
services/runtime_record_inspection_digest_manifest_utf8_byte_encoding_service.py
```

This service owns:

```text
digest-manifest JSON text
→
immutable UTF-8 bytes without BOM
```

It does not own inspection-report byte encoding.

It does not replace, modify, generalize, or delegate to:

```text
RuntimeRecordInspectionUtf8ByteEncodingService
```

---

# OWNERSHIP SEPARATION

Frozen inspection-report ownership remains:

```text
RuntimeRecordInspectionReport
→
RuntimeRecordInspectionRepresentationService
→
RuntimeRecordInspectionJsonEncodingService
→
RuntimeRecordInspectionUtf8ByteEncodingService
```

Frozen digest-manifest ownership becomes:

```text
RuntimeRecordInspectionDigestManifest
→
RuntimeRecordInspectionDigestManifestRepresentationService
→
RuntimeRecordInspectionDigestManifestJsonEncodingService
→
RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService
```

The two byte encoders may use identical mechanics while retaining separate semantic ownership.

```text
Shared Encoding Mechanics
≠
Shared Semantic Ownership
```

```text
Equivalent Byte Operation
≠
Equivalent Capability Identity
```

---

# REJECTED OWNER OPTIONS

The following ownership choices are rejected:

```text
reuse RuntimeRecordInspectionUtf8ByteEncodingService
modify RuntimeRecordInspectionUtf8ByteEncodingService
delegate to RuntimeRecordInspectionUtf8ByteEncodingService
add byte behavior to the digest-manifest JSON encoder
add byte behavior to the manifest model
create a generic RuntimeUtf8ByteEncodingService
create a generic codec service
create an orchestration service
```

Reasons:

```text
reuse widens frozen semantic ownership
delegation hides semantic boundary expansion
JSON-owned bytes collapse text and byte transformations
model-owned bytes collapse model and encoding responsibilities
generic ownership exceeds the narrow first capability
orchestration composes capabilities not yet authorized
```

---

# ACCEPTED INPUT

The first digest-manifest UTF-8 byte capability accepts exactly:

```text
one plain Python str
```

The exact runtime rule is:

```python
type(json_text) is str
```

The string must already represent digest-manifest JSON text according to the frozen upstream JSON contract.

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
RuntimeRecordInspectionDigestManifest
primitive digest-manifest dictionary
collection of strings
stream
path
file
```

---

# EXACT TYPE BOUNDARY

The service validates only exact runtime input type.

Required reductions:

```text
String Subclass
≠
Exact Plain String
```

```text
Byte-Like Object
≠
Accepted JSON Text
```

```text
Manifest Object
≠
Manifest JSON Text
```

```text
Compatible Text Behavior
≠
Accepted Runtime Type
```

---

# INVALID INPUT ERROR

Invalid input must raise:

```text
TypeError
```

The exact future error message should be:

```text
json_text must be an exact str
```

This preserves the established UTF-8 byte-encoding vocabulary.

The service must not return:

```text
None
False
empty fallback bytes
error bytes
status bytes
warning bytes
partial bytes
```

```text
Encoding Failure
≠
UTF-8 Byte Result
```

---

# SEMANTIC INPUT OWNERSHIP

The runtime input is an exact plain string.

The semantic input is:

```text
one JSON string produced according to the frozen
digest-manifest JSON encoding contract
```

Expected upstream content includes:

```text
manifest_schema_version
digest_algorithm
sha256_digest
byte_length
codec
bom_present
```

The byte encoder does not create this text.

It must not import or instantiate:

```text
RuntimeRecordInspectionDigestManifestJsonEncodingService
```

The caller owns composition.

```text
Manifest JSON Creation
≠
Manifest UTF-8 Byte Encoding
```

---

# JSON VALIDATION BOUNDARY

The byte encoder validates only:

```text
exact plain-string input
```

It must not validate:

```text
JSON syntax
JSON object shape
digest-manifest key names
digest-manifest field order
manifest schema version
digest algorithm
SHA-256 syntax
byte length
codec declaration
BOM declaration
source identity
source provenance
source authenticity
```

An exact string that is not valid JSON may still be encoded.

Accepted type-level examples include:

```text
""
"not-json"
"{"
"  text  "
"\n"
```

```text
String Type Validity
≠
JSON Semantic Validity
```

```text
UTF-8 Encodability
≠
Digest-Manifest Contract Validity
```

---

# PUBLIC METHOD

The accepted public method name is:

```text
to_utf8_bytes
```

The future conceptual signature is:

```python
def to_utf8_bytes(
    self,
    json_text: str,
) -> bytes:
```

No optional arguments are authorized.

No codec argument is authorized.

No BOM argument is authorized.

No normalization argument is authorized.

No error-mode argument is authorized.

No destination argument is authorized.

No framing or compression argument is authorized.

---

# OUTPUT TYPE

The service returns exactly:

```text
bytes
```

The runtime concrete type must be exactly:

```python
bytes
```

The service must not return:

```text
bytearray
memoryview
str
list
tuple
stream
BytesIO
path
file
iterator
generator
digest
manifest
verification result
export result
```

```text
Immutable Bytes
≠
Mutable Bytearray
```

```text
Byte Value
≠
Byte Stream
```

---

# ACCEPTED BYTE OPERATION

The exact future operation is:

```python
json_text.encode("utf-8")
```

No additional transformation is required.

The service must not use:

```text
codecs.encode
utf-8-sig
caller-supplied codec
platform encoding
locale encoding
ASCII
UTF-16
UTF-32
custom error mode
manual byte construction
manual BOM handling
```

---

# CODEC CONTRACT

The accepted codec is exactly:

```text
utf-8
```

The codec is fixed.

It is not configurable.

The service must not accept a codec argument.

It must not inspect a codec field inside JSON text.

It must not derive the codec from:

```text
manifest metadata
environment variables
locale
platform defaults
configuration
file extension
content type
```

```text
UTF-8 Encoding
≠
Codec Selection
```

---

# UTF-8-SIG PROHIBITION

The service must not use:

```text
utf-8-sig
```

It must not produce UTF-8 bytes with a byte-order mark.

```text
UTF-8 Encoding
≠
UTF-8-SIG Encoding
```

```text
UTF-8 Bytes
≠
UTF-8 Bytes With BOM
```

---

# BOM CONTRACT

The output must contain no UTF-8 BOM.

The service must not prepend:

```text
EF BB BF
```

For ordinary non-empty text:

```python
not result.startswith(b"\xef\xbb\xbf")
```

must be true.

For empty input:

```python
result == b""
```

must be true.

The service does not read the manifest’s `bom_present` field.

It does not validate that field.

It simply uses standard UTF-8 encoding without BOM.

```text
BOM-Free Encoding Behavior
≠
Manifest BOM Verification
```

---

# EXACT TEXT PRESERVATION

The service must encode the supplied string exactly.

Required relation:

```python
result == json_text.encode("utf-8")
```

The service must not:

```text
trim text
append text
prepend text
change case
normalize Unicode
collapse whitespace
replace characters
escape Unicode
unescape JSON
parse JSON
reformat JSON
append newline
remove newline
```

```text
Text Encoding
≠
Text Transformation
```

---

# NEWLINE CONTRACT

The service introduces no newline.

It must not append:

```text
\n
\r\n
platform newline
```

If the supplied exact string already contains newline characters, those characters are encoded normally.

```text
Newline Preservation
≠
Newline Generation
```

---

# EMPTY STRING CONTRACT

The exact empty string is accepted.

Python:

```python
"".encode("utf-8")
```

produces:

```python
b""
```

The service must return exactly:

```python
b""
```

for empty-string input.

The encoder does not reject empty text based on JSON semantics.

```text
Exact String Acceptance
≠
Valid Manifest JSON Confirmation
```

---

# WHITESPACE CONTRACT

Whitespace is encoded exactly as supplied.

The service must preserve:

```text
leading spaces
trailing spaces
tabs
newlines
carriage returns
spaces inside JSON strings
spaces outside valid JSON geometry
```

It must not trim, normalize, or collapse whitespace.

---

# UNICODE CONTRACT

Unicode text must encode using standard UTF-8.

Examples:

```text
α
Δ
É
→
≠
```

must produce their exact UTF-8 byte sequences.

The service must not:

```text
ASCII-escape Unicode
normalize Unicode
transliterate Unicode
drop characters
replace characters
use ignore mode
use replacement mode
```

The default strict UTF-8 operation is sufficient for Python strings.

---

# NULL-CHARACTER CONTRACT

An embedded null character:

```python
"\x00"
```

must encode as:

```python
b"\x00"
```

The service must not:

```text
strip null characters
treat null as a terminator
truncate after null
replace null
reject null based on semantic JSON rules
```

---

# SOURCE NON-MUTATION

Python strings are immutable.

The service must not create a semantically modified intermediate string before encoding.

The supplied exact string must remain the sole source of byte content.

```text
Input String Content
→
Exact UTF-8 Byte Content
```

---

# DETERMINISM

For one unchanged exact string:

```python
service.to_utf8_bytes(json_text)
==
service.to_utf8_bytes(json_text)
```

must always be true.

Two independent service instances must return equal bytes for equal input text.

The service introduces no:

```text
timestamp
generated identifier
random value
environment metadata
host metadata
process metadata
filesystem metadata
registry state
network state
counter
cache
global state
```

Required relation:

```text
same exact string
→
equal UTF-8 byte value
```

---

# BYTE IDENTITY

Repeated calls must return equal byte values.

Byte object identity is not part of the contract.

Required:

```text
equal bytes value
```

Not required:

```text
different Python bytes object identity
```

Python may reuse immutable byte objects.

---

# SERVICE STATE

The service requires no constructor arguments.

The service is stateless.

It retains no:

```text
last input
last output
call count
cache
JSON encoder
manifest
registry
clock
path
codec configuration
BOM configuration
error configuration
```

Multiple instances remain behaviorally equivalent.

---

# IMPORT BOUNDARY

The future production service requires no imports.

The operation exists directly on Python `str`.

The service must not import:

```text
codecs
json
pathlib
os
sys
tempfile
hashlib
datetime
time
uuid
random
secrets
io
gzip
zlib
bz2
lzma
socket
requests
urllib
registries
inspectors
event engines
database libraries
third-party libraries
```

---

# EXISTING ENCODER PRESERVATION

The frozen inspection-report byte encoder remains:

```text
services/runtime_record_inspection_utf8_byte_encoding_service.py
```

It must remain unchanged.

Its tests must remain unchanged.

The new service must not import, instantiate, or delegate to:

```text
RuntimeRecordInspectionUtf8ByteEncodingService
```

The existing encoder must remain digest-manifest-unaware.

```text
Shared Encoding Mechanics
≠
Service Delegation
```

---

# DIGEST-MANIFEST JSON ENCODER PRESERVATION

The frozen JSON service remains:

```text
services/runtime_record_inspection_digest_manifest_json_encoding_service.py
```

It must remain unchanged and byte-unaware.

Its source must not gain:

```text
.encode("utf-8")
to_utf8_bytes
bytes(
bytearray(
memoryview(
```

```text
Manifest JSON Encoding
≠
Manifest UTF-8 Encoding
```

---

# DIGEST-MANIFEST REPRESENTATION PRESERVATION

The frozen representation service remains:

```text
services/runtime_record_inspection_digest_manifest_representation_service.py
```

It must remain byte-unaware.

It must not gain:

```text
to_utf8_bytes
.encode(
bytes(
bytearray(
memoryview(
```

---

# MODEL PRESERVATION

The frozen manifest model remains:

```text
models/runtime_record_inspection_digest_manifest.py
```

It must remain representation-free, JSON-free, and byte-free.

The model must not gain:

```text
to_dict
to_primitive
to_json
to_json_text
to_utf8_bytes
serialize
encode
```

---

# JSON CREATION SCOPE

JSON creation remains upstream.

The byte encoder must not:

```text
import json
accept primitive dictionaries
accept manifest models
call json.dumps
construct JSON text
sort keys
select JSON separators
validate JSON
```

```text
JSON Text Creation
≠
UTF-8 Byte Encoding
```

---

# DECODING SCOPE

UTF-8 decoding remains:

```text
HOLD
```

The service must not expose:

```text
from_utf8_bytes
decode
decode_utf8
to_json_text
restore_text
```

```text
UTF-8 Encoding
≠
UTF-8 Decoding
```

---

# CANONICAL BYTE SCOPE

Canonical-byte authority remains:

```text
HOLD
```

Deterministic encoding of deterministic JSON text produces repeatable bytes.

It does not establish:

```text
cross-language canonicalization
canonical artifact format
canonical file format
canonical identity
signature stability
content-addressed identity
platform-wide canonical-byte authority
```

```text
Deterministic UTF-8 Bytes
≠
Canonical Bytes
```

---

# HASHING SCOPE

Hashing remains:

```text
HOLD
```

The service must not calculate:

```text
SHA-256
byte hash
text hash
checksum
hex digest
binary digest
signature
```

It must not import:

```text
hashlib
```

```text
UTF-8 Byte Encoding
≠
Hashing
```

---

# VERIFICATION SCOPE

Verification remains:

```text
HOLD
```

The service must not verify:

```text
recorded SHA-256 digest
recorded byte length
codec declaration
BOM declaration
source bytes
source equality
source authenticity
manifest authenticity
manifest integrity
```

```text
Produced Bytes
≠
Verified Bytes
```

---

# BYTE-LENGTH SCOPE

Byte-length calculation and verification remain:

```text
HOLD
```

The service must not:

```text
return byte length
return a tuple of bytes and length
compare byte length
validate recorded byte length
add length metadata
```

A future separately owned capability may use:

```python
len(encoded_bytes)
```

```text
Bytes
≠
Byte-Length Verification
```

---

# IDENTITY SCOPE

Identity generation remains:

```text
HOLD
```

The service must not add or generate:

```text
manifest_id
artifact_id
record_id
source_id
encoded_at
created_at
file_name
path
content_type
charset
canonical_id
```

```text
Bytes Exist
≠
Artifact Identity Exists
```

---

# PERSISTENCE SCOPE

Persistence remains:

```text
HOLD
```

The service must not:

```text
open files
read files
write files
create directories
accept paths
return paths
save bytes
load bytes
create sidecars
create binary artifacts
write databases
```

The capability ends when the bytes value is returned.

```text
Byte Encoding
≠
Persistence
```

---

# EXPORT AND TRANSPORT SCOPE

Export and transport remain:

```text
HOLD
```

The service accepts no:

```text
destination
file name
stream
socket
buffer
URL
repository
upload target
download target
publication target
```

```text
Bytes Available
≠
Authorized To Export
```

```text
Byte Encoding
≠
Transport
```

---

# CONTENT-TYPE SCOPE

Content-type declaration remains:

```text
HOLD
```

The service must not produce or declare:

```text
application/json
application/octet-stream
charset=utf-8
content length
content disposition
file extension
```

```text
Byte Encoding
≠
Content-Type Declaration
```

---

# COLLECTION SCOPE

Collection encoding remains:

```text
HOLD
```

The service accepts one exact string only.

It rejects:

```text
list of strings
tuple of strings
set of strings
manifest collection
registry snapshot
JSON document collection
byte collection
```

No collection method is authorized.

---

# FRAMING SCOPE

Framing remains:

```text
HOLD
```

The service must not add:

```text
length prefix
delimiter
record separator
archive framing
stream framing
network framing
message header
```

```text
Raw UTF-8 Bytes
≠
Framed Transport Payload
```

---

# COMPRESSION SCOPE

Compression remains:

```text
HOLD
```

The service must not use:

```text
gzip
zlib
bz2
lzma
brotli
zip
archive formats
```

```text
UTF-8 Bytes
≠
Compressed Bytes
```

---

# REDACTION SCOPE

Redaction remains:

```text
HOLD
```

The service must encode supplied text exactly.

It must not:

```text
remove
mask
replace
truncate
classify
hide
redact
```

```text
Exact Byte Encoding
≠
Redacted Byte Encoding
```

---

# PLATFORM INTEGRATION SCOPE

Platform integration remains:

```text
HOLD
```

The service must not inherit:

```text
src.services.inspectable.Inspectable
```

It must not expose:

```text
inspect
health
status
```

It must not register with:

```text
PlatformRegistry
MissionControl
ResearchKernel
```

---

# EVENT PUBLICATION SCOPE

Event publication remains:

```text
HOLD
```

The service must publish no:

```text
application events
Runtime events
audit events
logs
notifications
```

```text
Byte Encoding
≠
Event Publication
```

---

# PUBLIC DISCLOSURE SCOPE

Public disclosure remains:

```text
HOLD
```

The service grants no permission to:

```text
publish
share
transmit
upload
display publicly
export
disclose
```

```text
Byte Encoded
≠
Publicly Disclosable
```

---

# AUTHORITY SCOPE

The bytes result does not establish:

```text
trust
verification
admission
authorization
publication permission
sharing permission
export permission
execution permission
governance authority
public-disclosure authority
```

```text
Machine-Transferable
≠
Authorized To Transfer
```

```text
Equal Bytes
≠
Equal Runtime Authority
```

```text
Equal Bytes
≠
Equal Registry Membership
```

```text
Integrity Metadata
≠
Integrity Proof
```

---

# PROHIBITED PUBLIC METHODS

The service must not expose:

```text
to_bytes
encode
encode_bytes
from_utf8_bytes
decode
decode_utf8
to_json_text
to_json
serialize
deserialize
save
load
persist
export
write
read
hash
digest
checksum
sign
verify
compress
decompress
frame
stream
publish
upload
download
inspect
health
status
encode_collection
to_bytes_list
```

The only capability-specific public method is:

```text
to_utf8_bytes
```

---

# ACCEPTED PRODUCTION LOCATION

The accepted future production location is:

```text
services/runtime_record_inspection_digest_manifest_utf8_byte_encoding_service.py
```

No other production location is authorized.

No frozen upstream production file requires modification.

---

# ACCEPTED TEST LOCATION

The accepted future test location is:

```text
tests/runtime/test_runtime_record_inspection_digest_manifest_utf8_byte_encoding_service.py
```

No test file is authorized until the immutable service contract is complete.

---

# MINIMUM IMPLEMENTATION SHAPE

The future implementation is expected to be structurally equivalent to:

```python
class RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService:
    def to_utf8_bytes(
        self,
        json_text: str,
    ) -> bytes:
        if type(json_text) is not str:
            raise TypeError(
                "json_text must be an exact str"
            )

        return json_text.encode("utf-8")
```

This is a vocabulary reference only.

It does not authorize production implementation.

---

# PROHIBITED FIRST-CAPABILITY EXPANSION

The first capability must not include:

```text
existing encoder modification
existing encoder delegation
generic byte-encoding ownership
JSON creation
manifest input acceptance
primitive-dictionary input acceptance
multiple input types
string-subclass acceptance
JSON validation
manifest validation
codec configuration
UTF-8-SIG
BOM insertion
Unicode normalization
newline generation
decoding
canonical-byte authority
hashing
checksum generation
verification
byte-length verification
identity generation
timestamp generation
content-type declaration
persistence
sidecar creation
export
transport
streaming
framing
compression
collection encoding
registry integration
orchestration
signing
trust evaluation
redaction
public disclosure
governance authority
execution authority
```

---

# OWNERSHIP MAP

```text
RuntimeRecordInspectionDigestManifest
→
owns immutable validated digest metadata
```

```text
RuntimeRecordInspectionDigestManifestService
→
owns validated caller-supplied fact binding
```

```text
RuntimeRecordInspectionDigestManifestRepresentationService
→
owns manifest-to-primitive-dictionary transformation
```

```text
RuntimeRecordInspectionDigestManifestJsonEncodingService
→
owns digest-manifest primitive-dictionary-to-JSON-text encoding
```

```text
RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService
→
owns digest-manifest JSON-text-to-UTF-8-byte encoding
```

The existing service retains:

```text
RuntimeRecordInspectionUtf8ByteEncodingService
→
owns inspection-report JSON-text-to-UTF-8-byte encoding
```

Future ownership remains unresolved for:

```text
digest-manifest byte hashing
digest-manifest verification
digest-manifest byte-length verification
digest-manifest persistence
digest-manifest export
digest-manifest transport
digest-manifest registry integration
end-to-end orchestration
```

All remain:

```text
HOLD
```

---

# REDUCTION CONCLUSION

The first digest-manifest UTF-8 byte capability is reduced to:

```text
exact plain digest-manifest JSON string
→
immutable UTF-8 bytes without BOM
```

The service owns:

```text
exact string acceptance
fixed UTF-8 codec
exact .encode("utf-8") operation
BOM absence
exact text preservation
immutable bytes return
deterministic equality
stateless behavior
```

Everything else remains outside scope.

The next authorized artifact is:

```text
READ_ONLY_RUNTIME_RECORD_INSPECTION_DIGEST_MANIFEST_UTF8_BYTE_ENCODING_IMMUTABLE_SERVICE_CONTRACT_001.md
```

```text
Tests: HOLD
Implementation: HOLD
```

---

# FINAL REDUCTIONS

```text
Runtime Type Compatibility
≠
Semantic Ownership
```

```text
Shared Encoding Mechanics
≠
Shared Service Ownership
```

```text
Manifest JSON Text
≠
Manifest UTF-8 Bytes
```

```text
UTF-8 Encoding
≠
UTF-8-SIG Encoding
```

```text
Deterministic UTF-8 Bytes
≠
Canonical Bytes
```

```text
Byte Encoding
≠
Verification
```

```text
Bytes Available
≠
Authorized To Export
```

```text
Byte Encoded
≠
Publicly Disclosable
```

```text
No proof → No bind → No side effect.
```

**UNKNOWN → HOLD**
