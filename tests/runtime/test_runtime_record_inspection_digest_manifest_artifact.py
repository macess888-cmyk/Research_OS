from dataclasses import FrozenInstanceError, fields, is_dataclass
import importlib
from pathlib import Path

import pytest

from models.runtime_record_inspection_digest_manifest import (
    RuntimeRecordInspectionDigestManifest,
)
from models.runtime_record_inspection_digest_manifest_artifact import (
    RuntimeRecordInspectionDigestManifestArtifact,
)


def make_manifest(**overrides):
    values = {
        "manifest_schema_version": "1.0",
        "digest_algorithm": "sha256",
        "sha256_digest": "0" * 64,
        "byte_length": 0,
        "codec": "utf-8",
        "bom_present": False,
    }
    values.update(overrides)
    return RuntimeRecordInspectionDigestManifest(**values)


def make_artifact(**overrides):
    values = {
        "manifest_artifact_id": "RIDMA-000000001",
        "manifest": make_manifest(),
    }
    values.update(overrides)
    return RuntimeRecordInspectionDigestManifestArtifact(**values)


def test_module_imports():
    module = importlib.import_module(
        "models.runtime_record_inspection_digest_manifest_artifact"
    )
    assert module is not None


def test_class_imports_from_selected_module():
    module = importlib.import_module(
        "models.runtime_record_inspection_digest_manifest_artifact"
    )
    assert (
        module.RuntimeRecordInspectionDigestManifestArtifact
        is RuntimeRecordInspectionDigestManifestArtifact
    )


def test_model_is_dataclass():
    assert is_dataclass(
        RuntimeRecordInspectionDigestManifestArtifact
    )


def test_dataclass_field_order_is_exact():
    assert tuple(
        field.name
        for field in fields(
            RuntimeRecordInspectionDigestManifestArtifact
        )
    ) == (
        "manifest_artifact_id",
        "manifest",
    )


def test_constructor_requires_manifest_artifact_id():
    with pytest.raises(TypeError):
        RuntimeRecordInspectionDigestManifestArtifact(
            manifest=make_manifest(),
        )


def test_constructor_requires_manifest():
    with pytest.raises(TypeError):
        RuntimeRecordInspectionDigestManifestArtifact(
            manifest_artifact_id="RIDMA-000000001",
        )


def test_positional_construction_is_supported():
    manifest = make_manifest()

    artifact = RuntimeRecordInspectionDigestManifestArtifact(
        "RIDMA-000000001",
        manifest,
    )

    assert artifact.manifest_artifact_id == "RIDMA-000000001"
    assert artifact.manifest is manifest


def test_keyword_construction_is_supported():
    manifest = make_manifest()

    artifact = RuntimeRecordInspectionDigestManifestArtifact(
        manifest_artifact_id="RIDMA-000000001",
        manifest=manifest,
    )

    assert artifact.manifest_artifact_id == "RIDMA-000000001"
    assert artifact.manifest is manifest


@pytest.mark.parametrize(
    "value",
    [
        "RIDMA-000000001",
        "RIDMA-000000002",
        "RIDMA-000000010",
        "RIDMA-000000100",
        "RIDMA-000001000",
        "RIDMA-999999999",
    ],
)
def test_valid_manifest_artifact_ids_are_preserved(value):
    artifact = make_artifact(
        manifest_artifact_id=value
    )

    assert artifact.manifest_artifact_id == value


@pytest.mark.parametrize(
    "value",
    [
        None,
        True,
        False,
        0,
        1,
        1.0,
        b"RIDMA-000000001",
        [],
        (),
        {},
        set(),
        object(),
    ],
)
def test_manifest_artifact_id_rejects_non_string_values(
    value,
):
    with pytest.raises(
        TypeError,
        match="manifest_artifact_id",
    ):
        make_artifact(manifest_artifact_id=value)


def test_manifest_artifact_id_type_error_message_is_exact():
    with pytest.raises(
        TypeError,
        match=(
            "^manifest_artifact_id must be a string$"
        ),
    ):
        make_artifact(manifest_artifact_id=None)


