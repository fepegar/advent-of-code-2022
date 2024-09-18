import logging
import os
from pathlib import Path
from collections.abc import Callable

from colorama import Fore
from colorama import Style
import coloredlogs


LOGGER_FORMAT = '%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s'
TypeResult = int | str | None


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    level_string = os.environ.get('AOC_LOGLEVEL')
    if level_string is not None:
        level = getattr(logging, level_string)
    coloredlogs.install(logger=logger, fmt=LOGGER_FORMAT, level=level)
    return logger


def read_input(caller_path: str | Path, relative_filepath: str) -> str:
    directory = Path(caller_path).parent
    data_path = directory / relative_filepath
    text = data_path.read_text()
    return text


def main(
    file_path: str,
    solve_part_1: None | Callable[[str], TypeResult],
    solve_part_2: None | Callable[[str], TypeResult],
    logger: logging.Logger,
    examples_only: bool = False,
    skip_examples: bool = False,
) -> tuple[TypeResult, TypeResult, TypeResult, TypeResult]:
    example = read_input(file_path, 'example.txt')
    data = read_input(file_path, 'input.txt')

    example_1 = answer_1 = example_2 = answer_2 = None

    if solve_part_1 is not None:
        string = f'{Style.BRIGHT}{Fore.YELLOW}PART 1{Style.RESET_ALL}'
        logger.info(string)
        if not skip_examples:
            example_1 = solve_part_1(example)
            logger.info('Example: %s', f'{Fore.YELLOW}{example_1}')
        if not examples_only:
            answer_1 = solve_part_1(data)
            string = f'{Style.BRIGHT}{Fore.YELLOW}{answer_1}{Style.RESET_ALL}'
            logger.info('Answer:  %s', string)

    if solve_part_1 is not None and solve_part_2 is not None:
        logger.info('')

    if solve_part_2 is not None:
        string = f'{Style.BRIGHT}{Fore.CYAN}PART 2{Style.RESET_ALL}'
        logger.info(string)
        if not skip_examples:
            example_2 = solve_part_2(example)
            logger.info('Example: %s', f'{Fore.CYAN}{example_2}')
        if not examples_only:
            answer_2 = solve_part_2(data)
            string = f'{Style.BRIGHT}{Fore.CYAN}{answer_2}{Style.RESET_ALL}'
            logger.info('Answer:  %s', string)

    return example_1, answer_1, example_2, answer_2
