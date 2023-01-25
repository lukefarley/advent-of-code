import re
import itertools


def change_direction(current_direction, change, lr_swap=False):
    directions = ["right", "down", "left", "up"]
    if lr_swap:
        if change == "R":
            change = "L"
        if change == "L":
            change = "R"
    if change == "R":
        return directions[(directions.index(current_direction) + 1) % 4]
    elif change == "L":
        return directions[(directions.index(current_direction) - 1) % 4]


def move(current_pos, direction, grid):
    current_row = current_pos[0]
    current_col = current_pos[1]

    row_min_col = min(
        [idx for idx, val in enumerate(grid[current_row]) if val in [".", "#"]]
    )
    row_max_col = max(
        [idx for idx, val in enumerate(grid[current_row]) if val in [".", "#"]]
    )

    col_min_row = min(
        [
            idx
            for idx, val in enumerate([grid[k][current_col] for k in range(len(grid))])
            if val in [".", "#"]
        ]
    )
    col_max_row = max(
        [
            idx
            for idx, val in enumerate([grid[k][current_col] for k in range(len(grid))])
            if val in [".", "#"]
        ]
    )

    if direction == "right":
        if current_col + 1 > row_max_col:
            new_pos = (current_row, row_min_col)
        else:
            new_pos = (current_row, current_col + 1)
    elif direction == "left":
        if current_col - 1 < row_min_col:
            new_pos = (current_row, row_max_col)
        else:
            new_pos = (current_row, current_col - 1)
    elif direction == "up":
        if current_row - 1 < col_min_row:
            new_pos = (col_max_row, current_col)
        else:
            new_pos = (current_row - 1, current_col)
    elif direction == "down":
        if current_row + 1 > col_max_row:
            new_pos = (col_min_row, current_col)
        else:
            new_pos = (current_row + 1, current_col)

    new_row = new_pos[0]
    new_col = new_pos[1]
    if grid[new_row][new_col] == "#":
        return current_pos
    else:
        return new_pos


def move2(current_pos, direction, grid, side_lookup):
    current_row = current_pos[0]
    current_col = current_pos[1]
    current_lr_swap = current_pos[2]

    current_side = side_lookup[(current_row, current_col)]
    side_min_x = cube_sides[current_side][0][0]
    side_max_x = cube_sides[current_side][0][1]
    side_min_y = cube_sides[current_side][1][0]
    side_max_y = cube_sides[current_side][1][1]

    side_current_row = current_row - side_min_x
    side_current_col = current_col - side_min_y

    row_min_col = min(
        [idx for idx, val in enumerate(grid[current_row]) if val in [".", "#"]]
    )
    row_max_col = max(
        [idx for idx, val in enumerate(grid[current_row]) if val in [".", "#"]]
    )

    col_min_row = min(
        [
            idx
            for idx, val in enumerate([grid[k][current_col] for k in range(len(grid))])
            if val in [".", "#"]
        ]
    )
    col_max_row = max(
        [
            idx
            for idx, val in enumerate([grid[k][current_col] for k in range(len(grid))])
            if val in [".", "#"]
        ]
    )

    if direction == "right":
        if side_current_col + 1 > 49:
            if current_side == 1:
                new_pos = (
                    cube_sides[4][0][1] - 1,
                    cube_sides[4][1][0] + side_current_row,
                )
                new_direction = "up"
                new_lr_swap = True
            elif current_side == 2:
                new_pos = (cube_sides[3][0][0] + side_current_row, cube_sides[4][1][0])
                new_direction = "right"
                new_lr_swap = False
            elif current_side == 3:
                new_pos = (
                    cube_sides[4][0][1] - 1 - side_current_row,
                    cube_sides[4][1][1] - 1,
                )
                new_direction = "left"
                new_lr_swap = False
            elif current_side == 4:
                pass
            elif current_side == 5:
                pass
            elif current_side == 6:
                pass
        else:
            new_pos = (current_row, current_col + 1)
    elif direction == "left":
        if side_current_col - 1 < 0:
            if current_side == 1:
                new_pos = (cube_sides[2][0][0], cube_sides[2][1][0] + side_current_row)
                new_direction = "down"
                new_lr_swap = False
            elif current_side == 2:
                new_pos = (cube_sides[5][0][1] - 1, cube_sides[5][1][0])
                new_direction = "right"
            elif current_side == 3:
                new_pos = (
                    cube_sides[2][0][0] + side_current_row,
                    cube_sides[2][1][0] + side_current_col,
                )
                new_direction = "left"
                new_lr_swap = True
            elif current_side == 4:
                pass
            elif current_side == 5:
                pass
            elif current_side == 6:
                pass
        else:
            new_pos = (current_row, current_col - 1)
    elif direction == "up":
        if side_current_row - 1 < 0:
            if current_side == 1:
                new_pos = (
                    cube_sides[5][0][1] - 1,
                    cube_sides[5][1][0] + side_current_col,
                )
                new_direction = "up"
                new_lr_swap = True
            elif current_side == 2:
                new_pos = (
                    cube_sides[5][0][1] - 1 - side_current_row,
                    cube_sides[5][1][0] + side_current_col,
                )
                new_direction = "right"
                new_lr_swap = False
            elif current_side == 3:
                pass
            elif current_side == 4:
                pass
            elif current_side == 5:
                pass
            elif current_side == 6:
                pass
        else:
            new_pos = (current_row - 1, current_col)
    elif direction == "down":
        if side_current_row + 1 > 49:
            if current_side == 1:
                new_pos = (cube_sides[3][0][0], cube_sides[3][1][0] + side_current_col)
                new_direction = "down"
                new_lr_swap = False
            elif current_side == 2:
                new_pos = (
                    cube_sides[4][0][1] - 1,
                    cube_sides[4][1][0] + side_current_row,
                )
                new_direction = "down"
                new_lr_swap = True
            elif current_side == 3:
                pass
            elif current_side == 4:
                pass
            elif current_side == 5:
                pass
            elif current_side == 6:
                pass
        else:
            new_pos = (current_row + 1, current_col)

    new_row = new_pos[0]
    new_col = new_pos[1]
    if grid[new_row][new_col] == "#":
        return current_pos, current_direction, current_lr_swap
    else:
        return new_pos, new_direction, new_lr_swap


