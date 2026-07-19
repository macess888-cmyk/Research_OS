from dataclasses import is_dataclass
from datetime import datetime, timezone
import importlib
from pathlib import Path

import pytest

from models.runtime_record_inspection_artifact_registration_result import (
    RuntimeRecordInspectionArtifactRegistrationResult,
)
from models.runtime_record_inspection_digest_manifest import (
    RuntimeRecordInspectionDigestManifest,
)
from models.runtime_record_inspection_digest_manifest_artifact import (
    RuntimeRecordInspectionDigestManifestArtifact,
)
from models.runtime_record_inspection_report import (
    RuntimeRecordInspectionReport,
)
from models.runtime_record_inspection_report_artifact import (
    RuntimeRecordInspectionReportArtifact,
)
from services.runtime_record_inspection_artifact_registry import (
    RuntimeRecordInspectionArtifactRegistry,
)


RECORDED_AT = datetime(
    2026,
    7,
    19,
    12,
    0,
    tzinfo=timezone.utc,
)


def make_report(**overrides):
    values = {
        "record_id": "RR-000000001",
        "record_type": "RuntimeEventRecord",
        "record_category": "EVENT",
        "append_position": 1,
        "recorded_at": RECORDED_AT,
        "schema_version": "1.0",
        "provenance_ref": "PRV-000000001",
        "external_id": None,
        "declared_fields": (
            ("event_type", "OBSERVED"),
            ("target_ref", None),
            ("actor_ref", None),
            ("source_ref", None),
            ("scope_ref", None),
            ("branch_ref", None),
            ("occurred_at", None),
            ("effective_at", None),
        ),
    }
    values.update(overrides)
    return RuntimeRecordInspectionReport(**values)


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


def make_report_artifact(**overrides):
    values = {
        "report_artifact_id": "RIRA-000000001",
        "report": make_report(),
    }
    values.update(overrides)
    return RuntimeRecordInspectionReportArtifact(**values)


def make_manifest_artifact(**overrides):
    values = {
        "manifest_artifact_id": "RIDMA-000000001",
        "manifest": make_manifest(),
    }
    values.update(overrides)
    return RuntimeRecordInspectionDigestManifestArtifact(**values)


def make_registry():
    return RuntimeRecordInspectionArtifactRegistry()


def test_module_imports():
    module = importlib.import_module(
        "services.runtime_record_inspection_artifact_registry"
    )
    assert module is not None


def test_class_imports_from_selected_module():
    module = importlib.import_module(
        "services.runtime_record_inspection_artifact_registry"
    )

    assert (
        module.RuntimeRecordInspectionArtifactRegistry
        is RuntimeRecordInspectionArtifactRegistry
    )


def test_registry_is_not_dataclass():
    assert not is_dataclass(
        RuntimeRecordInspectionArtifactRegistry
    )


def test_constructor_requires_no_arguments():
    registry = RuntimeRecordInspectionArtifactRegistry()

    assert isinstance(
        registry,
        RuntimeRecordInspectionArtifactRegistry,
    )


@pytest.mark.parametrize(
    "args,kwargs",
    [
        ((None,), {}),
        (({},), {}),
        ((), {"initial": {}}),
        ((), {"path": "registry.json"}),
    ],
)
def test_constructor_rejects_arguments(args, kwargs):
    with pytest.raises(TypeError):
        RuntimeRecordInspectionArtifactRegistry(
            *args,
            **kwargs,
        )


def test_new_registry_is_empty():
    registry = make_registry()

    assert registry.report_count == 0
    assert registry.manifest_count == 0
    assert registry.total_count == 0


def test_private_storage_attributes_exist():
    registry = make_registry()

    assert hasattr(
        registry,
        "_report_artifacts_by_id",
    )
    assert hasattr(
        registry,
        "_manifest_artifacts_by_id",
    )


def test_private_storage_attributes_are_dictionaries():
    registry = make_registry()

    assert isinstance(
        registry._report_artifacts_by_id,
        dict,
    )
    assert isinstance(
        registry._manifest_artifacts_by_id,
        dict,
    )


def test_private_storage_maps_are_separate():
    registry = make_registry()

    assert (
        registry._report_artifacts_by_id
        is not registry._manifest_artifacts_by_id
    )


def test_new_registry_storage_maps_are_empty():
    registry = make_registry()

    assert registry._report_artifacts_by_id == {}
    assert registry._manifest_artifacts_by_id == {}


