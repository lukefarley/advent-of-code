def parse_pair(pair):
    pair = [[int(y) for y in x.split("-")] for x in pair.split(",")]
    first = pair[0]
    second = pair[1]

    return first, second


def fully_contains(pair):
    first, second = pair

    if first[0] <= second[0] and first[1] >= second[1]:
        return 1
    elif first[0] >= second[0] and first[1] <= second[1]:
        return 1
    else:
        return 0


def overlaps(pair):
    first, second = pair

    if first[0] <= second[0] and first[1] >= second[0]:
        return 1
    if first[0] >= second[0] and first[0] <= second[1]:
        return 1
    else:
        return 0


if __name__ == "__main__":
    with open("data/day04.txt") as f:
        pairs = [x.strip() for x in f.readlines()]

    parsed_pairs = [parse_pair(pair) for pair in pairs]

    print("Part 1:", sum([fully_contains(pair) for pair in parsed_pairs]))
    print("Part 2:", sum([overlaps(pair) for pair in parsed_pairs]))
