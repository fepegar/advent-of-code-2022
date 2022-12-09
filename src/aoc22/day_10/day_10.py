from aoc22 import get_logger
from aoc22 import main


_logger = get_logger(__name__)
DELAY = 2


class Instruction:
    def __init__(self, duration: int, x: int):
        self.duration = duration
        self.x = x
        self.cycle = 0

    def run(self):
        self.cycle += 1
        if self.cycle == self.duration:
            return self.x
        else:
            return 0


class NoOp(Instruction):
    def __init__(self):
        super().__init__(1, 0)


class AddX(Instruction):
    def __init__(self, x: int):
        super().__init__(2, x)


class Register:
    def __init__(self, name: str):
        self.name = name
        self.value = 1
        self.cycle = 1
        self.instructions: list[str] = []
        self.schedule: dict[int, int] = {}

    def __repr__(self):
        string = (
            f'Cycle = {self.cycle:3}'
            f' | {self.name} = {self.value:2}'
            f' | signal strength = {self.signal_strength:4}'
        )
        return string

    @property
    def signal_strength(self):
        return self.value * self.cycle

    def run(self, instruction: str | None = None) -> None:
        self.cycle += 1
        if instruction is not None:
            match instruction.split():
                case ['noop']:
                    pass
                case ['addx', n]:  # pylint: disable=invalid-name
                    self.schedule[self.cycle + 1] = int(n)
        scheduled = self.schedule.get(self.cycle, 0)
        self.value += scheduled


def part_1_(data: str) -> int:
    register = Register('X')
    print(register)
    for instruction in data.splitlines():
        register.run(instruction)
        print(register)
    for _ in range(DELAY):
        register.run()
        print(register)
    return register.signal_strength


def part_1(data: str) -> int:
    register = Register('X')
    values = []
    next_cycle = 20
    for instruction in data.splitlines():
        # print(f'{instruction:8}')
        match instruction.split():
            case ['noop']:
                register.cycle += 1
                # print(register)
                if register.cycle == next_cycle:
                    values.append(register.signal_strength)
                    next_cycle += 40
            case ['addx', n]:  # pylint: disable=invalid-name
                register.cycle += 1
                if register.cycle == next_cycle:
                    values.append(register.signal_strength)
                    next_cycle += 40
                # print(register)
                register.value += int(n)
                register.cycle += 1
                if register.cycle == next_cycle:
                    values.append(register.signal_strength)
                    next_cycle += 40
                # print(register)

    return sum(values)


def part_2(data: str) -> int:
    result = int(data)
    return result


if __name__ == '__main__':
    main(__file__, part_1, part_2, _logger)
