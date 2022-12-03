import itertools

tst = """on x=-20..26,y=-36..17,z=-47..7
on x=-20..33,y=-21..23,z=-26..28
on x=-22..28,y=-29..23,z=-38..16
on x=-46..7,y=-6..46,z=-50..-1
on x=-49..1,y=-3..46,z=-24..28
on x=2..47,y=-22..22,z=-23..27
on x=-27..23,y=-28..26,z=-21..29
on x=-39..5,y=-6..47,z=-3..44
on x=-30..21,y=-8..43,z=-13..34
on x=-22..26,y=-27..20,z=-29..19
off x=-48..-32,y=26..41,z=-47..-37
on x=-12..35,y=6..50,z=-50..-2
off x=-48..-32,y=-32..-16,z=-15..-5
on x=-18..26,y=-33..15,z=-7..46
off x=-40..-22,y=-38..-28,z=23..41
on x=-16..35,y=-41..10,z=-47..6
off x=-32..-23,y=11..30,z=-14..3
on x=-49..-5,y=-3..45,z=-29..18
off x=18..30,y=-20..-8,z=-3..13
on x=-41..9,y=-7..43,z=-33..15
on x=-54112..-39298,y=-85059..-49293,z=-27449..7877
on x=967..23432,y=45373..81175,z=27513..53682"""

tst = """on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11
on x=10..10,y=10..10,z=10..10"""

input_ = [x.split(" ") for x in tst.split("\n")]

# Part 1
# with open("data/day22.txt") as f:
#     input_ = [x.split(" ") for x in f.read().strip().split("\n")]

on_off = [1 if x[0] == "on" else 0 for x in input_]
coords = [x[1] for x in input_]
coords = [
    [
        list(range(max(int(z.split("..")[0]), -50), min(int(z.split("..")[1]) + 1, 50)))
        for z in [y.split("=")[1] for y in x.split(",")]
    ]
    for x in coords
]
# coords = [[list(range(int(z.split("..")[0]), int(z.split("..")[1])+1)) for z in [y.split("=")[1] for y in x.split(",")]] for x in coords]

grid = list(
    itertools.product(list(range(-50, 51)), list(range(-50, 51)), list(range(-50, 51)))
)
grid = dict(zip(grid, [0 for _ in range(len(grid))]))

for i, c in enumerate(coords[:-2]):
    val = on_off[i]
    points = list(itertools.product(c[0], c[1], c[2]))
    for p in points:
        grid[p] = val

# Part 2
# we can probably just keep track of how many cubes are on

(-49, -5)
(-32, -23)


def get_num_overlap(p1x1, p1x2, p2x1, p2x2):
    assert p1x1 <= p1x2 and p2x1 <= p2x2

    total_num = max(p1x1, p1x2, p2x1, p2x2) - min(p1x1, p1x2, p2x1, p2x2) + +1

    if p1x1 > 0 and p1x2 > 0 and p2x1 <= 0 and p2x2 <= 0:
        return 0, total_num
    elif p1x1 <= 0 and p1x2 <= 0 and p2x1 > 0 and p2x1 > 0:
        return 0, total_num
    elif p1x2 < p2x1:
        return 0, total_num
    elif p2x2 < p1x1:
        return 0, total_num
    else:
        # there is overlap
        max_x1 = max(p1x1, p2x1)
        min_x2 = min(p1x2, p2x2)
        num_intersect = min_x2 - max_x1 + 1
        num_non_intersect = total_num - num_intersect
        return num_intersect, num_non_intersect


def get_num_overlap2(s1, s2, on=1):

    x1min, x1max = s1[0]
    y1min, y1max = s1[1]
    z1min, z1max = s1[2]

    x2min, x2max = s2[0]
    y2min, y2max = s2[1]
    z2min, z2max = s2[2]

    if on:
        # if turning on, return the union of s1 and s2
        return [
            (min(x1min, x2min), max(x1max, x2max)),
            (min(y1min, y2min), max(y1max, y2max)),
            (min(z1min, z2min), max(z1max, z2max)),
        ]
    else:
        # if tuning off, return s1 difference s2
        pass

    # if turning off, we need to know how many points are in s2 that are not in s1

    num_x_overlap, num_x_non_overlap = get_num_overlap(x1min, x1max, x2min, x2max)
    num_y_overlap, num_y_non_overlap = get_num_overlap(y1min, y1max, y2min, y2max)
    num_z_overlap, num_z_non_overlap = get_num_overlap(z1min, z1max, z2min, z2max)

    total_num_overlap = num_x_overlap * num_y_overlap * num_z_overlap
    total_num_non_overlap = num_x_non_overlap * num_y_non_overlap * num_z_non_overlap

    return total_num_overlap, total_num_non_overlap


input_ = [x.split(" ") for x in tst.split("\n")]

on_off = [1 if x[0] == "on" else 0 for x in input_]
coords = [x[1] for x in input_]
coords = [
    [
        (int(z.split("..")[0]), int(z.split("..")[1]))
        for z in [y.split("=")[1] for y in x.split(",")]
    ]
    for x in coords
]

num_on = 0
num_on = (
    (coords[0][0][1] - coords[0][0][0] + 1)
    * (coords[0][1][1] - coords[0][1][0] + 1)
    * (coords[0][2][1] - coords[0][2][0] + 1)
)
