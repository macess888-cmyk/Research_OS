import json
from collections import OrderedDict
from copy import deepcopy
from pathlib import Path
from types import MappingProxyType

import pytest

from models.runtime_record_inspection_digest_manifest import (
    RuntimeRecordInspectionDigestManifest,
)
from services.runtime_record_inspection_digest_manifest_json_encoding_service import (
    RuntimeRecordInspectionDigestManifestJsonEncodingService,
)


PRODUCTION_PATH = (
    Path("services")
    / "runtime_record_inspection_digest_manifest_json_encoding_service.py"
)

EXISTING_JSON_ENCODER_PATH = (
    Path("services")
    / "runtime_record_inspection_json_encoding_service.py"
)

MANIFEST_REPRESENTATION_PATH = (
    Path("services")
    / "runtime_record_inspection_digest_manifest_representation_service.py"
)

EXPECTED_ERROR = "primitive must be an exact dict"

EXPECTED_JSON = (
    '{"manifest_schema_version":"1.0",'
    '"digest_algorithm":"sha256",'
    '"sha256_digest":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",'
    '"byte_length":128,'
    '"codec":"utf-8",'
    '"bom_present":false}'
)

PROHIBITED_PUBLIC_METHODS = {
    "to_json",
    "serialize",
    "deserialize",
    "from_json",
    "decode_json",
    "encode_bytes",
    "to_utf8_bytes",
    "dump",
    "dumps",
    "load",
    "loads",
    "save",
    "persist",
    "export",
    "write",
    "read",
    "hash",
    "digest",
    "checksum",
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
    "to_json_list",
    "build_manifest",
    "create_manifest",
    "to_primitive_dict",
}


class DerivedDict(dict):
    pass


class ExplodingMapping:
    def __iter__(self):
        raise AssertionError("mapping must not be traversed")

    def __getitem__(self, key: object) -> object:
        raise AssertionError("mapping must not be traversed")

    def keys(self):
        raise AssertionError("mapping must not be traversed")


@pytest.fixture
def primitive() -> dict[str, object]:
    return {
        "manifest_schema_version": "1.0",
        "digest_algorithm": "sha256",
        "sha256_digest": "a" * 64,
        "byte_length": 128,
        "codec": "utf-8",
        "bom_present": False,
    }


@pytest.fixture
def service() -> RuntimeRecordInspectionDigestManifestJsonEncodingService:
    return RuntimeRecordInspectionDigestManifestJsonEncodingService()


def test_service_can_be_constructed() -> None:
    service = RuntimeRecordInspectionDigestManifestJsonEncodingService()

    assert (
        type(service)
        is RuntimeRecordInspectionDigestManifestJsonEncodingService
    )


def test_service_instances_are_independent() -> None:
    first = RuntimeRecordInspectionDigestManifestJsonEncodingService()
    second = RuntimeRecordInspectionDigestManifestJsonEncodingService()

    assert first is not second


def test_service_constructor_requires_no_arguments() -> None:
    service = RuntimeRecordInspectionDigestManifestJsonEncodingService()

    assert (
        type(service)
        is RuntimeRecordInspectionDigestManifestJsonEncodingService
    )


def test_service_exposes_required_method(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
) -> None:
    assert callable(service.to_json_text)


@pytest.mark.parametrize(
    "method_name",
    sorted(PROHIBITED_PUBLIC_METHODS),
)
def test_service_exposes_no_prohibited_public_method(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
    method_name: str,
) -> None:
    assert not hasattr(service, method_name)


def test_exact_plain_dictionary_is_accepted(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
    primitive: dict[str, object],
) -> None:
    result = service.to_json_text(primitive)

    assert type(result) is str


@pytest.mark.parametrize(
    "invalid_primitive",
    [
        None,
        True,
        False,
        0,
        1,
        1.5,
        "{}",
        b"{}",
        bytearray(),
        memoryview(b""),
        [],
        (),
        set(),
        frozenset(),
        object(),
        OrderedDict(),
        MappingProxyType({}),
        DerivedDict(),
        ExplodingMapping(),
        [{}],
        ({},),
    ],
)
def test_non_exact_dictionary_values_are_rejected(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
    invalid_primitive: object,
) -> None:
    with pytest.raises(TypeError, match=f"^{EXPECTED_ERROR}$"):
        service.to_json_text(invalid_primitive)  # type: ignore[arg-type]