def test_registry_instances_have_separate_report_storage():
    first = make_registry()
    second = make_registry()

    assert (
        first._report_artifacts_by_id
        is not second._report_artifacts_by_id
    )


def test_registry_instances_have_separate_manifest_storage():
    first = make_registry()
    second = make_registry()

    assert (
        first._manifest_artifacts_by_id
        is not second._manifest_artifacts_by_id
    )


def test_registration_in_one_instance_does_not_affect_another():
    first = make_registry()
    second = make_registry()

    first.register_report_artifact(
        make_report_artifact()
    )

    assert first.report_count == 1
    assert second.report_count == 0
    assert second.total_count == 0


def test_storage_is_not_shared_as_class_state():
    assert (
        "_report_artifacts_by_id"
        not in RuntimeRecordInspectionArtifactRegistry.__dict__
    )
    assert (
        "_manifest_artifacts_by_id"
        not in RuntimeRecordInspectionArtifactRegistry.__dict__
    )


@pytest.mark.parametrize(
    "method_name",
    [
        "register_report_artifact",
        "register_manifest_artifact",
        "get_report_artifact",
        "get_manifest_artifact",
    ],
)
def test_required_public_methods_are_present(
    method_name,
):
    assert callable(
        getattr(
            RuntimeRecordInspectionArtifactRegistry,
            method_name,
        )
    )


@pytest.mark.parametrize(
    "property_name",
    [
        "report_count",
        "manifest_count",
        "total_count",
    ],
)
def test_count_properties_are_present(property_name):
    descriptor = (
        RuntimeRecordInspectionArtifactRegistry
        .__dict__[property_name]
    )

    assert isinstance(descriptor, property)


@pytest.mark.parametrize(
    "value",
    [
        None,
        True,
        False,
        0,
        1,
        1.0,
        "artifact",
        b"artifact",
        [],
        (),
        {},
        set(),
        object(),
    ],
)
def test_report_registration_rejects_invalid_types(
    value,
):
    registry = make_registry()

    with pytest.raises(
        TypeError,
        match=(
            "^artifact must be a "
            "RuntimeRecordInspectionReportArtifact$"
        ),
    ):
        registry.register_report_artifact(value)

    assert registry.report_count == 0
    assert registry.manifest_count == 0
    assert registry.total_count == 0


def test_report_registration_rejects_report_value():
    registry = make_registry()

    with pytest.raises(
        TypeError,
        match="RuntimeRecordInspectionReportArtifact",
    ):
        registry.register_report_artifact(
            make_report()
        )


def test_report_registration_rejects_manifest_value():
    registry = make_registry()

    with pytest.raises(
        TypeError,
        match="RuntimeRecordInspectionReportArtifact",
    ):
        registry.register_report_artifact(
            make_manifest()
        )


def test_report_registration_rejects_manifest_artifact():
    registry = make_registry()

    with pytest.raises(
        TypeError,
        match="RuntimeRecordInspectionReportArtifact",
    ):
        registry.register_report_artifact(
            make_manifest_artifact()
        )


@pytest.mark.parametrize(
    "value",
    [
        None,
        True,
        False,
        0,
        1,
        1.0,
        "artifact",
        b"artifact",
        [],
        (),
        {},
        set(),
        object(),
    ],
)
def test_manifest_registration_rejects_invalid_types(
    value,
):
    registry = make_registry()

    with pytest.raises(
        TypeError,
        match=(
            "^artifact must be a "
            "RuntimeRecordInspectionDigestManifestArtifact$"
        ),
    ):
        registry.register_manifest_artifact(value)

    assert registry.report_count == 0
    assert registry.manifest_count == 0
    assert registry.total_count == 0


def test_manifest_registration_rejects_report_value():
    registry = make_registry()

    with pytest.raises(
        TypeError,
        match=(
            "RuntimeRecordInspectionDigestManifestArtifact"
        ),
    ):
        registry.register_manifest_artifact(
            make_report()
        )


def test_manifest_registration_rejects_manifest_value():
    registry = make_registry()

    with pytest.raises(
        TypeError,
        match=(
            "RuntimeRecordInspectionDigestManifestArtifact"
        ),
    ):
        registry.register_manifest_artifact(
            make_manifest()
        )


def test_manifest_registration_rejects_report_artifact():
    registry = make_registry()

    with pytest.raises(
        TypeError,
        match=(
            "RuntimeRecordInspectionDigestManifestArtifact"
        ),
    ):
        registry.register_manifest_artifact(
            make_report_artifact()
        )


