import functools
import operator


def get_forest(filepath="data/day03.txt"):
    f = open(filepath)
    forest = f.readlines()
    f.close()
    forest = [x.strip("\n") * 1000 for x in forest]

    return forest


def calc_num_trees(forest, xstep, ystep):
    x = 0
    y = 0
    num_trees = 0

    while y < len(forest):
        if forest[y][x] == "#":
            num_trees += 1

        x += xstep
        y += ystep

    return num_trees


if __name__ == "__main__":
    forest = get_forest()

    steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    print([calc_num_trees(forest, s[0], s[1]) for s in steps])
    print(
        functools.reduce(
            operator.mul, [calc_num_trees(forest, s[0], s[1]) for s in steps]
        )
    )
