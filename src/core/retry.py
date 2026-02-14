from tenacity import RetryCallState, retry, stop_after_attempt, wait_exponential

from .errors import A2SUnavailableError
from .logging import log


class A2SRetry:
    """Class for A2S retry."""

    ATTEMPTS = 5
    MIN_WAIT = 1
    MAX_WAIT = 10

    @staticmethod
    def retry_failed(retry_state: RetryCallState) -> None:
        """Raise A2SUnavailableError exception."""
        exc = retry_state.outcome.exception()
        msg = f"A2S unreachable after {retry_state.attempt_number} attempts"
        raise A2SUnavailableError(msg) from exc

    @staticmethod
    def log_retry(retry_state: RetryCallState) -> None:
        """Log retry attempt."""
        exc = retry_state.outcome.exception()
        log.warning(
            "Attempt %s failed (%s). Retrying in %.1f sec...",
            retry_state.attempt_number,
            type(exc).__name__,
            retry_state.next_action.sleep,
        )

    decorator = retry(
        stop=stop_after_attempt(5),
        wait=wait_exponential(min=1, max=10),
        before_sleep=log_retry,
        retry_error_callback=retry_failed,
        reraise=True,
    )
