import sys
from pathlib import Path

day_02_dir = Path().parent / 'day_02'
sys.path.append(str(day_02_dir.absolute()))

from day_02 import part_1
from day_02 import part_2
from day_02 import read_input


def test_day_02():
    example = read_input(day_02_dir, 'example.txt')
    data = read_input(day_02_dir, 'input.txt')
    assert part_1(example) == 15
    assert part_1(data) == 13682
    assert part_2(example) == 12
    assert part_2(data) == 12881
