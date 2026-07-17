import json
from collections import OrderedDict
from copy import deepcopy
from pathlib import Path
from types import MappingProxyType

import pytest

from services.runtime_record_inspection_json_encoding_service import (
    RuntimeRecordInspectionJsonEncodingService,
)


PROHIBITED_METHODS = {
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
}

PROHIBITED_OUTPUT_KEYS = {
    "encoding_version",
    "serializer_version",
    "format_version",
    "schema_id",
    "encoded_at",
    "created_at",
    "exported_at",
    "hash",
    "digest",
    "signature",
    "status",
    "healthy",
    "valid",
    "authorized",
    "admitted",
    "canonical",
    "persistent",
    "public",
    "publishable",
    "disclosure_authorized",
    "sharing_allowed",
    "export_authorized",
    "redacted",
}


def make_primitive() -> dict[str, object]:
    return {
        "record_id": "RR-000000001",
        "record_type": "RuntimeEventRecord",
        "record_category": "EVENT",
        "append_position": 0,
        "recorded_at": "2026-07-17T12:30:45.123456+00:00",
        "schema_version": "1.0",
        "provenance_ref": "PRV-000000001",
        "external_id": "  Éxternal-Δ→≠α  ",
        "declared_fields": [
            ["event_type", " OBJECT_CREATED "],
            ["target_ref", "OBJ-α"],
            ["actor_ref", None],
            ["source_ref", "SRC-001"],
            ["scope_ref", None],
            ["branch_ref", "main"],
            ["occurred_at", "2026-07-17T05:30:45.123456-07:00"],
            ["effective_at", None],
        ],
    }


@pytest.fixture
def service() -> RuntimeRecordInspectionJsonEncodingService:
    return RuntimeRecordInspectionJsonEncodingService()


@pytest.fixture
def primitive() -> dict[str, object]:
    return make_primitive()


def test_service_constructs_without_arguments() -> None:
    service = RuntimeRecordInspectionJsonEncodingService()

    assert type(service) is RuntimeRecordInspectionJsonEncodingService


def test_service_has_no_required_state() -> None:
    first = RuntimeRecordInspectionJsonEncodingService()
    second = RuntimeRecordInspectionJsonEncodingService()

    assert vars(first) == {}
    assert vars(second) == {}


@pytest.mark.parametrize(
    "invalid_primitive",
    [
        None,
        [],
        (),
        "json",
        1,
        b"{}",
        bytearray(b"{}"),
        OrderedDict(),
        MappingProxyType({}),
    ],
)
def test_rejects_non_exact_dict_inputs(
    service: RuntimeRecordInspectionJsonEncodingService,
    invalid_primitive: object,
) -> None:
    with pytest.raises(
        TypeError,
        match="primitive must be an exact dict",
    ):
        service.to_json_text(invalid_primitive)  # type: ignore[arg-type]


def test_rejects_dict_subclass(
    service: RuntimeRecordInspectionJsonEncodingService,
) -> None:
    class DerivedDict(dict):
        pass

    with pytest.raises(
        TypeError,
        match="primitive must be an exact dict",
    ):
        service.to_json_text(DerivedDict())


def test_returns_exact_str(
    service: RuntimeRecordInspectionJsonEncodingService,
    primitive: dict[str, object],
) -> None:
    result = service.to_json_text(primitive)

    assert type(result) is str


