raw_tst = """2199943210
3987894921
9856789892
8767896789
9899965678"""

tst = [[int(y) for y in list(x)] for x in raw_tst.split("\n")]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # if x > 0:
        #     self.left_neighbor = Point(x-1, y, grid)
        # if self.x < len(self.grid[0]) - 1:
        #     self.right_neighbor = Point(x+1, y, grid)

    def left_neighbor(self):
        return (self.x - 1, self.y)

    def right_neighbor(self):
        return (self.x + 1, self.y)

    def above_neighbor(self):
        return (self.x, self.y - 1)

    def below_neighbor(self):
        return (self.x, self.y + 1)

    def is_lowpoint(self, grid):
        return (self.y, self.x) in find_lowpoints(grid)[1]

    def get_val(self, grid):
        return grid[self.y][self.x]

    # def get_all_neighbors(self, grid, grid_height, grid_width):
    #     neighbors = []
    #     if self.has_right_neighbor(grid_width):
    #         neighbors.append(grid[self.y][self.x+1])
    #     if self.has_left_neighbor():
    #         neighbors.append(grid[self.y][self.x-1])
    #     if self.has_below_neighbor(grid_height):
    #         neighbors.append(grid[self.y+1][self.x])
    #     if self.has_above_neighbor():
    #         neighbors.append(grid[self.y-1][self.x-1])


class Grid:
    def __init__(self, g):
        self.g = g

    def is_valid(self, p):
        return (
            (p.x >= 0) and (p.x < len(self.g[0])) and (p.y >= 0) and (p.y < len(self.g))
        )

    def get(self, p):
        return self.g[p.y][p.x]


def find_basin(grid, lp, basin=set()):

    ln = lp.left_neighbor()
    ln = Point(ln[0], ln[1])

    rn = lp.right_neighbor()
    rn = Point(rn[0], rn[1])

    an = lp.above_neighbor()
    an = Point(an[0], an[1])

    bn = lp.below_neighbor()
    bn = Point(bn[0], bn[1])

    neighbors = [ln, rn, an, bn]
    valid_neighbors = [n for n in neighbors if grid.is_valid(n)]

    # neighbor_coords = [(n.x, n.y) for n in valid_neighbors]
    # neighbor_vals = [grid.get(n) for n in valid_neighbors]

    # check if lp is less than all it's neighbors not already in the basin
    neighbors_to_check = [n for n in valid_neighbors if (n.x, n.y) not in basin]
    vals_to_check = [grid.get(n) for n in neighbors_to_check]

    print("-" * 50)
    print(basin)
    print((lp.x, lp.y))
    print("Neighbors to check:", [(p.x, p.y) for p in neighbors_to_check])
    print("Neighbor vals:", vals_to_check)

    if grid.get(lp) == 9:
        return basin

    if sum([grid.get(lp) <= v for v in vals_to_check]) == len(vals_to_check):
        # this point is also in the basin
        basin.add((lp.x, lp.y))

        # recursively continue getting basin
        for n in neighbors_to_check:
            find_basin(grid, n, basin)

    return basin

    #     if not grid.is_valid(n):
    #         continue

    #     if grid.get(n) == 9:
    #         continue

    #     if grid.get(n) > grid.get(lp):
    #         basin = basin + [n]
    #         if grid.get(n) < 9:
    #             basin += find_basin(grid, n)


# def find_basin(grid, lp):
#     basin = []

#     z = [row.copy() for row in grid.copy()]
#     z[lp.y][lp.x] = 9

#     ln = lp.left_neighbor()
#     ln = Point(ln[0], ln[1])

#     rn = lp.right_neighbor()
#     rn = Point(rn[0], rn[1])

#     an = lp.above_neighbor()
#     an = Point(an[0], an[1])

#     bn = lp.below_neighbor()
#     bn = Point(bn[0], bn[1])

#     print("Current lowpoint:", (lp.x, lp.y))
#     neighbors = [(p.x, p.y) for p in [ln, rn, an, bn]]
#     print("Neighbors:", neighbors)
#     print("Neighbors lowpoints?", [Point(p[0], p[1]).is_lowpoint(z) for p in neighbors])


