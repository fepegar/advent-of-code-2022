from __future__ import annotations

from pathlib import Path

from aoc22 import get_logger
from aoc22 import main


_logger = get_logger(__name__)


class File:
    def __init__(self, path: str | Path, size: int, parent: Folder | None = None):
        self.path = Path(path)
        self._size = size
        self.files: dict[str, File | Folder] = {}
        self.parent = parent

    def __repr__(self) -> str:
        return f'{self.name} (file, size={self.size})'

    @property
    def name(self):
        return self.path.name

    @property
    def size(self):
        return self._size

    def print_for_tree(self, indent: int) -> None:
        print(' ' * indent, '-', self)


class Folder(File):
    def __init__(self, path: Path, parent: Folder | None = None):
        super().__init__(path, 0, parent=parent)

    def __repr__(self) -> str:
        return f'{self.name} (dir)'

    @property
    def size(self):
        sizes = {file.name: file.size for file in self.files.values()}
        return sum(sizes.values())

    def fill_size(self, sizes: dict[str, int]):
        if self.name in sizes:
            raise ValueError(f'Folder {self.name} already in sizes')
        sizes[self.path] = self.size
        for file in self.files.values():
            if isinstance(file, Folder):
                file.fill_size(sizes)

    def print(self, indent: int = 0):
        self.print_for_tree(indent)
        for file in self.files.values():
            if isinstance(file, Folder):
                file.print(indent + 2)
            else:
                file.print_for_tree(indent + 2)


def make_tree(data: str) -> Folder:
    # todo: match case to parse command
    known_folders = {}
    current_path = Path('/')
    current_folder: Folder = Folder(current_path)
    root = current_folder
    known_folders[current_path] = current_folder
    for line in data.splitlines()[1:]:
        is_command = line.startswith('$')
        if is_command:
            split = line.split()
            command = split[1]
            match command:
                case 'cd':
                    target_folder_name = split[2]
                    if target_folder_name == '..':
                        assert current_folder.parent is not None
                        current_folder = current_folder.parent
                        current_path = current_path.parent
                    else:
                        current_folder = current_folder.files[target_folder_name]
                        assert isinstance(current_folder, Folder)
                        current_path = current_path / target_folder_name
                case 'ls':
                    pass
        else:
            str_a, str_b = line.split()
            if str_a == 'dir':
                name = str_b
                if name not in current_folder.files:
                    new_path = current_path / name
                    new_folder = Folder(new_path, parent=current_folder)
                    current_folder.files[name] = new_folder
            else:
                size, name = int(str_a), str_b
                if name not in current_folder.files:
                    current_folder.files[name] = File(name, size, current_folder)
    return root


def part_1(data: str):
    root = make_tree(data)
    sizes: dict[Path, int] = {}
    root.fill_size(sizes)
    return sum(size for size in sizes.values() if size <= 100_000)


def part_2(data: str):
    total = 70_000_000
    need = 30_000_000
    root = make_tree(data)
    sizes: dict[Path, int] = {}
    root.fill_size(sizes)
    used = root.size
    available = total - used
    candidates = []
    for path, size in sizes.items():
        would_have = available + size
        if would_have >= need:
            candidates.append(size)
    return min(candidates)


if __name__ == '__main__':
    main(__file__, part_1, part_2, _logger)
