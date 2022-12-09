from itertools import count


class Register:
    def __init__(self, name: str):
        self.name = name
        self.value = 1
        self.cycle = 1
        self.instructions: list[str] = []
        self.schedule: dict[int, int] = {}

    @property
    def signal_strength(self) -> int:
        return self.value * self.cycle


def add_value(register: Register, values: list[int], next_cycle: int) -> int:
    if register.cycle == next_cycle:
        values.append(register.signal_strength)
        next_cycle += 40
    return next_cycle


def print_sprite(sprite_position: int) -> None:
    sprite_line = 40 * ['.']
    for i in range(-1, 2):
        sprite_line[sprite_position + i] = '#'
    sprite_string = ''.join(sprite_line)
    print('Sprite position:', sprite_string)


def update(cycle: int, pixel_position: int, sprite_position: int, line: str) -> str:
    print(
        f'During cycle {cycle:2}:',
        f'CRT draws pixel in position {pixel_position}',
    )
    if abs(pixel_position - sprite_position) <= 1:
        line += '#'
    else:
        line += '.'
    print('Current CRT row:', line)
    return line


def part_1(data: str) -> int:
    register = Register('X')
    values: list[int] = []
    next_cycle = 20
    for instruction in data.splitlines():
        register.cycle += 1
        next_cycle = add_value(register, values, next_cycle)
        match instruction.split():
            case ['noop']:
                pass
            case ['addx', n]:  # pylint: disable=invalid-name
                register.value += int(n)
                register.cycle += 1
                next_cycle = add_value(register, values, next_cycle)
    return sum(values)


def part_2(data: str) -> str:
    instructions = list(reversed(data.splitlines()))
    sprite_position = 1
    working = False
    line = ''
    lines = []
    print_sprite(sprite_position)
    for cycle in count(1):
        print()
        pixel_position = cycle - 1
        if cycle > 0:
            pixel_position = pixel_position % 40
        line = update(cycle, pixel_position, sprite_position, line)

        if not working:
            try:
                instruction = instructions.pop()
            except IndexError:
                break
            print(
                f'Start cycle {cycle:3}:',
                f'begin executing {instruction}',
            )
            match instruction.split():
                case ['noop']:
                    pass
                case ['addx', n]:  # pylint: disable=invalid-name
                    working = True
        else:
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
    print('\n'.join(lines))
    return 'EZFPRAKL'  # [after looking at output]
