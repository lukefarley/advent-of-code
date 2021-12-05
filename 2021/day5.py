class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)

    @classmethod
    def from_string(cls, s: str):
        spl = [x.split(",") for x in s.split(" -> ")]
        return cls(spl[0][0], spl[0][1], spl[1][0], spl[1][1])

    def get_points(self):
        if self.p1.x <= self.p2.x:
            xs = list(range(self.p1.x, self.p2.x + 1))
        else:
            xs = list(reversed(range(self.p2.x, self.p1.x + 1)))

        if self.p1.y <= self.p2.y:
            ys = list(range(self.p1.y, self.p2.y + 1))
        else:
            ys = list(reversed(range(self.p2.y, self.p1.y + 1)))

        if len(xs) == 1:
            xs = [xs[0] for _ in range(len(ys))]
        if len(ys) == 1:
            ys = [ys[0] for _ in range(len(xs))]

        return [Point(xi, yi) for xi, yi in zip(xs, ys)]

    def is_horizontal_or_vertical(self):
        if self.p1.x == self.p2.x or self.p1.y == self.p2.y:
            return True
        else:
            return False


class Grid:
    def __init__(self, size):
        self.coords = [[0 for _ in range(size)] for _ in range(size)]

    def draw_line(self, line):

        points = line.get_points()

        for p in points:
            self.coords[p.y][p.x] += 1


if __name__ == "__main__":
    with open("data/day5.txt") as f:
        raw_lines = f.read().split("\n")

    lines = [Line.from_string(l) for l in raw_lines]
    max_num = max([max((l.p1.x, l.p1.y, l.p2.x, l.p2.y)) for l in lines])

    g = Grid(max_num + 1)

    for l in [lin for lin in lines if lin.is_horizontal_or_vertical()]:
        g.draw_line(l)

    print("Part 1:", sum([sum([num >= 2 for num in row]) for row in g.coords]))

    g = Grid(max_num + 1)

    for l in lines:
        g.draw_line(l)

    print("Part 2:", sum([sum([num >= 2 for num in row]) for row in g.coords]))
