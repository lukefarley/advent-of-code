import re

with open("data/day04.txt") as f:
    cards = [x.strip() for x in f.readlines()]


def get_points(card):
    num_match = 0
    winning_nums = [
        int(x) for x in re.findall("\d+", card.split(": ")[1].split(" | ")[0])
    ]
    my_nums = [int(x) for x in re.findall("\d+", card.split(": ")[1].split(" | ")[1])]
    for num in my_nums:
        if num in winning_nums:
            num_match += 1

    if num_match == 0:
        return 0
    else:
        return 2 ** (num_match - 1)


def num_matching_nums(card):
    num_match = 0
    winning_nums = [
        int(x) for x in re.findall("\d+", card.split(": ")[1].split(" | ")[0])
    ]
    my_nums = [int(x) for x in re.findall("\d+", card.split(": ")[1].split(" | ")[1])]
    for num in my_nums:
        if num in winning_nums:
            num_match += 1
    return num_match


print("Part 1:", sum([get_points(card) for card in cards]))

lookup = dict(zip(list(range(len(cards))), [1] * len(cards)))
total_points = 0

for i in range(len(cards)):
    num_cards = lookup[i]
    num_match = num_matching_nums(cards[i])

    for j in range(i + 1, i + num_match + 1):
        if j < len(cards):
            lookup[j] += num_cards

print("Part 2:", sum(lookup.values()))
