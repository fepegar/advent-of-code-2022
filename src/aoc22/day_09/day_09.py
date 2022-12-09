from aoc22 import get_logger
from aoc22 import main

from tqdm.auto import tqdm


_logger = get_logger(__name__)


class Knot:
    def __init__(self) -> None:
        self.x = 10  # pylint: disable=invalid-name
        self.y = 6  # pylint: disable=invalid-name


class Head(Knot):
    def move(self, direction: str) -> None:
        if direction == 'U':
            self.y += 1
        elif direction == 'D':
            self.y -= 1
        elif direction == 'R':
            self.x += 1
        elif direction == 'L':
            self.x -= 1
        else:
            raise ValueError(f'Unknown direction: {direction}')


class Tail(Knot):
    def manhattan_distance(self, head: Knot) -> int:
        return abs(self.x - head.x) + abs(self.y - head.y)

    def move(self, head: Knot) -> tuple[int, int]:
        distance = self.manhattan_distance(head)
        diff_x = head.x - self.x
        diff_y = head.y - self.y
        if distance < 2:  # adjacent perpendicularly
            pass
        elif distance == 2 and diff_x and diff_y:  # adjacent diagonally
            pass
        elif diff_x == 0 or diff_y == 0:  # move like a rook towards the head
            if diff_x > 0:
                self.x += 1
            elif diff_x < 0:
                self.x -= 1
            elif diff_y > 0:
                self.y += 1
            elif diff_y < 0:
                self.y -= 1
            else:
                raise ValueError('Should not happen')
        elif diff_x and diff_y:  # move like a bishop towards the head
            if diff_x > 0:
                self.x += 1
            elif diff_x < 0:
                self.x -= 1
            if diff_y > 0:
                self.y += 1
            elif diff_y < 0:
                self.y -= 1
        return self.x, self.y


def plot_grid(head: Head, tail: Tail, width: int, height: int) -> str:
    lines = []
    grid = [['.'] * width for _ in range(height)]
    grid[height - tail.y - 1][tail.x] = 'T'
    grid[height - head.y - 1][head.x] = 'H'
    for row in grid:
        lines.append(''.join(row))
    return '\n'.join(lines)


def plot_snake(head: Head, tails: list[Tail], width: int, height: int) -> str:
    lines = []
    grid = [['.'] * width for _ in range(height)]
    for i, tail in enumerate(reversed(tails)):
        index = len(tails) - i
        grid[height - tail.y - 1][tail.x] = str(index)
    grid[height - head.y - 1][head.x] = 'H'
    for row in grid:
        lines.append(''.join(row))
    return '\n'.join(lines)


def part_1(data: str) -> int:
    visited = []
    head = Head()
    tail = Tail()
    for move in tqdm(data.splitlines()):
        direction, length = move[0], int(move[1:])
        for _ in range(length):
            # Move H
            head.move(direction)
            # Move T
            visited.append(tail.move(head))
    return len(set(visited))


def part_2(data: str) -> int:
    visited = []
    head = Head()
    knots = [Tail() for _ in range(9)]
    previous: Head | Tail
    for move in tqdm(data.splitlines()):
        direction, length = move[0], int(move[1:])
        for _ in range(length):
            # Move H
            head.move(direction)
            # Move T
            previous = head
            for tail in knots:
                tail_position = tail.move(previous)
                previous = tail
            visited.append(tail_position)
    return len(set(visited))


if __name__ == '__main__':
    main(__file__, part_1, part_2, _logger)
