from pathlib import Path

BASE_DIR = Path(__file__).absolute().parent


def subroutine(data: str, buffer_len: int) -> int:
    buffer = []
    for i in range(len(data)):
        if len(buffer) == buffer_len:
            buffer.pop(0)

        buffer.append(data[i])

        if len(buffer) < buffer_len:
            continue

        if len(set(buffer)) == len(buffer):
            return i+1


def solution1():
    start_of_packet = 0
    with open(BASE_DIR / 'input.txt') as f:
        start_of_packet = subroutine(f.read().strip(), 4)
    print(f"Start of packet: {start_of_packet}")


def solution2():
    start_of_message = 0
    with open(BASE_DIR / 'input.txt') as f:
        start_of_message = subroutine(f.read().strip(), 14)
    print(f"Start of message: {start_of_message}")
