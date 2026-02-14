class AppError(Exception):
    """Base application error."""


class A2SError(AppError):
    """Base A2S error."""


class A2SUnavailableError(A2SError):
    """Raised when A2S server is unreachable after retries."""
