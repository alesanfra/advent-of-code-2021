import pathlib

WINDOW = 3

with open(pathlib.Path(__file__).absolute().parent / "data" / "puzzle_1.txt", "r") as f:
    rows = [int(n) for n in f.readlines()]

result = sum(int(sum(rows[i + 1: i + WINDOW + 1]) > sum(rows[i:i + WINDOW])) for i in range(len(rows) - WINDOW))
print(result)
