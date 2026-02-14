"""Logger utility for tracking production progress."""

import logging
import sys
from pathlib import Path

def setup_logger(name: str = "producer") -> logging.Logger:
    """
    Configure a logger for multimedia production.

    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)

    # Ensure we don't add multiple handlers
    if logger.handlers:
        return logger

    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # File handler
    log_dir = Path("output/logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    file_handler = logging.FileHandler(log_dir / "production.log")
    file_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    # Configure levels
    logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    console_handler.setLevel(logging.INFO)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


logger = setup_logger()
