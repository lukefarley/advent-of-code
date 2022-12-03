def get_round_score_1(round_strategy):

    opponent = round_strategy[0]
    you = round_strategy[2]

    shapes_index = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}

    diff = (shapes_index[you] - shapes_index[opponent]) % 3

    if diff == 0:
        outcome_score = 3
    elif diff == 1:
        outcome_score = 6
    elif diff == 2:
        outcome_score = 0

    return outcome_score + shapes_index[you] + 1


def get_round_score_2(round_strategy):

    opponent = round_strategy[0]
    outcome_shape = round_strategy[2]

    shapes_index = {"A": 0, "B": 1, "C": 2}

    if outcome_shape == "X":
        outcome_score = 0
        response_score = ((shapes_index[opponent] - 1) % 3) + 1
    elif outcome_shape == "Y":
        outcome_score = 3
        response_score = shapes_index[opponent] + 1
    elif outcome_shape == "Z":
        outcome_score = 6
        response_score = ((shapes_index[opponent] + 1) % 3) + 1

    return response_score + outcome_score


if __name__ == "__main__":
    with open("data/day02.txt") as f:
        strategy = [x.strip() for x in f.readlines()]

        round_scores = [get_round_score_1(s) for s in strategy]
        print("Part 1:", sum(round_scores))

        round_scores = [get_round_score_2(s) for s in strategy]
        print("Part 2:", sum(round_scores))
