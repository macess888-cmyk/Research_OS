from pathlib import Path

import pytest

from models.runtime_record_inspection_digest_manifest import (
    RuntimeRecordInspectionDigestManifest,
)
from services.runtime_record_inspection_digest_manifest_utf8_byte_encoding_service import (
    RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService,
)


PRODUCTION_PATH = (
    Path("services")
    / "runtime_record_inspection_digest_manifest_utf8_byte_encoding_service.py"
)

EXISTING_UTF8_ENCODER_PATH = (
    Path("services")
    / "runtime_record_inspection_utf8_byte_encoding_service.py"
)

MANIFEST_JSON_ENCODER_PATH = (
    Path("services")
    / "runtime_record_inspection_digest_manifest_json_encoding_service.py"
)

MANIFEST_REPRESENTATION_PATH = (
    Path("services")
    / "runtime_record_inspection_digest_manifest_representation_service.py"
)

EXPECTED_ERROR = "json_text must be an exact str"

REPRESENTATIVE_JSON_TEXT = (
    '{"manifest_schema_version":"1.0",'
    '"digest_algorithm":"sha256",'
    '"sha256_digest":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",'
    '"byte_length":128,'
    '"codec":"utf-8",'
    '"bom_present":false}'
)

PROHIBITED_PUBLIC_METHODS = {
    "to_bytes",
    "encode",
    "encode_bytes",
    "from_utf8_bytes",
    "decode",
    "decode_utf8",
    "to_json_text",
    "to_json",
    "serialize",
    "deserialize",
    "save",
    "load",
    "persist",
    "export",
    "write",
    "read",
    "hash",
    "digest",
    "checksum",
    "sign",
    "verify",
    "compress",
    "decompress",
    "frame",
    "stream",
    "publish",
    "upload",
    "download",
    "inspect",
    "health",
    "status",
    "encode_collection",
    "to_bytes_list",
    "build_manifest",
    "create_manifest",
    "to_primitive_dict",
}


class DerivedString(str):
    pass


class ExplodingStringLike:
    def __str__(self) -> str:
        raise AssertionError("invalid input must not be converted")

    def encode(self, *args: object, **kwargs: object) -> bytes:
        raise AssertionError("invalid input must not be encoded")


@pytest.fixture
def json_text() -> str:
    return REPRESENTATIVE_JSON_TEXT


@pytest.fixture
def service() -> RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService:
    return RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService()


def test_service_can_be_constructed() -> None:
    service = RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService()

    assert (
        type(service)
        is RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService
    )


def test_service_instances_are_independent() -> None:
    first = RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService()
    second = RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService()

    assert first is not second


def test_service_constructor_requires_no_arguments() -> None:
    service = RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService()

    assert (
        type(service)
        is RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService
    )


def test_service_exposes_required_method(
    service: RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService,
) -> None:
    assert callable(service.to_utf8_bytes)


@pytest.mark.parametrize(
    "method_name",
    sorted(PROHIBITED_PUBLIC_METHODS),
)
def test_service_exposes_no_prohibited_public_method(
    service: RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService,
    method_name: str,
) -> None:
    assert not hasattr(service, method_name)


def test_exact_plain_string_is_accepted(
    service: RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService,
    json_text: str,
) -> None:
    result = service.to_utf8_bytes(json_text)

    assert type(result) is bytes


@pytest.mark.parametrize(
    "invalid_json_text",
    [
        None,
        True,
        False,
        0,
        1,
        1.5,
        b"",
        bytearray(),
        memoryview(b""),
        [],
        (),
        set(),
        frozenset(),
        {},
        object(),
        Path("manifest.json"),
        ["{}"],
        ("{}",),
        ExplodingStringLike(),
    ],
)
def test_non_exact_string_values_are_rejected(
    service: RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService,
    invalid_json_text: object,
) -> None:
    with pytest.raises(TypeError, match=f"^{EXPECTED_ERROR}$"):
        service.to_utf8_bytes(invalid_json_text)  # type: ignore[arg-type]


def test_string_subclass_is_rejected(
    service: RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService,
    json_text: str,
) -> None:
    with pytest.raises(TypeError, match=f"^{EXPECTED_ERROR}$"):
        service.to_utf8_bytes(DerivedString(json_text))


def test_bytes_input_is_rejected(
    service: RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService,
    json_text: str,
) -> None:
    with pytest.raises(TypeError, match=f"^{EXPECTED_ERROR}$"):
        service.to_utf8_bytes(json_text.encode("utf-8"))  # type: ignore[arg-type]


def test_manifest_model_is_rejected(
    service: RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService,
) -> None:
    manifest = RuntimeRecordInspectionDigestManifest(
        manifest_schema_version="1.0",
        digest_algorithm="sha256",
        sha256_digest="a" * 64,
        byte_length=128,
        codec="utf-8",
        bom_present=False,
    )

    with pytest.raises(TypeError, match=f"^{EXPECTED_ERROR}$"):
        service.to_utf8_bytes(manifest)  # type: ignore[arg-type]