def test_type_validation_precedes_report_id_access():
    class Sentinel:
        @property
        def report_artifact_id(self):
            raise AssertionError(
                "report_artifact_id was accessed"
            )

    registry = make_registry()

    with pytest.raises(TypeError):
        registry.register_report_artifact(
            Sentinel()
        )


def test_type_validation_precedes_manifest_id_access():
    class Sentinel:
        @property
        def manifest_artifact_id(self):
            raise AssertionError(
                "manifest_artifact_id was accessed"
            )

    registry = make_registry()

    with pytest.raises(TypeError):
        registry.register_manifest_artifact(
            Sentinel()
        )


def test_new_report_registration_returns_result():
    registry = make_registry()

    result = registry.register_report_artifact(
        make_report_artifact()
    )

    assert isinstance(
        result,
        RuntimeRecordInspectionArtifactRegistrationResult,
    )


def test_new_report_registration_result_fields():
    registry = make_registry()
    artifact = make_report_artifact()

    result = registry.register_report_artifact(
        artifact
    )

    assert result.artifact_kind == "REPORT"
    assert (
        result.artifact_id
        == artifact.report_artifact_id
    )
    assert result.status == "REGISTERED"
    assert result.existing_artifact is None
    assert result.candidate_artifact is artifact


def test_new_report_registration_result_properties():
    registry = make_registry()

    result = registry.register_report_artifact(
        make_report_artifact()
    )

    assert result.registry_changed is True
    assert result.registration_accepted is True
    assert result.collision_detected is False


def test_new_report_registration_updates_counts():
    registry = make_registry()

    registry.register_report_artifact(
        make_report_artifact()
    )

    assert registry.report_count == 1
    assert registry.manifest_count == 0
    assert registry.total_count == 1


def test_new_report_registration_retains_exact_object():
    registry = make_registry()
    artifact = make_report_artifact()

    registry.register_report_artifact(
        artifact
    )

    assert (
        registry.get_report_artifact(
            artifact.report_artifact_id
        )
        is artifact
    )


def test_new_manifest_registration_returns_result():
    registry = make_registry()

    result = registry.register_manifest_artifact(
        make_manifest_artifact()
    )

    assert isinstance(
        result,
        RuntimeRecordInspectionArtifactRegistrationResult,
    )


def test_new_manifest_registration_result_fields():
    registry = make_registry()
    artifact = make_manifest_artifact()

    result = registry.register_manifest_artifact(
        artifact
    )

    assert result.artifact_kind == "DIGEST_MANIFEST"
    assert (
        result.artifact_id
        == artifact.manifest_artifact_id
    )
    assert result.status == "REGISTERED"
    assert result.existing_artifact is None
    assert result.candidate_artifact is artifact


def test_new_manifest_registration_result_properties():
    registry = make_registry()

    result = registry.register_manifest_artifact(
        make_manifest_artifact()
    )

    assert result.registry_changed is True
    assert result.registration_accepted is True
    assert result.collision_detected is False


def test_new_manifest_registration_updates_counts():
    registry = make_registry()

    registry.register_manifest_artifact(
        make_manifest_artifact()
    )

    assert registry.report_count == 0
    assert registry.manifest_count == 1
    assert registry.total_count == 1


def test_new_manifest_registration_retains_exact_object():
    registry = make_registry()
    artifact = make_manifest_artifact()

    registry.register_manifest_artifact(
        artifact
    )

    assert (
        registry.get_manifest_artifact(
            artifact.manifest_artifact_id
        )
        is artifact
    )


def test_multiple_report_artifacts_register():
    registry = make_registry()

    for index in range(1, 4):
        registry.register_report_artifact(
            make_report_artifact(
                report_artifact_id=(
                    f"RIRA-{index:09d}"
                ),
                report=make_report(
                    record_id=f"RR-{index:09d}",
                    append_position=index,
                ),
            )
        )

    assert registry.report_count == 3
    assert registry.manifest_count == 0
    assert registry.total_count == 3


def test_multiple_manifest_artifacts_register():
    registry = make_registry()

    for index in range(1, 4):
        registry.register_manifest_artifact(
            make_manifest_artifact(
                manifest_artifact_id=(
                    f"RIDMA-{index:09d}"
                ),
                manifest=make_manifest(
                    sha256_digest=(
                        f"{index:x}" * 64
                    )[:64],
                    byte_length=index,
                ),
            )
        )

    assert registry.report_count == 0
    assert registry.manifest_count == 3
    assert registry.total_count == 3


