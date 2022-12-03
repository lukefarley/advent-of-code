from dataclasses import dataclass

tst = [[[[[9, 8], 1], 2], 3], 4]


@dataclass
class Pair:
    left: None
    right: None
    depth: None

    def __init__(self, left, right, depth):
        self.left = left
        self.right = right
        self.depth = depth

    def __str__(self):
        return f"({self.left}, {self.right})"


def parse(x, depth=0):
    left = x[0]
    right = x[1]
    if isinstance(left, int) and isinstance(right, int):
        depth += 1
        return Pair(x[0], x[1], depth)
    elif isinstance(left, int):
        depth += 1
        return Pair(x[0], parse(x[1], depth), depth)
    elif isinstance(right, int):
        depth += 1
        return Pair(parse(x[0], depth), x[1], depth)
    else:
        depth += 1
        return Pair(parse(x[0], depth), parse(x[1], depth), depth)


p = parse(tst)


def traverse(p):
    left = p.left
    right = p.right
    depth = p.depth

    if isinstance(left, Pair):
        traverse(left)
    if isinstance(right, Pair):
        traverse(right)

    if depth >= 5:
        print("explode")


while isinstance(p.left, Pair) or isinstance(p.right, Pair):
    if p.depth >= 4:
        if isinstance(p.left, Pair):
            print("explode")
        if isinstance(p.right, Pair):
            print("explode")


# def parse(x):
#     S = deque()
#     listx = list(x)
#     i = 0
#     while listx:
#         if listx[i] == "[":
#             S.append(listx[i])
