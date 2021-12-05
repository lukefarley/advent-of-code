import numpy as np


def calc_gamma(diagnostic_report: np.ndarray) -> np.array:
    ncol = diagnostic_report.shape[1]

    return np.array(
        [
            int(diagnostic_report[:, j].sum() >= (len(diagnostic_report) / 2))
            for j in range(ncol)
        ]
    )


def calc_epsilon(gamma):
    return 1 - gamma


def find_rating(diagnostic_report, type):

    for i in range(len(diagnostic_report[0])):
        z = calc_gamma(diagnostic_report)
        if type == "co2":
            z = calc_epsilon(z)
        diagnostic_report = diagnostic_report[diagnostic_report[:, i] == z[i]]
        if len(diagnostic_report) == 1:
            return diagnostic_report[0]


if __name__ == "__main__":
    with open("data/day3.txt") as f:
        diagnostic_report = np.array(
            [[int(z) for z in list(x.strip())] for x in f.readlines()]
        )

    gamma = calc_gamma(diagnostic_report)
    epsilon = calc_epsilon(gamma)

    print(
        "Part 1:",
        int("".join([str(x) for x in list(gamma)]), 2)
        * int("".join([str(x) for x in list(epsilon)]), 2),
    )

    oxygen = find_rating(diagnostic_report, "oxygen")
    co2 = find_rating(diagnostic_report, "co2")

    print(
        "Part 2:",
        int("".join([str(x) for x in list(oxygen)]), 2)
        * int("".join([str(x) for x in list(co2)]), 2),
    )
