from aoc22 import get_logger
from aoc22 import main


_logger = get_logger(__name__)


class Register:
    def __init__(self, name: str):
        self.name = name
        self.value = 1
        self.cycle = 1
        self.instructions: list[str] = []
        self.schedule: dict[int, int] = {}

    def __repr__(self) -> str:
        string = (
            f'Cycle = {self.cycle:3}'
            f' | {self.name} = {self.value:2}'
            f' | signal strength = {self.signal_strength:4}'
        )
        return string

    @property
    def signal_strength(self) -> int:
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


def step(register: Register, lines: list[str], line: str, instruction: str) -> str:
    sprite_line = 40 * ['.']
    for i in range(-1, 2):
        sprite_line[register.value + i] = '#'
    sprite_string = ''.join(sprite_line)
    print('Sprite position:', sprite_string, end='\n\n')
    if abs(register.cycle - register.value) <= 1:
        line += '#'
    else:
        line += '.'
    print('Current CRT row:', line, end='\n\n')
    if not register.cycle % 40:
        lines.append(line)
        line = ''
    print(
        f'End of cycle {register.cycle}:'
        f' finish executing {instruction}'
        f' (Register X is now {register.value})',
    )
    register.cycle += 1
    print()
    return line


def part_1(data: str) -> int:
    register = Register('X')
    values = []
    next_cycle = 20
    for instruction in data.splitlines():
        match instruction.split():
            case ['noop']:
                register.cycle += 1
                if register.cycle == next_cycle:
                    values.append(register.signal_strength)
                    next_cycle += 40
            case ['addx', n]:  # pylint: disable=invalid-name
                register.cycle += 1
                if register.cycle == next_cycle:
                    values.append(register.signal_strength)
                    next_cycle += 40
                register.value += int(n)
                register.cycle += 1
                if register.cycle == next_cycle:
                    values.append(register.signal_strength)
                    next_cycle += 40
    return sum(values)


def print_sprite(sprite_position: int) -> None:
    sprite_line = 40 * ['.']
    for i in range(-1, 2):
        sprite_line[sprite_position + i] = '#'
    sprite_string = ''.join(sprite_line)
    print('Sprite position:', sprite_string)


def part_2(data: str) -> str:
    instructions = list(reversed(data.splitlines()))
    from itertools import count

    sprite_position = 1
    working = False
    line = ''
    lines = []
    print_sprite(sprite_position)
    for cycle in count(1):
        if cycle == 39:
            pass
        print()
        pixel_position = cycle - 1
        if cycle > 0:
            pixel_position = pixel_position % 40
        if not working:
            try:
                instruction = instructions.pop()
            except IndexError:
                break
            print('Popped', instruction)
            match instruction.split():
                case ['noop']:
                    print(
                        f'Start cycle {cycle:3}:',
                        f'begin executing {instruction}',
                    )
                    print(
                        f'During cycle {cycle:2}:',
                        f'CRT draws pixel in position {pixel_position}',
                    )
                    if abs(pixel_position - sprite_position) <= 1:
                        line += '#'
                    else:
                        line += '.'
                    print('Current CRT row:', line)
                case ['addx', n]:  # pylint: disable=invalid-name
                    print(
                        f'Start cycle {cycle:3}:',
                        f'begin executing {instruction}',
                    )
                    print(
                        f'During cycle {cycle:2}:',
                        f'CRT draws pixel in position {pixel_position}',
                    )
                    if abs(pixel_position - sprite_position) <= 1:
                        line += '#'
                    else:
                        line += '.'
                    print('Current CRT row:', line)
                    working = True
        else:
            print(
                f'During cycle {cycle:2}:',
                f'CRT draws pixel in position {pixel_position}',
            )
            if abs(pixel_position - sprite_position) <= 1:
                line += '#'
            else:
                line += '.'
            print('Current CRT row:', line)
            sprite_position += int(n)
            print(
                f'End of cycle {cycle:2}:',
                f'finish executing {instruction}',
                f'(Register X is now {sprite_position})',
            )
            print_sprite(sprite_position)
            working = False
        if cycle % 40 == 0:
            lines.append(line)
            line = ''
        # if cycle == 65: break
    print('\n'.join(lines))
    return 'EZFPRAKL'  # after looking at output


if __name__ == '__main__':
    main(__file__, part_1, part_2, _logger)
