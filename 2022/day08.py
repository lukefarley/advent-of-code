def is_visible(trees, i, j):
    tree_val = int(trees[i][j])

    # check left
    left_trees = [int(t) for t in list(trees[i][:j])]
    if not any([lt >= tree_val for lt in left_trees]) or not left_trees:
        return 1

    # check right
    right_trees = [int(t) for t in list(trees[i][j + 1 :])]
    if not any([rt >= tree_val for rt in right_trees]) or not right_trees:
        return 1

    # check up
    above_trees = [int(t[j]) for t in trees[:i]]
    if not any([at >= tree_val for at in above_trees]) or not above_trees:
        return 1

    # check down
    below_trees = [int(t[j]) for t in trees[i + 1 :]]
    if not any([bt >= tree_val for bt in below_trees]) or not below_trees:
        return 1

    return 0


def get_scenic_score(trees, i, j):
    tree_val = int(trees[i][j])

    num_trees_left = 0
    num_trees_right = 0
    num_trees_above = 0
    num_trees_below = 0

    # look left
    for k in range(1, j + 1):
        if int(trees[i][j - k]) < tree_val:
            num_trees_left += 1
        else:
            num_trees_left += 1
            break

    # look right
    for k in range(1, len(trees[0]) - j):
        if int(trees[i][j + k]) < tree_val:
            num_trees_right += 1
        else:
            num_trees_right += 1
            break

    # look up
    for k in range(1, i + 1):
        if int(trees[i - k][j]) < tree_val:
            num_trees_above += 1
        else:
            num_trees_above += 1
            break

    # look down
    for k in range(1, len(trees) - i):
        if int(trees[i + k][j]) < tree_val:
            num_trees_below += 1
        else:
            num_trees_below += 1
            break

    return num_trees_left * num_trees_right * num_trees_above * num_trees_below


if __name__ == "__main__":
    with open("data/day08.txt") as f:
        trees = [x.strip() for x in f.readlines()]

        num_visible = 0
        for x in range(len(trees)):
            for y in range(len(trees[0])):
                num_visible += is_visible(trees, x, y)

        print("Part 1:", num_visible)

        scenic_scores = []
        for x in range(len(trees)):
            for y in range(len(trees[0])):
                scenic_scores.append(get_scenic_score(trees, x, y))

        print("Part 2:", max(scenic_scores))