def test_mixed_registration_counts_are_independent():
    registry = make_registry()

    registry.register_report_artifact(
        make_report_artifact(
            report_artifact_id="RIRA-000000001",
        )
    )
    registry.register_report_artifact(
        make_report_artifact(
            report_artifact_id="RIRA-000000002",
            report=make_report(
                record_id="RR-000000002",
                append_position=2,
            ),
        )
    )

    for index in range(1, 4):
        registry.register_manifest_artifact(
            make_manifest_artifact(
                manifest_artifact_id=(
                    f"RIDMA-{index:09d}"
                ),
                manifest=make_manifest(
                    sha256_digest=(
                        f"{index:x}" * 64
                    )[:64],
                    byte_length=index,
                ),
            )
        )

    assert registry.report_count == 2
    assert registry.manifest_count == 3
    assert registry.total_count == 5


def test_cross_namespace_matching_suffixes_coexist():
    registry = make_registry()

    report_result = (
        registry.register_report_artifact(
            make_report_artifact(
                report_artifact_id=(
                    "RIRA-000000001"
                )
            )
        )
    )
    manifest_result = (
        registry.register_manifest_artifact(
            make_manifest_artifact(
                manifest_artifact_id=(
                    "RIDMA-000000001"
                )
            )
        )
    )

    assert report_result.status == "REGISTERED"
    assert manifest_result.status == "REGISTERED"
    assert registry.total_count == 2


def test_equal_report_reregistration_same_object():
    registry = make_registry()
    artifact = make_report_artifact()

    registry.register_report_artifact(
        artifact
    )
    result = registry.register_report_artifact(
        artifact
    )

    assert result.status == "ALREADY_REGISTERED"
    assert result.existing_artifact is artifact
    assert result.candidate_artifact is artifact
    assert result.registry_changed is False
    assert result.registration_accepted is True
    assert result.collision_detected is False


def test_equal_report_reregistration_separate_object():
    registry = make_registry()
    original = make_report_artifact()
    candidate = make_report_artifact()

    assert original == candidate
    assert original is not candidate

    registry.register_report_artifact(
        original
    )
    result = registry.register_report_artifact(
        candidate
    )

    assert result.status == "ALREADY_REGISTERED"
    assert result.existing_artifact is original
    assert result.candidate_artifact is candidate


def test_equal_report_reregistration_preserves_original():
    registry = make_registry()
    original = make_report_artifact()
    candidate = make_report_artifact()

    registry.register_report_artifact(
        original
    )
    registry.register_report_artifact(
        candidate
    )

    assert (
        registry.get_report_artifact(
            original.report_artifact_id
        )
        is original
    )


def test_equal_report_reregistration_does_not_change_counts():
    registry = make_registry()
    original = make_report_artifact()
    candidate = make_report_artifact()

    registry.register_report_artifact(
        original
    )
    before = (
        registry.report_count,
        registry.manifest_count,
        registry.total_count,
    )

    registry.register_report_artifact(
        candidate
    )

    after = (
        registry.report_count,
        registry.manifest_count,
        registry.total_count,
    )

    assert after == before


def test_equal_manifest_reregistration_same_object():
    registry = make_registry()
    artifact = make_manifest_artifact()

    registry.register_manifest_artifact(
        artifact
    )
    result = registry.register_manifest_artifact(
        artifact
    )

    assert result.status == "ALREADY_REGISTERED"
    assert result.existing_artifact is artifact
    assert result.candidate_artifact is artifact


def test_equal_manifest_reregistration_separate_object():
    registry = make_registry()
    original = make_manifest_artifact()
    candidate = make_manifest_artifact()

    assert original == candidate
    assert original is not candidate

    registry.register_manifest_artifact(
        original
    )
    result = registry.register_manifest_artifact(
        candidate
    )

    assert result.status == "ALREADY_REGISTERED"
    assert result.existing_artifact is original
    assert result.candidate_artifact is candidate


def test_equal_manifest_reregistration_preserves_original():
    registry = make_registry()
    original = make_manifest_artifact()
    candidate = make_manifest_artifact()

    registry.register_manifest_artifact(
        original
    )
    registry.register_manifest_artifact(
        candidate
    )

    assert (
        registry.get_manifest_artifact(
            original.manifest_artifact_id
        )
        is original
    )


