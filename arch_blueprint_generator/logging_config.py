"""
Logging configuration for the blueprint generator.
"""

import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional


def setup_logging(
    level: int = logging.INFO,
    log_file: Optional[str] = None,
    log_format: Optional[str] = None
) -> logging.Logger:
    """Set up logging for the blueprint generator.
    
    Args:
        level: Logging level
        log_file: Path to log file, or None for console only
        log_format: Custom log format string, or None for default
        
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger("architectum.blueprint_generator")
    logger.setLevel(level)
    
    # Clear any existing handlers to avoid duplicate logs
    if logger.handlers:
        logger.handlers.clear()
    
    # Default format
    if log_format is None:
        log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    formatter = logging.Formatter(log_format)
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler (if specified)
    if log_file:
        log_path = Path(log_file)
        
        # Create log directory if it doesn't exist
        if not log_path.parent.exists():
            os.makedirs(log_path.parent, exist_ok=True)
        
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    logger.debug(f"Logging initialized at level {logging.getLevelName(level)}")
    return logger


# Default logger
logger = setup_logging()
