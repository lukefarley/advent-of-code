def find_first_group_with_distinct_chars(buffer, n):
    for i in range(len(buffer) - n + 1):
        group = buffer[i : i + n]
        unique_chars = "".join(set(group))

        if len(group) == len(unique_chars):
            return i + n


if __name__ == "__main__":
    with open("data/day06.txt") as f:
        buffer = f.read()

    print("Part 1:", find_first_group_with_distinct_chars(buffer, 4))
    print("Part 2:", find_first_group_with_distinct_chars(buffer, 14))