@pytest.mark.parametrize(
    "value",
    [
        "",
        " ",
        "RIDMA",
        "RIDMA-",
        "RIDMA-1",
        "RIDMA-00000001",
        "RIDMA-0000000001",
        "RIDMA_000000001",
        "RIDM-000000001",
        "RIM-000000001",
        "RIA-000000001",
        "RIRA-000000001",
        "ridma-000000001",
        "Ridma-000000001",
        " RIDMA-000000001",
        "RIDMA-000000001 ",
        "RIDMA-00000000A",
    ],
)
def test_manifest_artifact_id_rejects_invalid_syntax(
    value,
):
    with pytest.raises(
        ValueError,
        match="manifest_artifact_id",
    ):
        make_artifact(manifest_artifact_id=value)


def test_manifest_artifact_id_syntax_error_message_is_exact():
    with pytest.raises(
        ValueError,
        match=(
            "^manifest_artifact_id must match "
            "RIDMA-#########$"
        ),
    ):
        make_artifact(
            manifest_artifact_id="RIDMA-1"
        )


def test_zero_manifest_artifact_id_is_rejected():
    with pytest.raises(
        ValueError,
        match=(
            "^manifest_artifact_id numeric component "
            "must be greater than zero$"
        ),
    ):
        make_artifact(
            manifest_artifact_id="RIDMA-000000000"
        )


def test_maximum_manifest_artifact_id_is_accepted():
    artifact = make_artifact(
        manifest_artifact_id="RIDMA-999999999"
    )

    assert (
        artifact.manifest_artifact_id
        == "RIDMA-999999999"
    )


@pytest.mark.parametrize(
    "value",
    [
        "ridma-000000001",
        "Ridma-000000001",
        "rIDMA-000000001",
    ],
)
def test_manifest_artifact_id_is_case_sensitive(value):
    with pytest.raises(ValueError):
        make_artifact(manifest_artifact_id=value)


@pytest.mark.parametrize(
    "value",
    [
        " RIDMA-000000001",
        "RIDMA-000000001 ",
        "\tRIDMA-000000001",
        "RIDMA-000000001\n",
    ],
)
def test_manifest_artifact_id_rejects_whitespace(value):
    with pytest.raises(ValueError):
        make_artifact(manifest_artifact_id=value)


def test_valid_string_subclass_identifier_is_accepted():
    class ManifestArtifactId(str):
        pass

    value = ManifestArtifactId("RIDMA-000000001")

    artifact = make_artifact(
        manifest_artifact_id=value
    )

    assert artifact.manifest_artifact_id is value


def test_valid_manifest_is_accepted():
    manifest = make_manifest()

    artifact = make_artifact(manifest=manifest)

    assert artifact.manifest is manifest


def test_manifest_object_identity_is_preserved():
    manifest = make_manifest()

    artifact = make_artifact(manifest=manifest)

    assert artifact.manifest is manifest


@pytest.mark.parametrize(
    "value",
    [
        None,
        {},
        [],
        (),
        "manifest",
        b"manifest",
        1,
        1.0,
        object(),
    ],
)
def test_manifest_rejects_invalid_types(value):
    with pytest.raises(
        TypeError,
        match="manifest",
    ):
        make_artifact(manifest=value)


def test_manifest_type_error_message_is_exact():
    with pytest.raises(
        TypeError,
        match=(
            "^manifest must be a "
            "RuntimeRecordInspectionDigestManifest$"
        ),
    ):
        make_artifact(manifest=None)


def test_manifest_subclass_is_accepted():
    class ManifestSubclass(
        RuntimeRecordInspectionDigestManifest
    ):
        pass

    manifest = ManifestSubclass(
        manifest_schema_version="1.0",
        digest_algorithm="sha256",
        sha256_digest="0" * 64,
        byte_length=0,
        codec="utf-8",
        bom_present=False,
    )

    artifact = make_artifact(manifest=manifest)

    assert artifact.manifest is manifest


def test_identifier_type_failure_precedes_manifest_failure():
    with pytest.raises(
        TypeError,
        match="manifest_artifact_id",
    ):
        make_artifact(
            manifest_artifact_id=None,
            manifest=None,
        )


