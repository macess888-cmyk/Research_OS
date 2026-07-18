from dataclasses import dataclass


@dataclass(frozen=True)
class RuntimeRecordInspectionReportDerivedManifestBindingVerificationResult:
    digest_matches: bool
    byte_length_matches: bool
    bom_matches: bool

    def __post_init__(self) -> None:
        if type(self.digest_matches) is not bool:
            raise TypeError(
                "digest_matches must be an exact bool"
            )

        if type(self.byte_length_matches) is not bool:
            raise TypeError(
                "byte_length_matches must be an exact bool"
            )

        if type(self.bom_matches) is not bool:
            raise TypeError(
                "bom_matches must be an exact bool"
            )

    @property
    def binding_matches(self) -> bool:
        return (
            self.digest_matches
            and self.byte_length_matches
            and self.bom_matches
        )