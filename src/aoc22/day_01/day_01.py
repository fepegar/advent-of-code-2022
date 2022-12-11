from aoc22 import get_logger


logger = get_logger(__name__)


def get_totals(data: str) -> list[int]:
    elves = []
    all_calories: list[int] = []
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
