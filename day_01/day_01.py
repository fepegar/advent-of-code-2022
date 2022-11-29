from pathlib import Path


this_dir = Path(__file__).parent
verbose = True

def p(*args):
    if verbose:
        print(*args)


def read_input(relative_filepath):
    filepath = this_dir / relative_filepath
    return filepath.read_text()


def part_1(data):
    elves = []
    all_calories = []
    for line in data.splitlines():
        if not line:
            elves.append(all_calories)
            all_calories = []
        else:
            all_calories.append(int(line))
    elves.append(all_calories)
    totals = [sum(all_calories) for all_calories in elves]
    return max(totals)


def part_2(data):
    elves = []
    all_calories = []
    for line in data.splitlines():
        if not line:
            elves.append(all_calories)
            all_calories = []
        else:
            all_calories.append(int(line))
    elves.append(all_calories)
    print(elves)
    totals = sorted(sum(all_calories) for all_calories in elves)
    print(totals)
    top = totals[-3:]
    print(top)
    return sum(top)


if __name__ == "__main__":
    example = read_input('example.txt')
    data = read_input('input.txt')
    p('Part 1')
    example_1 = part_1(example)
    p('Example 1:', example_1)
    answer_1 = part_1(data)
    p('Answer 1:', answer_1)
    p()
    p('Part 2')
    example_2 = part_2(example)
    p('Example 2:', example_2)
    answer_2 = part_2(data)
    p('Answer 2:', answer_2)
