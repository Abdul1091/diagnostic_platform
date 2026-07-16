from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import Enum
from uuid import UUID, uuid4

from app.core.exceptions import ValidationError


class ProjectStatus(Enum):
    """Lifecycle states of a research project."""

    PLANNING = "planning"
    ACTIVE = "active"
    ON_HOLD = "on_hold"
    COMPLETED = "completed"
    ARCHIVED = "archived"


@dataclass
class ResearchProject:
    """
    Represents a scientific research project.

    A Research Project is the top-level container for all scientific work
    performed within the platform.
    """

    title: str
    research_question: str

    id: UUID = field(default_factory=uuid4)
    description: str = ""
    status: ProjectStatus = ProjectStatus.PLANNING

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )
    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    def __post_init__(self) -> None:
        """Validate project state."""

        if not self.title.strip():
            raise ValidationError(
                entity="ResearchProject",
                field="title",
                message="Project title cannot be empty.",
            )

        if not self.research_question.strip():
            raise ValidationError(
                entity="ResearchProject",
                field="research_question",
                message="Research question cannot be empty.",
            )