import itertools


def solve(template, rules, niter):

    unique_chars = list(set(rules.values()))

    pairs_count = {
        "".join(k): 0 for k in itertools.product("".join(unique_chars), repeat=2)
    }
    for x, y in zip(template, template[1:]):
        pairs_count[x + y] += 1

    chars_count = {k: 0 for k in unique_chars}
    for x in template:
        chars_count[x] += 1

    new_rules = {k: [k[0] + v, v + k[1]] for k, v in rules.items()}
    pairs = list(new_rules.keys())

    for _ in range(niter):
        pairs_count_copy = pairs_count.copy()
        for pair in pairs:
            num_of_pair = pairs_count_copy[pair]
            for new_pair in new_rules[pair]:
                pairs_count[new_pair] += num_of_pair
            chars_count[rules[pair]] += num_of_pair

            pairs_count[pair] -= num_of_pair

    counts = list(chars_count.values())
    return max(counts) - min(counts)


if __name__ == "__main__":
    with open("data/day14.txt") as f:
        template, rules = f.read().split("\n\n")

    rules = rules.split("\n")
    rules = {k: v for k, v in [r.split(" -> ") for r in rules]}

    print("Part 1:", solve(template, rules, 10))
    print("Part 2:", solve(template, rules, 40))
