def check_valid(num, previous):
    for x in range(1, len(previous)):
        for y in range(x, len(previous)):
            if previous[x] == previous[y]:
                continue
            if previous[x] + previous[y] == num:
                return True
    return False


def check_contiguous_sum(target, numbers, window=2):
    numbers = [n for n in numbers if n < target]
    for i in range(len(numbers) - (window - 1)):
        # print(i)
        if sum(numbers[i : i + window]) == target:
            return True, sum(numbers[i : i + window])
    return False, 0


if __name__ == "__main__":
    with open("data/day09.txt") as f:
        numbers = [int(x.strip("\n")) for x in f.readlines()]

    # results = []
    # start = 25
    # for cutoff in range(start, len(numbers)):
    #     print(cutoff)
    #     previous = numbers[:cutoff]
    #     x = numbers[cutoff]
    #     last_valid = check_valid(x, previous)
    #     results.append(last_valid)
    #     if not last_valid:
    #         print()
    #         print("Not valid:", x)
    #         break

    target = 26134589
    for window in range(50):
        print(window)
        print(check_contiguous_sum(target, numbers, window=window))