#     if ln.is_lowpoint(z):
#         basin = basin + [ln]
#         basin = basin + find_basin(z, ln)


#     if rn.is_lowpoint(z):
#         basin = basin + [rn]
#         basin = basin + find_basin(z, rn)


#     if an.is_lowpoint(z):
#         basin = basin + [rn]
#         basin = basin + find_basin(z, rn)


#     if bn.is_lowpoint(z):
#         basin = basin + [bn]
#         basin = basin + find_basin(z, bn)

#     return basin


def find_lowpoints(grid):
    width = len(grid[0])
    height = len(grid)

    lowpoints = []
    position_of_lowpoints = []

    for j in range(height):
        for i in range(width):
            p = grid[j][i]

            if j > 0:
                above_neighbor = grid[j - 1][i]
            if j < (height - 1):
                below_neighbor = grid[j + 1][i]
            if i > 0:
                left_neighbor = grid[j][i - 1]
            if i < (width - 1):
                right_neighbor = grid[j][i + 1]

            if i + j == 0:
                # top left corner
                if p < right_neighbor and p < below_neighbor:
                    lowpoints.append(p)
                    position_of_lowpoints.append((j, i))

            elif i == (width - 1) and j == 0:
                # top right corner
                if p < left_neighbor and p < below_neighbor:
                    lowpoints.append(p)
                    position_of_lowpoints.append((j, i))

            elif i == 0 and j == (height - 1):
                if p < right_neighbor and p < above_neighbor:
                    lowpoints.append(p)
                    position_of_lowpoints.append((j, i))

            elif i == (width - 1) and j == (height - 1):
                if p < above_neighbor and p < left_neighbor:
                    lowpoints.append(p)
                    position_of_lowpoints.append((j, i))

            elif j == 0:
                # top row, not corners
                if p < below_neighbor and p < left_neighbor and p < right_neighbor:
                    lowpoints.append(p)
                    position_of_lowpoints.append((j, i))

            elif i == 0:
                if p < below_neighbor and p < above_neighbor and p < right_neighbor:
                    lowpoints.append(p)
                    position_of_lowpoints.append((j, i))

            elif i == (width - 1):
                if p < below_neighbor and p < above_neighbor and p < left_neighbor:
                    lowpoints.append(p)
                    position_of_lowpoints.append((j, i))

            elif j == (height - 1):
                if p < above_neighbor and p < left_neighbor and p < right_neighbor:
                    lowpoints.append(p)
                    position_of_lowpoints.append((j, i))

            else:
                if (
                    p < above_neighbor
                    and p < left_neighbor
                    and p < right_neighbor
                    and p < below_neighbor
                ):
                    lowpoints.append(p)
                    position_of_lowpoints.append((j, i))

            # print(i, j, lowpoints)

    return lowpoints, position_of_lowpoints


def get_neighbors(x, y):
    return [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]


def get_basin(lowpoint, grid):
    basin = [lowpoint]

    lp_num = lowpoint[0]
    lp_coords = lowpoint[1]

    z = grid.copy()
    z[lp_coords[0]][lp_coords[1]] = 9
    new_lowpoints = find_lowpoints(z)
    new_lowpoint_coords = set(new_lowpoints[1])
    neighbors = set(get_neighbors(lp_coords[0], lp_coords[1]))

    basin.append(list(neighbors.intersection(new_lowpoint_coords)))


if __name__ == "__main__":
    with open("data/day09.txt") as f:
        grid = [[int(y) for y in list(x.strip())] for x in f.readlines()]

    # tst = [[int(y) for y in list(x)] for x in raw_tst.split("\n")]
    # lowpoints_tst = find_lowpoints(tst)

    lowpoints = find_lowpoints(grid)
    print("Part 1:", sum([1 + lowpoint for lowpoint in lowpoints[0]]))

    grid = Grid(grid)

    basins = []
    for lp in lowpoints[1]:
        lp_point = Point(lp[1], lp[0])
        basin = find_basin(grid, lp_point, basin=set())

        basins.append(basin)

    sorted([len(b) for b in basins])

    bs = [find_basin(grid, Point(lp[1], lp[0]), basin=set()) for lp in lowpoints[1]]
