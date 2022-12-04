import importlib

import pytest

from aoc22 import read_input


@pytest.mark.parametrize(
    'day_module_name,example_1,part_1,example_2,part_2',
    [
        ('day_01', 24000, 72602, 45000, 160912),
        ('day_02', 15, 13682, 12, 12881),
        ('day_03', 157, 7845, 70, 2790),
        ('day_04', 2, 540, 4, 872),
    ],
)
def test_day(
    day_module_name: str,
    example_1: int,
    part_1: int,
    example_2: int,
    part_2: int,
):
    day_module = importlib.import_module(f'aoc22.{day_module_name}')
    day_path = day_module.__file__
    example = read_input(day_path, 'example.txt')
    data = read_input(day_path, 'input.txt')
    assert day_module.part_1(example) == example_1
    assert day_module.part_1(data) == part_1
    assert day_module.part_2(example) == example_2
    assert day_module.part_2(data) == part_2
