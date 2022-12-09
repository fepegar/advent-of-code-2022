# mypy: allow-untyped-decorators

import importlib

import typer

from aoc22 import main
from aoc22 import get_logger


_logger = get_logger(__name__)
app = typer.Typer()


@app.command()
def run_day(
    day: int = typer.Argument(  # noqa: B008
        ...,
        help='Day between 1 and 25.',
    ),
    examples_only: bool = typer.Option(  # noqa: B008
        False,
        '-e',
        help='Run examples only.',
    ),
    one_only: bool = typer.Option(  # noqa: B008
        False,
        '-1',
        help='Run part 1 only.',
    ),
    two_only: bool = typer.Option(  # noqa: B008
        False,
        '-2',
        help='Run part 2 only.',
    ),
) -> None:
    """Run code for a specific day."""
    day_module_name = f'day_{day:02d}'
    day_module = importlib.import_module(f'aoc22.{day_module_name}')
    day_path = day_module.__file__
    assert isinstance(day_path, str)

    solve_part_1 = None if two_only else day_module.part_1
    solve_part_2 = None if one_only else day_module.part_2

    main(
        day_path,
        solve_part_1,
        solve_part_2,
        _logger,
        examples_only=examples_only,
    )
