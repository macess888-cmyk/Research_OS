from dataclasses import FrozenInstanceError, fields, is_dataclass
from pathlib import Path

import pytest

from models.runtime_record_inspection_digest_manifest import (
    RuntimeRecordInspectionDigestManifest,
)


VALID_DIGEST = (
    "e3b0c44298fc1c149afbf4c8996fb924"
    "27ae41e4649b934ca495991b7852b855"
)

EXPECTED_FIELDS = [
    "manifest_schema_version",
    "digest_algorithm",
    "sha256_digest",
    "byte_length",
    "codec",
    "bom_present",
]

PROHIBITED_FIELDS = {
    "manifest_id",
    "artifact_id",
    "record_id",
    "report_id",
    "external_id",
    "provenance_ref",
    "schema_version",
    "source_commit",
    "created_at",
    "generated_at",
    "manifested_at",
    "file_name",
    "path",
    "content_type",
    "manifest_digest",
    "signature",
    "verified",
    "trusted",
    "authorized",
    "public",
    "exported",
    "persisted",
}

PROHIBITED_METHODS = {
    "set_digest",
    "set_byte_length",
    "set_codec",
    "set_bom",
    "update",
    "replace_fields",
    "mutate",
    "clear",
    "append",
    "to_dict",
    "to_primitive",
    "to_json",
    "to_json_text",
    "to_bytes",
    "serialize",
    "encode",
    "sign",
    "verify",
    "save",
    "load",
    "persist",
    "export",
    "write",
    "read",
    "register",
    "inspect",
    "health",
    "status",
}


def make_manifest(
    **overrides: object,
) -> RuntimeRecordInspectionDigestManifest:
    values: dict[str, object] = {
        "manifest_schema_version": "1.0",
        "digest_algorithm": "sha256",
        "sha256_digest": VALID_DIGEST,
        "byte_length": 0,
        "codec": "utf-8",
        "bom_present": False,
    }
    values.update(overrides)

    return RuntimeRecordInspectionDigestManifest(**values)  # type: ignore[arg-type]


def test_model_is_frozen_dataclass() -> None:
    assert is_dataclass(RuntimeRecordInspectionDigestManifest)
    assert (
        RuntimeRecordInspectionDigestManifest.__dataclass_params__.frozen
        is True
    )


def test_model_has_exact_field_order() -> None:
    assert [
        field.name
        for field in fields(RuntimeRecordInspectionDigestManifest)
    ] == EXPECTED_FIELDS


def test_model_has_exact_field_count() -> None:
    assert len(fields(RuntimeRecordInspectionDigestManifest)) == 6


def test_model_fields_have_no_defaults() -> None:
    for field in fields(RuntimeRecordInspectionDigestManifest):
        assert field.default.__class__.__name__ == "_MISSING_TYPE"
        assert field.default_factory.__class__.__name__ == "_MISSING_TYPE"


def test_valid_manifest_constructs() -> None:
    manifest = make_manifest()

    assert type(manifest) is RuntimeRecordInspectionDigestManifest
    assert manifest.manifest_schema_version == "1.0"
    assert manifest.digest_algorithm == "sha256"
    assert manifest.sha256_digest == VALID_DIGEST
    assert manifest.byte_length == 0
    assert manifest.codec == "utf-8"
    assert manifest.bom_present is False


@pytest.mark.parametrize(
    "invalid_value",
    [None, 1, 1.0, [], {}, b"1.0"],
)
def test_manifest_schema_version_rejects_non_exact_string(
    invalid_value: object,
) -> None:
    with pytest.raises(
        TypeError,
        match="manifest_schema_version must be an exact str",
    ):
        make_manifest(manifest_schema_version=invalid_value)


def test_manifest_schema_version_rejects_string_subclass() -> None:
    class DerivedString(str):
        pass

    with pytest.raises(
        TypeError,
        match="manifest_schema_version must be an exact str",
    ):
        make_manifest(manifest_schema_version=DerivedString("1.0"))


@pytest.mark.parametrize(
    "invalid_value",
    ["", "1", "1.1", "2.0", "v1.0"],
)
def test_manifest_schema_version_rejects_invalid_value(
    invalid_value: str,
) -> None:
    with pytest.raises(
        ValueError,
        match="manifest_schema_version must be exactly '1.0'",
    ):
        make_manifest(manifest_schema_version=invalid_value)


