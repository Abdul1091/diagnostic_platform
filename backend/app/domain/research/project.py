from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import Enum
from uuid import UUID, uuid4
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.domain.research.studio import ResearchStudio

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

    studios: list["ResearchStudio"] = field(default_factory=list)

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )
    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    def add_studio(self, studio: "ResearchStudio") -> None:
        """
        Add a Research Studio to the project.

        Raises:
            ValidationError:
                If the studio already exists in the project.
        """

        if studio in self.studios:
            raise ValidationError(
                entity="ResearchProject",
                field="studios",
                message="Research Studio already exists in this project.",
            )

        self.studios.append(studio)
        self.updated_at = datetime.now(UTC)

    @property
    def studio_count(self) -> int:
        """Return the number of studios."""

        return len(self.studios)

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