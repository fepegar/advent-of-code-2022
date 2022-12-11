from string import ascii_letters

from aoc22 import get_logger


logger = get_logger(__name__)


def get_shared_item(line: str) -> str:
    half = len(line) // 2
    first, second = line[:half], line[half:]
    intersection = set(first).intersection(set(second))
    assert len(intersection) == 1
    return intersection.pop()


def get_priority(char: str) -> int:
    return ascii_letters.index(char) + 1


def part_1(data: str) -> int:
    rucksacks = data.splitlines()
    shared_items = (get_shared_item(rucksack) for rucksack in rucksacks)
    score = sum(get_priority(item) for item in shared_items)
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