def test_matches_exact_json_dumps_contract(
    service: RuntimeRecordInspectionJsonEncodingService,
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


def test_preserves_supplied_insertion_order(
    service: RuntimeRecordInspectionJsonEncodingService,
) -> None:
    primitive = {
        "z": 1,
        "a": 2,
        "middle": 3,
    }

    result = service.to_json_text(primitive)

    assert result == '{"z":1,"a":2,"middle":3}'


def test_does_not_sort_keys(
    service: RuntimeRecordInspectionJsonEncodingService,
) -> None:
    result = service.to_json_text({"z": 1, "a": 2})

    assert result.index('"z"') < result.index('"a"')


def test_preserves_unicode_directly(
    service: RuntimeRecordInspectionJsonEncodingService,
) -> None:
    result = service.to_json_text(
        {"value": "α Δ É → ≠"}
    )

    assert "α" in result
    assert "Δ" in result
    assert "É" in result
    assert "→" in result
    assert "≠" in result


def test_does_not_ascii_escape_unicode(
    service: RuntimeRecordInspectionJsonEncodingService,
) -> None:
    result = service.to_json_text({"value": "α"})

    assert "\\u03b1" not in result.lower()


def test_uses_compact_separators(
    service: RuntimeRecordInspectionJsonEncodingService,
) -> None:
    result = service.to_json_text({"a": 1, "b": 2})

    assert result == '{"a":1,"b":2}'


def test_contains_no_formatting_spaces_outside_strings(
    service: RuntimeRecordInspectionJsonEncodingService,
) -> None:
    result = service.to_json_text({"a": 1, "b": [2, 3]})

    assert '": ' not in result
    assert ", " not in result


def test_contains_no_indentation(
    service: RuntimeRecordInspectionJsonEncodingService,
) -> None:
    result = service.to_json_text({"a": {"b": 1}})

    assert "\n" not in result
    assert "\t" not in result


def test_contains_no_trailing_newline(
    service: RuntimeRecordInspectionJsonEncodingService,
    primitive: dict[str, object],
) -> None:
    result = service.to_json_text(primitive)

    assert not result.endswith("\n")
    assert not result.endswith("\r")


def test_preserves_string_whitespace_and_case(
    service: RuntimeRecordInspectionJsonEncodingService,
) -> None:
    result = service.to_json_text(
        {"value": "  Mixed Case Δ  "}
    )

    decoded = json.loads(result)

    assert decoded["value"] == "  Mixed Case Δ  "


def test_preserves_integer_as_json_number(
    service: RuntimeRecordInspectionJsonEncodingService,
) -> None:
    result = service.to_json_text({"append_position": 0})

    assert result == '{"append_position":0}'
    assert '"0"' not in result


def test_encodes_none_as_null(
    service: RuntimeRecordInspectionJsonEncodingService,
) -> None:
    result = service.to_json_text({"value": None})

    assert result == '{"value":null}'


def test_preserves_none_valued_key(
    service: RuntimeRecordInspectionJsonEncodingService,
) -> None:
    result = service.to_json_text({"value": None})
    decoded = json.loads(result)

    assert "value" in decoded
    assert decoded["value"] is None


def test_preserves_declared_field_pair_geometry(
    service: RuntimeRecordInspectionJsonEncodingService,
    primitive: dict[str, object],
) -> None:
    result = service.to_json_text(primitive)
    decoded = json.loads(result)

    declared_fields = decoded["declared_fields"]

    assert type(declared_fields) is list
    assert all(type(entry) is list for entry in declared_fields)
    assert all(len(entry) == 2 for entry in declared_fields)


def test_preserves_declared_field_order(
    service: RuntimeRecordInspectionJsonEncodingService,
    primitive: dict[str, object],
) -> None:
    result = service.to_json_text(primitive)
    decoded = json.loads(result)

    assert [entry[0] for entry in decoded["declared_fields"]] == [
        "event_type",
        "target_ref",
        "actor_ref",
        "source_ref",
        "scope_ref",
        "branch_ref",
        "occurred_at",
        "effective_at",
    ]


def test_repeated_calls_are_equal(
    service: RuntimeRecordInspectionJsonEncodingService,
    primitive: dict[str, object],
) -> None:
    first = service.to_json_text(primitive)
    second = service.to_json_text(primitive)

    assert first == second


def test_two_service_instances_produce_equal_output(
    primitive: dict[str, object],
) -> None:
    first = RuntimeRecordInspectionJsonEncodingService()
    second = RuntimeRecordInspectionJsonEncodingService()

    assert first.to_json_text(primitive) == second.to_json_text(primitive)


def test_encoding_does_not_mutate_source(
    service: RuntimeRecordInspectionJsonEncodingService,
    primitive: dict[str, object],
) -> None:
    before = deepcopy(primitive)

    service.to_json_text(primitive)

    assert primitive == before
    assert list(primitive.keys()) == list(before.keys())


def test_encoding_does_not_mutate_nested_lists(
    service: RuntimeRecordInspectionJsonEncodingService,
    primitive: dict[str, object],
) -> None:
    before_declared = deepcopy(primitive["declared_fields"])

    service.to_json_text(primitive)

    assert primitive["declared_fields"] == before_declared


def test_unsupported_value_raises_native_type_error(
    service: RuntimeRecordInspectionJsonEncodingService,
) -> None:
    primitive = {"unsupported": object()}

    with pytest.raises(TypeError):
        service.to_json_text(primitive)


def test_does_not_fallback_to_stringification(
    service: RuntimeRecordInspectionJsonEncodingService,
) -> None:
    marker = object()

    with pytest.raises(TypeError):
        service.to_json_text({"unsupported": marker})


def test_service_exposes_no_prohibited_methods(
    service: RuntimeRecordInspectionJsonEncodingService,
) -> None:
    for method_name in PROHIBITED_METHODS:
        assert not hasattr(service, method_name)


def test_output_contains_no_generated_fields(
    service: RuntimeRecordInspectionJsonEncodingService,
    primitive: dict[str, object],
) -> None:
    result = service.to_json_text(primitive)
    decoded = json.loads(result)

    assert PROHIBITED_OUTPUT_KEYS.isdisjoint(decoded.keys())


@pytest.mark.parametrize(
    "collection",
    [
        [],
        (),
        [make_primitive()],
        (make_primitive(),),
    ],
)
def test_rejects_collection_inputs(
    service: RuntimeRecordInspectionJsonEncodingService,
    collection: object,
) -> None:
    with pytest.raises(
        TypeError,
        match="primitive must be an exact dict",
    ):
        service.to_json_text(collection)  # type: ignore[arg-type]


def test_service_does_not_inherit_platform_inspectable() -> None:
    from src.services.inspectable import Inspectable

    assert not issubclass(
        RuntimeRecordInspectionJsonEncodingService,
        Inspectable,
    )


def test_output_is_not_bytes(
    service: RuntimeRecordInspectionJsonEncodingService,
    primitive: dict[str, object],
) -> None:
    result = service.to_json_text(primitive)

    assert not isinstance(result, bytes)
    assert not isinstance(result, bytearray)
    assert not isinstance(result, memoryview)


def test_production_source_contains_only_expected_import() -> None:
    source_path = (
        Path("services")
        / "runtime_record_inspection_json_encoding_service.py"
    )
    source = source_path.read_text(encoding="utf-8")

    prohibited_fragments = [
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
        "runtime_record_inspection_report",
        "runtime_record_inspection_representation_service",
        "runtime_record_inspector",
        "runtime_record_registry",
        "src.services.inspectable",
        "event_engine",
        "default=str",
        ".encode(",
    ]

    assert "import json" in source

    for fragment in prohibited_fragments:
        assert fragment not in source


def test_production_source_uses_exact_encoding_arguments() -> None:
    source_path = (
        Path("services")
        / "runtime_record_inspection_json_encoding_service.py"
    )
    source = source_path.read_text(encoding="utf-8")

    assert "ensure_ascii=False" in source
    assert "sort_keys=False" in source
    assert 'separators=(",", ":")' in source


def test_production_source_contains_no_indentation_argument() -> None:
    source_path = (
        Path("services")
        / "runtime_record_inspection_json_encoding_service.py"
    )
    source = source_path.read_text(encoding="utf-8")

    assert "indent=" not in source


def test_production_source_contains_no_current_time_generation() -> None:
    source_path = (
        Path("services")
        / "runtime_record_inspection_json_encoding_service.py"
    )
    source = source_path.read_text(encoding="utf-8")

    assert "datetime.now" not in source
    assert "datetime.utcnow" not in source


def test_encoding_creates_no_files(
    service: RuntimeRecordInspectionJsonEncodingService,
    primitive: dict[str, object],
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    before = sorted(path.relative_to(tmp_path) for path in tmp_path.rglob("*"))

    service.to_json_text(primitive)

    after = sorted(path.relative_to(tmp_path) for path in tmp_path.rglob("*"))

    assert after == before