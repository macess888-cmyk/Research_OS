from dataclasses import dataclass
import re

from models.runtime_record_inspection_digest_manifest_artifact import (
    RuntimeRecordInspectionDigestManifestArtifact,
)
from models.runtime_record_inspection_report_artifact import (
    RuntimeRecordInspectionReportArtifact,
)


_ARTIFACT_KINDS = frozenset(
    {
        "REPORT",
        "DIGEST_MANIFEST",
    }
)

_REGISTRATION_STATUSES = frozenset(
    {
        "REGISTERED",
        "ALREADY_REGISTERED",
        "IDENTITY_COLLISION",
    }
)

_REPORT_ARTIFACT_ID_PATTERN = re.compile(
    r"^RIRA-[0-9]{9}$"
)

_MANIFEST_ARTIFACT_ID_PATTERN = re.compile(
    r"^RIDMA-[0-9]{9}$"
)


@dataclass(frozen=True)
class RuntimeRecordInspectionArtifactRegistrationResult:
    """
    Immutable observation of one runtime-record inspection artifact
    registration attempt.

    The result records local registry classification only. It does not
    persist, create a receipt, admit, trust, authorize, or trigger side
    effects.
    """

    artifact_kind: str
    artifact_id: str
    status: str
    existing_artifact: (
        RuntimeRecordInspectionReportArtifact
        | RuntimeRecordInspectionDigestManifestArtifact
        | None
    )
    candidate_artifact: (
        RuntimeRecordInspectionReportArtifact
        | RuntimeRecordInspectionDigestManifestArtifact
    )

    def __post_init__(self) -> None:
        self._validate_artifact_kind()
        self._validate_artifact_id()
        self._validate_status()
        self._validate_candidate_artifact()
        self._validate_existing_artifact()
        self._validate_artifact_kind_consistency()
        self._validate_identifier_consistency()
        self._validate_status_consistency()

    def _validate_artifact_kind(self) -> None:
        if not isinstance(self.artifact_kind, str):
            raise TypeError(
                "artifact_kind must be a string"
            )

        if self.artifact_kind not in _ARTIFACT_KINDS:
            raise ValueError(
                "artifact_kind must be REPORT or "
                "DIGEST_MANIFEST"
            )

    def _validate_artifact_id(self) -> None:
        if not isinstance(self.artifact_id, str):
            raise TypeError(
                "artifact_id must be a string"
            )

        if self.artifact_kind == "REPORT":
            if not _REPORT_ARTIFACT_ID_PATTERN.fullmatch(
                self.artifact_id
            ):
                raise ValueError(
                    "artifact_id must match RIRA-######### "
                    "for REPORT"
                )

            numeric_component = int(
                self.artifact_id[5:]
            )
        else:
            if not _MANIFEST_ARTIFACT_ID_PATTERN.fullmatch(
                self.artifact_id
            ):
                raise ValueError(
                    "artifact_id must match RIDMA-######### "
                    "for DIGEST_MANIFEST"
                )

            numeric_component = int(
                self.artifact_id[6:]
            )

        if numeric_component <= 0:
            raise ValueError(
                "artifact_id numeric component must be "
                "greater than zero"
            )

    def _validate_status(self) -> None:
        if not isinstance(self.status, str):
            raise TypeError(
                "status must be a string"
            )

        if self.status not in _REGISTRATION_STATUSES:
            raise ValueError(
                "status must be REGISTERED, "
                "ALREADY_REGISTERED, or "
                "IDENTITY_COLLISION"
            )

    def _validate_candidate_artifact(self) -> None:
        if not isinstance(
            self.candidate_artifact,
            (
                RuntimeRecordInspectionReportArtifact,
                RuntimeRecordInspectionDigestManifestArtifact,
            ),
        ):
            raise TypeError(
                "candidate_artifact must be a supported "
                "runtime-record inspection artifact"
            )

    def _validate_existing_artifact(self) -> None:
        if self.existing_artifact is None:
            return

        if not isinstance(
            self.existing_artifact,
            (
                RuntimeRecordInspectionReportArtifact,
                RuntimeRecordInspectionDigestManifestArtifact,
            ),
        ):
            raise TypeError(
                "existing_artifact must be None or a "
                "supported runtime-record inspection artifact"
            )

    def _validate_artifact_kind_consistency(
        self,
    ) -> None:
        if self.artifact_kind == "REPORT":
            if not isinstance(
                self.candidate_artifact,
                RuntimeRecordInspectionReportArtifact,
            ):
                raise TypeError(
                    "candidate_artifact must be a "
                    "RuntimeRecordInspectionReportArtifact "
                    "for REPORT"
                )

            if (
                self.existing_artifact is not None
                and not isinstance(
                    self.existing_artifact,
                    RuntimeRecordInspectionReportArtifact,
                )
            ):
                raise TypeError(
                    "existing_artifact must be a "
                    "RuntimeRecordInspectionReportArtifact "
                    "for REPORT"
                )

            return

        if not isinstance(
            self.candidate_artifact,
            RuntimeRecordInspectionDigestManifestArtifact,
        ):
            raise TypeError(
                "candidate_artifact must be a "
                "RuntimeRecordInspectionDigestManifestArtifact "
                "for DIGEST_MANIFEST"
            )

        if (
            self.existing_artifact is not None
            and not isinstance(
                self.existing_artifact,
                RuntimeRecordInspectionDigestManifestArtifact,
            )
        ):
            raise TypeError(
                "existing_artifact must be a "
                "RuntimeRecordInspectionDigestManifestArtifact "
                "for DIGEST_MANIFEST"
            )

    def _validate_identifier_consistency(
        self,
    ) -> None:
        if self.artifact_kind == "REPORT":
            candidate_id = (
                self.candidate_artifact.report_artifact_id
            )
            existing_id = (
                None
                if self.existing_artifact is None
                else self.existing_artifact.report_artifact_id
            )
        else:
            candidate_id = (
                self.candidate_artifact.manifest_artifact_id
            )
            existing_id = (
                None
                if self.existing_artifact is None
                else self.existing_artifact.manifest_artifact_id
            )

        if self.artifact_id != candidate_id:
            raise ValueError(
                "artifact_id must match candidate_artifact "
                "identifier"
            )

        if (
            existing_id is not None
            and self.artifact_id != existing_id
        ):
            raise ValueError(
                "artifact_id must match existing_artifact "
                "identifier"
            )

    def _validate_status_consistency(self) -> None:
        if self.status == "REGISTERED":
            if self.existing_artifact is not None:
                raise ValueError(
                    "existing_artifact must be None when "
                    "status is REGISTERED"
                )
            return

        if self.status == "ALREADY_REGISTERED":
            if self.existing_artifact is None:
                raise ValueError(
                    "existing_artifact is required when "
                    "status is ALREADY_REGISTERED"
                )

            if (
                self.existing_artifact
                != self.candidate_artifact
            ):
                raise ValueError(
                    "existing_artifact must equal "
                    "candidate_artifact when status is "
                    "ALREADY_REGISTERED"
                )
            return

        if self.existing_artifact is None:
            raise ValueError(
                "existing_artifact is required when "
                "status is IDENTITY_COLLISION"
            )

        if (
            self.existing_artifact
            == self.candidate_artifact
        ):
            raise ValueError(
                "existing_artifact must differ from "
                "candidate_artifact when status is "
                "IDENTITY_COLLISION"
            )

    @property
    def registry_changed(self) -> bool:
        return self.status == "REGISTERED"

    @property
    def registration_accepted(self) -> bool:
        return self.status in {
            "REGISTERED",
            "ALREADY_REGISTERED",
        }

    @property
    def collision_detected(self) -> bool:
        return self.status == "IDENTITY_COLLISION"