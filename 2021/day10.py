def parse(string, return_stack=False):
    left_chars = ["{", "(", "[", "<"]
    right_chars = ["}", ")", "]", ">"]

    left_right_lookup = dict(zip(left_chars, right_chars))

    score_lookup = dict(zip(right_chars, [1197, 3, 57, 25137]))

    stack = []
    for i, s in enumerate(string):
        if s in left_chars:
            stack.append(s)
        if s in right_chars:
            pop = stack.pop()
            if left_right_lookup[pop] != s:
                return score_lookup[s]

    if return_stack:
        return stack
    else:
        return 0


def calc_score(nums):
    total = 0
    for n in nums:
        total = total * 5 + n
    return total


if __name__ == "__main__":
    with open("data/day10.txt") as f:
        lines = [x.strip() for x in f.readlines()]

    print("Part 1:", sum([parse(line) for line in lines]))

    left_chars = ["{", "(", "[", "<"]
    right_chars = ["}", ")", "]", ">"]

    left_right_lookup = dict(zip(left_chars, right_chars))
    score_lookup = dict(zip(right_chars, [3, 1, 2, 4]))

    incomplete_lines = [line for line in lines if parse(line) == 0]
    scores = [
        [
            score_lookup[left_right_lookup[k]]
            for k in list(reversed(parse(line, return_stack=True)))
        ]
        for line in incomplete_lines
    ]
    totals = [calc_score(s) for s in scores]
    print("Part 2:", sorted(totals)[len(totals) // 2])
