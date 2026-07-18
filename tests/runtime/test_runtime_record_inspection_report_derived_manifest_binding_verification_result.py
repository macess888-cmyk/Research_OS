import copy
import importlib
import inspect
import sys
from dataclasses import (
    MISSING,
    FrozenInstanceError,
    fields,
    is_dataclass,
)

import pytest

from models.runtime_record_inspection_report_derived_manifest_binding_verification_result import (
    RuntimeRecordInspectionReportDerivedManifestBindingVerificationResult,
)


INVALID_BOOLEAN_VALUES = (
    None,
    0,
    1,
    -1,
    "",
    "True",
    "False",
    [],
    (),
    {},
    object(),
)

BOOLEAN_COMBINATIONS = (
    (True, True, True, True),
    (True, True, False, False),
    (True, False, True, False),
    (True, False, False, False),
    (False, True, True, False),
    (False, True, False, False),
    (False, False, True, False),
    (False, False, False, False),
)


def make_result(**overrides):
    values = {
        "digest_matches": True,
        "byte_length_matches": True,
        "bom_matches": True,
    }
    values.update(overrides)

    return RuntimeRecordInspectionReportDerivedManifestBindingVerificationResult(
        **values
    )


def test_result_class_is_importable_from_canonical_module():
    module = importlib.import_module(
        "models."
        "runtime_record_inspection_report_derived_manifest_"
        "binding_verification_result"
    )

    assert (
        module
        .RuntimeRecordInspectionReportDerivedManifestBindingVerificationResult
        is RuntimeRecordInspectionReportDerivedManifestBindingVerificationResult
    )


def test_result_is_a_dataclass():
    assert is_dataclass(
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationResult
    )


def test_result_dataclass_is_frozen():
    result = make_result()

    with pytest.raises(FrozenInstanceError):
        result.digest_matches = False


def test_result_fields_are_exact_and_ordered():
    assert tuple(
        field.name
        for field in fields(
            RuntimeRecordInspectionReportDerivedManifestBindingVerificationResult
        )
    ) == (
        "digest_matches",
        "byte_length_matches",
        "bom_matches",
    )


def test_result_field_annotations_are_exact_bool():
    assert (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationResult
        .__annotations__
    ) == {
        "digest_matches": bool,
        "byte_length_matches": bool,
        "bom_matches": bool,
    }


def test_constructor_signature_contains_only_required_result_fields():
    signature = inspect.signature(
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationResult
    )

    assert tuple(signature.parameters) == (
        "digest_matches",
        "byte_length_matches",
        "bom_matches",
    )

    for parameter in signature.parameters.values():
        assert parameter.default is inspect.Parameter.empty


def test_keyword_construction_preserves_true_values():
    result = make_result()

    assert result.digest_matches is True
    assert result.byte_length_matches is True
    assert result.bom_matches is True


def test_keyword_construction_preserves_false_values():
    result = make_result(
        digest_matches=False,
        byte_length_matches=False,
        bom_matches=False,
    )

    assert result.digest_matches is False
    assert result.byte_length_matches is False
    assert result.bom_matches is False


def test_positional_construction_maps_values_in_frozen_field_order():
    result = (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationResult(
            True,
            False,
            True,
        )
    )

    assert result.digest_matches is True
    assert result.byte_length_matches is False
    assert result.bom_matches is True


@pytest.mark.parametrize(
    (
        "digest_matches",
        "byte_length_matches",
        "bom_matches",
        "expected_binding_matches",
    ),
    BOOLEAN_COMBINATIONS,
)
def test_all_boolean_combinations_are_valid_and_derive_expected_binding(
    digest_matches,
    byte_length_matches,
    bom_matches,
    expected_binding_matches,
):
    result = (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationResult(
            digest_matches=digest_matches,
            byte_length_matches=byte_length_matches,
            bom_matches=bom_matches,
        )
    )

    assert result.digest_matches is digest_matches
    assert result.byte_length_matches is byte_length_matches
    assert result.bom_matches is bom_matches
    assert result.binding_matches is expected_binding_matches
    assert type(result.binding_matches) is bool


