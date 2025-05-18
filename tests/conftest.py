"""
Pytest configuration.
"""

import os
import pytest


@pytest.fixture(autouse=True)
def clear_logging_handlers():
    """Clear logging handlers after each test."""
    yield
    # After test, clear handlers from the logger to avoid interference between tests
    import logging
    logger = logging.getLogger("architectum.blueprint_generator")
    if logger.handlers:
        logger.handlers.clear()
