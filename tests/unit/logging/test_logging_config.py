"""
Tests for logging configuration.
"""

import logging
import os
import pytest
from pathlib import Path

from arch_blueprint_generator.logging_config import setup_logging


def test_setup_logging_default():
    """Test default logging setup."""
    logger = setup_logging()
    
    assert logger.name == "architectum.blueprint_generator"
    assert logger.level == logging.INFO
    assert len(logger.handlers) > 0
    assert all(isinstance(h, logging.Handler) for h in logger.handlers)


def test_setup_logging_custom_level():
    """Test logging setup with custom level."""
    logger = setup_logging(level=logging.DEBUG)
    
    assert logger.level == logging.DEBUG


def test_setup_logging_with_file(tmp_path):
    """Test logging setup with file output."""
    log_file = tmp_path / "test.log"
    logger = setup_logging(log_file=str(log_file))
    
    # Check that file handler was added
    assert any(isinstance(h, logging.FileHandler) for h in logger.handlers)
    
    # Log a test message
    test_message = "Test log message"
    logger.info(test_message)
    
    # Check that the message was written to the file
    assert log_file.exists()
    log_content = log_file.read_text()
    assert test_message in log_content


def test_setup_logging_custom_format():
    """Test logging setup with custom format."""
    custom_format = "%(levelname)s - %(message)s"
    logger = setup_logging(log_format=custom_format)
    
    # Get formatter from handler
    formatter = logger.handlers[0].formatter
    
    # Check that the format string matches
    assert formatter._fmt == custom_format


def test_setup_logging_creates_log_directory(tmp_path):
    """Test that logging setup creates log directory if it doesn't exist."""
    log_dir = tmp_path / "logs"
    log_file = log_dir / "test.log"
    
    # Directory should not exist yet
    assert not log_dir.exists()
    
    logger = setup_logging(log_file=str(log_file))
    
    # Log something to ensure file is created
    logger.info("Test message")
    
    # Now directory and file should exist
    assert log_dir.exists()
    assert log_file.exists()


def test_setup_logging_resets_handlers():
    """Test that logging setup resets existing handlers."""
    # Setup logger once
    logger1 = setup_logging()
    handlers_count_1 = len(logger1.handlers)
    
    # Setup same logger again
    logger2 = setup_logging()
    handlers_count_2 = len(logger2.handlers)
    
    # Should have same number of handlers, not doubled
    assert handlers_count_1 == handlers_count_2
    
    # Should be the same logger instance
    assert logger1 is logger2
