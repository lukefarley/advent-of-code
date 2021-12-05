from typing import List


def perform_action_1(command: str, current_pos: List) -> List:
    direction, val = command.split(" ")
    val = int(val)

    if direction == "forward":
        current_pos[0] += val
    elif direction == "down":
        current_pos[1] += val
    elif direction == "up":
        current_pos[1] -= val
    else:
        raise ValueError("direction must be 'forward', 'down', or 'up'")

    return current_pos


def perform_action_2(command: str, current_pos: List) -> List:
    direction, val = command.split(" ")
    val = int(val)

    if direction == "forward":
        current_pos[0] += val 
        current_pos[1] += val * current_pos[2]
    elif direction == "down":
        current_pos[2] += val
    elif direction == "up":
        current_pos[2] -= val
    else:
        raise ValueError("direction must be 'forward', 'down', or 'up'")

    return current_pos
    

if __name__ == "__main__":
    with open("data/day2.txt") as f:
        commands = [x.strip() for x in f.readlines()]
    
    current_pos = [0, 0]
    for c in commands:
        current_pos = perform_action_1(c, current_pos)

    print("Part 1:", current_pos[0] * current_pos[1])

    current_pos = [0, 0, 0]
    for c in commands:
        current_pos = perform_action_2(c, current_pos)
    
    print("Part 2:", current_pos[0] * current_pos[1])
