from pathlib import Path

import pytest

from services.runtime_record_inspection_utf8_byte_encoding_service import (
    RuntimeRecordInspectionUtf8ByteEncodingService,
)


PROHIBITED_METHODS = {
    "encode",
    "encode_text",
    "to_bytes",
    "to_bytearray",
    "to_memoryview",
    "decode",
    "from_utf8_bytes",
    "to_text",
    "to_json_text",
    "parse_json",
    "validate_json",
    "save",
    "load",
    "persist",
    "export",
    "write",
    "read",
    "hash",
    "digest",
    "checksum",
    "fingerprint",
    "sign",
    "verify",
    "redact",
    "mask",
    "classify",
    "publish",
    "upload",
    "download",
    "inspect",
    "health",
    "status",
    "encode_collection",
    "encode_stream",
}


@pytest.fixture
def service() -> RuntimeRecordInspectionUtf8ByteEncodingService:
    return RuntimeRecordInspectionUtf8ByteEncodingService()


def test_service_constructs_without_arguments() -> None:
    service = RuntimeRecordInspectionUtf8ByteEncodingService()

    assert type(service) is RuntimeRecordInspectionUtf8ByteEncodingService


def test_service_has_no_required_state() -> None:
    first = RuntimeRecordInspectionUtf8ByteEncodingService()
    second = RuntimeRecordInspectionUtf8ByteEncodingService()

    assert vars(first) == {}
    assert vars(second) == {}


@pytest.mark.parametrize(
    "invalid_json_text",
    [
        None,
        {},
        [],
        (),
        1,
        b"{}",
        bytearray(b"{}"),
        memoryview(b"{}"),
        ["{}"],
        ("{}",),
    ],
)
def test_rejects_non_exact_string_inputs(
    service: RuntimeRecordInspectionUtf8ByteEncodingService,
    invalid_json_text: object,
) -> None:
    with pytest.raises(
        TypeError,
        match="json_text must be an exact str",
    ):
        service.to_utf8_bytes(invalid_json_text)  # type: ignore[arg-type]


def test_rejects_string_subclass(
    service: RuntimeRecordInspectionUtf8ByteEncodingService,
) -> None:
    class DerivedString(str):
        pass

    with pytest.raises(
        TypeError,
        match="json_text must be an exact str",
    ):
        service.to_utf8_bytes(DerivedString("{}"))


def test_returns_exact_bytes(
    service: RuntimeRecordInspectionUtf8ByteEncodingService,
) -> None:
    result = service.to_utf8_bytes('{"a":1}')

    assert type(result) is bytes


def test_matches_exact_utf8_encoding(
    service: RuntimeRecordInspectionUtf8ByteEncodingService,
) -> None:
    json_text = (
        '{"record_id":"RR-000000001",'
        '"external_id":"Éxternal-Δ→≠α"}'
    )

    result = service.to_utf8_bytes(json_text)

    assert result == json_text.encode("utf-8")


def test_encodes_ascii_exactly(
    service: RuntimeRecordInspectionUtf8ByteEncodingService,
) -> None:
    result = service.to_utf8_bytes('{"a":1}')

    assert result == b'{"a":1}'


@pytest.mark.parametrize(
    "value",
    [
        "α",
        "Δ",
        "É",
        "→",
        "≠",
        "α Δ É → ≠",
    ],
)
def test_encodes_unicode_exactly(
    service: RuntimeRecordInspectionUtf8ByteEncodingService,
    value: str,
) -> None:
    assert service.to_utf8_bytes(value) == value.encode("utf-8")


def test_encodes_expected_multibyte_sequences(
    service: RuntimeRecordInspectionUtf8ByteEncodingService,
) -> None:
    assert service.to_utf8_bytes("α") == b"\xce\xb1"
    assert service.to_utf8_bytes("→") == b"\xe2\x86\x92"
    assert service.to_utf8_bytes("É") == b"\xc3\x89"


def test_accepts_empty_string(
    service: RuntimeRecordInspectionUtf8ByteEncodingService,
) -> None:
    assert service.to_utf8_bytes("") == b""


def test_accepts_invalid_json_text_as_exact_string(
    service: RuntimeRecordInspectionUtf8ByteEncodingService,
) -> None:
    assert service.to_utf8_bytes("not-json") == b"not-json"
    assert service.to_utf8_bytes("{") == b"{"


def test_preserves_leading_and_trailing_spaces(
    service: RuntimeRecordInspectionUtf8ByteEncodingService,
) -> None:
    value = "  text  "

    assert service.to_utf8_bytes(value) == b"  text  "


def test_preserves_tabs_and_newlines(
    service: RuntimeRecordInspectionUtf8ByteEncodingService,
) -> None:
    value = "\tline1\nline2\r\n"

    assert service.to_utf8_bytes(value) == value.encode("utf-8")


def test_introduces_no_newline(
    service: RuntimeRecordInspectionUtf8ByteEncodingService,
) -> None:
    result = service.to_utf8_bytes('{"a":1}')

    assert not result.endswith(b"\n")
    assert not result.endswith(b"\r")


def test_encodes_null_character(
    service: RuntimeRecordInspectionUtf8ByteEncodingService,
) -> None:
    assert service.to_utf8_bytes("\x00") == b"\x00"


def test_does_not_interpret_escape_sequences(
    service: RuntimeRecordInspectionUtf8ByteEncodingService,
) -> None:
    value = r"\u0041"

    result = service.to_utf8_bytes(value)

    assert result == b"\\u0041"
    assert result != b"A"


