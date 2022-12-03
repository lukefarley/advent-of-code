def find_bad_item(rucksack):
    num_items = len(rucksack)
    first_compartment = rucksack[: int(num_items / 2)]
    second_compartment = rucksack[int(num_items / 2) :]

    for item in first_compartment:
        if item in second_compartment:
            return item

    return ValueError("Bad item not found")


def find_badge(group):
    for item in group[0]:
        if item in group[1] and item in group[2]:
            return item

    return ValueError("Badge not found")


if __name__ == "__main__":
    with open("data/day03.txt") as f:
        rucksacks = [x.strip() for x in f.readlines()]

        priorities = dict(
            zip(
                [chr(x) for x in list(range(97, 97 + 26))]
                + [chr(x) for x in list(range(65, 65 + 26))],
                list(range(1, 53)),
            )
        )

        bad_items = [find_bad_item(r) for r in rucksacks]
        print("Part 1:", sum([priorities[bad_item] for bad_item in bad_items]))

        group_idx = [[3 * i, 1 + 3 * i, 2 + 3 * i] for i in range(len(rucksacks) // 3)]
        groups = [rucksacks[min(gidx) : max(gidx) + 1] for gidx in group_idx]
        badges = [find_badge(g) for g in groups]
        print("Part 2:", sum([priorities[b] for b in badges]))
