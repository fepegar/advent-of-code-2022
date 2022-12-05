from collections import defaultdict
import re

from aoc22 import get_logger
from aoc22 import main


_logger = get_logger(__name__)
TypeStacks = dict[int, list[str]]


class Crane:
    def __init__(self, data: str):
        self.stacks = self._read_stacks(data)
        self.movements = self._read_movements(data)

    def _read_stacks(self, data: str) -> TypeStacks:
        stacks: TypeStacks = defaultdict(list)
        for line in data.splitlines():
            if '1' in line:
                break
            indices = [i for i, char in enumerate(line) if char == '[']
            indices_stacks = [i // 4 + 1 for i in indices]
            letters = [line[i + 1] for i in indices]
            for i, letter in zip(indices_stacks, letters):
                stacks[i].insert(0, letter)
        return stacks

    def _read_movements(self, data: str) -> list[tuple[int, int, int]]:
        movements = re.findall(r'move (\d+) from (\d) to (\d)', data)
        return movements

    def run(self, *, model: int) -> str:
        for movement in self.movements:
            num_crates, src_idx, dst_idx = (int(n) for n in movement)
            src = self.stacks[src_idx]
            dst = self.stacks[dst_idx]
            match model:
                case 9000:
                    for _ in range(num_crates):
                        dst.append(src.pop())
                case 9001:
                    dst.extend(src[-num_crates:])
                    src[-num_crates:] = []
        tops = [self.stacks[i][-1] for i in sorted(self.stacks)]
        return ''.join(tops)


def part_1(data: str) -> str:
    crane = Crane(data)
    return crane.run(model=9000)


def part_2(data: str) -> str:
    crane = Crane(data)
    return crane.run(model=9001)


if __name__ == '__main__':
    main(__file__, part_1, part_2, _logger)
