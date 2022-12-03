import matplotlib.pyplot as plt


def _fold(p, axis, num):
    val = p[0 if axis == "x" else 1]
    diff = val - num
    new_val = num - diff
    return (new_val, p[1]) if axis == "x" else (p[0], new_val)


def do_folds(grid, points, axis, num):

    points = [p for p in points if p[0 if axis == "x" else 1] > num]

    for p in points:
        folded = _fold(p, axis, num)
        grid[folded[1]][folded[0]] = 1

    if axis == "x":
        grid = [x[:num] for x in grid]
    else:
        grid = grid[:num]

    new_points = []
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if grid[j][i] == 1:
                new_points.append((i, j))

    return grid, new_points


if __name__ == "__main__":

    # read
    with open("data/day13.txt") as f:
        raw = f.read()

    dots, folds = raw.split("\n\n")

    dots = dots.split("\n")
    folds = folds.split("\n")
    folds_var = [f.split("=")[0][-1] for f in folds]
    folds_num = [int(f.split("=")[1]) for f in folds]

    # initialize
    points = [(int(d.split(",")[0]), int(d.split(",")[1])) for d in dots]

    grid = [
        [0 for _ in range(max([p[0] for p in points]) + 1)]
        for _ in range(max([p[1] for p in points]) + 1)
    ]

    for x, y in points:
        grid[y][x] = 1

    # do folds
    for k in range(len(folds)):
        grid, points = do_folds(grid, points, folds_var[k], folds_num[k])

        if k == 0:
            print("Part 1:", len(points))

    print("Part 2", "\n", "-" * 50)
    plt.scatter([p[0] for p in points], [-p[1] for p in points])
    plt.ylim(-15, 10)
    plt.show()
