def get_num_children(num_days, lookup):
    num_children = num_days // 7

    for k in range(1, num_children + 1):
        z = max(0, num_days - (7 * k + 2))
        if z in lookup:
            num_children += lookup[z]
        else:
            num_children += get_num_children(z, lookup)

    return num_children


if __name__ == "__main__":
    with open("data/day06.txt") as f:
        raw = f.read().split(",")

    lookup = {}
    for i in range(262):
        lookup[i] = get_num_children(i, lookup)

    print("Part 1:", sum([lookup[80 + (6 - int(x))] for x in raw]) + len(raw))
    print("Part 2:", sum([lookup[256 + (6 - int(x))] for x in raw]) + len(raw))
