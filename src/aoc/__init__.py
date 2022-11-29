
import logging
from pathlib import Path


format = '%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s'


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(format)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


def read_input(caller_path: str, relative_filepath: str) -> str:
    path = Path(caller_path).parent / relative_filepath
    return path.read_text()
