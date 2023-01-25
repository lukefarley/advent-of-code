from collections import deque


def get_neighbors(point):
    x = point[0]
    y = point[1]

    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    return neighbors


def move_blizzard(points):
    new_points = {k: v.copy() for k, v in points.items()}

    max_x = max([p[0] for p in points])
    max_y = max([p[1] for p in points])

    for x in range(1, max_x):
        for y in range(1, max_y):

            vals = points[(x, y)]

            for val in vals:
                if val == ">":
                    if points[(x + 1, y)] == ["#"]:
                        new_points[(1, y)].append(val)
                    else:
                        new_points[(x + 1, y)].append(val)
                    new_points[(x, y)].remove(val)
                elif val == "<":
                    if points[(x - 1, y)] == ["#"]:
                        new_points[(max_x - 1, y)].append(val)
                    else:
                        new_points[(x - 1, y)].append(val)
                    new_points[(x, y)].remove(val)
                elif val == "^":
                    if points[(x, y - 1)] == ["#"]:
                        new_points[(x, max_y - 1)].append(val)
                    else:
                        new_points[(x, y - 1)].append(val)
                    new_points[(x, y)].remove(val)
                elif val == "v":
                    if points[(x, y + 1)] == ["#"]:
                        new_points[(x, 1)].append(val)
                    else:
                        new_points[(x, y + 1)].append(val)
                    new_points[(x, y)].remove(val)

    return new_points


grid = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#""".split(
    "\n"
)

with open("data/day24.txt") as f:
    grid = [x.strip() for x in f.readlines()]

max_x = len(grid[0])
max_y = len(grid)

all_points = {0: {}}
for rownum in range(len(grid)):
    for colnum in range(len(grid[0])):
        all_points[0][(colnum, rownum)] = [grid[rownum][colnum]]
        if all_points[0][(colnum, rownum)] == ["."]:
            all_points[0][(colnum, rownum)] = []

points = all_points[0]

# build a state of the grid at each point in time
for minutes in range(1, 1000):
    all_points[minutes] = move_blizzard(all_points[minutes - 1])


def shortest_path(start, dest, all_points, starting_minutes_passed, max_x, max_y):

    q = deque()
    q.append((start, starting_minutes_passed))

    while q:

        current_node = q.popleft()

        point = current_node[0]
        minutes_passed = current_node[1]

        if point == dest:
            return minutes_passed

        neighboring_points = [
            p
            for p in get_neighbors(point)
            if p[0] >= 1 and p[0] <= max_x - 1 and p[1] >= 1 and p[1] <= max_y - 1
        ]
        neighbors = [
            (np, all_points[minutes_passed + 1][np]) for np in neighboring_points
        ]

        for neighbor in neighbors:
            if neighbor[1] == []:
                if (neighbor[0], minutes_passed + 1) not in q:
                    q.append((neighbor[0], minutes_passed + 1))

        if all_points[minutes_passed + 1][point] == []:
            if (point, minutes_passed + 1) not in q:
                q.append((point, minutes_passed + 1))


there = shortest_path((1, 0), (max_x - 2, max_y - 2), all_points, 0, max_x, max_y) + 1
back = (
    shortest_path((max_x - 2, max_y - 2), (1, 1), all_points, there, max_x, max_y) + 1
)
there_again = (
    shortest_path((1, 0), (max_x - 2, max_y - 2), all_points, back, max_x, max_y) + 1
)
print("Part 1:", there)
print("Part 2:", there_again)
