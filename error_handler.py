import logging

logger = logging.getLogger(__name__)

def handle_error(e: Exception) -> None:
    """
    Handles unexpected exceptions and logs errors.
    """
    logger.error(f"An unexpected error occurred: {e}", exc_info=True)
