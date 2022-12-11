from collections import deque


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
