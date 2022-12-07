from __future__ import annotations

import abc
import enum

from aoc22 import get_logger
from aoc22 import main


logger = get_logger(__name__)


@enum.unique
class Outcome(str, enum.Enum):
    WIN = 'WIN'
    DRAW = 'DRAW'
    LOSE = 'LOSE'


class Code(str, enum.Enum):
    LOSE = 'X'
    DRAW = 'Y'
    WIN = 'Z'
    ROCK = 'X'
    PAPER = 'Y'
    SCISSORS = 'Z'


class Shape(abc.ABC):
    ROCK = 'ROCK'
    PAPER = 'PAPER'
    SCISSORS = 'SCISSORS'

    weaker_class: type[Shape]
    stronger_class: type[Shape]
    score: int

    outcome_scores = {
        Outcome.WIN: 6,
        Outcome.DRAW: 3,
        Outcome.LOSE: 0,
    }

    def fight(self, other: Shape) -> int:
        match other:
            case self.weaker_class():
                score = self.outcome_scores[Outcome.WIN]
            case self.stronger_class():
                score = self.outcome_scores[Outcome.LOSE]
            case self.__class__():
                score = self.outcome_scores[Outcome.DRAW]
        return score

    @classmethod
    def from_their_code(cls, code: str) -> Shape:
        shape: Shape
        match code:
            case 'A':
                shape = Rock()
            case 'B':
                shape = Paper()
            case 'C':
                shape = Scissors()
        return shape

    @classmethod
    def from_my_code(cls, code: str) -> Shape:
        shape: Shape
        match code:
            case Code.ROCK:
                shape = Rock()
            case Code.PAPER:
                shape = Paper()
            case Code.SCISSORS:
                shape = Scissors()
        return shape

    @classmethod
    def from_their_shape_and_my_code(cls, their_shape: Shape, my_code: str) -> Shape:
        shape: Shape
        match my_code:
            case Code.LOSE:
                shape = their_shape.weaker_class()
            case Code.DRAW:
                shape = their_shape
            case Code.WIN:
                shape = their_shape.stronger_class()
        return shape


class Rock(Shape):
    def __init__(self) -> None:
        self.weaker_class = Scissors
        self.stronger_class = Paper
        self.score = 1


class Paper(Shape):
    def __init__(self) -> None:
        self.weaker_class = Rock
        self.stronger_class = Scissors
        self.score = 2


class Scissors(Shape):
    def __init__(self) -> None:
        self.weaker_class = Paper
        self.stronger_class = Rock
        self.score = 3


def get_shapes_guess(their_code: str, my_code: str) -> tuple[Shape, Shape]:
    their_shape = Shape.from_their_code(their_code)
    my_shape = Shape.from_my_code(my_code)
    return their_shape, my_shape


def get_shapes_real(their_code: str, my_code: str) -> tuple[Shape, Shape]:
    their_shape = Shape.from_their_code(their_code)
    my_shape = Shape.from_their_shape_and_my_code(their_shape, my_code)
    return their_shape, my_shape


def play_game_guess(game: str) -> int:
    their_code, my_code = game.split()
    their_shape, my_shape = get_shapes_guess(their_code, my_code)
    score = my_shape.score + my_shape.fight(their_shape)
    return score


def play_game_real(game: str) -> int:
    their_code, my_code = game.split()
    their_shape, my_shape = get_shapes_real(their_code, my_code)
    score = my_shape.score + my_shape.fight(their_shape)
    return score


def part_1(data: str) -> int:
    games = data.splitlines()
    score = sum(play_game_guess(game) for game in games)
    return score


def part_2(data: str) -> int:
    games = data.splitlines()
    score = sum(play_game_real(game) for game in games)
    return score


if __name__ == '__main__':
    main(__file__, part_1, part_2, logger)
