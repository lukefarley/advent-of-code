from collections import deque


def get_adjacent_points(point, topo, max_x=41, max_y=159):
    x = point[0]
    y = point[1]

    adjacent = []
    if x > 0:
        if (
            ord(topo[x - 1][y]) <= ord(topo[x][y]) + 1
            or topo[x - 1][y] == "E"
            or topo[x][y] == "S"
        ):
            adjacent.append((x - 1, y))
    if x < max_x - 1:
        if (
            ord(topo[x + 1][y]) <= ord(topo[x][y]) + 1
            or topo[x + 1][y] == "E"
            or topo[x][y] == "S"
        ):
            adjacent.append((x + 1, y))
    if y > 0:
        if (
            ord(topo[x][y - 1]) <= ord(topo[x][y]) + 1
            or topo[x][y - 1] == "E"
            or topo[x][y] == "S"
        ):
            adjacent.append((x, y - 1))
    if y < max_y - 1:
        if (
            ord(topo[x][y + 1]) <= ord(topo[x][y]) + 1
            or topo[x][y + 1] == "E"
            or topo[x][y] == "S"
        ):
            adjacent.append((x, y + 1))
    return adjacent


def dijkstra(topo, S, E):

    num_steps_lookup = {}
    num_steps_lookup[S] = 0

    Q = deque()
    Q.append((S, 0))

    while Q:
        # get the next point to visit with the fewest number of steps taken
        current_point, num_steps = Q.popleft()

        # if we've reached E, then return the number of steps it's taken
        if current_point == E:
            return num_steps

        num_steps += 1

        for neighbor in get_adjacent_points(current_point, topo):
            if (
                neighbor not in num_steps_lookup
            ):  # check if we've visited this point before
                # if not, record how many steps it took to get here and add it to the queue
                num_steps_lookup[neighbor] = num_steps
                Q.append((neighbor, num_steps))
            else:
                # if we have, then check if we've reached it in fewer steps
                if num_steps < num_steps_lookup[neighbor]:
                    # if so, then update the number of steps for this point in the lookup table and add it to the queue
                    # otherwise, no need to add it to the queue
                    num_steps_lookup[neighbor] = num_steps
                    Q.append((neighbor, num_steps))

        # sort the queue by number of steps taken
        Q = deque(sorted(Q, key=lambda x: x[1]))


if __name__ == "__main__":
    with open("data/day12.txt") as f:
        topo = [x.strip() for x in f.readlines()]

    for i in range(len(topo)):
        for j in range(len(topo[0])):
            if topo[i][j] == "E":
                E = (i, j)
                break

    for i in range(len(topo)):
        for j in range(len(topo[0])):
            if topo[i][j] == "S":
                S = (i, j)
                break

    print("Part 1:", dijkstra(topo, S, E))

    trails = []
    for i in range(len(topo)):
        for j in range(len(topo[0])):
            if topo[i][j] == "a":
                S = (i, j)
                trails.append(dijkstra(topo, S, E))

    print("Part 2:", min([trail for trail in trails if trail]))
