import pathlib

with open(pathlib.Path(__file__).absolute().parent / "data" / "puzzle_3.txt", "r") as f:
    rows = f.readlines()

s = [int(x) for x in rows[0].strip("\n")]

for row in rows[1:]:
    for i, n in enumerate(row.strip("\n")):
        s[i] += int(n)

gamma_rate = int("".join("1" if digit > len(rows) / 2 else "0" for digit in s), 2)
epsilon_rate = int("".join("1" if digit < len(rows) / 2 else "0" for digit in s), 2)

consumption = gamma_rate * epsilon_rate
print(consumption)  # 3_959_450

