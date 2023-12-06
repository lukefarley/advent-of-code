import re


def calc_wins(time, record_distance):

    num_wins = 0
    for speed in range(time):
        distance = (time - speed) * speed
        if distance > record_distance:
            num_wins += 1

    return num_wins


def min_max_binary_search(time, record_distance, looking_for="max"):

    left, right = 0, time - 1

    while left <= right:

        speed = (left + right) // 2
        distance = (time - speed) * speed

        if distance > record_distance:
            # wins
            speed_adj = 1 if looking_for == "max" else -1
            distance_neighboring_speed = (time - (speed + speed_adj)) * (
                speed + speed_adj
            )

            if distance_neighboring_speed <= record_distance:
                return speed
            else:
                if looking_for == "min":
                    right = speed - 1
                else:
                    left = speed + 1
        else:
            if looking_for == "max":
                right = speed - 1
            else:
                left = speed + 1


if __name__ == "__main__":

    with open("data/day06.txt") as f:
        times, distances = [
            [int(y) for y in re.findall("\d+", x)] for x in f.readlines()
        ]

    res = 1
    for num_wins in [calc_wins(times[i], distances[i]) for i in range(len(times))]:
        res *= num_wins

    print("Part 1:", res)

    time = int("".join([str(x) for x in times]))
    distance = int("".join([str(x) for x in distances]))

    print(
        "Part 2:",
        min_max_binary_search(time, distance, "max")
        - min_max_binary_search(time, distance, "min")
        + 1,
    )
