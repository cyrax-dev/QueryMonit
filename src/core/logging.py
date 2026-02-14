import logging


def setup_logger() -> logging.Logger:
    """Set up the logger with the specified log level and formatter."""
    logger = logging.getLogger("QueryMonit")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    formatter = logging.Formatter(
        "[%(asctime)s] %(module)5s:%(lineno)-3d (%(levelname)-4s) - %(message)s",
        datefmt="%Y-%m-%d / %H:%M:%S",
    )

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger


log = setup_logger()
