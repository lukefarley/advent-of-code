from collections import Counter


def get_neighbors(x, y):

    neighbor_dict = {
        "north": [(x, y - 1), (x + 1, y - 1), (x - 1, y - 1)],
        "south": [(x, y + 1), (x + 1, y + 1), (x - 1, y + 1)],
        "west": [(x - 1, y), (x - 1, y + 1), (x - 1, y - 1)],
        "east": [(x + 1, y), (x + 1, y + 1), (x + 1, y - 1)],
    }

    return neighbor_dict


def get_proposal(point, points, ordered_directions):
    x = point[0]
    y = point[1]

    neighbors = get_neighbors(x, y)

    proposed_point = (x, y)

    all_neighbors = []
    for d in neighbors:
        all_neighbors += neighbors[d]
    all_neighbors = set(all_neighbors)

    if all(
        [
            points[neighbor] == "."
            for neighbor in [n for sublist in neighbors.values() for n in sublist]
        ]
    ):
        proposed_point = (x, y)
    else:
        for direction in ordered_directions:
            if direction == "N":
                if any([points[neighbor] == "#" for neighbor in neighbors["north"]]):
                    # if "#" in [p[2] for p in points if (p[0], p[1]) in neighbors["north"]]:
                    continue
                else:
                    proposed_point = (x, y - 1)
                    break
            elif direction == "S":
                if any([points[neighbor] == "#" for neighbor in neighbors["south"]]):
                    continue
                else:
                    proposed_point = (x, y + 1)
                    break
            elif direction == "W":
                if any([points[neighbor] == "#" for neighbor in neighbors["west"]]):
                    continue
                else:
                    proposed_point = (x - 1, y)
                    break
            elif direction == "E":
                if any([points[neighbor] == "#" for neighbor in neighbors["east"]]):
                    continue
                else:
                    proposed_point = (x + 1, y)
                    break

    return proposed_point


if __name__ == "__main__":

    with open("data/day23.txt") as f:
        grid = [x.strip() for x in f.readlines()]

    points = {}
    for rownum, row in enumerate(grid):
        for colnum, val in enumerate(row):
            points[(colnum, rownum)] = val

    elves = {k: v for k, v in points.items() if v == "#"}

    min_x = min([p[0] for p in points])
    max_x = max([p[0] for p in points])
    min_y = min([p[1] for p in points])
    max_y = max([p[1] for p in points])

    for x in range(min_x - 3, max_x + 4):
        for y in range(min_y - 3, max_y + 4):
            if (x, y) not in [p for p in points if points[p] == "#"]:
                points[(x, y)] = "."

    round_num = 0
    directions = ["N", "S", "W", "E"]
    ordered_directions = [
        directions[k] for k in [(round_num + m) % 4 for m in range(4)]
    ]

    while True:

        if (round_num + 1) % 50 == 0:
            print(f"Round {round_num + 1}")

        num_elves_moved = 0

        ordered_directions = [
            directions[k] for k in [(round_num + m) % 4 for m in range(4)]
        ]

        proposals = {}
        for elf in {k: v for k, v in points.items() if v == "#"}:
            proposals[elf] = get_proposal(elf, points, ordered_directions)

        counts = Counter(proposals.values())

        for elf in proposals:
            if counts[proposals[elf]] > 1:
                proposals[elf] = elf

            if elf != proposals[elf]:
                points[elf] = "."
                points[proposals[elf]] = "#"
                num_elves_moved += 1

        if num_elves_moved == 0:
            print(f"Part 2: {round_num + 1}")
            break

        elves = {k: v for k, v in points.items() if v == "#"}
        max_x = max([elf[0] for elf in elves])
        min_x = min([elf[0] for elf in elves])
        min_y = min([elf[1] for elf in elves])
        max_y = max([elf[1] for elf in elves])

        # pad
        for x in range(min_x - 3, min_x):
            for y in range(min_y - 3, max_y + 4):
                points[(x, y)] = "."

        for x in range(max_x + 1, max_x + 4):
            for y in range(min_y - 3, max_y + 4):
                points[(x, y)] = "."

        for x in range(min_x - 3, max_x + 4):
            for y in range(min_y - 3, min_y):
                points[(x, y)] = "."

        for x in range(min_x - 3, max_x + 4):
            for y in range(max_y + 1, max_y + 4):
                points[(x, y)] = "."

        if round_num + 1 == 10:
            min_x = min([p[0] for p in points if points[p] == "#"])
            max_x = max([p[0] for p in points if points[p] == "#"])
            min_y = min([p[1] for p in points if points[p] == "#"])
            max_y = max([p[1] for p in points if points[p] == "#"])

            print(
                "Part 1:",
                len(
                    [
                        p
                        for p in points
                        if p[0] >= min_x
                        and p[0] <= max_x
                        and p[1] >= min_y
                        and p[1] <= max_y
                        and points[p] == "."
                    ]
                ),
            )

        round_num += 1
