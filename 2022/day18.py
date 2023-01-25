from collections import deque


with open("data/day18.txt") as f:
    raw = [x.strip() for x in f.readlines()]

coords = [[int(x) for x in r.split(",")] for r in raw]


def get_sides(x, y, z):

    top = [(x, y, z + 1), (x + 1, y, z + 1), (x, y + 1, z + 1), (x + 1, y + 1, z + 1)]

    bottom = [(x, y, z), (x + 1, y, z), (x, y + 1, z), (x + 1, y + 1, z)]

    left = [(x, y, z), (x, y + 1, z), (x, y, z + 1), (x, y + 1, z + 1)]

    right = [(x + 1, y, z), (x + 1, y + 1, z), (x + 1, y, z + 1), (x + 1, y + 1, z + 1)]

    front = [(x, y, z), (x + 1, y, z), (x, y, z + 1), (x + 1, y, z + 1)]

    back = [(x, y + 1, z), (x + 1, y + 1, z), (x, y + 1, z + 1), (x + 1, y + 1, z + 1)]

    return [top, bottom, left, right, front, back]


def get_neighbors(x, y, z):

    return [
        (x + 1, y, z),
        (x - 1, y, z),
        (x, y + 1, z),
        (x, y - 1, z),
        (x, y, z + 1),
        (x, y, z - 1),
    ]


# a slow way of testing if a point is an airpocket: bfs of neighboring cubes not in the
# set of cubes until we reach a point we know is open to the outside
def is_airpocket(x, y, z, coords):

    tcoords = [tuple(c) for c in coords]

    if (x, y, z) in tcoords:
        return []

    min_x = min([c[0] for c in coords])
    max_x = max([c[0] for c in coords])
    min_y = min([c[1] for c in coords])
    max_y = max([c[1] for c in coords])
    min_z = min([c[2] for c in coords])
    max_z = max([c[2] for c in coords])

    q = deque()
    q.append(((x, y, z), []))

    while q:
        point, prev_points = q.pop()

        point_neighbors = [
            n
            for n in get_neighbors(point[0], point[1], point[2])
            if n not in prev_points
        ]

        for neighbor in point_neighbors:
            if neighbor not in tcoords:
                if neighbor[0] > max_x or neighbor[1] > max_y or neighbor[2] > max_z:
                    # reached a point outside the surface
                    return []
                elif neighbor[0] < min_x or neighbor[1] < min_y or neighbor[2] < min_z:
                    # reached a point outside the surface
                    return []
                else:
                    prev_points.append(point)
                    q.append((neighbor, prev_points))

        q = deque(sorted(q, key=lambda x: max(x[0])))

    airpockets = [point] + prev_points
    return airpockets


if __name__ == "__main__":

    all_sides = []
    for c in coords:
        for side in get_sides(c[0], c[1], c[2]):
            if side in all_sides:
                all_sides = [s for s in all_sides if s != side]
            else:
                all_sides.append(side)

    print("Part 1:", len(all_sides))

    max_x = max([c[0] for c in coords])
    max_y = max([c[1] for c in coords])
    max_z = max([c[2] for c in coords])

    airpockets = []
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            for z in range(max_z + 1):
                if (x, y, z) not in airpockets:
                    airpockets = airpockets + is_airpocket(x, y, z, coords)

    airpockets = list(set(airpockets))

    airpocket_sides = []
    for ap in airpockets:
        for side in get_sides(ap[0], ap[1], ap[2]):
            if side in airpocket_sides:
                airpocket_sides = [s for s in airpocket_sides if s != side]
            else:
                airpocket_sides.append(side)

    print("Part 2:", len([s for s in all_sides if s not in airpocket_sides]))
