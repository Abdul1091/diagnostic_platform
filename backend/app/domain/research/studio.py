from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import UUID, uuid4
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.domain.research.workspace import DesignWorkspace

from app.core.exceptions import ValidationError

class StudioStatus(Enum):
    """Lifecycle states of a Research Studio."""

    PLANNING = "planning"
    ACTIVE = "active"
    ON_HOLD = "on_hold"
    COMPLETED = "completed"
    ARCHIVED = "archived"


class StudioType(Enum):
    """Major scientific phases supported by the platform."""

    BIOLOGICAL_DISCOVERY = "biological_discovery"
    MOLECULAR_ENGINEERING = "molecular_engineering"
    RECOMBINANT_PRODUCTION = "recombinant_production"
    IMMUNOLOGICAL_EVALUATION = "immunological_evaluation"
    DIAGNOSTIC_DEVELOPMENT = "diagnostic_development"
    DIAGNOSTIC_VALIDATION = "diagnostic_validation"


@dataclass
class ResearchStudio:
    """
    Represents a major phase of a scientific research project.

    A Research Studio provides a dedicated environment for
    a specific stage of the research lifecycle.
    """

    project_id: UUID
    name: str
    studio_type: StudioType

    id: UUID = field(default_factory=uuid4)

    description: str = ""

    status: StudioStatus = StudioStatus.PLANNING

    workspaces: list["DesignWorkspace"] = field(default_factory=list)

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    def add_workspace(self, workspace: "DesignWorkspace") -> None:
        """
        Add a Design Workspace to the Research Studio.

        Raises:
            ValidationError:
                If the workspace already exists in the studio.
        """

        if workspace in self.workspaces:
            raise ValidationError(
                entity="ResearchStudio",
                field="workspaces",
                message="Design Workspace already exists in this studio.",
            )

        self.workspaces.append(workspace)
        self.updated_at = datetime.now(UTC)

    @property
    def workspace_count(self) -> int:
        """
        Return the number of workspaces.
        """

        return len(self.workspaces)

    def __post_init__(self) -> None:
        """Validate studio state."""

        if not self.name.strip():
            raise ValidationError(
                entity="ResearchStudio",
                field="name",
                message="Research Studio name cannot be empty.",
            )