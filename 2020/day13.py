import functools
import operator

with open("data/day_13_input.txt") as f:
    s = f.read().split("\n")
    my_time = int(s[0])
    buses = s[1].split(",")

idx = [buses.index(x) for x in buses if x != "x"]
buses = [int(x) for x in buses if x != "x"]

# part 1
part1 = [bus - (my_time % bus) for bus in buses]
print("Part 1:", min(part1) * buses[part1.index(min(part1))])

# part 2
t = buses[0]
for i in range(len(buses) - 1):
    p = functools.reduce(operator.mul, buses[: i + 1])
    q = 1
    while True:
        next_num = t + (p * q)
        if next_num % buses[i + 1] == buses[i + 1] - (idx[i + 1] % buses[i + 1]):
            t = next_num
            if i == len(buses) - 2:
                print("Part 2:", next_num)
            break
        q += 1