def test_report_identity_collision_returns_collision():
    registry = make_registry()

    original = make_report_artifact(
        report=make_report(
            record_id="RR-000000001",
        )
    )
    candidate = make_report_artifact(
        report=make_report(
            record_id="RR-000000002",
        )
    )

    assert original != candidate

    registry.register_report_artifact(
        original
    )
    result = registry.register_report_artifact(
        candidate
    )

    assert result.status == "IDENTITY_COLLISION"
    assert result.registry_changed is False
    assert result.registration_accepted is False
    assert result.collision_detected is True


def test_report_collision_result_fields():
    registry = make_registry()

    original = make_report_artifact(
        report=make_report(
            record_id="RR-000000001",
        )
    )
    candidate = make_report_artifact(
        report=make_report(
            record_id="RR-000000002",
        )
    )

    registry.register_report_artifact(
        original
    )
    result = registry.register_report_artifact(
        candidate
    )

    assert result.artifact_kind == "REPORT"
    assert (
        result.artifact_id
        == original.report_artifact_id
    )
    assert result.existing_artifact is original
    assert result.candidate_artifact is candidate


def test_report_collision_does_not_change_counts():
    registry = make_registry()

    original = make_report_artifact()
    candidate = make_report_artifact(
        report=make_report(
            record_id="RR-000000002",
        )
    )

    registry.register_report_artifact(
        original
    )
    before = (
        registry.report_count,
        registry.manifest_count,
        registry.total_count,
    )

    registry.register_report_artifact(
        candidate
    )

    after = (
        registry.report_count,
        registry.manifest_count,
        registry.total_count,
    )

    assert after == before


def test_report_collision_preserves_original():
    registry = make_registry()

    original = make_report_artifact()
    candidate = make_report_artifact(
        report=make_report(
            record_id="RR-000000002",
        )
    )

    registry.register_report_artifact(
        original
    )
    registry.register_report_artifact(
        candidate
    )

    assert (
        registry.get_report_artifact(
            original.report_artifact_id
        )
        is original
    )


def test_repeated_report_collisions_never_replace_original():
    registry = make_registry()
    original = make_report_artifact()

    registry.register_report_artifact(
        original
    )

    for index in range(2, 5):
        result = registry.register_report_artifact(
            make_report_artifact(
                report=make_report(
                    record_id=f"RR-{index:09d}",
                    append_position=index,
                )
            )
        )

        assert (
            result.status
            == "IDENTITY_COLLISION"
        )

    assert registry.report_count == 1
    assert (
        registry.get_report_artifact(
            original.report_artifact_id
        )
        is original
    )


def test_manifest_identity_collision_returns_collision():
    registry = make_registry()

    original = make_manifest_artifact(
        manifest=make_manifest(
            sha256_digest="0" * 64,
        )
    )
    candidate = make_manifest_artifact(
        manifest=make_manifest(
            sha256_digest="1" * 64,
        )
    )

    registry.register_manifest_artifact(
        original
    )
    result = registry.register_manifest_artifact(
        candidate
    )

    assert result.status == "IDENTITY_COLLISION"
    assert result.existing_artifact is original
    assert result.candidate_artifact is candidate
    assert result.collision_detected is True


def test_manifest_collision_preserves_original():
    registry = make_registry()

    original = make_manifest_artifact()
    candidate = make_manifest_artifact(
        manifest=make_manifest(
            sha256_digest="1" * 64,
        )
    )

    registry.register_manifest_artifact(
        original
    )
    registry.register_manifest_artifact(
        candidate
    )

    assert registry.manifest_count == 1
    assert (
        registry.get_manifest_artifact(
            original.manifest_artifact_id
        )
        is original
    )


def test_report_content_repetition_with_different_ids_registers():
    registry = make_registry()
    report = make_report()

    first = make_report_artifact(
        report_artifact_id="RIRA-000000001",
        report=report,
    )
    second = make_report_artifact(
        report_artifact_id="RIRA-000000002",
        report=report,
    )

    first_result = (
        registry.register_report_artifact(
            first
        )
    )
    second_result = (
        registry.register_report_artifact(
            second
        )
    )

    assert first_result.status == "REGISTERED"
    assert second_result.status == "REGISTERED"
    assert registry.report_count == 2


def test_manifest_content_repetition_with_different_ids_registers():
    registry = make_registry()
    manifest = make_manifest()

    first = make_manifest_artifact(
        manifest_artifact_id="RIDMA-000000001",
        manifest=manifest,
    )
    second = make_manifest_artifact(
        manifest_artifact_id="RIDMA-000000002",
        manifest=manifest,
    )

    registry.register_manifest_artifact(
        first
    )
    result = registry.register_manifest_artifact(
        second
    )

    assert result.status == "REGISTERED"
    assert registry.manifest_count == 2