def test_identifier_syntax_failure_precedes_manifest_failure():
    with pytest.raises(
        ValueError,
        match="manifest_artifact_id",
    ):
        make_artifact(
            manifest_artifact_id="invalid",
            manifest=None,
        )


def test_zero_identifier_failure_precedes_manifest_failure():
    with pytest.raises(
        ValueError,
        match=(
            "numeric component must be greater "
            "than zero"
        ),
    ):
        make_artifact(
            manifest_artifact_id="RIDMA-000000000",
            manifest=None,
        )


def test_manifest_failure_occurs_after_valid_identifier():
    with pytest.raises(
        TypeError,
        match="manifest must be",
    ):
        make_artifact(
            manifest_artifact_id="RIDMA-000000001",
            manifest=None,
        )


def test_instance_dictionary_contains_only_contract_fields():
    artifact = make_artifact()

    assert set(artifact.__dict__) == {
        "manifest_artifact_id",
        "manifest",
    }


@pytest.mark.parametrize(
    "attribute",
    [
        "identifier_prefix",
        "numeric_component",
        "artifact_type",
        "validation_status",
    ],
)
def test_no_derived_identifier_state_is_stored(
    attribute,
):
    assert not hasattr(make_artifact(), attribute)


@pytest.mark.parametrize(
    "attribute",
    [
        "manifest_schema_version",
        "digest_algorithm",
        "sha256_digest",
        "byte_length",
        "codec",
        "bom_present",
    ],
)
def test_manifest_fields_are_not_duplicated_on_wrapper(
    attribute,
):
    assert not hasattr(make_artifact(), attribute)


def test_manifest_artifact_id_is_immutable():
    artifact = make_artifact()

    with pytest.raises(FrozenInstanceError):
        artifact.manifest_artifact_id = (
            "RIDMA-000000002"
        )

    assert (
        artifact.manifest_artifact_id
        == "RIDMA-000000001"
    )


def test_manifest_is_immutable_on_wrapper():
    artifact = make_artifact()
    original_manifest = artifact.manifest

    with pytest.raises(FrozenInstanceError):
        artifact.manifest = make_manifest(
            sha256_digest="1" * 64
        )

    assert artifact.manifest is original_manifest


@pytest.mark.parametrize(
    "attribute",
    [
        "manifest_artifact_id",
        "manifest",
    ],
)
def test_fields_cannot_be_deleted(attribute):
    artifact = make_artifact()

    with pytest.raises(FrozenInstanceError):
        delattr(artifact, attribute)


def test_wrapper_equals_itself():
    artifact = make_artifact()

    assert artifact == artifact


def test_same_id_and_equal_manifest_are_equal():
    first = make_artifact()
    second = make_artifact()

    assert first == second


def test_same_id_and_different_manifest_are_not_equal():
    first = make_artifact()
    second = make_artifact(
        manifest=make_manifest(
            sha256_digest="1" * 64
        )
    )

    assert first != second


def test_different_id_and_same_manifest_are_not_equal():
    manifest = make_manifest()

    first = make_artifact(
        manifest_artifact_id="RIDMA-000000001",
        manifest=manifest,
    )
    second = make_artifact(
        manifest_artifact_id="RIDMA-000000002",
        manifest=manifest,
    )

    assert first != second


def test_different_id_and_different_manifest_are_not_equal():
    first = make_artifact()
    second = make_artifact(
        manifest_artifact_id="RIDMA-000000002",
        manifest=make_manifest(
            sha256_digest="1" * 64
        ),
    )

    assert first != second


def test_wrapper_is_not_equal_to_retained_manifest():
    artifact = make_artifact()

    assert artifact != artifact.manifest


def test_wrapper_is_not_equal_to_tuple():
    artifact = make_artifact()

    assert artifact != (
        artifact.manifest_artifact_id,
        artifact.manifest,
    )


def test_wrapper_is_not_equal_to_dictionary():
    artifact = make_artifact()

    assert artifact != {
        "manifest_artifact_id": (
            artifact.manifest_artifact_id
        ),
        "manifest": artifact.manifest,
    }


def test_wrapper_is_hashable():
    assert isinstance(hash(make_artifact()), int)


