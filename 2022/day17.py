with open("data/day17.txt") as f:
    jet_pattern = f.read().strip()


rock_types = {
    0: [(3, 4), (4, 4), (5, 4), (6, 4)],
    1: [(3, 5), (4, 4), (5, 5), (4, 6)],
    2: [(3, 4), (4, 4), (5, 4), (5, 5), (5, 6)],
    3: [(3, 4), (3, 5), (3, 6), (3, 7)],
    4: [(3, 4), (4, 4), (3, 5), (4, 5)],
}


def jet_move_rock(jet, rock_coords, chamber):
    # min_x_coord = min([coord[0] for coord in rock_coords])
    # max_x_coord = max([coord[0] for coord in rock_coords])

    if jet == ">":
        # move right
        new_rock_coords = [(coord[0] + 1, coord[1]) for coord in rock_coords]
        if any([coord in chamber for coord in new_rock_coords]):
            return rock_coords
        else:
            return new_rock_coords

    elif jet == "<":
        new_rock_coords = [(coord[0] - 1, coord[1]) for coord in rock_coords]
        if any([coord in chamber for coord in new_rock_coords]):
            return rock_coords
        else:
            return new_rock_coords

    return rock_coords


def rock_fall(rock_coords, chamber):

    new_rock_coords = [(coord[0], coord[1] - 1) for coord in rock_coords]
    if any([coord in chamber for coord in new_rock_coords]):
        chamber = chamber + rock_coords
        return rock_coords, True
    else:
        return new_rock_coords, False


chamber = [(i, 0) for i in range(8)]
chamber = chamber + [(0, i) for i in range(25000)]
chamber = chamber + [(8, i) for i in range(25000)]

heights = {}
jet_pattern_pos = 0
for rock_num in range(8088):
    max_y_chamber = max([p[1] for p in chamber if p[0] > 0 and p[0] < 8])
    heights[rock_num] = max_y_chamber

    rock_coords = rock_types[rock_num % 5]
    rock_coords = [(c[0], c[1] + max_y_chamber) for c in rock_coords]

    stopped = False

    while not stopped:
        # input()

        # # for coord in rock_coords:
        # #     chamber.append((coord[0], coord[1] + max_y_chamber))
        # xs = [p[0] for p in chamber]
        # ys = [p[1] for p in chamber]
        # plt.scatter(xs, ys)
        # plt.grid()

        # apply jet movement
        current_jet = jet_pattern[jet_pattern_pos]
        rock_coords = jet_move_rock(current_jet, rock_coords, chamber)
        jet_pattern_pos = (jet_pattern_pos + 1) % len(jet_pattern)

        # apply fall movement
        rock_coords, stopped = rock_fall(rock_coords, chamber)
        if stopped:
            chamber = chamber + rock_coords


print("Part 1:", max([p[1] for p in chamber if p[0] > 0 and p[0] < 8]))
heights[8088] = max([p[1] for p in chamber if p[0] > 0 and p[0] < 8])

for k in {k: v for k, v in heights.items() if k > 0}:
    if k < 8088 - 8:
        next_8 = [heights[i] for i in range(k, k + 8)]
        if [n % heights[k] for n in next_8] == [0, 0, 0, 3, 3, 5, 6, 9]:
            print(k)
