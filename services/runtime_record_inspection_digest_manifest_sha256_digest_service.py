import hashlib


class RuntimeRecordInspectionDigestManifestSha256DigestService:
    def to_sha256_hexdigest(
        self,
        content_bytes: bytes,
    ) -> str:
        if type(content_bytes) is not bytes:
            raise TypeError(
                "content_bytes must be an exact bytes"
            )

        return hashlib.sha256(
            content_bytes
        ).hexdigest()