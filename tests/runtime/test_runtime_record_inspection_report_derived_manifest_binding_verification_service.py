import hashlib
import importlib
import inspect
import sys
from datetime import datetime, timezone

import pytest

from models.runtime_record_inspection_digest_manifest import (
    RuntimeRecordInspectionDigestManifest,
)
from models.runtime_record_inspection_embedded_report_integrity_verification_result import (
    RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult,
)
from models.runtime_record_inspection_report import (
    RuntimeRecordInspectionReport,
)
from models.runtime_record_inspection_report_derived_manifest_binding_verification_result import (
    RuntimeRecordInspectionReportDerivedManifestBindingVerificationResult,
)
from services.runtime_record_inspection_embedded_report_integrity_verification_service import (
    RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService,
)
from services.runtime_record_inspection_json_encoding_service import (
    RuntimeRecordInspectionJsonEncodingService,
)
from services.runtime_record_inspection_representation_service import (
    RuntimeRecordInspectionRepresentationService,
)
from services.runtime_record_inspection_report_derived_manifest_binding_verification_service import (
    RuntimeRecordInspectionReportDerivedManifestBindingVerificationService,
)
from services.runtime_record_inspection_utf8_byte_encoding_service import (
    RuntimeRecordInspectionUtf8ByteEncodingService,
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

INVALID_REPORT_INPUTS = (
    None,
    {},
    (),
    "report",
    b"report",
    object(),
)

INVALID_MANIFEST_INPUTS = (
    None,
    {},
    (),
    "manifest",
    b"manifest",
    object(),
)


def make_report() -> RuntimeRecordInspectionReport:
    return RuntimeRecordInspectionReport(
        record_id="RR-000000001",
        record_type="RuntimeEventRecord",
        record_category="EVENT",
        append_position=0,
        recorded_at=datetime(
            2026,
            7,
            18,
            12,
            0,
            tzinfo=timezone.utc,
        ),
        schema_version="1.0",
        provenance_ref="PRV-000000001",
        external_id="external-001",
        declared_fields=(
            ("event_type", "OBSERVED"),
            ("target_ref", "TARGET-001"),
            ("actor_ref", "ACTOR-001"),
            ("source_ref", "SOURCE-001"),
            ("scope_ref", "SCOPE-001"),
            ("branch_ref", "BRANCH-001"),
            ("occurred_at", None),
            ("effective_at", None),
        ),
    )


def make_manifest(
    *,
    sha256_digest: str = "0" * 64,
    byte_length: int = 0,
) -> RuntimeRecordInspectionDigestManifest:
    return RuntimeRecordInspectionDigestManifest(
        manifest_schema_version="1.0",
        digest_algorithm="sha256",
        sha256_digest=sha256_digest,
        byte_length=byte_length,
        codec="utf-8",
        bom_present=False,
    )


def make_matching_manifest(
    report: RuntimeRecordInspectionReport,
) -> RuntimeRecordInspectionDigestManifest:
    primitive = (
        RuntimeRecordInspectionRepresentationService()
        .to_primitive_dict(report)
    )
    json_text = (
        RuntimeRecordInspectionJsonEncodingService()
        .to_json_text(primitive)
    )
    report_bytes = (
        RuntimeRecordInspectionUtf8ByteEncodingService()
        .to_utf8_bytes(json_text)
    )

    return make_manifest(
        sha256_digest=hashlib.sha256(report_bytes).hexdigest(),
        byte_length=len(report_bytes),
    )


class ReportSubclass(RuntimeRecordInspectionReport):
    pass


class ManifestSubclass(RuntimeRecordInspectionDigestManifest):
    pass


class RecordingRepresentationService:
    def __init__(
        self,
        calls,
        primitive,
        error=None,
    ):
        self.calls = calls
        self.primitive = primitive
        self.error = error
        self.received_report = None
        self.call_count = 0

    def to_primitive_dict(self, report):
        self.call_count += 1
        self.calls.append("to_primitive_dict")
        self.received_report = report

        if self.error is not None:
            raise self.error

        return self.primitive


class RecordingJsonEncodingService:
    def __init__(
        self,
        calls,
        json_text,
        error=None,
    ):
        self.calls = calls
        self.json_text = json_text
        self.error = error
        self.received_primitive = None
        self.call_count = 0

    def to_json_text(self, primitive):
        self.call_count += 1
        self.calls.append("to_json_text")
        self.received_primitive = primitive

        if self.error is not None:
            raise self.error

        return self.json_text


class RecordingUtf8ByteEncodingService:
    def __init__(
        self,
        calls,
        report_bytes,
        error=None,
    ):
        self.calls = calls
        self.report_bytes = report_bytes
        self.error = error
        self.received_json_text = None
        self.call_count = 0

    def to_utf8_bytes(self, json_text):
        self.call_count += 1
        self.calls.append("to_utf8_bytes")
        self.received_json_text = json_text

        if self.error is not None:
            raise self.error

        return self.report_bytes


class RecordingIntegrityVerificationService:
    def __init__(
        self,
        calls,
        result,
        error=None,
    ):
        self.calls = calls
        self.result = result
        self.error = error
        self.received_report_bytes = None
        self.received_manifest = None
        self.call_count = 0

    def verify_integrity(
        self,
        report_bytes,
        manifest,
    ):
        self.call_count += 1
        self.calls.append("verify_integrity")
        self.received_report_bytes = report_bytes
        self.received_manifest = manifest

        if self.error is not None:
            raise self.error

        return self.result


def install_recording_pipeline(
    service,
    *,
    integrity_result=None,
    representation_error=None,
    json_error=None,
    utf8_error=None,
    integrity_error=None,
):
    calls = []
    primitive = {"sentinel": object()}
    json_text = '{"sentinel":true}'
    report_bytes = b"sentinel-report-bytes"

    if integrity_result is None:
        integrity_result = (
            RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult(
                digest_matches=True,
                byte_length_matches=True,
                bom_matches=True,
            )
        )

    representation_service = RecordingRepresentationService(
        calls,
        primitive,
        representation_error,
    )
    json_service = RecordingJsonEncodingService(
        calls,
        json_text,
        json_error,
    )
    utf8_service = RecordingUtf8ByteEncodingService(
        calls,
        report_bytes,
        utf8_error,
    )
    integrity_service = RecordingIntegrityVerificationService(
        calls,
        integrity_result,
        integrity_error,
    )

    service._representation_service = representation_service
    service._json_encoding_service = json_service
    service._utf8_byte_encoding_service = utf8_service
    service._integrity_verification_service = integrity_service

    return {
        "calls": calls,
        "primitive": primitive,
        "json_text": json_text,
        "report_bytes": report_bytes,
        "integrity_result": integrity_result,
        "representation_service": representation_service,
        "json_service": json_service,
        "utf8_service": utf8_service,
        "integrity_service": integrity_service,
    }


def test_service_class_is_importable_from_canonical_module():
    module = importlib.import_module(
        "services."
        "runtime_record_inspection_report_derived_manifest_"
        "binding_verification_service"
    )

    assert (
        module
        .RuntimeRecordInspectionReportDerivedManifestBindingVerificationService
        is RuntimeRecordInspectionReportDerivedManifestBindingVerificationService
    )


def test_service_constructor_accepts_no_arguments():
    service = (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService()
    )

    assert type(service) is (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService
    )

    with pytest.raises(TypeError):
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService(
            object()
        )


def test_service_constructor_initializes_exact_upstream_services():
    service = (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService()
    )

    assert type(service._representation_service) is (
        RuntimeRecordInspectionRepresentationService
    )
    assert type(service._json_encoding_service) is (
        RuntimeRecordInspectionJsonEncodingService
    )
    assert type(service._utf8_byte_encoding_service) is (
        RuntimeRecordInspectionUtf8ByteEncodingService
    )
    assert type(service._integrity_verification_service) is (
        RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService
    )


def test_service_starts_with_only_authorized_private_state():
    service = (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService()
    )

    assert set(service.__dict__) == {
        "_representation_service",
        "_json_encoding_service",
        "_utf8_byte_encoding_service",
        "_integrity_verification_service",
    }


def test_verify_binding_signature_is_exact():
    signature = inspect.signature(
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService
        .verify_binding
    )

    assert tuple(signature.parameters) == (
        "self",
        "report",
        "manifest",
    )

    assert (
        signature.parameters["report"].annotation
        is RuntimeRecordInspectionReport
    )
    assert (
        signature.parameters["manifest"].annotation
        is RuntimeRecordInspectionDigestManifest
    )
    assert signature.return_annotation is (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationResult
    )


@pytest.mark.parametrize(
    "invalid_report",
    INVALID_REPORT_INPUTS,
)
def test_non_report_inputs_are_rejected(invalid_report):
    service = (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService()
    )

    with pytest.raises(
        TypeError,
        match=(
            r"^report must be an exact "
            r"RuntimeRecordInspectionReport$"
        ),
    ):
        service.verify_binding(
            invalid_report,
            make_manifest(),
        )


def test_report_subclass_is_rejected():
    base = make_report()
    report = ReportSubclass(
        record_id=base.record_id,
        record_type=base.record_type,
        record_category=base.record_category,
        append_position=base.append_position,
        recorded_at=base.recorded_at,
        schema_version=base.schema_version,
        provenance_ref=base.provenance_ref,
        external_id=base.external_id,
        declared_fields=base.declared_fields,
    )

    service = (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService()
    )

    with pytest.raises(
        TypeError,
        match=(
            r"^report must be an exact "
            r"RuntimeRecordInspectionReport$"
        ),
    ):
        service.verify_binding(
            report,
            make_manifest(),
        )


@pytest.mark.parametrize(
    "invalid_manifest",
    INVALID_MANIFEST_INPUTS,
)
def test_non_manifest_inputs_are_rejected(invalid_manifest):
    service = (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService()
    )

    with pytest.raises(
        TypeError,
        match=(
            r"^manifest must be an exact "
            r"RuntimeRecordInspectionDigestManifest$"
        ),
    ):
        service.verify_binding(
            make_report(),
            invalid_manifest,
        )


def test_manifest_subclass_is_rejected():
    base = make_manifest()
    manifest = ManifestSubclass(
        manifest_schema_version=base.manifest_schema_version,
        digest_algorithm=base.digest_algorithm,
        sha256_digest=base.sha256_digest,
        byte_length=base.byte_length,
        codec=base.codec,
        bom_present=base.bom_present,
    )

    service = (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService()
    )

    with pytest.raises(
        TypeError,
        match=(
            r"^manifest must be an exact "
            r"RuntimeRecordInspectionDigestManifest$"
        ),
    ):
        service.verify_binding(
            make_report(),
            manifest,
        )


def test_invalid_report_fails_before_manifest_validation():
    service = (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService()
    )

    with pytest.raises(
        TypeError,
        match=(
            r"^report must be an exact "
            r"RuntimeRecordInspectionReport$"
        ),
    ):
        service.verify_binding(
            object(),
            object(),
        )


def test_invalid_report_short_circuits_all_upstream_services():
    service = (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService()
    )
    pipeline = install_recording_pipeline(service)

    with pytest.raises(TypeError):
        service.verify_binding(
            object(),
            make_manifest(),
        )

    assert pipeline["calls"] == []


def test_invalid_manifest_short_circuits_all_upstream_services():
    service = (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService()
    )
    pipeline = install_recording_pipeline(service)

    with pytest.raises(TypeError):
        service.verify_binding(
            make_report(),
            object(),
        )

    assert pipeline["calls"] == []


def test_upstream_services_are_called_once_in_exact_order():
    service = (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService()
    )
    pipeline = install_recording_pipeline(service)

    service.verify_binding(
        make_report(),
        make_manifest(),
    )

    assert pipeline["calls"] == [
        "to_primitive_dict",
        "to_json_text",
        "to_utf8_bytes",
        "verify_integrity",
    ]

    assert pipeline["representation_service"].call_count == 1
    assert pipeline["json_service"].call_count == 1
    assert pipeline["utf8_service"].call_count == 1
    assert pipeline["integrity_service"].call_count == 1


def test_intermediate_outputs_flow_to_next_service_unchanged():
    report = make_report()
    manifest = make_manifest()
    service = (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService()
    )
    pipeline = install_recording_pipeline(service)

    service.verify_binding(
        report,
        manifest,
    )

    assert (
        pipeline["representation_service"].received_report
        is report
    )
    assert (
        pipeline["json_service"].received_primitive
        is pipeline["primitive"]
    )
    assert (
        pipeline["utf8_service"].received_json_text
        is pipeline["json_text"]
    )
    assert (
        pipeline["integrity_service"].received_report_bytes
        is pipeline["report_bytes"]
    )
    assert (
        pipeline["integrity_service"].received_manifest
        is manifest
    )


@pytest.mark.parametrize(
    (
        "digest_matches",
        "byte_length_matches",
        "bom_matches",
        "expected_binding_matches",
    ),
    BOOLEAN_COMBINATIONS,
)
def test_service_preserves_all_partial_integrity_outcomes(
    digest_matches,
    byte_length_matches,
    bom_matches,
    expected_binding_matches,
):
    integrity_result = (
        RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult(
            digest_matches=digest_matches,
            byte_length_matches=byte_length_matches,
            bom_matches=bom_matches,
        )
    )
    service = (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService()
    )
    pipeline = install_recording_pipeline(
        service,
        integrity_result=integrity_result,
    )

    result = service.verify_binding(
        make_report(),
        make_manifest(),
    )

    assert type(result) is (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationResult
    )
    assert result is not pipeline["integrity_result"]
    assert result.digest_matches is digest_matches
    assert result.byte_length_matches is byte_length_matches
    assert result.bom_matches is bom_matches
    assert result.binding_matches is expected_binding_matches


def test_same_false_aggregate_preserves_different_partial_evidence():
    service = (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService()
    )

    first_integrity = (
        RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult(
            digest_matches=False,
            byte_length_matches=True,
            bom_matches=True,
        )
    )
    install_recording_pipeline(
        service,
        integrity_result=first_integrity,
    )
    first = service.verify_binding(
        make_report(),
        make_manifest(),
    )

    second_integrity = (
        RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult(
            digest_matches=True,
            byte_length_matches=False,
            bom_matches=True,
        )
    )
    install_recording_pipeline(
        service,
        integrity_result=second_integrity,
    )
    second = service.verify_binding(
        make_report(),
        make_manifest(),
    )

    assert first.binding_matches is False
    assert second.binding_matches is False
    assert first != second


def test_real_pipeline_returns_complete_match_for_matching_manifest():
    report = make_report()
    manifest = make_matching_manifest(report)
    service = (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService()
    )

    result = service.verify_binding(
        report,
        manifest,
    )

    assert result.digest_matches is True
    assert result.byte_length_matches is True
    assert result.bom_matches is True
    assert result.binding_matches is True


def test_real_pipeline_preserves_digest_mismatch():
    report = make_report()
    matching_manifest = make_matching_manifest(report)

    manifest = make_manifest(
        sha256_digest="f" * 64,
        byte_length=matching_manifest.byte_length,
    )

    service = (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService()
    )

    result = service.verify_binding(
        report,
        manifest,
    )

    assert result.digest_matches is False
    assert result.byte_length_matches is True
    assert result.bom_matches is True
    assert result.binding_matches is False


def test_real_pipeline_preserves_length_mismatch():
    report = make_report()
    matching_manifest = make_matching_manifest(report)

    manifest = make_manifest(
        sha256_digest=matching_manifest.sha256_digest,
        byte_length=matching_manifest.byte_length + 1,
    )

    service = (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService()
    )

    result = service.verify_binding(
        report,
        manifest,
    )

    assert result.digest_matches is True
    assert result.byte_length_matches is False
    assert result.bom_matches is True
    assert result.binding_matches is False


def test_service_does_not_mutate_report_or_manifest():
    report = make_report()
    manifest = make_matching_manifest(report)

    report_snapshot = (
        report.record_id,
        report.record_type,
        report.record_category,
        report.append_position,
        report.recorded_at,
        report.schema_version,
        report.provenance_ref,
        report.external_id,
        report.declared_fields,
    )
    manifest_snapshot = (
        manifest.manifest_schema_version,
        manifest.digest_algorithm,
        manifest.sha256_digest,
        manifest.byte_length,
        manifest.codec,
        manifest.bom_present,
    )

    service = (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService()
    )
    service.verify_binding(
        report,
        manifest,
    )

    assert report_snapshot == (
        report.record_id,
        report.record_type,
        report.record_category,
        report.append_position,
        report.recorded_at,
        report.schema_version,
        report.provenance_ref,
        report.external_id,
        report.declared_fields,
    )
    assert manifest_snapshot == (
        manifest.manifest_schema_version,
        manifest.digest_algorithm,
        manifest.sha256_digest,
        manifest.byte_length,
        manifest.codec,
        manifest.bom_present,
    )


def test_repeated_calls_are_deterministic_and_return_separate_results():
    report = make_report()
    manifest = make_matching_manifest(report)
    service = (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService()
    )

    first = service.verify_binding(
        report,
        manifest,
    )
    second = service.verify_binding(
        report,
        manifest,
    )

    assert first == second
    assert first is not second


def test_service_retains_no_call_history():
    report = make_report()
    manifest = make_matching_manifest(report)
    service = (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService()
    )

    expected_keys = set(service.__dict__)

    service.verify_binding(
        report,
        manifest,
    )
    service.verify_binding(
        report,
        manifest,
    )

    assert set(service.__dict__) == expected_keys


def test_representation_exception_propagates_unchanged():
    error = LookupError("representation failed")
    service = (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService()
    )
    pipeline = install_recording_pipeline(
        service,
        representation_error=error,
    )

    with pytest.raises(LookupError) as captured:
        service.verify_binding(
            make_report(),
            make_manifest(),
        )

    assert captured.value is error
    assert pipeline["calls"] == [
        "to_primitive_dict",
    ]


def test_json_exception_propagates_unchanged():
    error = LookupError("json failed")
    service = (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService()
    )
    pipeline = install_recording_pipeline(
        service,
        json_error=error,
    )

    with pytest.raises(LookupError) as captured:
        service.verify_binding(
            make_report(),
            make_manifest(),
        )

    assert captured.value is error
    assert pipeline["calls"] == [
        "to_primitive_dict",
        "to_json_text",
    ]


def test_utf8_exception_propagates_unchanged():
    error = LookupError("utf8 failed")
    service = (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService()
    )
    pipeline = install_recording_pipeline(
        service,
        utf8_error=error,
    )

    with pytest.raises(LookupError) as captured:
        service.verify_binding(
            make_report(),
            make_manifest(),
        )

    assert captured.value is error
    assert pipeline["calls"] == [
        "to_primitive_dict",
        "to_json_text",
        "to_utf8_bytes",
    ]


def test_integrity_exception_propagates_unchanged():
    error = LookupError("integrity failed")
    service = (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService()
    )
    pipeline = install_recording_pipeline(
        service,
        integrity_error=error,
    )

    with pytest.raises(LookupError) as captured:
        service.verify_binding(
            make_report(),
            make_manifest(),
        )

    assert captured.value is error
    assert pipeline["calls"] == [
        "to_primitive_dict",
        "to_json_text",
        "to_utf8_bytes",
        "verify_integrity",
    ]


def test_only_verify_binding_is_public_domain_method():
    public_methods = {
        name
        for name, value in inspect.getmembers(
            RuntimeRecordInspectionReportDerivedManifestBindingVerificationService,
            predicate=inspect.isfunction,
        )
        if not name.startswith("_")
    }

    assert public_methods == {
        "verify_binding",
    }


def test_service_module_does_not_import_application_frameworks():
    module_name = (
        "services."
        "runtime_record_inspection_report_derived_manifest_"
        "binding_verification_service"
    )

    importlib.import_module(module_name)

    for forbidden_module in (
        "streamlit",
        "flask",
        "django",
        "fastapi",
        "sqlalchemy",
        "requests",
    ):
        assert forbidden_module not in sys.modules


def test_production_source_uses_exact_upstream_method_names():
    module = importlib.import_module(
        "services."
        "runtime_record_inspection_report_derived_manifest_"
        "binding_verification_service"
    )
    source = inspect.getsource(module)

    assert ".to_primitive_dict(" in source
    assert ".to_json_text(" in source
    assert ".to_utf8_bytes(" in source
    assert ".verify_integrity(" in source

    assert ".to_representation(" not in source
    assert ".encode_json(" not in source
    assert ".encode_utf8(" not in source


def test_production_source_contains_no_direct_primitive_reimplementation():
    module = importlib.import_module(
        "services."
        "runtime_record_inspection_report_derived_manifest_"
        "binding_verification_service"
    )
    source = inspect.getsource(module)

    forbidden_fragments = (
        "import hashlib",
        "import hmac",
        "compare_digest",
        "hashlib.sha256",
        "import json",
        "json.dumps",
        '.encode("utf-8")',
        "len(report_bytes)",
        "startswith(",
        'b"\\xef\\xbb\\xbf"',
        "RuntimeRecordRegistry",
        "runtime_record_registry",
        "RuntimeEventRecord",
        "RuntimeObjectVersionRecord",
        "ProgressionAssertionRecord",
        "HoldRecord",
        "RuntimeRecordInspector",
        "RuntimeRecordInspectionDigestManifestService",
        "create_manifest",
        "from datetime",
        "import datetime",
        "import time",
        "pathlib",
    )

    for fragment in forbidden_fragments:
        assert fragment not in source


def test_production_source_contains_no_custom_service_protocols():
    module = importlib.import_module(
        "services."
        "runtime_record_inspection_report_derived_manifest_"
        "binding_verification_service"
    )
    source = inspect.getsource(module)

    for fragment in (
        "def __repr__",
        "def __str__",
        "def __lt__",
        "def __le__",
        "def __gt__",
        "def __ge__",
        "def __hash__",
    ):
        assert fragment not in source


@pytest.mark.parametrize(
    "attribute_name",
    (
        "report_id",
        "manifest_id",
        "record_id",
        "subject_id",
        "identity_matches",
        "subject_matches",
        "provenance",
        "provenance_ref",
        "provenance_matches",
        "lineage",
        "lineage_ref",
        "historical_binding_matches",
        "custody",
        "custody_ref",
        "custody_matches",
        "created_at",
        "observed_at",
        "verified_at",
        "bound_at",
        "timestamp",
        "admitted",
        "trusted",
        "authorized",
    ),
)
def test_returned_result_contains_no_excluded_semantics(
    attribute_name,
):
    report = make_report()
    manifest = make_matching_manifest(report)
    service = (
        RuntimeRecordInspectionReportDerivedManifestBindingVerificationService()
    )

    result = service.verify_binding(
        report,
        manifest,
    )

    assert not hasattr(result, attribute_name)