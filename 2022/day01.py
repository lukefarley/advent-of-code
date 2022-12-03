if __name__ == "__main__":
    with open("data/day01.txt") as f:
        calories = [[int(y) for y in x.split("\n")] for x in f.read().split("\n\n")]

    totals = [sum(elf) for elf in calories]
    print("Part 1:", max(totals))
    print("Part 2:", sum(sorted(totals)[-3:]))
