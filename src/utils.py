"""Utility helpers for the application."""
import logging

logger = logging.getLogger(__name__)


def greet(name: str) -> str:
    """Return a greeting string for the given name."""
    if not name:
        raise ValueError("name must not be empty")
    logger.debug("greet() called with name=%r", name)
    return f"Hello, {name}!"


def format_message(msg: str) -> str:
    """Wrap a message with a simple border."""
    border = "-" * (len(msg) + 4)
    return f"{border}\n| {msg} |\n{border}"
