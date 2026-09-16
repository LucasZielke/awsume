from .config_management import CONFIG_MANAGEMENT_HELP


class AwsumeException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ProfileNotFoundError(AwsumeException):
    def __init__(self, profile_name="", message=""):
        self.profile_name = profile_name
        self.message = message

    def __str__(self):
        if self.message:
            return self.message
        return f"Profile {self.profile_name} not found."


class InvalidProfileError(AwsumeException):
    def __init__(self, profile_name, message=""):
        self.profile_name = profile_name
        self.message = message

    def __str__(self):
        return f"Invalid profile [{self.profile_name}] {self.message}"


class ImmutableProfileError(AwsumeException):
    def __init__(self, profile_name, message=""):
        self.profile_name = profile_name
        self.message = message

    def __str__(self):
        return f"Immutable profile [{self.profile_name}] {self.message}"


class ValidationException(AwsumeException):
    def __init__(self, message="no message"):
        self.message = message

    def __str__(self):
        return f"Validation Exception - {self.message}"


class ConfigParseException(AwsumeException):
    def __init__(self, file_name, message="no message", error=None):
        self.file_name = file_name
        self.message = message
        self.error = error

    def __str__(self):
        return f"ConfigParseException - ({self.file_name}) {self.message} {self.error}"


class ConfigOperationException(AwsumeException):
    def __init__(self, message="no message"):
        self.message = message

    def __str__(self):
        return f"{self.message}\n{CONFIG_MANAGEMENT_HELP}"


class UserAuthenticationError(AwsumeException):
    def __init__(self, message=""):
        self.message = message

    def __str__(self):
        return self.message if self.message else "Unable to get session token"


class RoleAuthenticationError(AwsumeException):
    def __init__(self, message=""):
        self.message = message

    def __str__(self):
        return self.message if self.message else "Unable to assume role"


class SAMLAssertionNotFoundError(AwsumeException):
    def __init__(self, message=""):
        self.message = message

    def __str__(self):
        return self.message if self.message else "No SAML assertion"


class SAMLAssertionMissingRoleError(AwsumeException):
    def __init__(self, message=""):
        self.message = message

    def __str__(self):
        return self.message if self.message else "No role in the SAML assertion"


class SAMLRoleNotFoundError(AwsumeException):
    def __init__(self, principal_arn, role_arn, message=""):
        self.role_arn = role_arn
        self.principal_arn = principal_arn
        self.message = message

    def __str__(self):
        return (
            self.message
            if self.message
            else f"No match for SAML principal and role: {self.principal_arn},{self.role_arn}"
        )


class SAMLAssertionParseError(AwsumeException):
    def __init__(self, message=""):
        self.message = message

    def __str__(self):
        return self.message if self.message else "Cannot parse SAML assertion"


class NoCredentialsError(AwsumeException):
    def __init__(self, message=""):
        self.message = message

    def __str__(self):
        return self.message if self.message else "No credentials"


class EarlyExit(AwsumeException):
    def __init__(self, data: dict | None = None):
        self.data = data

    def __str__(self):
        return "Early exit exception, nothing left to do"
