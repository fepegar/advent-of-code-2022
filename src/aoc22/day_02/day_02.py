import enum

from tqdm.auto import tqdm

from aoc22 import get_logger
from aoc22 import read_input


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


class Shape:
    ROCK = 'ROCK'
    PAPER = 'PAPER'
    SCISSORS = 'SCISSORS'

    outcome_scores = {
        Outcome.WIN: 6,
        Outcome.DRAW: 3,
        Outcome.LOSE: 0,
    }

    def fight(self, other):
        match other:
            case self.weaker_class():
                return self.outcome_scores[Outcome.WIN]
            case self.stronger_class():
                return self.outcome_scores[Outcome.LOSE]
            case self.__class__():
                return self.outcome_scores[Outcome.DRAW]

    @classmethod
    def from_their_code(cls, code: str) -> 'Shape':
        match code:
            case 'A':
                return Rock()
            case 'B':
                return Paper()
            case 'C':
                return Scissors()

    @classmethod
    def from_my_code(cls, code: str) -> 'Shape':
        match code:
            case Code.ROCK:
                return Rock()
            case Code.PAPER:
                return Paper()
            case Code.SCISSORS:
                return Scissors()

    @classmethod
    def from_their_shape_and_my_code(
        cls,
        their_shape: 'Shape',
        my_code: str,
    ) -> 'Shape':
        match my_code:
            case Code.LOSE:
                return their_shape.weaker_class()
            case Code.DRAW:
                return their_shape
            case Code.WIN:
                return their_shape.stronger_class()


class Rock(Shape):
    def __init__(self):
        self.weaker_class = Scissors
        self.stronger_class = Paper
        self.score = 1


class Paper(Shape):
    def __init__(self):
        self.weaker_class = Rock
        self.stronger_class = Scissors
        self.score = 2


class Scissors(Shape):
    def __init__(self):
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
    score = sum(play_game_guess(game) for game in tqdm(games))
    return score


def part_2(data: str) -> int:
    games = data.splitlines()
    score = sum(play_game_real(game) for game in tqdm(games))
    return score


if __name__ == '__main__':
    example = read_input(__file__, 'example.txt')
    data = read_input(__file__, 'input.txt')

    logger.info('PART 1')

    example_1 = part_1(example)
    logger.info('Example 1: %s', example_1)

    answer_1 = part_1(data)
    logger.info('Answer 1:  %s', answer_1)

    logger.info('############################')

    logger.info('PART 2')

    example_2 = part_2(example)
    logger.info('Example 2: %s', example_2)

    answer_2 = part_2(data)
    logger.info('Answer 2:  %s', answer_2)
