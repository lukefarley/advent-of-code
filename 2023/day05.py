def lookup(val, map):

    for line in map:
        destination_start = line[0]
        source_start = line[1]
        length = line[2]

        if source_start <= val < source_start + length:
            diff = val - source_start
            return destination_start + diff

    return val


def get_location(seed, maps):
    val = seed
    for m in maps:
        val = lookup(val, m)
    return val


def overlapping(r1, r2):
    return max(r1[0], r2[0]) <= min(r1[1], r1[1])


if __name__ == "__main__":
    with open("data/day05.txt") as f:
        raw = f.read().split("\n\n")

    seeds = [int(x) for x in raw[0].split(": ")[1].split(" ")]

    maps = [
        [[int(y) for y in x.split(" ")] for x in raw[i].split(":\n")[1].split("\n")]
        for i in range(1, 8)
    ]

    print("Part 1:", min([get_location(seed, maps) for seed in seeds]))

    seed_ranges = [(seeds[k], seeds[k + 1]) for k in range(0, len(seeds) - 1, 2)]

    seed_range_to_location = {}
    for line in maps[0]:
        seed_range_to_location[(line[1], line[1] + line[2] - 1)] = get_location(
            line[1], maps
        )

    print(
        "Part 2:",
        min(
            {
                v
                for k, v in seed_range_to_location.items()
                if any([overlapping(k, sr) for sr in seed_ranges])
            }
        ),
    )