@pytest.mark.parametrize("invalid_value", INVALID_BOOLEAN_VALUES)
def test_digest_matches_rejects_non_bool_values(invalid_value):
    with pytest.raises(
        TypeError,
        match=r"^digest_matches must be an exact bool$",
    ):
        make_result(digest_matches=invalid_value)


@pytest.mark.parametrize("invalid_value", INVALID_BOOLEAN_VALUES)
def test_byte_length_matches_rejects_non_bool_values(invalid_value):
    with pytest.raises(
        TypeError,
        match=r"^byte_length_matches must be an exact bool$",
    ):
        make_result(byte_length_matches=invalid_value)


@pytest.mark.parametrize("invalid_value", INVALID_BOOLEAN_VALUES)
def test_bom_matches_rejects_non_bool_values(invalid_value):
    with pytest.raises(
        TypeError,
        match=r"^bom_matches must be an exact bool$",
    ):
        make_result(bom_matches=invalid_value)


def test_digest_matches_type_failure_precedes_other_field_failures():
    with pytest.raises(
        TypeError,
        match=r"^digest_matches must be an exact bool$",
    ):
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationResult(
            digest_matches=1,
            byte_length_matches=1,
            bom_matches=1,
        )


def test_byte_length_matches_type_failure_precedes_bom_failure():
    with pytest.raises(
        TypeError,
        match=r"^byte_length_matches must be an exact bool$",
    ):
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationResult(
            digest_matches=True,
            byte_length_matches=1,
            bom_matches=1,
        )


def test_bom_matches_failure_is_observed_after_valid_prior_fields():
    with pytest.raises(
        TypeError,
        match=r"^bom_matches must be an exact bool$",
    ):
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationResult(
            digest_matches=True,
            byte_length_matches=True,
            bom_matches=1,
        )


def test_binding_matches_is_a_property():
    descriptor = inspect.getattr_static(
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationResult,
        "binding_matches",
    )

    assert isinstance(descriptor, property)
    assert descriptor.fset is None


def test_binding_matches_is_not_a_dataclass_field():
    assert "binding_matches" not in {
        field.name
        for field in fields(
            RuntimeRecordInspectionReportDerivedManifestBindingVerificationResult
        )
    }


def test_binding_matches_is_not_stored_in_instance_dictionary():
    result = make_result()

    assert "binding_matches" not in result.__dict__


def test_binding_matches_is_true_only_when_all_partial_facts_match():
    assert make_result().binding_matches is True

    assert make_result(
        digest_matches=False
    ).binding_matches is False

    assert make_result(
        byte_length_matches=False
    ).binding_matches is False

    assert make_result(
        bom_matches=False
    ).binding_matches is False


def test_binding_matches_is_deterministic_across_repeated_access():
    result = make_result(
        digest_matches=True,
        byte_length_matches=False,
        bom_matches=True,
    )

    first = result.binding_matches
    second = result.binding_matches
    third = result.binding_matches

    assert first is False
    assert second is first
    assert third is first


def test_binding_matches_cannot_be_assigned():
    result = make_result()

    with pytest.raises(
        (FrozenInstanceError, AttributeError),
    ):
        result.binding_matches = False


@pytest.mark.parametrize(
    "field_name",
    (
        "digest_matches",
        "byte_length_matches",
        "bom_matches",
    ),
)
def test_stored_fields_are_immutable(field_name):
    result = make_result()

    with pytest.raises(FrozenInstanceError):
        setattr(result, field_name, False)


@pytest.mark.parametrize(
    "field_name",
    (
        "digest_matches",
        "byte_length_matches",
        "bom_matches",
    ),
)
def test_stored_fields_cannot_be_deleted(field_name):
    result = make_result()

    with pytest.raises(FrozenInstanceError):
        delattr(result, field_name)


