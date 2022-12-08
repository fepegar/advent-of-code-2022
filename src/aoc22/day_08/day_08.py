import numpy as np

from aoc22 import get_logger
from aoc22 import main


_logger = get_logger(__name__)


def read_forest(data: str) -> np.ndarray:
    result = np.array([list(line) for line in data.splitlines()]).astype(np.uint8)
    return result


def look_left(forest, row, col):
    if col == 0:
        return True
    return np.all(forest[row, :col] < forest[row, col])


def look_right(forest, row, col):
    if col == forest.shape[1] - 1:
        return True
    return np.all(forest[row, col + 1 :] < forest[row, col])


def look_up(forest, row, col):
    if row == 0:
        return True
    return np.all(forest[:row, col] < forest[row, col])


def look_down(forest, row, col):
    if row == forest.shape[0] - 1:
        return True
    return np.all(forest[row + 1 :, col] < forest[row, col])


def scenic_up(forest, row, col):
    result = 0
    rows = range(row)
    for other_row in reversed(rows):
        result += 1
        if forest[other_row, col] >= forest[row, col]:
            break
    return result


def scenic_down(forest, row, col):
    result = 0
    rows = range(row + 1, forest.shape[0])
    for other_row in rows:
        result += 1
        if forest[other_row, col] >= forest[row, col]:
            break
    return result


def scenic_left(forest, row, col):
    result = 0
    cols = range(col)
    for other_col in reversed(cols):
        result += 1
        if forest[row, other_col] >= forest[row, col]:
            break
    return result


def scenic_right(forest, row, col):
    result = 0
    cols = range(col + 1, forest.shape[1])
    for other_col in cols:
        result += 1
        if forest[row, other_col] >= forest[row, col]:
            break
    return result


def part_1(data):
    forest = read_forest(data)
    result = 0
    for row, col in np.ndindex(forest.shape):
        visible = (
            look_up(forest, row, col)
            or look_down(forest, row, col)
            or look_left(forest, row, col)
            or look_right(forest, row, col)
        )
        result += visible
        _logger.debug(f'{forest[row, col]} at ({row}, {col}) is{"" if visible else " not"} visible')
    return result


def part_2(data: str) -> int:
    forest = read_forest(data)
    scores = []
    for row, col in np.ndindex(forest.shape):
        score = (
            scenic_up(forest, row, col)
            * scenic_down(forest, row, col)
            * scenic_left(forest, row, col)
            * scenic_right(forest, row, col)
        )
        scores.append(score)
    return max(scores)


if __name__ == '__main__':
    main(__file__, part_1, part_2, _logger)
