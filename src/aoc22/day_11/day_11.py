from __future__ import annotations

import re
from math import prod

from aoc22 import get_logger


_logger = get_logger(__name__)


class Monkey:
    def __init__(self, lines: list[str]):
        self.process_lines(lines)
        self.num_inspected = 0
        self.items: list[int] = []

    def process_lines(self, lines: list[str]) -> None:
        self.index = int(lines[0][-2])
        self.items = [int(n) for n in re.findall(r'\d+', lines[1])]
        self.operation = lines[2].split('=')[1].strip()
        self.test_divisible = int(lines[3].split('by')[1].strip())
        self.if_true_monkey = int(lines[4].split('monkey')[1].strip())
        self.if_false_monkey = int(lines[5].split('monkey')[1].strip())

    def add_item(self, item: int) -> None:
        self.items.append(item)

    def __repr__(self) -> str:
        lines = (
            f'Monkey {self.index}:',
            f'  Starting items: {", ".join(str(n) for n in self.items)}',
            f'  Operation: {self.operation}',
            f'  Test: divisible by {self.test_divisible}',
            f'    If true: throw to monkey {self.if_true_monkey}',
            f'    If false: throw to monkey {self.if_false_monkey}',
        )
        return '\n'.join(lines)

    def process_items(self, all_monkeys: list[Monkey], *, modulo: int) -> None:
        for old in self.items:  # pylint: disable=unused-variable  # noqa: B007
            new: int = eval(self.operation)  # pylint: disable=eval-used
            if modulo:
                new %= modulo
            else:
                new //= 3
            if new % self.test_divisible == 0:  # noqa: S001
                all_monkeys[self.if_true_monkey].add_item(new)
            else:
                all_monkeys[self.if_false_monkey].add_item(new)
            self.num_inspected += 1
        self.items = []


def read_monkeys(data: str) -> list[Monkey]:
    lines = data.splitlines()
    monkeys = []
    num_lines_monkey = 7
    assert (total := (len(lines) + 1)) % num_lines_monkey == 0
    for i in range(total // num_lines_monkey):
        ini = i * num_lines_monkey
        fin = ini + num_lines_monkey - 1
        monkey_lines = lines[ini:fin]
        monkey = Monkey(monkey_lines)
        monkeys.append(monkey)
    return monkeys


def process_monkeys(data: str, *, num_rounds: int, divide: bool = True) -> int:
    monkeys = read_monkeys(data)
    # Idea below shamefully stolen from
    # https://github.com/radosz99/aocd/blob/main/solutions/11.py
    modulo = prod(monkey.test_divisible for monkey in monkeys)
    from tqdm.auto import trange

    for round_idx in trange(1, num_rounds + 1):
        for monkey in monkeys:
            monkey.process_items(monkeys, modulo=modulo)
        if num_rounds == 20:
            _logger.debug(
                '\nAfter round %s,'
                'the monkeys are holding items with these worry levels:',
                round_idx,
            )
            for monkey in monkeys:
                _logger.debug(
                    'Monkey %s: %s',
                    monkey.index,
                    ', '.join(str(n) for n in monkey.items),
                )
        else:
            if round_idx == 1 or round_idx == 20 or round_idx % 1000 == 0:
                _logger.debug('\n== After round %s ==', round_idx)
                for monkey in monkeys:
                    _logger.debug(
                        'Monkey %s inspected items %s times.',
                        monkey.index,
                        monkey.num_inspected,
                    )

    for monkey in monkeys:
        _logger.debug(
            'Monkey %s inspected items %s times.',
            monkey.index,
            monkey.num_inspected,
        )
    all_nums_inspected = sorted(monkey.num_inspected for monkey in monkeys)
    second_most, most = all_nums_inspected[-2:]
    monkey_business = second_most * most
    return monkey_business


def part_1(data: str) -> int:
    monkey_business = process_monkeys(data, num_rounds=20, divide=True)
    return monkey_business


def part_2(data: str) -> int:
    monkey_business = process_monkeys(data, num_rounds=10000, divide=False)
    return monkey_business
