import re
from dataclasses import dataclass


_SHA256_DIGEST_PATTERN = re.compile(r"^[0-9a-f]{64}$")


@dataclass(frozen=True)
class RuntimeRecordInspectionDigestManifest:
    manifest_schema_version: str
    digest_algorithm: str
    sha256_digest: str
    byte_length: int
    codec: str
    bom_present: bool

    def __post_init__(self) -> None:
        if type(self.manifest_schema_version) is not str:
            raise TypeError(
                "manifest_schema_version must be an exact str"
            )

        if self.manifest_schema_version != "1.0":
            raise ValueError(
                "manifest_schema_version must be exactly '1.0'"
            )

        if type(self.digest_algorithm) is not str:
            raise TypeError(
                "digest_algorithm must be an exact str"
            )

        if self.digest_algorithm != "sha256":
            raise ValueError(
                "digest_algorithm must be exactly 'sha256'"
            )

        if type(self.sha256_digest) is not str:
            raise TypeError(
                "sha256_digest must be an exact str"
            )

        if not _SHA256_DIGEST_PATTERN.fullmatch(
            self.sha256_digest
        ):
            raise ValueError(
                "sha256_digest must be exactly 64 lowercase "
                "hexadecimal characters"
            )

        if type(self.byte_length) is not int:
            raise TypeError(
                "byte_length must be an exact int"
            )

        if self.byte_length < 0:
            raise ValueError(
                "byte_length must be non-negative"
            )

        if type(self.codec) is not str:
            raise TypeError(
                "codec must be an exact str"
            )

        if self.codec != "utf-8":
            raise ValueError(
                "codec must be exactly 'utf-8'"
            )

        if type(self.bom_present) is not bool:
            raise TypeError(
                "bom_present must be an exact bool"
            )

        if self.bom_present is not False:
            raise ValueError(
                "bom_present must be False"
            )