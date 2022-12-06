from day1 import Day1
from day2 import Day2
from day3 import Day3
from day4 import Day4
from day5 import Day5
from day6 import Day6

print("Enter day number for solution: ")
day = input()

if not day.isnumeric() or int(day) < 1 or int(day) > 6:
    print("Invalid day number")
    exit(1)

method_name = f"Day{int(day)}"
possibles = globals().copy()
possibles.update(locals())
method = possibles.get(method_name)
method()
