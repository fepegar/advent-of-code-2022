from aoc import day_01
from aoc.day_01 import part_1
from aoc.day_01 import part_2
from aoc.day_01 import read_input


def test_day_01():
    day_01_path = day_01.__file__
    example = read_input(day_01_path, 'example.txt')
    data = read_input(day_01_path, 'input.txt')
    assert part_1(example) == 24000
    assert part_1(data) == 72602
    assert part_2(example) == 45000
    assert part_2(data) == 160912
