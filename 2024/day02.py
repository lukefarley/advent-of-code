def eval_report(r):
    diffs = []
    for i in range(len(r) - 1):
        diffs.append(r[i + 1] - r[i])

    increasing = all([3 >= d >= 1 for d in diffs])
    decreasing = all([-1 >= d >= -3 for d in diffs])

    if increasing or decreasing:
        return 1
    else:
        return 0


def eval_p2(r):
    if eval_report(r):
        return 1
    else:
        for i in range(len(r)):
            new_r = r[:i] + r[i + 1 :]
            if eval_report(new_r):
                return 1

    return 0


with open("data/day02.txt") as f:
    data = [[int(y) for y in x.strip().split(" ")] for x in f.readlines()]

safe1 = [eval_report(r) for r in data]
safe2 = [eval_p2(r) for r in data]

print("Part 1:", sum(safe1))
print("Part 2:", sum(safe2))
