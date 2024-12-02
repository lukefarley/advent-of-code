with open("data/day01.txt") as f:
    data = [x.strip().split("   ") for x in f.readlines()]

left = [int(x[0]) for x in data]
right = [int(x[1]) for x in data]

sleft = sorted(left)
sright = sorted(right)

diffs = [abs(sleft[i] - sright[i]) for i in range(len(sleft))]

print("Part 1:", sum(diffs))

left_elements = list(set(left))

result = 0
for x in left_elements:
    result += x * sum([1 for y in right if y == x])

print("Part 2:", result)
