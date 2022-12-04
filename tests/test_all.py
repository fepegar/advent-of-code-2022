import importlib
from pathlib import Path

import pytest
import yaml

from aoc22 import read_input


with open(Path(__file__).parent / 'fixtures.yml', encoding='utf-8') as f:
    modules_and_fixtures = yaml.load(f, Loader=yaml.FullLoader)
modules_and_fixtures = [tuple(fixtures) for fixtures in modules_and_fixtures]


@pytest.mark.parametrize(
    'day_module_name,example_1,part_1,example_2,part_2',
    modules_and_fixtures,
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
