from functools import reduce
import pathlib


def main():
    top = sorted(reduce(lambda a, b: [*a, 0] if b == -1 else [*a[:-1], a[-1] + b], [int(line) if line != '\n' else -
                 1 for line in open(pathlib.Path(__file__).parent.absolute() / "input.txt", 'r')], [0]), reverse=True)[0]

    sum_top_3 = sum(sorted(reduce(lambda a, b: [*a, 0] if b == -1 else [*a[:-1], a[-1] + b], [int(
        line) if line != '\n' else -1 for line in open(pathlib.Path(__file__).parent.absolute() / "input.txt", 'r')], [0]), reverse=True)[:3])

    print(top, sum_top_3)
