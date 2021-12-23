import pathlib

with open(pathlib.Path(__file__).absolute().parent / "data" / "puzzle_2.txt", "r") as f:
    rows = [r.split(" ") for r in f.readlines()]

# PART 1
horizontal = 0
depth = 0

for command, value in rows:
    value = int(value)
    if command == "forward":
        horizontal += value
    elif command == "down":
        depth += value
    elif command == "up":
        depth -= value
    else:
        ValueError(f"Command {command} not recognized")

print(horizontal * depth)

# PART 2
horizontal = 0
depth = 0
aim = 0

for command, value in rows:
    value = int(value)
    if command == "forward":
        horizontal += value
        depth += aim * value
    elif command == "down":
        aim += value
    elif command == "up":
        aim -= value
    else:
        ValueError(f"Command {command} not recognized")

print(horizontal * depth)
