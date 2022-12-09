def sign(num):
    return 1 if num > 0 else -1


def move_head(head_pos, direction):

    head_x = head_pos[0]
    head_y = head_pos[1]

    if direction == "D":
        head_pos = (head_x, head_y - 1)
    elif direction == "U":
        head_pos = (head_x, head_y + 1)
    elif direction == "R":
        head_pos = (head_x + 1, head_y)
    else:
        head_pos = (head_x - 1, head_y)

    return head_pos


def move_tail(head_pos, tail_pos):

    head_x = head_pos[0]
    head_y = head_pos[1]

    tail_x = tail_pos[0]
    tail_y = tail_pos[1]

    xdif = head_x - tail_x
    ydif = head_y - tail_y

    if abs(xdif) >= 2 or abs(ydif) >= 2:
        if abs(xdif) >= 2:
            tail_x += sign(xdif)
        elif abs(xdif) == 1:
            tail_x = head_x

        if abs(ydif) >= 2:
            tail_y += sign(ydif)
        elif abs(ydif) == 1:
            tail_y = head_y

    return (tail_x, tail_y)


if __name__ == "__main__":

    with open("data/day09.txt") as f:
        instructions = [x.strip() for x in f.readlines()]

    head_pos = (0, 0)
    tail_pos = (0, 0)

    all_tail_pos = set()
    for instruction in instructions:
        direction, distance = instruction.split(" ")
        for i in range(int(distance)):
            head_pos = move_head(head_pos, direction)
            tail_pos = move_tail(head_pos, tail_pos)
            all_tail_pos.add(tail_pos)

    print("Part 1:", len(all_tail_pos))

    ropes = [(0, 0)] * 10

    all_tail_pos = set()
    for instruction in instructions:
        direction, distance = instruction.split(" ")
        for i in range(int(distance)):
            # for k in range(len(ropes)):
            ropes[0] = move_head(ropes[0], direction)
            for k in range(1, len(ropes)):
                ropes[k] = move_tail(ropes[k - 1], ropes[k])
            all_tail_pos.add(ropes[-1])

    print("Part 2:", len(all_tail_pos))
