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
        print(' ' * indent, '-', self)  # noqa: T201


class Folder(File):
    def __init__(self, path: Path, parent: Folder | None = None):
        super().__init__(path, 0, parent=parent)

    def __repr__(self) -> str:
        return f'{self.name} (dir)'

    @property
    def size(self):
        sizes = {file.name: file.size for file in self.files.values()}
        return sum(sizes.values())

    def fill_size(self, sizes: dict[Path, int]):
        if self.name in sizes:
            raise ValueError(f'Folder {self.name} already in sizes')
        sizes[self.path] = self.size
        for file in self.files.values():
            if isinstance(file, Folder):
                file.fill_size(sizes)

    def print_tree(self, indent: int = 0):
        self.print_for_tree(indent)
        for file in self.files.values():
            if isinstance(file, Folder):
                file.print_tree(indent + 2)
            else:
                file.print_for_tree(indent + 2)


class Reader:
    def __init__(self, data: str):
        self._lines = data.splitlines()
        self._current_path = Path('/')
        self._current_folder = Folder(self._current_path)
        self.root = self._current_folder

    def cd(self, target_folder_name: str) -> None:  # noqa: A003
        if target_folder_name == '..':
            assert self._current_folder.parent is not None
            self._current_folder = self._current_folder.parent
            self._current_path = self._current_path.parent
        else:
            folder = self._current_folder.files[target_folder_name]
            assert isinstance(folder, Folder)
            self._current_folder = folder
            self._current_path = self._current_path / target_folder_name

    def add_folder(self, name: str) -> None:
        if name not in self._current_folder.files:
            new_path = self._current_path / name
            new_folder = Folder(new_path, parent=self._current_folder)
            self._current_folder.files[name] = new_folder

    def add_file(self, name: str, size: int) -> None:
        if name not in self._current_folder.files:
            self._current_folder.files[name] = File(name, size, self._current_folder)

    def process_line(self, line: str) -> None:
        match line.split():
            case ['$', 'cd', target_folder_name]:
                self.cd(target_folder_name)
            case ['$', 'ls']:
                pass
            case ['dir', name]:
                self.add_folder(name)
            case [size_str, name]:
                self.add_file(name, int(size_str))
            case _:
                raise ValueError(f'Unknown line: {line}')

    def make_tree(self) -> Folder:
        for line in self._lines[1:]:
            self.process_line(line)
        return self.root


def part_1(data: str) -> int:
    root = Reader(data).make_tree()
    sizes: dict[Path, int] = {}
    root.fill_size(sizes)
    return sum(size for size in sizes.values() if size <= 100_000)


def part_2(data: str) -> int:
    total = 70_000_000
    need = 30_000_000
    root = Reader(data).make_tree()
    sizes: dict[Path, int] = {}
    root.fill_size(sizes)
    used = root.size
    available = total - used
    candidates = []
    for size in sizes.values():
        would_have = available + size
        if would_have >= need:
            candidates.append(size)
    return min(candidates)


if __name__ == '__main__':
    main(__file__, part_1, part_2, _logger)
