from models.runtime_record_inspection_digest_manifest import (
    RuntimeRecordInspectionDigestManifest,
)


class RuntimeRecordInspectionDigestManifestRepresentationService:
    def to_primitive_dict(
        self,
        manifest: RuntimeRecordInspectionDigestManifest,
    ) -> dict[str, object]:
        if type(manifest) is not RuntimeRecordInspectionDigestManifest:
            raise TypeError(
                "manifest must be an exact "
                "RuntimeRecordInspectionDigestManifest"
            )

        return {
            "manifest_schema_version": manifest.manifest_schema_version,
            "digest_algorithm": manifest.digest_algorithm,
            "sha256_digest": manifest.sha256_digest,
            "byte_length": manifest.byte_length,
            "codec": manifest.codec,
            "bom_present": manifest.bom_present,
        }