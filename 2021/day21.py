starting_pos = {1: 4, 2: 8}

def get_round_score(current_pos, rolls):
    s = (current_pos + sum(rolls)) % 10
    if s == 0:
        s = 10
    return s


def part1(p1_start, p2_start):
    p1_rolls = [[1, 2, 3]]
    p2_rolls = [[4, 5, 6]]
    for _ in range(1000):
        p1_rolls.append([r + 6 for r in p1_rolls[-1]])
        p2_rolls.append([r + 6 for r in p2_rolls[-1]])

    p1_score = 4
    p2_score = 9
    p1_total = 0
    p2_total = 0
    num_rolls = 0

    for p1_roll, p2_roll in zip(p1_rolls, p2_rolls):
        num_rolls += 6
        p1_score = get_round_score(p1_score, p1_roll)
        p1_total += p1_score
        if p1_total >= 1000:
            return ((num_rolls - 3) * p2_total)
            

        p2_score = get_round_score(p2_score, p2_roll)
        p2_total += p2_score

        if p2_total >= 1000:
            return num_rolls * p1_total

def part2(p1_start, p2_start):
    pass

if __name__ == "__main__":
    print("Part 1:", part1(4, 9))

    4
    [5, 5, 5], [5, 6, 5], [5, 5, 6], [5, 6, 6], [5, 7, 5], [5, 5, 7], [5, 7, 7]
    [
        [6, 7, 8], [7, 8, 9], [8, 9 , 10]
    ]

    8
    [9, 10, 1]

    [
        [10, 1, 2], [1, 2, 3], [2, 3, 4]
    ]

    [
        [[1, 2, 3], [2, 3, 4], [3, 4, 5]], 
        [[2, 3, 4], [3, 4, 5], [4, 5, 6]], 
        [[3, 4, 5], [4, 5, 6], [5, 6, 7]]
    ]
    

    11, 12, 13, 21, 22, 23, 31, 32, 33
    
    111,
    [112, 121, 211], 
    [113, 131, 311],
    [122, 212, 221],
    222,
    [223, 232, 322],
    333,
    [323, 332, 233]
    