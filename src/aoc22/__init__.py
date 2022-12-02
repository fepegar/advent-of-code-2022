import logging
from pathlib import Path


logger_format = (
    '%(asctime)s'
    ' - %(filename)s'
    ':%(lineno)d'
    ' - %(levelname)s'
    ' - %(message)s'
)


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(logger_format)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


logger = get_logger(__name__)


def read_input(caller_path: str | Path, relative_filepath: str) -> str:
    if (path := Path(caller_path)).is_dir():
        directory = path
    else:
        directory = path.parent
    data_path = directory / relative_filepath
    text = data_path.read_text()
    if not text:
        logger.warning('No input found in %s', path)
    return text