def test_equal_wrappers_have_equal_hashes():
    first = make_artifact()
    second = make_artifact()

    assert first == second
    assert hash(first) == hash(second)


def test_equal_wrappers_collapse_in_set():
    first = make_artifact()
    second = make_artifact()

    assert len({first, second}) == 1


def test_different_ids_remain_distinct_in_set():
    manifest = make_manifest()

    first = make_artifact(
        manifest_artifact_id="RIDMA-000000001",
        manifest=manifest,
    )
    second = make_artifact(
        manifest_artifact_id="RIDMA-000000002",
        manifest=manifest,
    )

    assert len({first, second}) == 2


def test_wrapper_can_be_dictionary_key():
    artifact = make_artifact()

    values = {artifact: "stored"}

    assert values[artifact] == "stored"


@pytest.mark.parametrize(
    "operator",
    [
        lambda first, second: first < second,
        lambda first, second: first <= second,
        lambda first, second: first > second,
        lambda first, second: first >= second,
    ],
)
def test_wrapper_has_no_ordering(operator):
    with pytest.raises(TypeError):
        operator(make_artifact(), make_artifact())


def test_class_defines_no_custom_bool():
    assert (
        "__bool__"
        not in (
            RuntimeRecordInspectionDigestManifestArtifact
            .__dict__
        )
    )


def test_default_repr_exposes_contract_fields():
    representation = repr(make_artifact())

    assert (
        "RuntimeRecordInspectionDigestManifestArtifact"
        in representation
    )
    assert "manifest_artifact_id" in representation
    assert "manifest=" in representation


@pytest.mark.parametrize(
    "method_name",
    [
        "__iter__",
        "__len__",
        "__getitem__",
        "to_dict",
        "to_json",
        "to_bytes",
        "serialize",
        "deserialize",
        "compute_digest",
        "allocate_id",
        "next_id",
        "generate_id",
        "new_id",
        "register",
        "persist",
        "save",
        "load",
        "verify",
        "admit",
        "authorize",
    ],
)
def test_class_excludes_unowned_methods(method_name):
    assert not hasattr(
        RuntimeRecordInspectionDigestManifestArtifact,
        method_name,
    )


@pytest.mark.parametrize(
    "attribute",
    [
        "created_at",
        "observed_at",
        "recorded_at",
        "registered_at",
        "effective_at",
        "source_ref",
        "creator_ref",
        "actor_ref",
        "method_ref",
        "environment_ref",
        "custody_ref",
        "custodian_ref",
        "transfer_ref",
        "storage_ref",
        "predecessor_ref",
        "parent_ref",
        "version_ref",
        "supersedes_ref",
        "derived_from_ref",
        "report_artifact_id",
        "report_ref",
        "association_ref",
        "binding_ref",
        "registry_ref",
        "append_position",
        "persisted",
        "admitted",
        "acceptable",
        "eligible",
        "approved",
        "trusted",
        "authorized",
        "authority_ref",
        "permission",
        "execution_allowed",
        "historical_binding_established",
        "creation_association_established",
        "custody_continuity_established",
        "external_anchor_established",
        "authentic",
        "verified_origin",
    ],
)
def test_wrapper_excludes_unowned_fields(attribute):
    assert not hasattr(make_artifact(), attribute)


def test_validation_methods_are_present():
    assert callable(
        RuntimeRecordInspectionDigestManifestArtifact
        ._validate_manifest_artifact_id
    )
    assert callable(
        RuntimeRecordInspectionDigestManifestArtifact
        ._validate_manifest
    )


@pytest.mark.parametrize(
    "method_name",
    [
        "_validate_registry",
        "_validate_provenance",
        "_validate_custody",
        "_validate_report",
    ],
)
def test_unowned_validation_methods_are_absent(
    method_name,
):
    assert not hasattr(
        RuntimeRecordInspectionDigestManifestArtifact,
        method_name,
    )


def test_class_has_boundary_docstring():
    docstring = (
        RuntimeRecordInspectionDigestManifestArtifact
        .__doc__
        or ""
    ).lower()

    assert "identity" in docstring
    assert "addressability" in docstring
    assert "persist" in docstring
    assert "authorize" in docstring


