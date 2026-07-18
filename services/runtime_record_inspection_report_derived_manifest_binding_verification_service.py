from models.runtime_record_inspection_digest_manifest import (
    RuntimeRecordInspectionDigestManifest,
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
from services.runtime_record_inspection_utf8_byte_encoding_service import (
    RuntimeRecordInspectionUtf8ByteEncodingService,
)


class RuntimeRecordInspectionReportDerivedManifestBindingVerificationService:
    def __init__(self) -> None:
        self._representation_service = (
            RuntimeRecordInspectionRepresentationService()
        )
        self._json_encoding_service = (
            RuntimeRecordInspectionJsonEncodingService()
        )
        self._utf8_byte_encoding_service = (
            RuntimeRecordInspectionUtf8ByteEncodingService()
        )
        self._integrity_verification_service = (
            RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService()
        )

    def verify_binding(
        self,
        report: RuntimeRecordInspectionReport,
        manifest: RuntimeRecordInspectionDigestManifest,
    ) -> RuntimeRecordInspectionReportDerivedManifestBindingVerificationResult:
        if type(report) is not RuntimeRecordInspectionReport:
            raise TypeError(
                "report must be an exact RuntimeRecordInspectionReport"
            )

        if type(manifest) is not RuntimeRecordInspectionDigestManifest:
            raise TypeError(
                "manifest must be an exact RuntimeRecordInspectionDigestManifest"
            )

        report_representation = (
            self._representation_service.to_primitive_dict(
                report
            )
        )

        report_json_text = (
            self._json_encoding_service.to_json_text(
                report_representation
            )
        )

        report_bytes = (
            self._utf8_byte_encoding_service.to_utf8_bytes(
                report_json_text
            )
        )

        integrity_result = (
            self._integrity_verification_service.verify_integrity(
                report_bytes,
                manifest,
            )
        )

        return RuntimeRecordInspectionReportDerivedManifestBindingVerificationResult(
            digest_matches=integrity_result.digest_matches,
            byte_length_matches=integrity_result.byte_length_matches,
            bom_matches=integrity_result.bom_matches,
        )