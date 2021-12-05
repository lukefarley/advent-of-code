import itertools
import numpy as np

TEST = """.#.
..#
###"""

# grid = np.zeros(shape = (30, 30, 30))
# origin = 15
# grid[origin][origin-1][origin] = 1
# grid[origin][origin+1][origin] = 1
# grid[origin-1][origin-1][origin] = 1
# grid[origin+1][origin-1][origin] = 1
# grid[origin+1][origin][origin] = 1

REAL = """..##.#.#.
          ##....#..
          ....####.
          #..##....
          #..#.##..
          .#..#....
          ##...##..
          .#...#...
          ........."""


grid = np.zeros(shape=(50, 50, 50, 50))
origin = 25
# grid[origin+1][origin][origin] = 1
# grid[origin-1][origin][origin] = 1
# grid[origin+2][origin][origin] = 1
# grid[origin-4][origin][origin] = 1

# grid[origin-1][origin+1][origin] = 1
# grid[origin-4][origin+1][origin] = 1
# grid[origin][origin+1][origin] = 1

# grid[origin][origin+2][origin] = 1
# grid[origin+1][origin+2][origin] = 1
# grid[origin+3][origin+2][origin] = 1
# grid[origin+2][origin+2][origin] = 1

# grid[origin+2][origin+3][origin] = 1
# grid[origin-3][origin+3][origin] = 1
# grid[origin-4][origin+3][origin] = 1

# grid[origin+3][origin+4][origin] = 1
# grid[origin-1][origin+4][origin] = 1
# grid[origin-2][origin+4][origin] = 1
# grid[origin+1][origin+4][origin] = 1

# grid[origin][origin-1][origin] = 1
# grid[origin-3][origin-1][origin] = 1

# grid[origin+1][origin-2][origin] = 1
# grid[origin+2][origin-2][origin] = 1
# grid[origin-3][origin-2][origin] = 1
# grid[origin-4][origin-2][origin] = 1

# grid[origin+1][origin-3][origin] = 1
# grid[origin-3][origin-3][origin] = 1

print("------------------------")

grid[origin + 1][origin][origin][origin] = 1
grid[origin - 1][origin][origin][origin] = 1
grid[origin + 2][origin][origin][origin] = 1
grid[origin - 4][origin][origin][origin] = 1

grid[origin - 1][origin + 1][origin][origin] = 1
grid[origin - 4][origin + 1][origin][origin] = 1
grid[origin][origin + 1][origin][origin] = 1

grid[origin][origin + 2][origin][origin] = 1
grid[origin + 1][origin + 2][origin][origin] = 1
grid[origin + 3][origin + 2][origin][origin] = 1
grid[origin + 2][origin + 2][origin][origin] = 1

grid[origin + 2][origin + 3][origin][origin] = 1
grid[origin - 3][origin + 3][origin][origin] = 1
grid[origin - 4][origin + 3][origin][origin] = 1

grid[origin + 3][origin + 4][origin][origin] = 1
grid[origin - 1][origin + 4][origin][origin] = 1
grid[origin - 2][origin + 4][origin][origin] = 1
grid[origin + 1][origin + 4][origin][origin] = 1

grid[origin][origin - 1][origin][origin] = 1
grid[origin - 3][origin - 1][origin][origin] = 1

grid[origin + 1][origin - 2][origin][origin] = 1
grid[origin + 2][origin - 2][origin][origin] = 1
grid[origin - 3][origin - 2][origin][origin] = 1
grid[origin - 4][origin - 2][origin][origin] = 1

grid[origin + 1][origin - 3][origin][origin] = 1
grid[origin - 3][origin - 3][origin][origin] = 1


def check_neighbors(grid, x, y, z, w):
    cube = grid[x][y][z][w]
    neighbors = []
    for xn in [x - 1, x, x + 1]:
        for yn in [y - 1, y, y + 1]:
            for zn in [z - 1, z, z + 1]:
                for wn in [w - 1, w, w + 1]:
                    if [xn, yn, zn, wn] != [x, y, z, w]:
                        neighbors.append(grid[xn, yn, zn, wn])
                        if sum(neighbors) > 3:
                            return 0
    if cube == 0 and sum(neighbors) == 3:
        return 1
    elif cube == 1 and sum(neighbors) != 2 and sum(neighbors) != 3:
        return 0
    else:
        return cube


def simulate(grid, nsim):
    for i in range(1, nsim + 1):
        print(i)
        new_grid = np.zeros(shape=grid.shape)

        lower_boundary = min([min(x) for x in np.where(grid == 1)])
        upper_boundary = max([max(x) for x in np.where(grid == 1)])

        for x in range(lower_boundary - 1, upper_boundary + 2):
            for y in range(lower_boundary - 1, upper_boundary + 2):
                for z in range(lower_boundary - 1, upper_boundary + 2):
                    for w in range(lower_boundary - 1, upper_boundary + 2):
                        new_grid[x, y, z, w] = check_neighbors(grid, x, y, z, w)
        grid = new_grid

    return grid


final = simulate(grid, 6)
