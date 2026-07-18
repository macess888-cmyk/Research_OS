import hmac


class RuntimeRecordInspectionDigestManifestDigestVerificationService:
    def verify_digest(
        self,
        computed_digest: str,
        expected_digest: str,
    ) -> bool:
        if type(computed_digest) is not str:
            raise TypeError(
                "computed_digest must be an exact str"
            )

        if type(expected_digest) is not str:
            raise TypeError(
                "expected_digest must be an exact str"
            )

        allowed = "0123456789abcdef"

        if (
            len(computed_digest) != 64
            or any(
                character not in allowed
                for character in computed_digest
            )
        ):
            raise ValueError(
                "computed_digest must be a lowercase 64-character SHA-256 hexadecimal string"
            )

        if (
            len(expected_digest) != 64
            or any(
                character not in allowed
                for character in expected_digest
            )
        ):
            raise ValueError(
                "expected_digest must be a lowercase 64-character SHA-256 hexadecimal string"
            )

        return hmac.compare_digest(
            computed_digest,
            expected_digest,
        )