@pytest.mark.parametrize(
    "value",
    [
        None,
        True,
        False,
        0,
        1,
        1.0,
        b"RIRA-000000001",
        [],
        (),
        {},
        set(),
        object(),
    ],
)
def test_report_lookup_rejects_non_string_values(
    value,
):
    registry = make_registry()

    with pytest.raises(
        TypeError,
        match=(
            "^report_artifact_id must be a string$"
        ),
    ):
        registry.get_report_artifact(value)

    assert registry.total_count == 0


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
def test_manifest_lookup_rejects_non_string_values(
    value,
):
    registry = make_registry()

    with pytest.raises(
        TypeError,
        match=(
            "^manifest_artifact_id must be a string$"
        ),
    ):
        registry.get_manifest_artifact(value)


@pytest.mark.parametrize(
    "value",
    [
        "",
        " ",
        "RIRA",
        "RIRA-",
        "RIRA-1",
        "RIRA-00000001",
        "RIRA-0000000001",
        "RIRA_000000001",
        "RIDMA-000000001",
        "rira-000000001",
        "Rira-000000001",
        " RIRA-000000001",
        "RIRA-000000001 ",
        "RIRA-00000000A",
    ],
)
def test_report_lookup_rejects_invalid_syntax(
    value,
):
    registry = make_registry()

    with pytest.raises(
        ValueError,
        match=(
            "^report_artifact_id must match "
            "RIRA-#########$"
        ),
    ):
        registry.get_report_artifact(value)


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
        "RIRA-000000001",
        "ridma-000000001",
        "Ridma-000000001",
        " RIDMA-000000001",
        "RIDMA-000000001 ",
        "RIDMA-00000000A",
    ],
)
def test_manifest_lookup_rejects_invalid_syntax(
    value,
):
    registry = make_registry()

    with pytest.raises(
        ValueError,
        match=(
            "^manifest_artifact_id must match "
            "RIDMA-#########$"
        ),
    ):
        registry.get_manifest_artifact(value)


def test_report_lookup_rejects_zero_identifier():
    registry = make_registry()

    with pytest.raises(
        ValueError,
        match=(
            "^report_artifact_id numeric component "
            "must be greater than zero$"
        ),
    ):
        registry.get_report_artifact(
            "RIRA-000000000"
        )


def test_manifest_lookup_rejects_zero_identifier():
    registry = make_registry()

    with pytest.raises(
        ValueError,
        match=(
            "^manifest_artifact_id numeric component "
            "must be greater than zero$"
        ),
    ):
        registry.get_manifest_artifact(
            "RIDMA-000000000"
        )


def test_report_lookup_returns_maximum_valid_id():
    registry = make_registry()
    artifact = make_report_artifact(
        report_artifact_id="RIRA-999999999",
    )

    registry.register_report_artifact(
        artifact
    )

    assert (
        registry.get_report_artifact(
            "RIRA-999999999"
        )
        is artifact
    )


def test_manifest_lookup_returns_maximum_valid_id():
    registry = make_registry()
    artifact = make_manifest_artifact(
        manifest_artifact_id=(
            "RIDMA-999999999"
        ),
    )

    registry.register_manifest_artifact(
        artifact
    )

    assert (
        registry.get_manifest_artifact(
            "RIDMA-999999999"
        )
        is artifact
    )


def test_report_lookup_missing_valid_id_raises_key_error():
    registry = make_registry()

    with pytest.raises(KeyError) as exc_info:
        registry.get_report_artifact(
            "RIRA-000000999"
        )

    assert exc_info.value.args == (
        "RIRA-000000999",
    )


def test_manifest_lookup_missing_valid_id_raises_key_error():
    registry = make_registry()

    with pytest.raises(KeyError) as exc_info:
        registry.get_manifest_artifact(
            "RIDMA-000000999"
        )

    assert exc_info.value.args == (
        "RIDMA-000000999",
    )


def test_lookup_accepts_string_subclass():
    class ReportArtifactId(str):
        pass

    registry = make_registry()
    artifact = make_report_artifact()

    registry.register_report_artifact(
        artifact
    )

    identifier = ReportArtifactId(
        artifact.report_artifact_id
    )

    assert (
        registry.get_report_artifact(
            identifier
        )
        is artifact
    )


