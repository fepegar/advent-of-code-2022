import sys
from pathlib import Path

day_01_dir = Path().parent / 'day_01'
sys.path.append(str(day_01_dir.absolute()))

from day_01 import part_1
from day_01 import part_2
from day_01 import read_input


def test_day_01():
    example = read_input(day_01_dir, 'example.txt')
    data = read_input(day_01_dir, 'input.txt')
    assert part_1(example) == 24000
    assert part_1(data) == 72602
    assert part_2(example) == 45000
    assert part_2(data) == 160912