def test_primitive_dictionary_is_rejected(
    service: RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService,
) -> None:
    primitive = {
        "manifest_schema_version": "1.0",
        "digest_algorithm": "sha256",
        "sha256_digest": "a" * 64,
        "byte_length": 128,
        "codec": "utf-8",
        "bom_present": False,
    }

    with pytest.raises(TypeError, match=f"^{EXPECTED_ERROR}$"):
        service.to_utf8_bytes(primitive)  # type: ignore[arg-type]


def test_invalid_input_is_rejected_before_conversion(
    service: RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService,
) -> None:
    with pytest.raises(TypeError, match=f"^{EXPECTED_ERROR}$"):
        service.to_utf8_bytes(ExplodingStringLike())  # type: ignore[arg-type]


def test_result_is_exact_bytes(
    service: RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService,
    json_text: str,
) -> None:
    result = service.to_utf8_bytes(json_text)

    assert type(result) is bytes


def test_matches_exact_utf8_encoding(
    service: RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService,
    json_text: str,
) -> None:
    result = service.to_utf8_bytes(json_text)

    assert result == json_text.encode("utf-8")


def test_representative_manifest_json_encodes_exactly(
    service: RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService,
    json_text: str,
) -> None:
    result = service.to_utf8_bytes(json_text)

    assert result == REPRESENTATIVE_JSON_TEXT.encode("utf-8")
    assert result.endswith(b"}")
    assert not result.endswith(b"\n")
    assert not result.endswith(b"\r")


def test_ascii_text_encodes_exactly(
    service: RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService,
) -> None:
    result = service.to_utf8_bytes('{"a":1}')

    assert result == b'{"a":1}'


def test_unicode_text_encodes_exactly(
    service: RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService,
) -> None:
    assert service.to_utf8_bytes("α") == b"\xce\xb1"
    assert service.to_utf8_bytes("→") == b"\xe2\x86\x92"
    assert service.to_utf8_bytes("É") == b"\xc3\x89"
    assert service.to_utf8_bytes("≠") == "≠".encode("utf-8")


def test_output_contains_no_utf8_bom(
    service: RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService,
    json_text: str,
) -> None:
    result = service.to_utf8_bytes(json_text)

    assert not result.startswith(b"\xef\xbb\xbf")


def test_empty_string_encodes_to_empty_bytes(
    service: RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService,
) -> None:
    assert service.to_utf8_bytes("") == b""


@pytest.mark.parametrize(
    "value",
    [
        "not-json",
        "{",
        "  text  ",
        "\n",
    ],
)
def test_json_semantics_are_not_validated(
    service: RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService,
    value: str,
) -> None:
    assert service.to_utf8_bytes(value) == value.encode("utf-8")


def test_whitespace_is_preserved_exactly(
    service: RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService,
) -> None:
    value = "  text  "

    assert service.to_utf8_bytes(value) == b"  text  "


def test_newlines_are_preserved_exactly(
    service: RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService,
) -> None:
    value = "a\nb\r\nc"

    assert service.to_utf8_bytes(value) == value.encode("utf-8")


def test_service_generates_no_newline(
    service: RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService,
) -> None:
    result = service.to_utf8_bytes('{"a":1}')

    assert result == b'{"a":1}'
    assert result != b'{"a":1}\n'
    assert result != b'{"a":1}\r\n'


def test_null_character_is_preserved(
    service: RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService,
) -> None:
    assert service.to_utf8_bytes("\x00") == b"\x00"


@pytest.mark.parametrize(
    "value",
    [
        " leading",
        "trailing ",
        "\ttext\t",
        "a\nb",
        "a\rb",
        "a\r\nb",
        "\x00",
        "α Δ É → ≠",
        '\\"quoted\\"',
    ],
)
def test_exact_text_is_preserved(
    service: RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService,
    value: str,
) -> None:
    assert service.to_utf8_bytes(value) == value.encode("utf-8")


def test_repeated_calls_are_deterministic(
    service: RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService,
    json_text: str,
) -> None:
    first = service.to_utf8_bytes(json_text)
    second = service.to_utf8_bytes(json_text)

    assert first == second


def test_independent_services_return_equal_results(
    json_text: str,
) -> None:
    first = RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService()
    second = RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService()

    assert first.to_utf8_bytes(json_text) == second.to_utf8_bytes(json_text)


def test_service_owns_no_mutable_instance_state(
    service: RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService,
    json_text: str,
) -> None:
    assert service.__dict__ == {}

    service.to_utf8_bytes(json_text)

    assert service.__dict__ == {}


def test_prior_call_does_not_affect_later_output(
    service: RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService,
    json_text: str,
) -> None:
    service.to_utf8_bytes("previous")

    result = service.to_utf8_bytes(json_text)

    assert result == json_text.encode("utf-8")