def test_lookup_does_not_mutate_registry():
    registry = make_registry()
    artifact = make_report_artifact()

    registry.register_report_artifact(
        artifact
    )

    before = dict(
        registry._report_artifacts_by_id
    )

    registry.get_report_artifact(
        artifact.report_artifact_id
    )

    assert (
        registry._report_artifacts_by_id
        == before
    )


def test_count_properties_return_exact_ints():
    registry = make_registry()

    assert type(registry.report_count) is int
    assert type(registry.manifest_count) is int
    assert type(registry.total_count) is int


def test_total_count_is_derived():
    registry = make_registry()

    registry.register_report_artifact(
        make_report_artifact()
    )
    registry.register_manifest_artifact(
        make_manifest_artifact()
    )

    assert registry.total_count == (
        registry.report_count
        + registry.manifest_count
    )


@pytest.mark.parametrize(
    "attribute",
    [
        "_report_count",
        "_manifest_count",
        "_total_count",
    ],
)
def test_counts_are_not_stored(
    attribute,
):
    assert not hasattr(
        make_registry(),
        attribute,
    )


def test_membership_is_monotonic():
    registry = make_registry()
    observed_counts = [
        registry.total_count,
    ]

    first = make_report_artifact()
    equal = make_report_artifact()
    collision = make_report_artifact(
        report=make_report(
            record_id="RR-000000002",
        )
    )
    manifest = make_manifest_artifact()

    registry.register_report_artifact(
        first
    )
    observed_counts.append(
        registry.total_count
    )

    registry.register_report_artifact(
        equal
    )
    observed_counts.append(
        registry.total_count
    )

    registry.register_report_artifact(
        collision
    )
    observed_counts.append(
        registry.total_count
    )

    registry.register_manifest_artifact(
        manifest
    )
    observed_counts.append(
        registry.total_count
    )

    assert observed_counts == sorted(
        observed_counts
    )


@pytest.mark.parametrize(
    "method_name",
    [
        "remove",
        "delete",
        "clear",
        "reset",
        "remove_report_artifact",
        "remove_manifest_artifact",
        "update",
        "replace",
        "overwrite",
        "upsert",
        "merge",
        "update_report_artifact",
        "update_manifest_artifact",
        "list_report_artifacts",
        "list_manifest_artifacts",
        "list_artifacts",
        "all_artifacts",
        "iter_artifacts",
        "history",
        "timeline",
        "contains",
        "contains_report_artifact",
        "contains_manifest_artifact",
        "register",
        "get_artifact",
        "lookup",
        "find",
        "allocate_id",
        "generate_id",
        "next_id",
        "next_report_artifact_id",
        "next_manifest_artifact_id",
        "to_dict",
        "to_json",
        "to_bytes",
        "serialize",
        "deserialize",
        "snapshot",
        "restore",
        "save",
        "load",
        "create_receipt",
        "issue_receipt",
        "sign",
        "compute_digest",
        "associate",
        "bind",
        "link",
        "pair",
        "attach",
        "admit",
        "approve",
        "trust",
        "authorize",
        "execute",
        "apply",
        "publish",
    ],
)
def test_registry_excludes_unowned_methods(
    method_name,
):
    assert not hasattr(
        RuntimeRecordInspectionArtifactRegistry,
        method_name,
    )


def test_instance_dictionary_contains_only_storage_maps():
    registry = make_registry()

    assert set(registry.__dict__) == {
        "_report_artifacts_by_id",
        "_manifest_artifacts_by_id",
    }


@pytest.mark.parametrize(
    "attribute",
    [
        "_collisions",
        "_collision_history",
        "_rejected_candidates",
        "_failed_registrations",
        "_results",
        "_registration_results",
        "_attempts",
        "_history",
        "actor_ref",
        "submitter_ref",
        "source_ref",
        "method_ref",
        "environment_ref",
        "custody_ref",
        "custodian_ref",
        "transfer_ref",
        "storage_location",
        "parent_ref",
        "predecessor_ref",
        "supersedes_ref",
        "derived_from_ref",
        "version_ref",
        "association_ref",
        "binding_ref",
        "pair_ref",
        "report_manifest_pairs",
        "admitted",
        "approved",
        "eligible",
        "trusted",
        "authentic",
        "verified",
        "authorized",
        "authority_ref",
        "permission",
        "execution_allowed",
        "registry_id",
        "registry_instance_id",
        "registry_version",
        "registered_at",
        "last_registered_at",
        "created_at",
        "append_position",
        "sequence_number",
        "registration_index",
        "persisted",
        "storage_path",
        "database_url",
        "snapshot_path",
    ],
)
def test_registry_excludes_unowned_state(
    attribute,
):
    assert not hasattr(
        make_registry(),
        attribute,
    )


