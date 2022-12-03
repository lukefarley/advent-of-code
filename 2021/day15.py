from collections import deque


# import networkx as nx

# G = nx.DiGraph()

# grid = [[int(y) for y in list(x)] for x in tst.split("\n")]

# for i in range(len(grid[0])):
#     for j in range(len(grid)):
#         G.add_node((i, j))

# for i in range(len(grid[0])):
#     for j in range(len(grid)):
#         if i > 0:
#             G.add_edge((i, j), (i-1, j), weight=grid[j][i-1])
#         if i < len(grid[0]) - 1:
#             G.add_edge((i, j), (i+1, j), weight=grid[j][i+1])
#         if j > 0:
#             G.add_edge((i, j), (i, j-1), weight=grid[j-1][i])
#         if j < len(grid) - 1:
#             G.add_edge((i, j), (i, j+1), weight=grid[j+1][i])

# path = nx.dijkstra_path(G, (0, 0), (len(grid)-1, len(grid)-1))
# sum([grid[node[1]][node[0]] for node in path]) - grid[1][0]


def get_new_grid(grid):
    grid_dim = len(grid)
    new_grid = [[0 for _ in range(grid_dim*5)] for _ in range(grid_dim*5)]
    
    for i in range(grid_dim):
        for j in range(grid_dim):
            new_grid[j][i] = grid[j][i]

    for i in range(grid_dim):
        for j in range(grid_dim, grid_dim*5):
            new_val = grid[j % grid_dim][i] + (j // grid_dim)
            new_val = new_val % 9
            new_val = 9 if new_val == 0 else new_val
            new_grid[j][i] = new_val
    
    for i in range(grid_dim, grid_dim*5):
        for j in range(grid_dim):
            new_val = grid[j][i % grid_dim] + (i // grid_dim)
            new_val = new_val % 9
            new_val = 9 if new_val == 0 else new_val
            new_grid[j][i] = new_val

    for i in range(grid_dim, grid_dim*5):
        for j in range(grid_dim, grid_dim*5):
            if new_grid[j][i] == 0:
                new_val = new_grid[j % grid_dim][i % grid_dim] + (i // grid_dim + j // grid_dim)
                new_val = new_val % 9
                new_val = 9 if new_val == 0 else new_val
                new_grid[j][i] = new_val

    return new_grid


def get_adjacent_nodes(node, max_dim=10):
    x = node[0]
    y = node[1]
    adjacent = []
    if x > 0:
        adjacent.append((x-1, y))
    if x < max_dim-1:
        adjacent.append((x+1, y))
    if y > 0:
        adjacent.append((x, y-1))
    if y < max_dim -1:
        adjacent.append((x, y+1))
    return adjacent


# first attempt -- works but Part 2 takes ~10 minutes to finish running (ha!)
def fancy_bfs(root, grid):

    risk_lookup = {}
    risk_lookup[root] = 0

    Q = deque()
    Q.append((root, 0))

    results = []

    while Q:
        u, risk, path = Q.popleft()

        path.append((u, risk))

        if u != (0, 0):
            risk += grid[u[1]][u[0]]

        if u == (len(grid)-1, len(grid)-1):
            print("-" * 50)
            print("Reached:", u, "having used", risk)
            print("Risk to leave here is", grid[u[1]][u[0]])
            results.append(risk)

        for v in get_adjacent_nodes(u, len(grid)):
            if v not in risk_lookup:
                # have not visited this node before -- store what the risk level was upon reaching it
                risk_lookup[v] = risk
                Q.append((v, risk, path))
            else:
                if risk < risk_lookup[v]:            # check if we've reached this node before using less risk, if we have, don't bother adding it's neighbors to the queue
                    # last_best = risk_lookup[v]
                    risk_lookup[v] = risk            # if not, update the risk lookup with the new risk value we reached this node with
                    # Q = deque([e for e in Q if not [ep for ep in e[2] if (ep[0] == v and ep[1] >= last_best)]])
                    Q.append((v, risk))

    return results

# implement dijkstra's algorithm -- takes ~20 seconds for part 2
def dijkstra(root, grid):

    risk_lookup = {}
    risk_lookup[root] = 0

    Q = deque()
    Q.append((root, 0))

    while Q:
        u, risk = Q.popleft()

        if u != (0, 0):
            risk += grid[u[1]][u[0]]

        if u == (len(grid)-1, len(grid)-1):
            print("-" * 50)
            print("Reached:", u, "having used", risk)
            print("Risk to leave here is", grid[u[1]][u[0]])
            return risk

        for v in get_adjacent_nodes(u, len(grid)):
            if v not in risk_lookup:                 # check if we've visited this node before
                risk_lookup[v] = risk
                Q.append((v, risk))
            else:
                if risk < risk_lookup[v]:            # check if we've reached this node before using less risk, if we have, don't bother adding it's neighbors to the queue
                    risk_lookup[v] = risk            # if not, update the risk lookup with the new risk value we reached this node with
                    Q.append((v, risk))

        Q = deque(sorted(Q, key = lambda x: x[1]))


if __name__ == "__main__":
    with open("data/day15.txt") as f:
        grid = [[int(y) for y in list(x)] for x in f.read().split("\n")]

    total_risks = fancy_bfs((0, 0), grid)
    print("Part 1:", min(total_risks))

    new_grid = get_new_grid(grid)
    total_risks = fancy_bfs((0, 0), new_grid)
    print("Part 2:", min(total_risks))

    print("Faster Part 2:", dijkstra((0, 0), new_grid))
