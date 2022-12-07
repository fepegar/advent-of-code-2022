import importlib
from pathlib import Path

import pytest
import yaml

from aoc22 import main
from aoc22 import get_logger
from aoc22 import TypeResult


_logger = get_logger(__name__)
TypeFixture = tuple[str, TypeResult, TypeResult, TypeResult, TypeResult]


def get_modules_and_fixtures() -> list[TypeFixture]:
    modules_and_fixtures: list[list[TypeResult]]
    with open(Path(__file__).parent / 'fixtures.yml', encoding='utf-8') as f:
        modules_and_fixtures = yaml.load(f, Loader=yaml.FullLoader)
    result = [tuple(fixtures) for fixtures in modules_and_fixtures]
    return result  # type: ignore[return-value]


@pytest.mark.parametrize(
    'day_module_name,example_1,part_1,example_2,part_2',
    get_modules_and_fixtures(),
)
def test_day(
    day_module_name: str,
    example_1: int,
    part_1: int,
    example_2: int,
    part_2: int,
) -> None:
    day_module = importlib.import_module(f'aoc22.{day_module_name}')
    day_path = day_module.__file__
    assert isinstance(day_path, str)
    answer_example_1, answer_1, answer_example_2, answer_2 = main(
        day_path,
        day_module.part_1,
        day_module.part_2,
        _logger,
    )
    assert answer_example_1 == example_1
    assert answer_1 == part_1
    assert answer_example_2 == example_2
    assert answer_2 == part_2
