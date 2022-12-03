tst = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""".split(
    "\n"
)


import itertools
import functools
import operator


class Octopus:
    def __init__(self, energy):
        self.energy = energy
        self.flashed = 0
        # self.flashed = 0

    # def step(self):
    #     if self.energy == 0:
    #         # if self.flashed == 0:
    #         self.energy += 1
    #     elif self.energy < 9:
    #         self.energy += 1
    #     else:
    #         self.energy = 0
    #         # self.flashed = 1
    def step(self):
        if self.energy < 9:
            self.energy += 1
        else:
            self.energy = 0

    def __str__(self):
        print(str(self.energy))


class Grid:
    def __init__(self, initial_vals):
        self.octopi = [
            [Octopus(int(initial_vals[i][j])) for j in range(len(initial_vals))]
            for i in range(len(initial_vals[0]))
        ]
        self.num_flashes = 0

    def _step(self, i, j):
        # step the octopus at position (i, j)
        # if the octopus flashes, step all of it's valid neighbors
        if self.octopi[j][i].flashed == 0:
            start_val = self.octopi[j][i].energy
            self.octopi[j][i].step()

            if start_val == 9:
                self.octopi[j][i].flashed = 1
                self.num_flashes += 1

                # print(self.get_adjacent_positions(i, j))
                for ii, jj in self.get_adjacent_positions(i, j):
                    self._step(ii, jj)

    def step(self):
        for i in range(10):
            for j in range(10):
                self.octopi[j][i].flashed = 0
        for i in range(10):
            for j in range(10):
                self._step(i, j)
                # self.num_flashes += sum([o.flashed for o in functools.reduce(operator.add, self.octopi)])

    # def step(self):
    #     for i in range(len(self.octopi[0])):
    #         for j in range(len(self.octopi)):
    #             self.octopi[j][i].step()

    #     # then, step each octopus again based on how many octopi of energy 0 they are adjacent to
    #     while any([o.energy == 0 for o in functools.reduce(operator.add, self.octopi)]):
    #         for i in range(len(self.octopi[0])):
    #             for j in range(len(self.octopi)):
    #                 adjacent = self.get_adjacent_energies(i, j)
    #                 num_adjacent_zeros = sum([x == 0 for x in adjacent])
    #                 for _ in range(num_adjacent_zeros):
    #                     self.octopi[j][i].step()

    def get_adjacent_positions(self, i, j):
        adjacent_positions = [
            (i, j - 1),
            (i, j + 1),
            (i - 1, j),
            (i + 1, j),
            (i - 1, j - 1),
            (i - 1, j + 1),
            (i + 1, j - 1),
            (i + 1, j + 1),
        ]
        valid_adjacent_positions = [
            ap for ap in adjacent_positions if self.check_valid_pos(ap[0], ap[1])
        ]

        return valid_adjacent_positions

    def get_adjacent_energies(self, i, j):

        adjacent_positions = [
            (i, j - 1),
            (i, j + 1),
            (i - 1, j),
            (i + 1, j),
            (i - 1, j - 1),
            (i - 1, j + 1),
            (i + 1, j - 1),
            (i + 1, j + 1),
        ]
        # print(adjacent_positions)

        valid_adjacent_positions = [
            ap for ap in adjacent_positions if self.check_valid_pos(ap[0], ap[1])
        ]
        # print(valid_adjacent_positions)

        adjacent_energies = []
        for ki, kj in valid_adjacent_positions:
            if self.check_valid_pos(ki, kj):
                adjacent_energies.append(self.octopi[kj][ki].energy)

        return adjacent_energies

    def check_valid_pos(self, i, j):
        return i >= 0 and i < len(self.octopi[0]) and j >= 0 and j < len(self.octopi)

    def print(self):
        return [[self.octopi[j][i].energy for i in range(10)] for j in range(10)]


g = Grid(tst)
for _ in range(100):
    for i in range(10):
        for j in range(10):
            g.octopi[j][i].flashed = 0
    g.step()

if __name__ == "__main__":
    with open("data/day11.txt") as f:
        raw = [x.strip() for x in f.readlines()]

    g = Grid(raw)
    for k in range(500):
        for i in range(10):
            for j in range(10):
                g.octopi[j][i].flashed = 0
        g.step()

        if k > 100:
            if (
                sum([o.flashed for o in functools.reduce(operator.add, g.octopi)])
                == 100
            ):
                print(k)
