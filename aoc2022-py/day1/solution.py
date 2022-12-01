import pathlib


def main():
    parsed = sorted([sum(map(lambda x: int(x) if x != '' else 0, s.split('\n'))) for s in open(
        pathlib.Path(__file__).parent.absolute() / "input.txt", 'r').read().split("\n\n")], reverse=True)

    print(parsed[0])
    print(sum(parsed[:3]))
