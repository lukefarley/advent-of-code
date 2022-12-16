def draw_rock(grid, rock_coords):
    prev_x = None
    prev_y = None
    for coord in rock_coords:
        x, y = coord.split(",")
        x = int(x)
        y = int(y)

        grid[y][x] = "#"

        if prev_x == x:
            if y > prev_y:
                for yval in range(prev_y, y + 1):
                    grid[yval][x] = "#"
            elif y < prev_y:
                for yval in range(prev_y, y - 1, -1):
                    grid[yval][x] = "#"

        if prev_y == y:
            if x > prev_x:
                for xval in range(prev_x, x + 1):
                    grid[y][xval] = "#"
            elif x < prev_x:
                for xval in range(prev_x, x - 1, -1):
                    grid[y][xval] = "#"

        prev_x = x
        prev_y = y

    return grid


def drop_sand(grid):
    x = 500
    y = 0

    while y <= 174:
        if grid[y + 1][x] == ".":
            y += 1
        elif grid[y + 1][x - 1] == ".":
            y += 1
            x -= 1
        elif grid[y + 1][x + 1] == ".":
            y += 1
            x += 1
        else:
            break

    if y <= 174:
        grid[y][x] = "o"
        come_to_rest = True
    else:
        come_to_rest = False

    return grid, come_to_rest


with open("data/day14.txt") as f:
    rock_formations = [x.strip() for x in f.readlines()]

all_rock_coords = [rock_formation.split(" -> ") for rock_formation in rock_formations]

min_x_coord = int(
    min(
        [
            min([int(rc.split(",")[0]) for rc in rock_coords])
            for rock_coords in all_rock_coords
        ]
    )
)
max_x_coord = int(
    max(
        [
            max([int(rc.split(",")[0]) for rc in rock_coords])
            for rock_coords in all_rock_coords
        ]
    )
)
max_y_coord = int(
    max(
        [
            max([int(rc.split(",")[1]) for rc in rock_coords])
            for rock_coords in all_rock_coords
        ]
    )
)

grid = [["." for _ in range(max_x_coord + 1000)] for _ in range(max_y_coord + 3)]

for rock_coords in all_rock_coords:
    grid = draw_rock(grid, rock_coords)

come_to_rest = True
num_sand_dropped = 0
while come_to_rest:
    grid, come_to_rest = drop_sand(grid)
    if come_to_rest:
        num_sand_dropped += 1

print("Part 1:", num_sand_dropped)

# reset grid and draw floor at bottom
grid = [["." for _ in range(max_x_coord + 500)] for _ in range(max_y_coord + 3)]

for rock_coords in all_rock_coords:
    grid = draw_rock(grid, rock_coords)

grid[-1] = ["#" for _ in range(len(grid[-1]))]

come_to_rest = True
num_sand_dropped = 0
while grid[0][500] != "o":
    grid, come_to_rest = drop_sand(grid)
    if come_to_rest:
        num_sand_dropped += 1

print("Part 2:", num_sand_dropped)
