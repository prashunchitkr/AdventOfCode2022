from pathlib import Path
from typing import Callable

BASE_DIR = Path(__file__).absolute().parent


def get_stacks(line: str) -> list[list[str]]:
    num_stacks = (len(line)+1) // 4
    print(f"Found {num_stacks} stacks")
    return [[] for _ in range(num_stacks)]


def parse_stack(stack: str, reverse=True) -> list[list[str]]:
    is_item_row: Callable[[str], bool] = lambda x: '[' in x
    rows = stack.split('\n')
    item_rows = list(filter(is_item_row, rows))

    stacks = get_stacks(item_rows[0])

    for row in item_rows:
        for i in range(1, len(row), 4):
            if row[i] == ' ':
                continue
            stack_idx = (i-1) // 4
            stacks[stack_idx].append(row[i])

    return [list(reversed(s)) for s in stacks] if reverse else stacks


def parse_instructuions(instructions: str) -> list[list[int]]:
    parsed_instructions: list[list[int]] = []
    for instruction in instructions.split('\n'):
        temp = []
        for c in instruction.split(' '):
            if c.isnumeric():
                temp.append(int(c))
        parsed_instructions.append(temp)
    return parsed_instructions


def move(stacks: list[list[str]], amt: int, frm: int, to: int):
    if amt == 0:
        return
    stacks[to-1].append(stacks[frm-1].pop())
    move(stacks, amt-1, frm, to)


def move_upgraded(stacks: list[list[str]], amt: int, frm: int, to: int):
    if amt == 0:
        return

    temp = stacks[frm-1][:amt]
    stacks[frm-1] = stacks[frm-1][amt:]
    stacks[to-1] = temp + stacks[to-1]


def solution1():
    with open(BASE_DIR / "input.txt", 'r') as infile:
        ip = infile.read()
        stack, steps = ip.split("\n\n")
        parsed_stacks = parse_stack(stack)
        parsed_instructuions = parse_instructuions(steps)
        for instruction in parsed_instructuions:
            move(parsed_stacks, instruction[0],
                 instruction[1], instruction[2])
        print(f"Final: {''.join(x[-1] for x in parsed_stacks)}")


def solution2():
    with open(BASE_DIR / "input.txt", 'r') as infile:
        ip = infile.read()
        stack, steps = ip.split("\n\n")
        parsed_stacks = parse_stack(stack, False)
        parsed_instructuions = parse_instructuions(steps)

        for instruction in parsed_instructuions:
            move_upgraded(parsed_stacks, instruction[0],
                          instruction[1], instruction[2])

        print(f"Final Updated: {''.join(x[0] for x in parsed_stacks)}")
