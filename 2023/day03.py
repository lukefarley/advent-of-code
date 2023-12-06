import re


def check_num(num, symbols):
    val = int(num[0])
    y = num[1]
    x1 = num[2]
    x2 = num[3]

    for symbol in symbols:
        symbol_y = symbol[1]
        symbol_x = symbol[2]

        if y - 1 <= symbol_y <= y + 1:
            if x1 - 1 <= symbol_x <= x2 + 1:
                return 1, val

    return 0, val


def get_adjacent_nums(gear, nums):
    adjacent_nums = []

    gear_y = gear[1]
    gear_x = gear[2]

    for num in nums:
        num_y = num[1]
        num_x1 = num[2]
        num_x2 = num[3]

        if num_y - 1 <= gear_y <= num_y + 1:
            if num_x1 - 1 <= gear_x <= num_x2 + 1:
                adjacent_nums.append(num)

    return adjacent_nums


if __name__ == "__main__":

    with open("data/day03.txt") as f:
        raw = [x.strip() for x in f.readlines()]

    re.findall("\d+", raw[0])
    raw[0]

    matches = list(re.finditer("\d+", raw[0]))

    nums = []
    symbols = []

    for idx, row in enumerate(raw):

        matches = list(re.finditer("\d+", row))
        symbol_matches = list(re.finditer("[^.0-9]", row))

        nums += [(match[0], idx, match.start(), match.end() - 1) for match in matches]
        symbols += [(match[0], idx, match.start()) for match in symbol_matches]

    gears = [s for s in symbols if s[0] == "*"]

    print(
        "Part 1:",
        sum([r[1] for r in [check_num(num, symbols) for num in nums] if r[0] == 1]),
    )
    print(
        "Part 2:",
        sum(
            [
                int(g[0][0]) * int(g[1][0])
                for g in [get_adjacent_nums(gear, nums) for gear in gears]
                if len(g) == 2
            ]
        ),
    )
