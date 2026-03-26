import logging
import sys
from pythonjsonlogger import jsonlogger


def setup_json_logging():
    formatter = jsonlogger.JsonFormatter(
        '%(asctime)s %(levelname)s %(message)s',
        rename_fields={"asctime": "timestamp", "levelname": "level"}
    )

    logHandler = logging.StreamHandler(sys.stdout)
    logHandler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.handlers = [logHandler]


    for logger_name in ("uvicorn", "uvicorn.access", "uvicorn.error", "fastapi", "alembic.runtime.migration"):
        logger = logging.getLogger(logger_name)
        logger.handlers = [logHandler]
        logger.propagate = False

    return logging.getLogger(__name__)

logger = setup_json_logging()