import functools
import operator

# tst = "target area: x=20..30, y=-10..-5"

# xmin = 20
# xmax = 30
# ymin = -10
# ymax = -5

tst = "target area: x=70..125, y=-159..-121"

xmin = 70
xmax = 125
ymin = -159
ymax = -121


def launch(x_velocity, y_velocity, tgt_xmin, tgt_xmax, tgt_ymin, tgt_ymax):
    pos = (0, 0)

    positions = []

    if y_velocity > 0:
        flipped = 0
    else:
        flipped = 1

    k = 0
    while True:
        x, y = pos

        if flipped == 0 and y_velocity - k < 0:
            flipped = 1

        pos = (x + max(0, x_velocity - k), y + y_velocity - k)
        positions.append(pos)

        # print(pos)

        if (
            pos[0] >= tgt_xmin
            and pos[0] <= tgt_xmax
            and pos[1] >= tgt_ymin
            and pos[1] <= tgt_ymax
        ):
            # print("In target")
            return positions
        elif pos[0] >= tgt_xmax:
            # print("Will never hit")
            return
        elif x_velocity - k <= 0 and pos[1] < tgt_ymax and flipped:
            # print("Will never hit")
            return

        k += 1


successful = {}
for x in range(150):
    for y in range(-500, 500):
        positions = launch(x, y, xmin, xmax, ymin, ymax)
        if positions:
            successful[(x, y)] = positions

positions = list(successful.values())
max([p[1] for p in functools.reduce(operator.add, positions)])

{k: v for k, v in successful.items() if any([p[1] == 45 for p in v])}
