from .. import get_logger
from .. import read_input


logger = get_logger(__name__)


def get_totals(data):
    elves = []
    all_calories = []
    for line in data.splitlines():
        if not line:
            elves.append(all_calories)
            all_calories = []
        else:
            all_calories.append(int(line))
    elves.append(all_calories)
    totals = [sum(all_calories) for all_calories in elves]
    logger.debug(totals)
    return totals


def part_1(data: str) -> int:
    totals = get_totals(data)
    return max(totals)


def part_2(data: str) -> int:
    totals = get_totals(data)
    top = totals[-3:]
    return sum(top)


if __name__ == '__main__':
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
