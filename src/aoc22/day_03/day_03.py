from string import ascii_letters

from tqdm.auto import tqdm

from aoc22 import get_logger
from aoc22 import read_input


logger = get_logger(__name__)


def get_shared_item(line: str) -> str:
    half = len(line) // 2
    first, second = line[:half], line[half:]
    intersection = set(first).intersection(set(second))
    assert len(intersection) == 1
    return intersection.pop()


def get_priority(char):
    return ascii_letters.index(char) + 1


def part_1(data: str) -> int:
    rucksacks = data.splitlines()
    shared_items = (get_shared_item(rucksack) for rucksack in tqdm(rucksacks))
    score = sum(get_priority(item) for item in tqdm(shared_items))
    return score


def part_2(data: str) -> int:
    rucksacks = data.splitlines()
    priorities = []
    for i in range(0, len(rucksacks), 3):
        sets = [set(rucksack) for rucksack in rucksacks[i : i + 3]]
        shared_items = set.intersection(*sets)
        assert len(shared_items) == 1
        priority = get_priority(shared_items.pop())
        priorities.append(priority)
    return sum(priorities)


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
