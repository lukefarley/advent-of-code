#############
#...........#
###B#C#A#B###
  #D#C#B#A#
  #D#B#A#C#
  #C#D#D#A#
  #########


raw = """#############
#...........#
###B#C#A#B###
  #D#C#B#A#
  #D#B#A#C#
  #C#D#D#A#
  #########"""

COST_LOOKUP = {"A": 1, "B": 10, "C": 100, "D": 1000}


def get_initial_state(raw):
    start = [x.replace("#", "").strip() for x in raw.split("\n")][2:-1]
    hallway = [(x, 0) for x in range(11)]
    state = dict(zip(hallway, "." * len(hallway)))

    state[(2, 1)] = start[0][0]
    state[(2, 2)] = start[0][1]
    state[(2, 3)] = start[0][2]
    state[(2, 4)] = start[0][3]

    state[(4, 1)] = start[1][0]
    state[(4, 2)] = start[1][1]
    state[(4, 3)] = start[1][2]
    state[(4, 4)] = start[1][3]

    state[(6, 1)] = start[2][0]
    state[(6, 2)] = start[2][1]
    state[(6, 3)] = start[2][2]
    state[(6, 4)] = start[2][3]

    state[(8, 1)] = start[3][0]
    state[(8, 2)] = start[3][1]
    state[(8, 3)] = start[3][2]
    state[(8, 4)] = start[3][3]

    return state

def get_neighbors(p):

    neighbors = []

    if p[1] == 0:
        if p[0] > 1:
            neighbors.append((p[0]-1, p[1]))
        if p[0] < 10:
            neighbors.append((p[0]+1, p[1]))
        if p[0] in [2, 4, 6, 8]:
            neighbors.append((p[0], p[1] + 1))
    else:
        neighbors.append((p[0], p[1]-1))
        if p[1] < 3:
            neighbors.append((p[0], p[1]+1))

    return neighbors

def get_valid_moves(state):
    letters = {k: v for k, v in state.items() if v != "."}
    valid_moves = {}

    for p in letters:
        neighbors = get_neighbors(p)
        for n in neighbors:
            if state[n] == ".":
                valid_moves[n] = (p, letters[p], COST_LOOKUP[letters[p]])

    return valid_moves


state = get_initial_state(raw)
valid_moves = get_valid_moves(state)
for move in valid_moves:
    state[move] = valid_moves[move][1]
    state[valid_moves[move][0]] = "."
    break


























#############
#CD.......CA#
###.#B#.#.###
  #D#B#.#A#
  #D#B#A#C#
  #C#B#D#A#
  #########

#############
#CC.......DA#
###.#B#.#.###
  #D#B#.#A#
  #D#B#A#C#
  #C#B#D#A#
  #########

#############
#AD.......CC#
###.#B#.#.###
  #D#B#.#A#
  #D#B#A#C#
  #C#B#D#A#
  #########


import networkx as nx

G = nx.Graph(
    [(0, 0), (1, 0), (3, 0), (5, 0), (7, 0), (9, 0), (10, 0),
     (2, 1), (2, 2), (2, 3), (2, 4),
     (4, 1), (4, 2), (4, 3), (4, 4),
     (6, 1), (6, 2), (6, 3), (6, 4),
     (8, 1), (8, 2), (8, 3), (8, 4)]
)

G.add_edge((0, 0), (1, 0))
G.add_edge((1, 0), (3, 0))
G.add_edge((3, 0), (5, 0))
G.add_edge((5, 0), (7, 0))
G.add_edge((7, 0), (9, 0))
G.add_edge((9, 0), (10, 0))

G.add_edge((1, 0), (2, 1))
G.add_edge((3, 0), (2, 1))
G.add_edge((2, 1), (2, 2))
G.add_edge((2, 2), (2, 3))
G.add_edge((2, 3), (2, 4))

G.add_edge((3, 0), (4, 1))
G.add_edge((5, 0), (4, 1))
G.add_edge((4, 1), (4, 2))
G.add_edge((4, 2), (4, 3))
G.add_edge((4, 3), (4, 4))

G.add_edge((5, 0), (6, 1))
G.add_edge((7, 0), (6, 1))
G.add_edge((6, 1), (6, 2))
G.add_edge((6, 2), (6, 3))
G.add_edge((6, 3), (6, 4))

G.add_edge((7, 0), (8, 1))
G.add_edge((9, 0), (8, 1))
G.add_edge((8, 1), (8, 2))
G.add_edge((8, 2), (8, 3))
G.add_edge((8, 3), (8, 4))






sum([6, 60, 3, 6000, 500, 7000, 30, 40, 700, 3, 8])
