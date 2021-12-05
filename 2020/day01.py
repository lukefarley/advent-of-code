if __name__ == "__main__":
    f = open("data/day01.txt")
    x = f.readlines()
    x = [int(xi.strip("\n")) for xi in x]

    print("Part 1:")
    for i in x:
        for j in x:
            if i + j == 2020:
                print(i, j)
                print(i * j)

    print("Part 2:")
    for i in x:
        for j in x:
            for k in x:
                if i + j + k == 2020:
                    print(i, j, k)
                    print(i * j * k)
