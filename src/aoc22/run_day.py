import importlib

import typer

from aoc22 import main
from aoc22 import get_logger


_logger = get_logger(__name__)
app = typer.Typer()


@app.command()  # type: ignore[misc]
def run_day(day: int) -> None:
    """Run code for a specific day.

    Args:
        day: Day between 1 and 25.
    """
    day_module_name = f'day_{day:02d}'
    day_module = importlib.import_module(f'aoc22.{day_module_name}')
    day_path = day_module.__file__
    assert isinstance(day_path, str)

    main(day_path, day_module.part_1, day_module.part_2, _logger)
