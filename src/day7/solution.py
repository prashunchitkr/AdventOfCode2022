from collections import defaultdict
from pathlib import Path
import pprint

BASE_DIR = Path(__file__).absolute().parent
TOTAL_SPACE = 70_000_000
NEEDED_SPACE = 30_000_000


def is_command(x: str): return x.startswith('$')
def is_file(x: str): return x.strip().split(' ')[0].isnumeric()
def is_subdir(x: str): return x.strip().startswith("dir")


class Directory:
    '''
    Using tree data structure
    '''

    def __init__(self, name='', parent=None, files=[], children=[]) -> None:
        self.name: str = name
        self.parent: Directory = parent
        self.files: list[dict] = files
        self.children: list[Directory] = children
        self.size = 0

    def __repr__(self) -> str:
        return self.name

    def get_size(self):
        self.size = sum([x['size'] for x in self.files]) + \
            sum([x.get_size() for x in self.children])
        return self.size


def get_arg(args: list, index: int):
    return args[index]


def parse_command(raw_text: str):
    return raw_text.strip().split(' ')[1:]


def parse_input_to_directory_index(raw_text: str):
    root = Directory(name='/', parent=None, children=[], files=[])
    current_dir = root

    for line in raw_text.splitlines():
        if is_command(line):
            cmd, *args = parse_command(line)
            match cmd:
                case 'cd':
                    target_dir = get_arg(args, 0)
                    if target_dir == '..':
                        current_dir = root if current_dir.name == '/' else current_dir.parent
                    elif target_dir == '/':
                        current_dir = root
                    else:
                        current_dir = [
                            x for x in current_dir.children if x.name == target_dir][0]
                case 'ls':
                    pass

        if (is_subdir(line)):
            subdir_name = line.strip().split(' ')[1]
            new_dir = Directory(
                name=subdir_name, parent=current_dir, children=[], files=[])
            current_dir.children.append(new_dir)

        if is_file(line):
            size, name = line.strip().split(' ')
            current_dir.files.append({
                'name': name,
                'size': int(size)
            })
    return root


def get_total_size(root: Directory, index):
    index[root] = root.get_size()
    for child in root.children:
        get_total_size(child, index)
    return index


def solution1():
    raw_text = (BASE_DIR / "input.txt").read_text()
    root = parse_input_to_directory_index(raw_text)
    directory_sizes = get_total_size(root, defaultdict(int))

    print(
        f"Sum of sizes of directories with a total size of at most 100000: {sum([v for k, v in directory_sizes.items() if k != '/' and v <= 100_000])}")


def solution2():
    raw_text = (BASE_DIR / "input.txt").read_text()
    root = parse_input_to_directory_index(raw_text)
    sizes = get_total_size(root, defaultdict(int))
    unused_space = TOTAL_SPACE - sizes[root]
    print(
        f"Size of smallest directory to delete {min(list(filter(lambda x: (x+unused_space)>= NEEDED_SPACE, list(sizes.values()))))}")