def test_produces_no_utf8_bom(
    service: RuntimeRecordInspectionUtf8ByteEncodingService,
) -> None:
    result = service.to_utf8_bytes('{"a":1}')

    assert not result.startswith(b"\xef\xbb\xbf")


def test_uses_strict_default_encoding_errors(
    service: RuntimeRecordInspectionUtf8ByteEncodingService,
) -> None:
    value = "\ud800"

    with pytest.raises(UnicodeEncodeError):
        service.to_utf8_bytes(value)


def test_repeated_calls_are_equal(
    service: RuntimeRecordInspectionUtf8ByteEncodingService,
) -> None:
    value = '{"value":"α"}'

    first = service.to_utf8_bytes(value)
    second = service.to_utf8_bytes(value)

    assert first == second


def test_two_service_instances_produce_equal_output() -> None:
    value = '{"value":"α"}'
    first = RuntimeRecordInspectionUtf8ByteEncodingService()
    second = RuntimeRecordInspectionUtf8ByteEncodingService()

    assert first.to_utf8_bytes(value) == second.to_utf8_bytes(value)


def test_input_value_remains_unchanged(
    service: RuntimeRecordInspectionUtf8ByteEncodingService,
) -> None:
    value = '  {"value":"Δ"}  '
    before = value

    service.to_utf8_bytes(value)

    assert value == before


def test_output_is_not_bytearray(
    service: RuntimeRecordInspectionUtf8ByteEncodingService,
) -> None:
    result = service.to_utf8_bytes("{}")

    assert not isinstance(result, bytearray)


def test_output_is_not_memoryview(
    service: RuntimeRecordInspectionUtf8ByteEncodingService,
) -> None:
    result = service.to_utf8_bytes("{}")

    assert not isinstance(result, memoryview)


def test_service_exposes_no_prohibited_methods(
    service: RuntimeRecordInspectionUtf8ByteEncodingService,
) -> None:
    for method_name in PROHIBITED_METHODS:
        assert not hasattr(service, method_name)


@pytest.mark.parametrize(
    "collection",
    [
        [],
        (),
        ["{}"],
        ("{}",),
        ["{}", "{}"],
    ],
)
def test_rejects_collection_inputs(
    service: RuntimeRecordInspectionUtf8ByteEncodingService,
    collection: object,
) -> None:
    with pytest.raises(
        TypeError,
        match="json_text must be an exact str",
    ):
        service.to_utf8_bytes(collection)  # type: ignore[arg-type]


def test_service_does_not_inherit_platform_inspectable() -> None:
    from src.services.inspectable import Inspectable

    assert not issubclass(
        RuntimeRecordInspectionUtf8ByteEncodingService,
        Inspectable,
    )


def test_production_source_requires_no_imports() -> None:
    source_path = (
        Path("services")
        / "runtime_record_inspection_utf8_byte_encoding_service.py"
    )
    source = source_path.read_text(encoding="utf-8")

    prohibited_fragments = [
        "import json",
        "from json",
        "import codecs",
        "from codecs",
        "import pathlib",
        "from pathlib",
        "import os",
        "from os",
        "import tempfile",
        "from tempfile",
        "import hashlib",
        "from hashlib",
        "import datetime",
        "from datetime",
        "import uuid",
        "import random",
        "runtime_record_inspection_json_encoding_service",
        "runtime_record_inspection_representation_service",
        "runtime_record_inspection_report",
        "runtime_record_inspector",
        "runtime_record_registry",
        "src.services.inspectable",
        "event_engine",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_uses_exact_utf8_operation() -> None:
    source_path = (
        Path("services")
        / "runtime_record_inspection_utf8_byte_encoding_service.py"
    )
    source = source_path.read_text(encoding="utf-8")

    assert '.encode("utf-8")' in source


def test_production_source_does_not_use_utf8_sig() -> None:
    source_path = (
        Path("services")
        / "runtime_record_inspection_utf8_byte_encoding_service.py"
    )
    source = source_path.read_text(encoding="utf-8")

    assert "utf-8-sig" not in source


def test_production_source_contains_no_lossy_error_mode() -> None:
    source_path = (
        Path("services")
        / "runtime_record_inspection_utf8_byte_encoding_service.py"
    )
    source = source_path.read_text(encoding="utf-8")

    prohibited_error_modes = [
        'errors="ignore"',
        'errors="replace"',
        'errors="backslashreplace"',
        'errors="surrogateescape"',
        'errors="surrogatepass"',
    ]

    for fragment in prohibited_error_modes:
        assert fragment not in source


def test_production_source_contains_no_decoding() -> None:
    source_path = (
        Path("services")
        / "runtime_record_inspection_utf8_byte_encoding_service.py"
    )
    source = source_path.read_text(encoding="utf-8")

    assert ".decode(" not in source


def test_production_source_contains_no_bytearray_or_memoryview() -> None:
    source_path = (
        Path("services")
        / "runtime_record_inspection_utf8_byte_encoding_service.py"
    )
    source = source_path.read_text(encoding="utf-8")

    assert "bytearray(" not in source
    assert "memoryview(" not in source


def test_production_source_contains_no_current_time_generation() -> None:
    source_path = (
        Path("services")
        / "runtime_record_inspection_utf8_byte_encoding_service.py"
    )
    source = source_path.read_text(encoding="utf-8")

    assert "datetime.now" not in source
    assert "datetime.utcnow" not in source


def test_encoding_creates_no_files(
    service: RuntimeRecordInspectionUtf8ByteEncodingService,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    before = sorted(path.relative_to(tmp_path) for path in tmp_path.rglob("*"))

    service.to_utf8_bytes('{"a":1}')

    after = sorted(path.relative_to(tmp_path) for path in tmp_path.rglob("*"))

    assert after == before