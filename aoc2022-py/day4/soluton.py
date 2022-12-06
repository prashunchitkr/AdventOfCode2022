from pathlib import Path

BASE_DIR = Path(__file__).absolute().parent


def get_compartment_list(assigned: str) -> list[int]:
    start, end = assigned.split('-')
    return [i for i in range(int(start), int(end)+1)]


def is_contained(e1: list[int], e2: list[int]) -> bool:
    if len(e1) > len(e2):
        return False
    if e1[0] in e2 and e1[-1] in e2:
        return True
    return False


def solution1():
    with open(BASE_DIR/"input.txt", 'r') as infile:
        count = 0
        for line in infile:
            line = line.strip()
            e1, e2 = line.split(',')
            c1, c2 = get_compartment_list(e1), get_compartment_list(e2)
            if is_contained(c1, c2) or is_contained(c2, c1):
                count += 1
        print(count)


def solution2():
    with open(BASE_DIR/"input.txt", 'r') as infile:
        count = 0
        for line in infile:
            line = line.strip()
            e1, e2 = line.split(',')
            c1, c2 = set(get_compartment_list(e1)), set(
                get_compartment_list(e2))
            if c1.intersection(c2):
                count += 1
        print(count)