def test_manifest_artifact_id_is_independent_of_digest():
    artifact = make_artifact(
        manifest_artifact_id="RIDMA-000000001",
        manifest=make_manifest(
            sha256_digest="f" * 64
        ),
    )

    assert (
        artifact.manifest_artifact_id
        == "RIDMA-000000001"
    )
    assert artifact.manifest.sha256_digest == "f" * 64


def test_same_digest_can_have_different_artifact_ids():
    manifest = make_manifest(
        sha256_digest="f" * 64
    )

    first = make_artifact(
        manifest_artifact_id="RIDMA-000000001",
        manifest=manifest,
    )
    second = make_artifact(
        manifest_artifact_id="RIDMA-000000002",
        manifest=manifest,
    )

    assert (
        first.manifest.sha256_digest
        == second.manifest.sha256_digest
    )
    assert first != second


def test_different_digests_can_share_id_in_memory():
    first = make_artifact(
        manifest_artifact_id="RIDMA-000000001",
        manifest=make_manifest(
            sha256_digest="0" * 64
        ),
    )
    second = make_artifact(
        manifest_artifact_id="RIDMA-000000001",
        manifest=make_manifest(
            sha256_digest="1" * 64
        ),
    )

    assert first != second


def test_same_manifest_value_with_different_ids_is_unequal():
    manifest = make_manifest()

    first = make_artifact(
        manifest_artifact_id="RIDMA-000000001",
        manifest=manifest,
    )
    second = make_artifact(
        manifest_artifact_id="RIDMA-000000002",
        manifest=manifest,
    )

    assert first != second


def test_manifest_identity_is_independent_of_byte_length():
    first = make_artifact(
        manifest=make_manifest(byte_length=0)
    )
    second = make_artifact(
        manifest=make_manifest(byte_length=1)
    )

    assert (
        first.manifest_artifact_id
        == second.manifest_artifact_id
    )
    assert first != second


def test_manifest_identity_is_independent_of_bom_claim():
    first = make_artifact(
        manifest=make_manifest(
            bom_present=False
        )
    )
    second = make_artifact(
        manifest=make_manifest(
            bom_present=True
        )
    )

    assert (
        first.manifest_artifact_id
        == second.manifest_artifact_id
    )
    assert first != second


def test_matching_numeric_suffix_does_not_create_cross_namespace_identity():
    assert "RIRA-000000001" != "RIDMA-000000001"


def test_repeated_construction_is_deterministic():
    manifest = make_manifest()

    first = make_artifact(manifest=manifest)
    second = make_artifact(manifest=manifest)

    assert first == second
    assert first.manifest is manifest
    assert second.manifest is manifest


def test_construction_emits_no_output(capsys):
    make_artifact()

    captured = capsys.readouterr()

    assert captured.out == ""
    assert captured.err == ""


def test_source_has_no_framework_or_service_imports():
    source_path = (
        Path(__file__).resolve().parents[2]
        / "models"
        / (
            "runtime_record_inspection_"
            "digest_manifest_artifact.py"
        )
    )
    source = source_path.read_text(
        encoding="utf-8"
    ).lower()

    prohibited_terms = (
        "streamlit",
        "flask",
        "django",
        "fastapi",
        "tkinter",
        "pyqt",
        "pandas",
        "numpy",
        "sqlalchemy",
        "runtime_record_registry",
        "artifact_registry",
        "from services",
        "import services",
        "hashlib",
        "uuid",
        "pathlib",
    )

    for term in prohibited_terms:
        assert term not in source


def test_source_defines_private_pattern_constant():
    module = importlib.import_module(
        "models.runtime_record_inspection_digest_manifest_artifact"
    )

    pattern = module._MANIFEST_ARTIFACT_ID_PATTERN

    assert pattern.pattern == r"^RIDMA-[0-9]{9}$"


def test_pattern_constant_is_not_dataclass_field():
    assert (
        "_MANIFEST_ARTIFACT_ID_PATTERN"
        not in {
            field.name
            for field in fields(
                RuntimeRecordInspectionDigestManifestArtifact
            )
        }
    )