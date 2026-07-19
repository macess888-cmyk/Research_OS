from dataclasses import dataclass
import re

from models.runtime_record_inspection_digest_manifest import (
    RuntimeRecordInspectionDigestManifest,
)


_MANIFEST_ARTIFACT_ID_PATTERN = re.compile(
    r"^RIDMA-[0-9]{9}$"
)


@dataclass(frozen=True)
class RuntimeRecordInspectionDigestManifestArtifact:
    """
    Immutable identity wrapper for one runtime-record inspection
    digest manifest.

    This model provides typed local addressability only. It does not
    allocate identity, establish uniqueness, register, persist, verify
    provenance or custody, assert associations, admit, authorize, or
    trigger side effects.
    """

    manifest_artifact_id: str
    manifest: RuntimeRecordInspectionDigestManifest

    def __post_init__(self) -> None:
        self._validate_manifest_artifact_id()
        self._validate_manifest()

    def _validate_manifest_artifact_id(self) -> None:
        if not isinstance(self.manifest_artifact_id, str):
            raise TypeError(
                "manifest_artifact_id must be a string"
            )

        if not _MANIFEST_ARTIFACT_ID_PATTERN.fullmatch(
            self.manifest_artifact_id
        ):
            raise ValueError(
                "manifest_artifact_id must match RIDMA-#########"
            )

        if int(self.manifest_artifact_id[6:]) <= 0:
            raise ValueError(
                "manifest_artifact_id numeric component must be "
                "greater than zero"
            )

    def _validate_manifest(self) -> None:
        if not isinstance(
            self.manifest,
            RuntimeRecordInspectionDigestManifest,
        ):
            raise TypeError(
                "manifest must be a "
                "RuntimeRecordInspectionDigestManifest"
            )