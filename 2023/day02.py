import re

num_cubes = {"red": 12, "green": 13, "blue": 14}
NUM_RED = 12
NUM_GREEN = 13
NUM_BLUE = 14


def read_game(game_str):
    game = {}
    game_id, game_results = game_str.split(":")

    game["game_id"] = int(game_id.replace("Game ", ""))

    for color in ["red", "green", "blue"]:
        game[color] = []

    draws = [x.strip() for x in game_results.split(";")]

    for draw in draws:
        results = draw.split(", ")
        for res in results:
            num, color = res.split(" ")
            game[color].append(int(num))

    return game


def game_is_valid(game_dict):
    for color in ["red", "green", "blue"]:
        if any([x > num_cubes[color] for x in game_dict[color]]):
            return 0
    return 1


def get_power(game_dict):
    power = 1
    for color in ["red", "green", "blue"]:
        power *= max(game_dict[color])

    return power


with open("data/day02.txt") as f:
    games = [x.strip() for x in f.readlines()]

game_dicts = [read_game(game) for game in games]


print("Part 1:", sum([game["game_id"] for game in game_dicts if game_is_valid(game)]))

powers = [get_power(game) for game in game_dicts]

print("Part 2:", sum(powers))