def test_manifest_model_is_rejected(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
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
        service.to_json_text(manifest)  # type: ignore[arg-type]


def test_dictionary_subclass_is_rejected(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
    primitive: dict[str, object],
) -> None:
    derived = DerivedDict(primitive)

    with pytest.raises(TypeError, match=f"^{EXPECTED_ERROR}$"):
        service.to_json_text(derived)


def test_invalid_mapping_is_rejected_before_traversal(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
) -> None:
    with pytest.raises(TypeError, match=f"^{EXPECTED_ERROR}$"):
        service.to_json_text(ExplodingMapping())  # type: ignore[arg-type]


def test_result_is_exact_string(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
    primitive: dict[str, object],
) -> None:
    result = service.to_json_text(primitive)

    assert type(result) is str


def test_matches_exact_json_dumps_contract(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
    primitive: dict[str, object],
) -> None:
    result = service.to_json_text(primitive)

    expected = json.dumps(
        primitive,
        ensure_ascii=False,
        sort_keys=False,
        separators=(",", ":"),
    )

    assert result == expected


def test_produces_exact_manifest_json_text(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
    primitive: dict[str, object],
) -> None:
    result = service.to_json_text(primitive)

    assert result == EXPECTED_JSON


def test_preserves_digest_manifest_field_order(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
    primitive: dict[str, object],
) -> None:
    result = service.to_json_text(primitive)

    expected_positions = [
        result.index('"manifest_schema_version"'),
        result.index('"digest_algorithm"'),
        result.index('"sha256_digest"'),
        result.index('"byte_length"'),
        result.index('"codec"'),
        result.index('"bom_present"'),
    ]

    assert expected_positions == sorted(expected_positions)


def test_preserves_non_alphabetical_insertion_order(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
) -> None:
    primitive = {
        "z": 1,
        "a": 2,
        "m": 3,
    }

    result = service.to_json_text(primitive)

    assert result == '{"z":1,"a":2,"m":3}'


def test_does_not_sort_keys(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
) -> None:
    primitive = {
        "z": 1,
        "a": 2,
    }

    result = service.to_json_text(primitive)
    sorted_result = json.dumps(
        primitive,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )

    assert result == '{"z":1,"a":2}'
    assert result != sorted_result


def test_preserves_unicode_directly(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
) -> None:
    primitive = {
        "value": "α Δ É → ≠",
    }

    result = service.to_json_text(primitive)

    assert "α" in result
    assert "Δ" in result
    assert "É" in result
    assert "→" in result
    assert "≠" in result
    assert "\\u03b1" not in result.lower()


def test_uses_compact_separators(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
) -> None:
    result = service.to_json_text({"a": 1, "b": 2})

    assert result == '{"a":1,"b":2}'
    assert '": ' not in result
    assert ", " not in result


def test_output_contains_no_indentation(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
    primitive: dict[str, object],
) -> None:
    result = service.to_json_text(primitive)

    assert "\n  " not in result
    assert "\t" not in result


def test_output_contains_no_trailing_newline(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
    primitive: dict[str, object],
) -> None:
    result = service.to_json_text(primitive)

    assert not result.endswith("\n")
    assert not result.endswith("\r")


def test_integer_remains_json_number(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
) -> None:
    result = service.to_json_text({"byte_length": 128})

    assert result == '{"byte_length":128}'
    assert '"128"' not in result


def test_false_remains_json_boolean(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
) -> None:
    result = service.to_json_text({"bom_present": False})

    assert result == '{"bom_present":false}'


def test_true_uses_native_json_behavior(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
) -> None:
    result = service.to_json_text({"value": True})

    assert result == '{"value":true}'


@pytest.mark.parametrize(
    "primitive",
    [
        {},
        {"unexpected": "value"},
        {"bom_present": True},
        {"byte_length": -1},
    ],
)
def test_exact_dictionary_shape_is_not_semantically_validated(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
    primitive: dict[str, object],
) -> None:
    result = service.to_json_text(primitive)

    assert result == json.dumps(
        primitive,
        ensure_ascii=False,
        sort_keys=False,
        separators=(",", ":"),
    )


def test_preserves_string_values(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
) -> None:
    primitive = {
        "value": "  Sha256 α →  ",
    }

    result = service.to_json_text(primitive)

    assert result == '{"value":"  Sha256 α →  "}'


def test_source_dictionary_is_not_mutated(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
    primitive: dict[str, object],
) -> None:
    before = primitive.copy()
    before_keys = list(primitive.keys())

    service.to_json_text(primitive)

    assert primitive == before
    assert list(primitive.keys()) == before_keys


def test_nested_values_are_not_mutated(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
) -> None:
    primitive = {
        "nested": {
            "values": [1, 2, {"flag": False}],
        }
    }
    before = deepcopy(primitive)

    service.to_json_text(primitive)

    assert primitive == before


def test_repeated_calls_are_deterministic(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
    primitive: dict[str, object],
) -> None:
    first = service.to_json_text(primitive)
    second = service.to_json_text(primitive)

    assert first == second


def test_independent_services_return_equal_results(
    primitive: dict[str, object],
) -> None:
    first = RuntimeRecordInspectionDigestManifestJsonEncodingService()
    second = RuntimeRecordInspectionDigestManifestJsonEncodingService()

    assert first.to_json_text(primitive) == second.to_json_text(primitive)


def test_service_owns_no_mutable_instance_state(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
    primitive: dict[str, object],
) -> None:
    assert service.__dict__ == {}

    service.to_json_text(primitive)

    assert service.__dict__ == {}


def test_prior_call_does_not_affect_later_output(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
    primitive: dict[str, object],
) -> None:
    service.to_json_text({"previous": "value"})

    result = service.to_json_text(primitive)

    assert result == EXPECTED_JSON


def test_native_unsupported_value_error_propagates(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
) -> None:
    marker = object()

    with pytest.raises(TypeError):
        service.to_json_text({"unsupported": marker})


def test_unsupported_value_is_not_stringified(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
) -> None:
    marker = object()

    with pytest.raises(TypeError):
        service.to_json_text({"unsupported": marker})


def test_encoding_creates_no_files(
    service: RuntimeRecordInspectionDigestManifestJsonEncodingService,
    primitive: dict[str, object],
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    before = sorted(path.relative_to(tmp_path) for path in tmp_path.rglob("*"))

    service.to_json_text(primitive)

    after = sorted(path.relative_to(tmp_path) for path in tmp_path.rglob("*"))

    assert after == before


def test_production_file_exists() -> None:
    assert PRODUCTION_PATH.is_file()


def test_production_source_imports_only_json() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")
    import_lines = [
        line.strip()
        for line in source.splitlines()
        if line.strip().startswith(("import ", "from "))
    ]

    assert import_lines == ["import json"]


def test_production_source_contains_exact_type_check() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert "type(primitive) is not dict" in source
    assert "isinstance(primitive, dict)" not in source


def test_production_source_contains_exact_error_message() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert EXPECTED_ERROR in source


def test_production_source_contains_exact_json_arguments() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    assert "json.dumps(" in source
    assert "ensure_ascii=False" in source
    assert "sort_keys=False" in source
    assert 'separators=(",", ":")' in source
    assert "sort_keys=True" not in source
    assert "ensure_ascii=True" not in source
    assert "indent=" not in source
    assert "default=" not in source


def test_production_source_contains_no_prohibited_dependencies() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "from models",
        "from services",
        "import pathlib",
        "from pathlib",
        "import os",
        "from os",
        "import sys",
        "from sys",
        "import tempfile",
        "from tempfile",
        "import hashlib",
        "from hashlib",
        "import datetime",
        "from datetime",
        "import time",
        "from time",
        "import uuid",
        "from uuid",
        "import random",
        "from random",
        "import secrets",
        "from secrets",
        "import pickle",
        "import yaml",
        "import sqlite3",
        "RuntimeRecordInspectionDigestManifestService",
        "RuntimeRecordInspectionDigestManifestRepresentationService",
        "RuntimeRecordInspectionJsonEncodingService",
        "RuntimeRecordInspectionReport",
        "RuntimeRecordInspectionRepresentationService",
        "RuntimeRecordInspector",
        "RuntimeRecordRegistry",
        "Inspectable",
        "EventEngine",
        "requests",
        "urllib",
        "http.client",
        "socket",
        "aiohttp",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_contains_no_byte_encoding() -> None:
    source = PRODUCTION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        ".encode(",
        "bytes(",
        "bytearray(",
        "memoryview(",
        "utf-8-sig",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


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


def test_existing_json_encoder_remains_digest_manifest_unaware() -> None:
    source = EXISTING_JSON_ENCODER_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "RuntimeRecordInspectionDigestManifest",
        "RuntimeRecordInspectionDigestManifestRepresentationService",
        "RuntimeRecordInspectionDigestManifestJsonEncodingService",
        "digest_manifest",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_manifest_representation_service_remains_json_unaware() -> None:
    source = MANIFEST_REPRESENTATION_PATH.read_text(encoding="utf-8")

    prohibited_fragments = [
        "import json",
        "json.dumps",
        "to_json",
        "to_json_text",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_manifest_model_remains_json_free() -> None:
    prohibited_methods = {
        "to_dict",
        "to_primitive",
        "to_json",
        "to_json_text",
        "serialize",
        "encode",
    }

    for method_name in prohibited_methods:
        assert not hasattr(
            RuntimeRecordInspectionDigestManifest,
            method_name,
        )