def test_equal_partial_evidence_produces_equal_results():
    first = make_result(
        digest_matches=True,
        byte_length_matches=False,
        bom_matches=True,
    )
    second = make_result(
        digest_matches=True,
        byte_length_matches=False,
        bom_matches=True,
    )

    assert first == second


def test_different_partial_evidence_produces_unequal_results():
    first = make_result(
        digest_matches=False,
        byte_length_matches=True,
        bom_matches=True,
    )
    second = make_result(
        digest_matches=True,
        byte_length_matches=False,
        bom_matches=True,
    )

    assert first != second


def test_same_false_aggregate_with_different_partial_evidence_is_not_equal():
    first = make_result(
        digest_matches=False,
        byte_length_matches=True,
        bom_matches=True,
    )
    second = make_result(
        digest_matches=True,
        byte_length_matches=False,
        bom_matches=True,
    )

    assert first.binding_matches is False
    assert second.binding_matches is False
    assert first != second


@pytest.mark.parametrize(
    "other",
    (
        (True, True, True),
        {
            "digest_matches": True,
            "byte_length_matches": True,
            "bom_matches": True,
        },
        object(),
    ),
)
def test_result_does_not_equal_unrelated_objects(other):
    assert make_result() != other


@pytest.mark.parametrize(
    "operation",
    (
        lambda left, right: left < right,
        lambda left, right: left <= right,
        lambda left, right: left > right,
        lambda left, right: left >= right,
    ),
)
def test_result_has_no_ordering_semantics(operation):
    first = make_result()
    second = make_result(
        digest_matches=False,
    )

    with pytest.raises(TypeError):
        operation(first, second)


def test_standard_repr_contains_only_stored_domain_fields():
    result = make_result(
        digest_matches=True,
        byte_length_matches=False,
        bom_matches=True,
    )

    representation = repr(result)

    assert (
        "RuntimeRecordInspectionReportDerivedManifestBindingVerificationResult"
        in representation
    )
    assert "digest_matches=True" in representation
    assert "byte_length_matches=False" in representation
    assert "bom_matches=True" in representation
    assert "binding_matches" not in representation


@pytest.mark.parametrize(
    "attribute_name",
    (
        "integrity_matches",
        "report_id",
        "manifest_id",
        "record_id",
        "subject_id",
        "binding_id",
        "identity_matches",
        "subject_matches",
        "provenance",
        "provenance_ref",
        "provenance_matches",
        "lineage",
        "lineage_ref",
        "creation_lineage_matches",
        "historical_binding_matches",
        "custody",
        "custody_ref",
        "custody_matches",
        "chain_of_custody",
        "created_at",
        "observed_at",
        "verified_at",
        "bound_at",
        "timestamp",
        "registry_ref",
        "registration_id",
        "registry_position",
        "registered",
        "admitted",
        "admissible",
        "accepted",
        "approved",
        "eligible",
        "trusted",
        "authentic",
        "reliable",
        "verified_true",
        "authorized",
        "permitted",
        "executable",
        "release_allowed",
    ),
)
def test_result_retains_no_excluded_domain_attributes(attribute_name):
    assert not hasattr(make_result(), attribute_name)


@pytest.mark.parametrize(
    "method_name",
    (
        "save",
        "load",
        "write",
        "read",
        "serialize",
        "deserialize",
        "to_json",
        "from_json",
        "to_dict",
        "from_dict",
        "set_digest_matches",
        "set_byte_length_matches",
        "set_bom_matches",
        "update",
        "mark_verified",
        "replace_in_place",
        "register",
        "admit",
        "authorize",
        "release",
        "execute",
        "emit",
        "persist",
    ),
)
def test_result_exposes_no_excluded_domain_methods(method_name):
    assert not hasattr(make_result(), method_name)


def test_too_few_constructor_arguments_are_rejected():
    with pytest.raises(TypeError):
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationResult(
            True,
            True,
        )