def test_encoding_creates_no_files(
    service: RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService,
    json_text: str,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    before = sorted(path.relative_to(tmp_path) for path in tmp_path.rglob("*"))

    service.to_utf8_bytes(json_text)

    after = sorted(path.relative_to(tmp_path) for path in tmp_path.rglob("*"))

    assert after == before


def test_production_file_exists() -> None:
    assert PRODUCTION_PATH.is_file()


def test_production_source_contains_no_imports() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")
    import_lines = [
        line.strip()
        for line in source.splitlines()
        if line.strip().startswith(("import ", "from "))
    ]

    assert import_lines == []


def test_production_source_contains_exact_type_check() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert "type(json_text) is not str" in source
    assert "isinstance(json_text, str)" not in source


def test_production_source_contains_exact_error_message() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert EXPECTED_ERROR in source


def test_production_source_contains_exact_encoding_operation() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert 'json_text.encode("utf-8")' in source
    assert "utf-8-sig" not in source.lower()
    assert "codecs.encode" not in source
    assert "errors=" not in source
    assert ".decode(" not in source


def test_production_source_contains_no_json_creation() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "import json",
        "json.dumps",
        "json.loads",
        "to_json_text",
        "manifest_schema_version",
        "digest_algorithm",
        "sha256_digest",
        "bom_present",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_existing_encoder_dependency() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert "RuntimeRecordInspectionUtf8ByteEncodingService" not in source
    assert "runtime_record_inspection_utf8_byte_encoding_service" not in source


def test_production_source_contains_no_manifest_json_service_dependency() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert "RuntimeRecordInspectionDigestManifestJsonEncodingService" not in source
    assert (
        "runtime_record_inspection_digest_manifest_json_encoding_service"
        not in source
    )


def test_production_source_contains_no_prohibited_dependencies() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "import ",
        "from ",
        "codecs",
        "json.dumps",
        "json.loads",
        "pathlib",
        "tempfile",
        "hashlib",
        "datetime",
        "uuid",
        "random",
        "secrets",
        "gzip",
        "zlib",
        "bz2",
        "lzma",
        "socket",
        "requests",
        "urllib",
        "sqlite3",
        "RuntimeRecordInspectionUtf8ByteEncodingService",
        "RuntimeRecordInspectionDigestManifestJsonEncodingService",
        "RuntimeRecordRegistry",
        "RuntimeRecordInspector",
        "Inspectable",
        "EventEngine",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_decoding() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert ".decode(" not in source
    assert "from_utf8_bytes" not in source
    assert "decode_utf8" not in source
    assert "restore_text" not in source


def test_production_source_contains_no_hashing() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "hashlib",
        "sha256(",
        "hexdigest(",
        "checksum",
        "signature",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_verification() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "verify",
        "validate_digest",
        "compare_digest",
        "verify_length",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_filesystem_behavior() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "open(",
        "Path(",
        "write_text",
        "write_bytes",
        "mkdir",
        "touch(",
        "unlink(",
        "rename(",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_time_generation() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert "datetime.now" not in source
    assert "datetime.utcnow" not in source
    assert "time.time" not in source


def test_production_source_contains_no_identifier_generation() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "uuid",
        "random",
        "secrets",
        "manifest_id",
        "artifact_id",
        "encoded_at",
        "created_at",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_content_type() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "application/json",
        "application/octet-stream",
        "charset=utf-8",
        "content_type",
        "content_length",
        "content_disposition",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_framing_or_compression() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "length_prefix",
        "delimiter",
        "record_separator",
        "framing",
        "gzip",
        "zlib",
        "bz2",
        "lzma",
        "brotli",
        "zipfile",
        "compress",
        "decompress",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_existing_utf8_encoder_remains_digest_manifest_unaware() -> None:
    source = EXISTING_UTF8_ENCODER_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "RuntimeRecordInspectionDigestManifest",
        "RuntimeRecordInspectionDigestManifestJsonEncodingService",
        "RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService",
        "digest_manifest",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_manifest_json_encoder_remains_byte_unaware() -> None:
    source = MANIFEST_JSON_ENCODER_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        '.encode("utf-8")',
        "to_utf8_bytes",
        "bytes(",
        "bytearray(",
        "memoryview(",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_manifest_representation_service_remains_byte_unaware() -> None:
    source = MANIFEST_REPRESENTATION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "to_utf8_bytes",
        ".encode(",
        "bytes(",
        "bytearray(",
        "memoryview(",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_manifest_model_remains_byte_free() -> None:
    prohibited_methods = {
        "to_dict",
        "to_primitive",
        "to_json",
        "to_json_text",
        "to_utf8_bytes",
        "serialize",
        "encode",
    }

    for method_name in prohibited_methods:
        assert not hasattr(
            RuntimeRecordInspectionDigestManifest,
            method_name,
        )