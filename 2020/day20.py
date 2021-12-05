import numpy as np
from collections import Counter
import functools
import operator

TEST = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""


tiles = TEST.split("\n\n")

# with open("data/day_20_input.txt") as f:
#     tiles = f.read().strip().split("\n\n")

tile_nums = [t.split(":\n")[0] for t in tiles]
tile_nums = [t.split(" ")[1] for t in tile_nums]
tiles = [t.split(":\n")[1] for t in tiles]
tiles = [t.split("\n") for t in tiles]
tiles = [[list(t) for t in tile] for tile in tiles]
tiles = np.array([np.array(tile) for tile in tiles])


def get_borders(tile):
    left_border = tile[:, 0]
    right_border = tile[:, len(tile) - 1]
    top_border = tile[0, :]
    bottom_border = tile[len(tile) - 1, :]

    return [top_border, right_border, bottom_border, left_border]


all_borders = [get_borders(tile) for tile in tiles]

m = {}
for p, t1 in enumerate(all_borders):
    m[p] = ([None, None, None, None], [0, 0, 0, 0])
    for q, t2 in enumerate(all_borders):
        if p != q:
            for i, b1 in enumerate(t1):
                for j, b2 in enumerate(t2):
                    if np.all(b1 == b2):
                        m[p][0][i] = q
                    if list(reversed(b1)) == list(b2):
                        m[p][0][i] = q
                        m[p][1][i] = 1
                        # m.append(' '.join([str(p), str(q), str(i), str(j)]))

# m = {tile_nums[k]: [tile_nums[vi] if vi else None for vi in v] for k, v in m.items()}

# print("Part 1:", functools.reduce(operator.mul, [int(tile_nums[int(k)]) for k in list({k: v for k, v in Counter([mi.split(" ")[0] for mi in m]).items() if v == 2}.keys())]))

corners = [
    int(k)
    for k in list(
        {
            k: v for k, v in Counter([mi.split(" ")[0] for mi in m]).items() if v == 2
        }.keys()
    )
]
x = [mi for mi in m if int(mi[0]) in corners]


col1 = np.array((tiles[6], tiles[7], tiles[1]))


# border_dict = {
#     0: "top",
#     1: "right",
#     2: "bottom",
#     3: "left"
# }

# tile_nums[int(z[0])] + " " + border_dict[int(z[2])] + \
# " ~~ " + tile_nums[int(z[1])] + " " + border_dict[int(z[3])]
