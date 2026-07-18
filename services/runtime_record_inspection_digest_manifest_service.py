from models.runtime_record_inspection_digest_manifest import (
    RuntimeRecordInspectionDigestManifest,
)


class RuntimeRecordInspectionDigestManifestService:
    def create_manifest(
        self,
        *,
        manifest_schema_version: str,
        digest_algorithm: str,
        sha256_digest: str,
        byte_length: int,
        codec: str,
        bom_present: bool,
    ) -> RuntimeRecordInspectionDigestManifest:
        return RuntimeRecordInspectionDigestManifest(
            manifest_schema_version=manifest_schema_version,
            digest_algorithm=digest_algorithm,
            sha256_digest=sha256_digest,
            byte_length=byte_length,
            codec=codec,
            bom_present=bom_present,
        )