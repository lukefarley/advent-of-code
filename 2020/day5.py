import numpy as np


def binary_split(c, z):
    if c == "B" or c == "R":
        z = z[len(z) // 2 :]
    elif c == "F" or c == "L":
        z = z[: len(z) // 2]

    return z


def get_pass_id(bp):
    rows = list(range(128))
    cols = list(range(8))

    for c in bp[:7]:
        rows = binary_split(c, rows)

    for c in bp[7:]:
        cols = binary_split(c, cols)

    return rows[0] * 8 + cols[0]


if __name__ == "__main__":
    with open("data/day_5_input.txt", "r") as f:
        bps = f.read().splitlines()

    ids = [get_pass_id(bp) for bp in bps]
    print(max(ids))

    full = set(range(min(ids), max(ids) + 1, 1))
    print(full - set(ids))
