import logging
from pathlib import Path
from collections.abc import Callable

from colorama import Fore
from colorama import Style
import coloredlogs


LOGGER_FORMAT = '%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s'
TypeResult = int | str


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    coloredlogs.install(logger=logger, fmt=LOGGER_FORMAT)
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

    string = f'{Style.BRIGHT}{Fore.YELLOW}PART 1{Style.RESET_ALL}'
    logger.info(string)
    example_1 = solve_part_1(example)
    logger.info('Example: %s', f'{Fore.YELLOW}{example_1}')
    answer_1 = solve_part_1(data)
    string = f'{Style.BRIGHT}{Fore.YELLOW}{answer_1}{Style.RESET_ALL}'
    logger.info('Answer:  %s', string)

    logger.info('')

    string = f'{Style.BRIGHT}{Fore.CYAN}PART 2{Style.RESET_ALL}'
    logger.info(string)
    example_2 = solve_part_2(example)
    logger.info('Example: %s', f'{Fore.CYAN}{example_2}')
    answer_2 = solve_part_2(data)
    string = f'{Style.BRIGHT}{Fore.CYAN}{answer_2}{Style.RESET_ALL}'
    logger.info('Answer:  %s', string)

    return example_1, answer_1, example_2, answer_2
