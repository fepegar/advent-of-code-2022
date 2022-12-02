from .. import get_logger
from .. import read_input


logger = get_logger(__name__)


dict_opponent = {
    'A': 'ROCK',
    'B': 'PAPER',
    'C': 'SCISSORS',
}

dict_you = {
    'X': 'ROCK',
    'Y': 'PAPER',
    'Z': 'SCISSORS',
}

shapes_scores = {
    'ROCK': 1,
    'PAPER': 2,
    'SCISSORS': 3,
}


DRAW = 3
WIN = 6
LOSE = 0


def play_game(game: str):
    opponent, you = game.split()
    score = shapes_scores[dict_you[you]]
    match dict_opponent[opponent]:
        case 'ROCK':
            match dict_you[you]:
                case 'ROCK':
                    score += DRAW
                case 'PAPER':
                    score += WIN
                case 'SCISSORS':
                    score += LOSE
        case 'PAPER':
            match dict_you[you]:
                case 'ROCK':
                    score += LOSE
                case 'PAPER':
                    score += DRAW
                case 'SCISSORS':
                    score += WIN
        case 'SCISSORS':
            match dict_you[you]:
                case 'ROCK':
                    score += WIN
                case 'PAPER':
                    score += LOSE
                case 'SCISSORS':
                    score += DRAW
    return score


def play_game_2(game):
    opponent, you = game.split()
    match dict_opponent[opponent]:
        case 'ROCK':
            match you:
                case 'X':
                    score = LOSE + shapes_scores['SCISSORS']
                case 'Y':
                    score = DRAW + shapes_scores['ROCK']
                case 'Z':
                    score = WIN + shapes_scores['PAPER']
        case 'PAPER':
            match you:
                case 'X':
                    score = LOSE + shapes_scores['ROCK']
                case 'Y':
                    score = DRAW + shapes_scores['PAPER']
                case 'Z':
                    score = WIN + shapes_scores['SCISSORS']
        case 'SCISSORS':
            match you:
                case 'X':
                    score = LOSE + shapes_scores['PAPER']
                case 'Y':
                    score = DRAW + shapes_scores['SCISSORS']
                case 'Z':
                    score = WIN + shapes_scores['ROCK']
    return score


def part_1(data: str):
    games = data.splitlines()
    score = 0
    for game in games:
        score += play_game(game)
    return score


def part_2(data: str):
    games = data.splitlines()
    score = 0
    for game in games:
        score += play_game_2(game)
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
