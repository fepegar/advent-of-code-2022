from aoc import get_logger
from aoc import read_input


logger = get_logger(__name__)


def part_1(data: str):
    result = None
    return result


def part_2(data: str):
    result = None
    return result


if __name__ == "__main__":
    example = read_input(__file__, 'example.txt')
    data = read_input(__file__, 'input.txt')

    logger.info('PART 1')

    example_1 = part_1(example)
    logger.info('Example 1: %s', example_1)

    answer_1 = part_1(data)
    logger.info('Answer 1:  %s', answer_1)

    logger.info('############################')

    logger.info('PART 2')

    example_2 = part_2(example)
    logger.info('Example 2: %s', example_2)

    answer_2 = part_2(data)
    logger.info('Answer 2:  %s', answer_2)