@pytest.mark.parametrize(
    "invalid_value",
    [None, 1, [], {}, b"sha256"],
)
def test_digest_algorithm_rejects_non_exact_string(
    invalid_value: object,
) -> None:
    with pytest.raises(
        TypeError,
        match="digest_algorithm must be an exact str",
    ):
        make_manifest(digest_algorithm=invalid_value)


def test_digest_algorithm_rejects_string_subclass() -> None:
    class DerivedString(str):
        pass

    with pytest.raises(
        TypeError,
        match="digest_algorithm must be an exact str",
    ):
        make_manifest(digest_algorithm=DerivedString("sha256"))


@pytest.mark.parametrize(
    "invalid_value",
    ["", "SHA-256", "sha-256", "SHA256", "sha1", "sha512", "md5"],
)
def test_digest_algorithm_rejects_invalid_value(
    invalid_value: str,
) -> None:
    with pytest.raises(
        ValueError,
        match="digest_algorithm must be exactly 'sha256'",
    ):
        make_manifest(digest_algorithm=invalid_value)


@pytest.mark.parametrize(
    "invalid_value",
    [None, 1, [], {}, b"digest"],
)
def test_sha256_digest_rejects_non_exact_string(
    invalid_value: object,
) -> None:
    with pytest.raises(
        TypeError,
        match="sha256_digest must be an exact str",
    ):
        make_manifest(sha256_digest=invalid_value)


def test_sha256_digest_rejects_string_subclass() -> None:
    class DerivedString(str):
        pass

    with pytest.raises(
        TypeError,
        match="sha256_digest must be an exact str",
    ):
        make_manifest(sha256_digest=DerivedString(VALID_DIGEST))


@pytest.mark.parametrize(
    "invalid_value",
    [
        "",
        "a" * 63,
        "a" * 65,
        "A" * 64,
        ("a" * 63) + "G",
        "0x" + ("a" * 64),
        "sha256:" + ("a" * 64),
        ("a" * 32) + " " + ("a" * 31),
        ("a" * 63) + "\n",
    ],
)
def test_sha256_digest_rejects_invalid_format(
    invalid_value: str,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "sha256_digest must be exactly 64 lowercase "
            "hexadecimal characters"
        ),
    ):
        make_manifest(sha256_digest=invalid_value)


@pytest.mark.parametrize(
    "valid_value",
    [0, 1, 100, 2**31],
)
def test_byte_length_accepts_non_negative_exact_int(
    valid_value: int,
) -> None:
    assert make_manifest(byte_length=valid_value).byte_length == valid_value


@pytest.mark.parametrize(
    "invalid_value",
    [None, False, True, 1.0, "1", [], {}],
)
def test_byte_length_rejects_non_exact_int(
    invalid_value: object,
) -> None:
    with pytest.raises(
        TypeError,
        match="byte_length must be an exact int",
    ):
        make_manifest(byte_length=invalid_value)


def test_byte_length_rejects_int_subclass() -> None:
    class DerivedInt(int):
        pass

    with pytest.raises(
        TypeError,
        match="byte_length must be an exact int",
    ):
        make_manifest(byte_length=DerivedInt(1))


@pytest.mark.parametrize(
    "invalid_value",
    [-1, -100],
)
def test_byte_length_rejects_negative_value(
    invalid_value: int,
) -> None:
    with pytest.raises(
        ValueError,
        match="byte_length must be non-negative",
    ):
        make_manifest(byte_length=invalid_value)


@pytest.mark.parametrize(
    "invalid_value",
    [None, 1, [], {}, b"utf-8"],
)
def test_codec_rejects_non_exact_string(
    invalid_value: object,
) -> None:
    with pytest.raises(
        TypeError,
        match="codec must be an exact str",
    ):
        make_manifest(codec=invalid_value)


def test_codec_rejects_string_subclass() -> None:
    class DerivedString(str):
        pass

    with pytest.raises(
        TypeError,
        match="codec must be an exact str",
    ):
        make_manifest(codec=DerivedString("utf-8"))


@pytest.mark.parametrize(
    "invalid_value",
    ["", "UTF-8", "utf8", "utf-8-sig", "ascii", "utf-16"],
)
def test_codec_rejects_invalid_value(
    invalid_value: str,
) -> None:
    with pytest.raises(
        ValueError,
        match="codec must be exactly 'utf-8'",
    ):
        make_manifest(codec=invalid_value)


@pytest.mark.parametrize(
    "invalid_value",
    [None, 0, 1, "false", "False", [], {}],
)
def test_bom_present_rejects_non_exact_bool(
    invalid_value: object,
) -> None:
    with pytest.raises(
        TypeError,
        match="bom_present must be an exact bool",
    ):
        make_manifest(bom_present=invalid_value)


