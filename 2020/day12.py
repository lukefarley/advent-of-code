TEST = """F10
N3
F7
R90
F11"""


class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.facing = "E"
        self.waypoint_x = 10
        self.waypoint_y = 1

    def _translate2(self, command):
        val = int(command[1:])
        print("translate2 called")
        if command[0] == "F":
            self.x += self.waypoint_x * val
            self.y += self.waypoint_y * val

        return self

    def _move_waypoint(self, command):
        val = int(command[1:])
        direction_to_move = command[0]
        print("move waypoint called")
        if direction_to_move == "E":
            self.waypoint_x += val
        if direction_to_move == "N":
            self.waypoint_y += val
        if direction_to_move == "W":
            self.waypoint_x -= val
        if direction_to_move == "S":
            self.waypoint_y -= val

        return self

    def _rotate_waypoint(self, command):
        print("rotate waypoint called")
        val = int(command[1:])
        direction = command[0]
        if direction == "R":
            for _ in range(int(val / 90)):
                xcopy = self.waypoint_x
                self.waypoint_x = self.waypoint_y
                self.waypoint_y = -xcopy
        if direction == "L":
            for _ in range(int(val / 90)):
                ycopy = self.waypoint_y
                self.waypoint_y = self.waypoint_x
                self.waypoint_x = -ycopy
        return self

    def move2(self, command):
        directions = ["E", "S", "W", "N"]
        if command[0] == "F":
            return self._translate2(command)
        if command[0] in directions:
            return self._move_waypoint(command)
        if command[0] in ["L", "R"]:
            return self._rotate_waypoint(command)

    def _translate1(self, command):
        val = int(command[1:])
        directions = ["E", "S", "W", "N"]

        if command[0] == "F":
            direction_to_move = self.facing
        elif command[0] in directions:
            direction_to_move = command[0]

        if direction_to_move == "E":
            self.x += val
        if direction_to_move == "N":
            self.y += val
        if direction_to_move == "W":
            self.x -= val
        if direction_to_move == "S":
            self.y -= val

        return self

    def _rotate1(self, command):
        val = int(command[1:])
        directions = ["E", "S", "W", "N"]
        if command[0] == "R":
            self.facing = directions[
                int((directions.index(self.facing) + (val / 90)) % 4)
            ]
        if command[0] == "L":
            self.facing = directions[
                int((directions.index(self.facing) - (val / 90)) % 4)
            ]
        return self

    def move1(self, command):
        directions = ["E", "S", "W", "N"]

        if command[0] == "F" or command[0] in directions:
            return self._translate1(command)
        elif command[0] in ["L", "R"]:
            return self._rotate1(command)

        return self


with open("data/day12.txt") as f:
    commands = f.read().strip().split("\n")

# commands = TEST.split("\n")

ship = Ship()
for c in commands:
    print("ship:", ship.x, ship.y, "waypoint:", ship.waypoint_x, ship.waypoint_y)
    print(c)
    ship.move2(c)

print(ship.x, ship.y, abs(ship.x) + abs(ship.y))
