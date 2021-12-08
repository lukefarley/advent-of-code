def get_fuel_usage(positions, alignment_pos):
    return sum([abs(p - alignment_pos) for p in positions])


def get_fuel_usage2(positions, alignment_pos):
    return sum([sum(list(range(1, abs(p - alignment_pos) + 1))) for p in positions])


def get_optimal_pos(positions, f):
    results = [f(positions, i) for i in range(max(positions))]
    return results.index(min(results))


if __name__ == "__main__":

    with open("data/day07.txt") as f:
        positions = [int(x) for x in f.read().split(",")]

    print(
        "Part 1:", get_fuel_usage(positions, get_optimal_pos(positions, get_fuel_usage))
    )

    print(
        "Part 2:",
        get_fuel_usage2(positions, get_optimal_pos(positions, get_fuel_usage2)),
    )