def test_registration_returns_new_result_each_time():
    registry = make_registry()
    artifact = make_report_artifact()

    first = registry.register_report_artifact(
        artifact
    )
    second = registry.register_report_artifact(
        artifact
    )

    assert first is not second


def test_report_artifact_subclass_is_accepted():
    class ReportArtifactSubclass(
        RuntimeRecordInspectionReportArtifact
    ):
        pass

    artifact = ReportArtifactSubclass(
        report_artifact_id="RIRA-000000001",
        report=make_report(),
    )
    registry = make_registry()

    result = registry.register_report_artifact(
        artifact
    )

    assert result.status == "REGISTERED"
    assert (
        registry.get_report_artifact(
            artifact.report_artifact_id
        )
        is artifact
    )


def test_manifest_artifact_subclass_is_accepted():
    class ManifestArtifactSubclass(
        RuntimeRecordInspectionDigestManifestArtifact
    ):
        pass

    artifact = ManifestArtifactSubclass(
        manifest_artifact_id=(
            "RIDMA-000000001"
        ),
        manifest=make_manifest(),
    )
    registry = make_registry()

    result = registry.register_manifest_artifact(
        artifact
    )

    assert result.status == "REGISTERED"


def test_required_validation_methods_are_present():
    assert callable(
        RuntimeRecordInspectionArtifactRegistry
        ._validate_report_artifact_id
    )
    assert callable(
        RuntimeRecordInspectionArtifactRegistry
        ._validate_manifest_artifact_id
    )


@pytest.mark.parametrize(
    "method_name",
    [
        "_validate_registry_id",
        "_validate_persistence",
        "_validate_receipt",
        "_validate_provenance",
        "_validate_custody",
        "_validate_association",
        "_validate_authority",
    ],
)
def test_unowned_validation_methods_are_absent(
    method_name,
):
    assert not hasattr(
        RuntimeRecordInspectionArtifactRegistry,
        method_name,
    )


def test_private_pattern_constants_are_present():
    module = importlib.import_module(
        "services.runtime_record_inspection_artifact_registry"
    )

    assert (
        module._REPORT_ARTIFACT_ID_PATTERN.pattern
        == r"^RIRA-[0-9]{9}$"
    )
    assert (
        module._MANIFEST_ARTIFACT_ID_PATTERN.pattern
        == r"^RIDMA-[0-9]{9}$"
    )


def test_class_has_boundary_docstring():
    docstring = (
        RuntimeRecordInspectionArtifactRegistry
        .__doc__
        or ""
    ).lower()

    assert "monotonic" in docstring
    assert "in-memory" in docstring
    assert "local" in docstring
    assert "collision" in docstring
    assert "allocate" in docstring
    assert "persist" in docstring
    assert "admit" in docstring
    assert "authorize" in docstring


def test_construction_emits_no_output(
    capsys,
):
    make_registry()

    captured = capsys.readouterr()

    assert captured.out == ""
    assert captured.err == ""


def test_registration_emits_no_output(
    capsys,
):
    registry = make_registry()
    artifact = make_report_artifact()

    registry.register_report_artifact(
        artifact
    )
    registry.register_report_artifact(
        artifact
    )
    registry.register_report_artifact(
        make_report_artifact(
            report=make_report(
                record_id="RR-000000002",
            )
        )
    )

    captured = capsys.readouterr()

    assert captured.out == ""
    assert captured.err == ""


def test_lookup_emits_no_output(
    capsys,
):
    registry = make_registry()
    artifact = make_report_artifact()

    registry.register_report_artifact(
        artifact
    )
    registry.get_report_artifact(
        artifact.report_artifact_id
    )

    with pytest.raises(KeyError):
        registry.get_report_artifact(
            "RIRA-000000999"
        )

    captured = capsys.readouterr()

    assert captured.out == ""
    assert captured.err == ""


def test_source_has_no_unowned_dependencies():
    source_path = (
        Path(__file__).resolve().parents[2]
        / "services"
        / (
            "runtime_record_inspection_"
            "artifact_registry.py"
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
        "pathlib",
        "pickle",
        "shelve",
        "sqlite3",
        "open(",
        "postgres",
        "mysql",
        "redis",
        "datetime",
        "import time",
        "hashlib",
        "uuid",
        "random",
        "secrets",
        "import os",
        "logging",
    )

    for term in prohibited_terms:
        assert term not in source