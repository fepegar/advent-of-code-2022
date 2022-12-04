import re

from aoc22 import get_logger
from aoc22 import main


_logger = get_logger(__name__)


def get_set(first: str, last: str) -> set[int]:
    return set(range(int(first), int(last) + 1))


def get_sets(pair: str) -> tuple[set[int], set[int]]:
    a_ini, a_fin, b_ini, b_fin = re.findall(r'(\d+)-(\d+),(\d+)-(\d+)', pair)[0]
    set_a = get_set(a_ini, a_fin)
    set_b = get_set(b_ini, b_fin)
    return set_a, set_b


def get_intersections_count(data: str, contained: bool) -> int:
    pairs = data.splitlines()
    result = 0
    for pair in pairs:
        set_a, set_b = get_sets(pair)
        intersection = set_a.intersection(set_b)
        if contained and intersection in (set_a, set_b):
            result += 1
        elif not contained and intersection:
            result += 1
    return result


def part_1(data: str) -> int:
    return get_intersections_count(data, True)


def part_2(data: str) -> int:
    return get_intersections_count(data, False)


if __name__ == '__main__':
    main(__file__, part_1, part_2, _logger)