def test_too_many_constructor_arguments_are_rejected():
    with pytest.raises(TypeError):
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationResult(
            True,
            True,
            True,
            False,
        )


def test_caller_supplied_binding_matches_is_rejected():
    with pytest.raises(TypeError):
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationResult(
            digest_matches=True,
            byte_length_matches=True,
            bom_matches=True,
            binding_matches=True,
        )


def test_result_fields_have_no_defaults():
    for field in fields(
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationResult
    ):
        assert field.default is MISSING
        assert field.default_factory is MISSING


def test_repeated_construction_with_same_values_is_deterministic():
    first = make_result(
        digest_matches=False,
        byte_length_matches=True,
        bom_matches=False,
    )
    second = make_result(
        digest_matches=False,
        byte_length_matches=True,
        bom_matches=False,
    )

    assert first == second
    assert first.binding_matches is second.binding_matches


def test_shallow_copy_is_equal_to_original():
    result = make_result(
        digest_matches=False,
        byte_length_matches=True,
        bom_matches=False,
    )

    copied = copy.copy(result)

    assert copied == result


def test_deep_copy_is_equal_to_original():
    result = make_result(
        digest_matches=False,
        byte_length_matches=True,
        bom_matches=False,
    )

    copied = copy.deepcopy(result)

    assert copied == result


def test_result_uses_normal_frozen_dataclass_hash_behavior():
    first = make_result(
        digest_matches=True,
        byte_length_matches=False,
        bom_matches=True,
    )
    second = make_result(
        digest_matches=True,
        byte_length_matches=False,
        bom_matches=True,
    )

    assert hash(first) == hash(second)


def test_result_module_does_not_import_application_frameworks():
    forbidden_modules = (
        "streamlit",
        "flask",
        "django",
        "fastapi",
        "sqlalchemy",
        "requests",
    )

    module_name = (
        "models."
        "runtime_record_inspection_report_derived_manifest_"
        "binding_verification_result"
    )

    importlib.import_module(module_name)

    for forbidden_module in forbidden_modules:
        assert forbidden_module not in sys.modules


def test_result_module_imports_only_dataclass_from_standard_library():
    module = importlib.import_module(
        "models."
        "runtime_record_inspection_report_derived_manifest_"
        "binding_verification_result"
    )

    source = inspect.getsource(module)

    forbidden_source_fragments = (
        "import hashlib",
        "import hmac",
        "import json",
        "import datetime",
        "from datetime",
        "RuntimeRecordRegistry",
        "runtime_record_registry",
        "runtime_record_inspection_representation_service",
        "runtime_record_inspection_json_encoding_service",
        "runtime_record_inspection_utf8_byte_encoding_service",
        "runtime_record_inspection_embedded_report_integrity_verification_service",
        "pydantic",
        "marshmallow",
        "attrs",
        "cerberus",
    )

    for fragment in forbidden_source_fragments:
        assert fragment not in source


def test_production_source_contains_exact_boolean_checks():
    module = importlib.import_module(
        "models."
        "runtime_record_inspection_report_derived_manifest_"
        "binding_verification_result"
    )

    source = inspect.getsource(module)

    assert "type(self.digest_matches) is not bool" in source
    assert "type(self.byte_length_matches) is not bool" in source
    assert "type(self.bom_matches) is not bool" in source
    assert "bool(" not in source


def test_production_source_contains_no_custom_ordering_methods():
    module = importlib.import_module(
        "models."
        "runtime_record_inspection_report_derived_manifest_"
        "binding_verification_result"
    )

    source = inspect.getsource(module)

    for method_name in (
        "__lt__",
        "__le__",
        "__gt__",
        "__ge__",
    ):
        assert method_name not in source


def test_production_source_contains_no_custom_hash_method():
    module = importlib.import_module(
        "models."
        "runtime_record_inspection_report_derived_manifest_"
        "binding_verification_result"
    )

    source = inspect.getsource(module)

    assert "def __hash__" not in source