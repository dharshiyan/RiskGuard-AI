import logging
from pathlib import Path

from src.infrastructure.config import ConfigManager

_config = ConfigManager()

_log_config = _config.logging["logging"]


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(_log_config["level"])

    formatter = logging.Formatter(_log_config["format"])

    # Console Handler
    if _log_config["console"]["enabled"]:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    # File Handler
    if _log_config["file"]["enabled"]:
        log_directory = Path(_log_config["file"]["directory"])
        log_directory.mkdir(parents=True, exist_ok=True)

        file_handler = logging.FileHandler(
            log_directory / _log_config["file"]["filename"],
            encoding="utf-8",
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    logger.propagate = False

    return logger