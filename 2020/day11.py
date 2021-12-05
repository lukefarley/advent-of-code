from collections import Counter
import functools
import operator


TEST = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""


def apply_rules(chart):
    num_changes = 0
    new_chart = chart.copy()
    for i in range(len(chart)):
        row = chart[i]
        if i != 0:
            prev_row = chart[i - 1]
        if i != len(chart) - 1:
            next_row = chart[i + 1]

        for j in range(len(row)):
            current_seat = row[j]
            if current_seat == ".":
                continue
            adjacent_seats = []

            # look left and right in current row
            if j != 0:
                adjacent_seats.append(row[j - 1])
            if j != len(row) - 1:
                adjacent_seats.append(row[j + 1])

            # look at previous row
            if i != 0:
                adjacent_seats.append(prev_row[j])
                if j != 0:
                    adjacent_seats.append(prev_row[j - 1])
                if j != len(row) - 1:
                    adjacent_seats.append(prev_row[j + 1])

            # look at next row
            if i != len(chart) - 1:
                adjacent_seats.append(next_row[j])
                if j != 0:
                    adjacent_seats.append(next_row[j - 1])
                if j != len(row) - 1:
                    adjacent_seats.append(next_row[j + 1])

            # print(i, j, current_seat, adjacent_seats)
            if current_seat == "L" and not "#" in adjacent_seats:
                num_changes += 1
                if j == 0:
                    new_chart[i] = "#" + new_chart[i][j + 1 :]
                elif j == len(row) - 1:
                    new_chart[i] = new_chart[i][:j] + "#"
                else:
                    new_chart[i] = new_chart[i][:j] + "#" + new_chart[i][j + 1 :]
            if current_seat == "#" and Counter(adjacent_seats)["#"] >= 4:
                num_changes += 1
                if j == 0:
                    new_chart[i] = "L" + new_chart[i][j + 1 :]
                elif j == len(row) - 1:
                    new_chart[i] = new_chart[i][:j] + "L"
                else:
                    new_chart[i] = new_chart[i][:j] + "L" + new_chart[i][j + 1 :]

    return new_chart, num_changes


def apply_rules2(chart):
    num_changes = 0
    new_chart = chart.copy()

    for i in range(len(chart)):
        row = chart[i]
        for j in range(len(row)):
            current_seat = row[j]
            if current_seat == ".":
                continue
            seats_in_sight = []

            # look left in current row
            k = 1
            while j - k >= 0:
                seats_in_sight.append(chart[i][j - k])
                if chart[i][j - k] != ".":
                    break
                k += 1

            # look right in current row
            k = 1
            while j + k <= len(chart[i]) - 1:
                seats_in_sight.append(chart[i][j + k])
                if chart[i][j + k] != ".":
                    break
                k += 1

            # look straight up
            k = 1
            while i - k >= 0:
                seats_in_sight.append(chart[i - k][j])
                if chart[i - k][j] != ".":
                    break
                k += 1
            # look up and right
            n = 1
            while j + n <= len(chart[i]) - 1 and i - n >= 0:
                seats_in_sight.append(chart[i - n][j + n])
                if chart[i - n][j + n] != ".":
                    break
                n += 1
            # look up and left
            n = 1
            while j - n >= 0 and i - n >= 0:
                seats_in_sight.append(chart[i - n][j - n])
                if chart[i - n][j - n] != ".":
                    break
                n += 1

            # look straight down at next rows
            k = 1
            while i + k <= len(chart) - 1:
                seats_in_sight.append(chart[i + k][j])
                if chart[i + k][j] != ".":
                    break
                k += 1

            # look down and right
            n = 1
            while j + n <= len(chart[i]) - 1 and i + n <= len(chart) - 1:
                seats_in_sight.append(chart[i + n][j + n])
                if chart[i + n][j + n] != ".":
                    break
                n += 1

            # look down and left
            n = 1
            while j - n >= 0 and i + n <= len(chart) - 1:
                seats_in_sight.append(chart[i + n][j - n])
                if chart[i + n][j - n] != ".":
                    break
                n += 1

            # print(i, j, current_seat, seats_in_sight)
            if current_seat == "L" and not "#" in seats_in_sight:
                num_changes += 1
                if j == 0:
                    new_chart[i] = "#" + new_chart[i][j + 1 :]
                elif j == len(row) - 1:
                    new_chart[i] = new_chart[i][:j] + "#"
                else:
                    new_chart[i] = new_chart[i][:j] + "#" + new_chart[i][j + 1 :]
            if current_seat == "#" and Counter(seats_in_sight)["#"] >= 5:
                num_changes += 1
                if j == 0:
                    new_chart[i] = "L" + new_chart[i][j + 1 :]
                elif j == len(row) - 1:
                    new_chart[i] = new_chart[i][:j] + "L"
                else:
                    new_chart[i] = new_chart[i][:j] + "L" + new_chart[i][j + 1 :]

    return new_chart, num_changes


if __name__ == "__main__":
    with open("data/day11.txt") as f:
        chart = [x.strip("\n") for x in f.read().strip().split("\n")]

    # chart = [x.strip('\n') for x in TEST.strip().split('\n')]

    k = 0
    while True:
        print("-" * 50)
        result = apply_rules2(chart)
        chart = result[0]
        num_changes = result[1]
        if num_changes == 0:
            break
    print(Counter(functools.reduce(operator.add, chart).strip())["#"])
