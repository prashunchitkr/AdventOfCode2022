from pathlib import Path
from functools import reduce


def get_point(x): return ord(x) - 96 if x.islower() else ord(x) - 64 + 26


def solution1():
    with open(Path(__file__).absolute().parent / "input.txt", 'r') as infile:
        sum = 0
        for line in infile:
            line = line.strip()
            container1, container2 = set(line[:len(line) // 2]), set(
                line[len(line) // 2:])
            common = container1.intersection(container2).pop()
            sum += get_point(common)
        print(sum)


def solution2():
    with open(Path(__file__).absolute().parent / "input.txt", 'r') as infile:
        sum = 0
        lines = [line.strip() for line in infile.readlines()]
        for i in range(len(lines) - 1)[::3]:
            common = reduce(lambda acc, curr: acc.intersection(set(curr)),
                            lines[i + 1:i + 3], set(lines[i])).pop()
            sum += get_point(common)
        print(sum)
