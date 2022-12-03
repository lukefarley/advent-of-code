tst = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>""".split("\n")

grid = [list(x) for x in tst]

def step(grid, num_moves=0):
    next_grid = [row.copy() for row in grid]

    # for each cell, first look to see if it will be occupied by an east facing cucumber
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if grid[j][i] == ".":
                if grid[j][i-1] == ">":
                    next_grid[j][i] = ">"
                    next_grid[j][i-1] = "."
                    num_moves += 1

    # for row in next_grid:
    #     print(row)

    next_grid2 = [row.copy() for row in next_grid]
    for i in range(len(next_grid[0])):
        for j in range(len(next_grid)):
            if next_grid[j][i] == ".":
                if next_grid[j-1][i] == "v":
                    next_grid2[j][i] = "v"
                    next_grid2[j-1][i] = "."
                    num_moves += 1

    return next_grid2, num_moves

with open("data/day25.txt") as f:
    grid = [list(x) for x in f.read().strip().split("\n")]

num_moves = 0
k = 0
while True:
    k += 1  
    prev_num_moves = num_moves
    grid, num_moves = step(grid, num_moves)
    if num_moves - prev_num_moves == 0:
        print(k, num_moves - prev_num_moves)
        break
