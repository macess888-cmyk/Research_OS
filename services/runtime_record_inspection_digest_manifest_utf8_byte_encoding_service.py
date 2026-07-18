class RuntimeRecordInspectionDigestManifestUtf8ByteEncodingService:
    def to_utf8_bytes(
        self,
        json_text: str,
    ) -> bytes:
        if type(json_text) is not str:
            raise TypeError(
                "json_text must be an exact str"
            )

        return json_text.encode("utf-8")