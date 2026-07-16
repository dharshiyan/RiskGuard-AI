from src.infrastructure.logging import get_logger

logger = get_logger(__name__)

logger.info("Configuration loaded successfully.")
logger.warning("Sample warning message.")
logger.error("Sample error message.")