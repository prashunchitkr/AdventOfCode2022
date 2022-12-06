import pathlib

NORMALIZE_MAP = {"X": "A", "Y": "B", "Z": "C"}

LOSE_MAP = {"A": "B", "B": "C", "C": "A"}
WIN_MAP = {v: k for k, v in LOSE_MAP.items()}

CHOICE_SCORE_MAP = {"A": 1, "B": 2, "C": 3}

SCORES = {"WIN": 6, "DRAW": 3, "LOSE": 0}

# 12276
# 9975


def solution():
    with open(pathlib.Path(__file__).parent.absolute() / "input.txt",
              'r') as infile:
        score = 0
        for line in infile:
            opponent, you = line.strip().split(' ')
            you = NORMALIZE_MAP[you]

            score += CHOICE_SCORE_MAP[you]

            if opponent == you:
                score += SCORES["DRAW"]
            elif you == LOSE_MAP[opponent]:
                score += SCORES["WIN"]
            else:
                score += SCORES["LOSE"]

        print(score)


def solution2():
    with open(pathlib.Path(__file__).parent.absolute() / "input.txt",
              'r') as infile:
        score = 0
        for line in infile:
            opponent, needed_result = line.strip().split(' ')
            your_pick = ''
            if needed_result == 'X':
                your_pick = WIN_MAP[opponent]
                score += SCORES["LOSE"]
            elif needed_result == 'Y':
                your_pick = opponent
                score += SCORES["DRAW"]
            elif needed_result == 'Z':
                your_pick = LOSE_MAP[opponent]
                score += SCORES["WIN"]
            score += CHOICE_SCORE_MAP[your_pick]

        print(score)
