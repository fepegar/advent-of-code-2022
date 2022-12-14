import numpy as np
import numpy.typing as npt

from aoc22 import get_logger


_logger = get_logger(__name__)
TypeForest = npt.NDArray[np.uint8]


def read_forest(data: str) -> TypeForest:
    result = np.array([list(line) for line in data.splitlines()]).astype(np.uint8)
    return result


def look_left(forest: TypeForest, row: int, col: int) -> bool:
    if col == 0:
        return True
    return bool(np.all(forest[row, :col] < forest[row, col]))


def look_right(forest: TypeForest, row: int, col: int) -> bool:
    if col == forest.shape[1] - 1:
        return True
    return bool(np.all(forest[row, col + 1 :] < forest[row, col]))


def look_up(forest: TypeForest, row: int, col: int) -> bool:
    if row == 0:
        return True
    return bool(np.all(forest[:row, col] < forest[row, col]))


def look_down(forest: TypeForest, row: int, col: int) -> bool:
    if row == forest.shape[0] - 1:
        return True
    return bool(np.all(forest[row + 1 :, col] < forest[row, col]))


def scenic_up(forest: TypeForest, row: int, col: int) -> int:
    result = 0
    rows = range(row)
    for other_row in reversed(rows):
        result += 1
        if forest[other_row, col] >= forest[row, col]:
            break
    return result


def scenic_down(forest: TypeForest, row: int, col: int) -> int:
    result = 0
    rows = range(row + 1, forest.shape[0])
    for other_row in rows:
        result += 1
        if forest[other_row, col] >= forest[row, col]:
            break
    return result


def scenic_left(forest: TypeForest, row: int, col: int) -> int:
    result = 0
    cols = range(col)
    for other_col in reversed(cols):
        result += 1
        if forest[row, other_col] >= forest[row, col]:
            break
    return result


def scenic_right(forest: TypeForest, row: int, col: int) -> int:
    result = 0
    cols = range(col + 1, forest.shape[1])
    for other_col in cols:
        result += 1
        if forest[row, other_col] >= forest[row, col]:
            break
    return result


def part_1(data: str) -> int:
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
        string = (
            f'{forest[row, col]} at ({row}, {col})'
            f' is{"" if visible else " not"} visible'
        )
        _logger.debug(string)
    return result


def part_2(data: str) -> int:
    forest = read_forest(data)
    scores: list[int] = []
    for row, col in np.ndindex(forest.shape):
        score = (
            scenic_up(forest, row, col)
            * scenic_down(forest, row, col)
            * scenic_left(forest, row, col)
            * scenic_right(forest, row, col)
        )
        scores.append(score)
    return max(scores)
