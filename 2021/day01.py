import numpy as np


if __name__ == "__main__":
    with open("data/day1.txt") as f:
        sonars = [int(x.strip()) for x in f.readlines()]

    part1 = sum((np.array(sonars[1:]) - np.array(sonars[:-1])) > 0)

    part2 = sum(
        (
            (np.array(sonars[1:-2]) + np.array(sonars[2:-1]) + np.array(sonars[3:]))
            - (np.array(sonars[:-3]) + np.array(sonars[1:-2]) + np.array(sonars[2:-1]))
        )
        > 0
    )

    print("Part 1:", part1)
    print("Part 2:", part2)