def test_bom_present_rejects_true() -> None:
    with pytest.raises(
        ValueError,
        match="bom_present must be False",
    ):
        make_manifest(bom_present=True)


def test_validation_order_starts_with_manifest_schema_version() -> None:
    with pytest.raises(
        TypeError,
        match="manifest_schema_version must be an exact str",
    ):
        make_manifest(
            manifest_schema_version=None,
            digest_algorithm=None,
            sha256_digest=None,
            byte_length=None,
            codec=None,
            bom_present=None,
        )


def test_validation_order_checks_digest_algorithm_second() -> None:
    with pytest.raises(
        TypeError,
        match="digest_algorithm must be an exact str",
    ):
        make_manifest(
            digest_algorithm=None,
            sha256_digest=None,
            byte_length=None,
            codec=None,
            bom_present=None,
        )


def test_validation_order_checks_digest_third() -> None:
    with pytest.raises(
        TypeError,
        match="sha256_digest must be an exact str",
    ):
        make_manifest(
            sha256_digest=None,
            byte_length=None,
            codec=None,
            bom_present=None,
        )


def test_validation_order_checks_byte_length_fourth() -> None:
    with pytest.raises(
        TypeError,
        match="byte_length must be an exact int",
    ):
        make_manifest(
            byte_length=None,
            codec=None,
            bom_present=None,
        )


def test_validation_order_checks_codec_fifth() -> None:
    with pytest.raises(
        TypeError,
        match="codec must be an exact str",
    ):
        make_manifest(
            codec=None,
            bom_present=None,
        )


def test_validation_order_checks_bom_last() -> None:
    with pytest.raises(
        TypeError,
        match="bom_present must be an exact bool",
    ):
        make_manifest(bom_present=None)


@pytest.mark.parametrize(
    "field_name,new_value",
    [
        ("manifest_schema_version", "2.0"),
        ("digest_algorithm", "sha512"),
        ("sha256_digest", "a" * 64),
        ("byte_length", 10),
        ("codec", "ascii"),
        ("bom_present", True),
    ],
)
def test_manifest_is_immutable(
    field_name: str,
    new_value: object,
) -> None:
    manifest = make_manifest()

    with pytest.raises(FrozenInstanceError):
        setattr(manifest, field_name, new_value)


def test_structural_equality() -> None:
    assert make_manifest() == make_manifest()


def test_structural_inequality() -> None:
    assert make_manifest(byte_length=0) != make_manifest(byte_length=1)


def test_model_has_no_prohibited_fields() -> None:
    field_names = {
        field.name
        for field in fields(RuntimeRecordInspectionDigestManifest)
    }

    assert field_names.isdisjoint(PROHIBITED_FIELDS)


def test_model_exposes_no_prohibited_methods() -> None:
    manifest = make_manifest()

    for method_name in PROHIBITED_METHODS:
        assert not hasattr(manifest, method_name)


def test_model_does_not_inherit_platform_inspectable() -> None:
    from src.services.inspectable import Inspectable

    assert not issubclass(
        RuntimeRecordInspectionDigestManifest,
        Inspectable,
    )


def test_model_source_contains_only_allowed_dependencies() -> None:
    source_path = (
        Path("models")
        / "runtime_record_inspection_digest_manifest.py"
    )
    source = source_path.read_text(encoding="utf-8")

    prohibited_fragments = [
        "import hashlib",
        "from hashlib",
        "import json",
        "from json",
        "import pathlib",
        "from pathlib",
        "import os",
        "from os",
        "import tempfile",
        "from tempfile",
        "import datetime",
        "from datetime",
        "import uuid",
        "import random",
        "runtime_record_inspection_sha256_digest_service",
        "runtime_record_inspection_utf8_byte_encoding_service",
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


def test_model_source_contains_no_derivation() -> None:
    source_path = (
        Path("models")
        / "runtime_record_inspection_digest_manifest.py"
    )
    source = source_path.read_text(encoding="utf-8")

    prohibited_fragments = [
        "hashlib",
        "sha256(",
        "hexdigest(",
        ".digest(",
        '.encode("utf-8")',
        ".decode(",
        "len(content_bytes)",
        "datetime.now",
        "datetime.utcnow",
        "uuid4",
        "object.__setattr__",
    ]

    for fragment in prohibited_fragments:
        assert fragment not in source