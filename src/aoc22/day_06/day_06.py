from collections import deque

from aoc22 import get_logger
from aoc22 import main


_logger = get_logger(__name__)


def find_set(data: str, offset: int) -> int:
    signal = deque(data)
    i = offset
    while True:
        start = list(signal)[:offset]
        if len(set(start[:offset])) == offset:
            break
        signal.rotate(-1)
        i += 1
    return i


def part_1(data: str) -> int:
    return find_set(data, 4)


def part_2(data: str) -> int:
    return find_set(data, 14)


if __name__ == '__main__':
    main(__file__, part_1, part_2, _logger)
