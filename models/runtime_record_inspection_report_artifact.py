from dataclasses import dataclass
import re

from models.runtime_record_inspection_report import (
    RuntimeRecordInspectionReport,
)


_REPORT_ARTIFACT_ID_PATTERN = re.compile(
    r"^RIRA-[0-9]{9}$"
)


@dataclass(frozen=True)
class RuntimeRecordInspectionReportArtifact:
    """
    Immutable identity wrapper for one runtime-record inspection report.

    This model provides typed local addressability only. It does not
    allocate identity, establish uniqueness, register, persist, verify
    provenance or custody, assert associations, admit, authorize, or
    trigger side effects.
    """

    report_artifact_id: str
    report: RuntimeRecordInspectionReport

    def __post_init__(self) -> None:
        self._validate_report_artifact_id()
        self._validate_report()

    def _validate_report_artifact_id(self) -> None:
        if not isinstance(self.report_artifact_id, str):
            raise TypeError(
                "report_artifact_id must be a string"
            )

        if not _REPORT_ARTIFACT_ID_PATTERN.fullmatch(
            self.report_artifact_id
        ):
            raise ValueError(
                "report_artifact_id must match RIRA-#########"
            )

        if int(self.report_artifact_id[5:]) <= 0:
            raise ValueError(
                "report_artifact_id numeric component must be "
                "greater than zero"
            )

    def _validate_report(self) -> None:
        if not isinstance(
            self.report,
            RuntimeRecordInspectionReport,
        ):
            raise TypeError(
                "report must be a RuntimeRecordInspectionReport"
            )