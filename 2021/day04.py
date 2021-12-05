import re


def check_win(hit_matrix):

    for i in range(len(hit_matrix)):
        if sum(hit_matrix[i]) == len(hit_matrix):
            return True

    for j in range(len(hit_matrix)):
        if sum([hit_matrix[i][j] for i in range(len(hit_matrix))]) == len(hit_matrix):
            return True

    return False


def play_bingo(board, draws):

    dim = len(board)

    hit_matrix = [[0 for _ in range(dim)] for _ in range(dim)]

    num_draws = 0
    for num in draws:
        num_draws += 1
        for i in range(dim):
            for j in range(dim):
                if board[i][j] == num:
                    hit_matrix[i][j] = 1

        if check_win(hit_matrix):
            unmarked_numbers = []
            for i in range(dim):
                for unmarked in [
                    x for j, x in enumerate(board[i]) if hit_matrix[i][j] == 0
                ]:
                    unmarked_numbers.append(unmarked)

            return {
                "Number of Draws until Win": num_draws,
                "Last number drawn": num,
                "Sum of unmarked numbers": sum(unmarked_numbers),
            }


if __name__ == "__main__":
    with open("data/day4.txt") as f:
        inp = [x.split("\n") for x in f.read().split("\n\n")]

    draws = [int(x) for x in inp[0][0].split(",")]
    boards = [
        [[int(z) for z in re.split("\s+", x.strip())] for x in y] for y in inp[1:]
    ]

    results = [play_bingo(b, draws) for b in boards]

    num_draws_until_win = [r["Number of Draws until Win"] for r in results]

    first = results[num_draws_until_win.index(min(num_draws_until_win))]
    print("Part 1:", first["Last number drawn"] * first["Sum of unmarked numbers"])

    last = results[num_draws_until_win.index(max(num_draws_until_win))]
    print("Part 2:", last["Last number drawn"] * last["Sum of unmarked numbers"])
