import logging
from pathlib import Path
from collections.abc import Callable


LOGGER_FORMAT = '%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s'
TypeResult = int | str


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(LOGGER_FORMAT)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


_logger = get_logger(__name__)


def read_input(caller_path: str | Path, relative_filepath: str) -> str:
    directory = Path(caller_path).parent
    data_path = directory / relative_filepath
    text = data_path.read_text()
    return text


def main(
    file_path: str,
    solve_part_1: Callable[[str], TypeResult],
    solve_part_2: Callable[[str], TypeResult],
    logger: logging.Logger,
) -> tuple[TypeResult, TypeResult, TypeResult, TypeResult]:
    example = read_input(file_path, 'example.txt')
    data = read_input(file_path, 'input.txt')

    logger.info('PART 1')
    example_1 = solve_part_1(example)
    logger.info('Example 1: %s', example_1)
    answer_1 = solve_part_1(data)
    logger.info('Answer 1:  %s', answer_1)

    logger.info('############################')

    logger.info('PART 2')
    example_2 = solve_part_2(example)
    logger.info('Example 2: %s', example_2)
    answer_2 = solve_part_2(data)
    logger.info('Answer 2:  %s', answer_2)

    return example_1, answer_1, example_2, answer_2
