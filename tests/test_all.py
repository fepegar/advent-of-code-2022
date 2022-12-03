import pytest

from aoc22 import read_input
from aoc22 import day_01
from aoc22 import day_02
from aoc22 import day_03


@pytest.mark.parametrize(
    'day_module,example_1,part_1,example_2,part_2',
    [
        (day_01, 24000, 72602, 45000, 160912),
        (day_02, 15, 13682, 12, 12881),
        (day_03, 157, 7845, 70, 2790),
    ],
)
def test_day(day_module, example_1, part_1, example_2, part_2):
    day_path = day_module.__file__
    example = read_input(day_path, 'example.txt')
    data = read_input(day_path, 'input.txt')
    assert day_module.part_1(example) == example_1
    assert day_module.part_1(data) == part_1
    assert day_module.part_2(example) == example_2
    assert day_module.part_2(data) == part_2
