import re

from models.runtime_record_inspection_artifact_registration_result import (
    RuntimeRecordInspectionArtifactRegistrationResult,
)
from models.runtime_record_inspection_digest_manifest_artifact import (
    RuntimeRecordInspectionDigestManifestArtifact,
)
from models.runtime_record_inspection_report_artifact import (
    RuntimeRecordInspectionReportArtifact,
)


_REPORT_ARTIFACT_ID_PATTERN = re.compile(
    r"^RIRA-[0-9]{9}$"
)

_MANIFEST_ARTIFACT_ID_PATTERN = re.compile(
    r"^RIDMA-[0-9]{9}$"
)


class RuntimeRecordInspectionArtifactRegistry:
    """
    Monotonic in-memory registry for typed runtime-record inspection
    artifacts.

    The service evaluates registry-local uniqueness, equal
    re-registration, and identity collision. It does not allocate,
    persist, admit, authorize, or trigger side effects.
    """

    def __init__(self) -> None:
        self._report_artifacts_by_id: dict[
            str,
            RuntimeRecordInspectionReportArtifact,
        ] = {}

        self._manifest_artifacts_by_id: dict[
            str,
            RuntimeRecordInspectionDigestManifestArtifact,
        ] = {}

    def register_report_artifact(
        self,
        artifact: RuntimeRecordInspectionReportArtifact,
    ) -> RuntimeRecordInspectionArtifactRegistrationResult:
        if not isinstance(
            artifact,
            RuntimeRecordInspectionReportArtifact,
        ):
            raise TypeError(
                "artifact must be a "
                "RuntimeRecordInspectionReportArtifact"
            )

        artifact_id = artifact.report_artifact_id
        existing = self._report_artifacts_by_id.get(
            artifact_id
        )

        if existing is None:
            self._report_artifacts_by_id[
                artifact_id
            ] = artifact

            return RuntimeRecordInspectionArtifactRegistrationResult(
                artifact_kind="REPORT",
                artifact_id=artifact_id,
                status="REGISTERED",
                existing_artifact=None,
                candidate_artifact=artifact,
            )

        if existing == artifact:
            return RuntimeRecordInspectionArtifactRegistrationResult(
                artifact_kind="REPORT",
                artifact_id=artifact_id,
                status="ALREADY_REGISTERED",
                existing_artifact=existing,
                candidate_artifact=artifact,
            )

        return RuntimeRecordInspectionArtifactRegistrationResult(
            artifact_kind="REPORT",
            artifact_id=artifact_id,
            status="IDENTITY_COLLISION",
            existing_artifact=existing,
            candidate_artifact=artifact,
        )

    def register_manifest_artifact(
        self,
        artifact: RuntimeRecordInspectionDigestManifestArtifact,
    ) -> RuntimeRecordInspectionArtifactRegistrationResult:
        if not isinstance(
            artifact,
            RuntimeRecordInspectionDigestManifestArtifact,
        ):
            raise TypeError(
                "artifact must be a "
                "RuntimeRecordInspectionDigestManifestArtifact"
            )

        artifact_id = artifact.manifest_artifact_id
        existing = self._manifest_artifacts_by_id.get(
            artifact_id
        )

        if existing is None:
            self._manifest_artifacts_by_id[
                artifact_id
            ] = artifact

            return RuntimeRecordInspectionArtifactRegistrationResult(
                artifact_kind="DIGEST_MANIFEST",
                artifact_id=artifact_id,
                status="REGISTERED",
                existing_artifact=None,
                candidate_artifact=artifact,
            )

        if existing == artifact:
            return RuntimeRecordInspectionArtifactRegistrationResult(
                artifact_kind="DIGEST_MANIFEST",
                artifact_id=artifact_id,
                status="ALREADY_REGISTERED",
                existing_artifact=existing,
                candidate_artifact=artifact,
            )

        return RuntimeRecordInspectionArtifactRegistrationResult(
            artifact_kind="DIGEST_MANIFEST",
            artifact_id=artifact_id,
            status="IDENTITY_COLLISION",
            existing_artifact=existing,
            candidate_artifact=artifact,
        )

    def get_report_artifact(
        self,
        report_artifact_id: str,
    ) -> RuntimeRecordInspectionReportArtifact:
        self._validate_report_artifact_id(
            report_artifact_id
        )

        return self._report_artifacts_by_id[
            report_artifact_id
        ]

    def get_manifest_artifact(
        self,
        manifest_artifact_id: str,
    ) -> RuntimeRecordInspectionDigestManifestArtifact:
        self._validate_manifest_artifact_id(
            manifest_artifact_id
        )

        return self._manifest_artifacts_by_id[
            manifest_artifact_id
        ]

    @property
    def report_count(self) -> int:
        return len(
            self._report_artifacts_by_id
        )

    @property
    def manifest_count(self) -> int:
        return len(
            self._manifest_artifacts_by_id
        )

    @property
    def total_count(self) -> int:
        return (
            self.report_count
            + self.manifest_count
        )

    def _validate_report_artifact_id(
        self,
        report_artifact_id: str,
    ) -> None:
        if not isinstance(
            report_artifact_id,
            str,
        ):
            raise TypeError(
                "report_artifact_id must be a string"
            )

        if not _REPORT_ARTIFACT_ID_PATTERN.fullmatch(
            report_artifact_id
        ):
            raise ValueError(
                "report_artifact_id must match "
                "RIRA-#########"
            )

        if int(report_artifact_id[5:]) <= 0:
            raise ValueError(
                "report_artifact_id numeric component "
                "must be greater than zero"
            )

    def _validate_manifest_artifact_id(
        self,
        manifest_artifact_id: str,
    ) -> None:
        if not isinstance(
            manifest_artifact_id,
            str,
        ):
            raise TypeError(
                "manifest_artifact_id must be a string"
            )

        if not _MANIFEST_ARTIFACT_ID_PATTERN.fullmatch(
            manifest_artifact_id
        ):
            raise ValueError(
                "manifest_artifact_id must match "
                "RIDMA-#########"
            )

        if int(manifest_artifact_id[6:]) <= 0:
            raise ValueError(
                "manifest_artifact_id numeric component "
                "must be greater than zero"
            )