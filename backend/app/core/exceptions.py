"""
Custom exception hierarchy for the Diagnostic Platform.
"""


class DiagnosticPlatformError(Exception):
    """
    Base exception for all platform errors.
    """

    pass


class ConfigurationError(DiagnosticPlatformError):
    """Raised when application configuration is invalid."""


class InfrastructureError(DiagnosticPlatformError):
    """Raised when infrastructure components fail."""


class PluginError(DiagnosticPlatformError):
    """Raised when plugin execution fails."""


class DomainError(DiagnosticPlatformError):
    """
    Base class for all domain-related errors.
    """


class ValidationError(DomainError):
    """
    Raised when a domain entity fails validation.
    """

    def __init__(
        self,
        entity: str,
        field: str,
        message: str,
    ) -> None:

        self.entity = entity
        self.field = field
        self.message = message

        super().__init__(
            f"[{entity}] {field}: {message}"
        )


class ResourceNotFoundError(DomainError):
    """Raised when a domain resource cannot be found."""


class BusinessRuleViolation(DomainError):
    """Raised when a business rule is violated."""