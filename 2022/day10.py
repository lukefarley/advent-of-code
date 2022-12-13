if __name__ == "__main__":
    with open("data/day10.txt") as f:
        instructions = [x.strip() for x in f.readlines()]

    cycle = 0
    X = 1
    cycle_lookup = {}

    for instruction in instructions:
        if instruction[:4] == "addx":
            for _ in range(2):
                cycle += 1
                cycle_lookup[cycle] = X
            X += int(instruction.split(" ")[1])
        elif instruction[:4] == "noop":
            cycle += 1
            cycle_lookup[cycle] = X

    print(
        "Part 1:",
        sum([cycle_lookup[k] * k for k in list(range(20, len(cycle_lookup), 40))]),
    )

    CRT = [["." for _ in range(40)] for _ in range(6)]
    for i in list(range(6)):
        for j in list(range(1, 41)):
            X = cycle_lookup[i * 40 + j]
            sprite_pos = [X - 1, X, X + 1]
            CRT[i][j - 1] = "#" if (j - 1) in sprite_pos else "."

    print("Part 2:")
    for k in range(6):
        print(" ".join(CRT[k]))
