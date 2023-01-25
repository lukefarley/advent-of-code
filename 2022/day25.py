def snafu_to_decimal(snafu):

    length = len(snafu)

    snafu_factor = {"0": 0, "1": 1, "2": 2, "-": -1, "=": -2}

    decimal = 0

    k = 0
    for i in range(length - 1, -1, -1):
        decimal += 5 ** i * snafu_factor[snafu[k]]
        k += 1

    return decimal


def decimal_to_snafu(decimal):

    remainders = []
    while decimal > 0:
        remainders.append(decimal % 5)
        decimal = decimal // 5

    snafu_str = ""
    i = 0
    for i in range(len(remainders)):
        remainder = remainders[i]
        if remainder == 3:
            remainders[i + 1] += 1
            snafu_str = "=" + snafu_str
        elif remainder == 4:
            remainders[i + 1] += 1
            snafu_str = "-" + snafu_str
        elif remainder == 5:
            remainders[i + 1] += 1
            snafu_str = "0" + snafu_str
        else:
            snafu_str = str(remainder) + snafu_str
        i += 1
        snafu_str

    return snafu_str


if __name__ == "__main__":

    with open("data/day25.txt") as f:
        snafu_nums = [x.strip() for x in f.readlines()]

    num = sum([snafu_to_decimal(snafu) for snafu in snafu_nums])
    print("Part 1:", decimal_to_snafu(num))
