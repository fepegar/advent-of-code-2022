from aoc22 import day_02
from aoc22.day_02 import part_1
from aoc22.day_02 import part_2
from aoc22.day_02 import read_input


def test_day_02():
    day_02_path = day_02.__file__
    example = read_input(day_02_path, 'example.txt')
    data = read_input(day_02_path, 'input.txt')
    assert part_1(example) == 15
    assert part_1(data) == 13682
    assert part_2(example) == 12
    assert part_2(data) == 12881