def get_next_instruction(instructions):
    if instructions[0] in [str(x) for x in range(10)]:
        return int(re.match("\d+", instructions)[0])
    else:
        return instructions[0]


raw = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.
\n
10R5L5R10L4R5L5"""

raw = raw.split("\n\n")

with open("data/day22.txt") as f:
    raw = f.read().split("\n\n")

grid = raw[0].split("\n")
instructions = raw[1].strip()

grid_width = max([len(grid[row]) for row in range(len(grid))])

for row in range(len(grid)):
    grid[row] = grid[row].ljust(grid_width, " ")

current_pos = (0, min([idx for idx, val in enumerate(grid[0]) if val == "."]))
current_direction = "right"

print("-" * 50)
print(current_pos)
print(current_direction)

while instructions:
    instruction = get_next_instruction(instructions)
    instructions = instructions[len(str(instruction)) :]

    if isinstance(instruction, int):
        # move
        for _ in range(instruction):
            current_pos = move(current_pos, current_direction, grid)
    else:
        current_direction = change_direction(current_direction, instruction)

    # print("-"*50)
    # print(current_pos)
    # print(current_direction)

directions = ["right", "down", "left", "up"]
print(
    "Part 1:",
    1000 * (current_pos[0] + 1)
    + 4 * (current_pos[1] + 1)
    + directions.index(current_direction),
)

cube_sides = {}
# cube_sides[1] = {"min_x": 50, "max_x": 100, "min_y": 50, "max_y": 100}
# cube_sides[2] = {"min_x": 0, "max_x": 50, "min_y": 100, "max_y": 150}

cube_sides[1] = ((50, 100), (50, 100))
cube_sides[2] = ((100, 150), (0, 50))
cube_sides[3] = ((100, 150), (50, 100))
cube_sides[4] = ((0, 50), (100, 150))
cube_sides[5] = ((0, 50), (50, 100))
cube_sides[6] = ((150, 200), (0, 50))

side_lookup = {}
for coord in list(itertools.product(list(range(50, 100)), list(range(50, 100)))):
    side_lookup[coord] = 1
for coord in list(itertools.product(list(range(100, 150)), list(range(0, 50)))):
    side_lookup[coord] = 2
for coord in list(itertools.product(list(range(100, 150)), list(range(50, 100)))):
    side_lookup[coord] = 3
for coord in list(itertools.product(list(range(0, 50)), list(range(100, 150)))):
    side_lookup[coord] = 4
for coord in list(itertools.product(list(range(0, 50)), list(range(50, 100)))):
    side_lookup[coord] = 5
for coord in list(itertools.product(list(range(150, 200)), list(range(0, 50)))):
    side_lookup[coord] = 6

cube_coords = []
cube_coords += [(k[1] - 50, k[0] - 50, 0) for k, v in side_lookup.items() if v == 1]
cube_coords += [(0, k[1], k[0] - 100) for k, v in side_lookup.items() if v == 2]
cube_coords += [(k[1] - 50, 50, k[0] - 100) for k, v in side_lookup.items() if v == 3]
cube_coords += [(50, k[1] - 100, k[0]) for k, v in side_lookup.items() if v == 4]
cube_coords += [(k[1], 0, k[0]) for k, v in side_lookup.items() if v == 5]
cube_coords += [
    ((k[0] - 150, k[1], 50), grid[k[0]][k[1]]) for k, v in side_lookup.items() if v == 6
]


side_lookup = {}
for coord in list(itertools.product(list(range(50, 100)), list(range(50, 100)))):
    side_lookup[coord] = 1
for coord in list(itertools.product(list(range(100, 150)), list(range(0, 50)))):
    side_lookup[coord] = 2
for coord in list(itertools.product(list(range(100, 150)), list(range(50, 100)))):
    side_lookup[coord] = 3
for coord in list(itertools.product(list(range(0, 50)), list(range(100, 150)))):
    side_lookup[coord] = 4
for coord in list(itertools.product(list(range(0, 50)), list(range(50, 100)))):
    side_lookup[coord] = 5
for coord in list(itertools.product(list(range(150, 200)), list(range(0, 50)))):
    side_lookup[coord] = 6
