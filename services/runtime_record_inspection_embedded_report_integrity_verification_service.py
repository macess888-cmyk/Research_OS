import hashlib
import hmac

from models.runtime_record_inspection_digest_manifest import (
    RuntimeRecordInspectionDigestManifest,
)
from models.runtime_record_inspection_embedded_report_integrity_verification_result import (
    RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult,
)


class RuntimeRecordInspectionEmbeddedReportIntegrityVerificationService:
    def verify_integrity(
        self,
        report_bytes: bytes,
        manifest: RuntimeRecordInspectionDigestManifest,
    ) -> RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult:
        if type(report_bytes) is not bytes:
            raise TypeError(
                "report_bytes must be an exact bytes"
            )

        if type(manifest) is not RuntimeRecordInspectionDigestManifest:
            raise TypeError(
                "manifest must be an exact RuntimeRecordInspectionDigestManifest"
            )

        computed_digest = hashlib.sha256(
            report_bytes
        ).hexdigest()

        digest_matches = hmac.compare_digest(
            computed_digest,
            manifest.sha256_digest,
        )

        byte_length_matches = (
            len(report_bytes)
            == manifest.byte_length
        )

        observed_bom_present = report_bytes.startswith(
            b"\xef\xbb\xbf"
        )

        bom_matches = (
            observed_bom_present
            is manifest.bom_present
        )

        return RuntimeRecordInspectionEmbeddedReportIntegrityVerificationResult(
            digest_matches=digest_matches,
            byte_length_matches=byte_length_matches,
            bom_matches=bom_matches,
        )