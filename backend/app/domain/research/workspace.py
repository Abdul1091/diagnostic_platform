from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import UUID, uuid4
from enum import Enum

from app.core.exceptions import ValidationError

class WorkspaceStatus(Enum):
    """Lifecycle states of a Design Workspace."""

    PLANNING = "planning"
    ACTIVE = "active"
    REVIEW = "review"
    COMPLETED = "completed"
    ARCHIVED = "archived"


@dataclass
class DesignWorkspace:
    """
    Represents a focused scientific design environment.

    A Design Workspace is where researchers carry out a specific
    design activity within a Research Studio.
    """

    studio_id: UUID
    name: str

    id: UUID = field(default_factory=uuid4)

    description: str = ""

    status: WorkspaceStatus = WorkspaceStatus.PLANNING

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    def __post_init__(self) -> None:
        """Validate workspace state."""

        if not self.name.strip():
            raise ValidationError(
                entity="DesignWorkspace",
                field="name",
                message="Workspace name cannot be empty.",
            )