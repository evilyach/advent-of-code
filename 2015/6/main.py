from collections import namedtuple
from enum import Enum
from typing import NamedTuple

Action = Enum("Action", "on off toggle")
Coords = namedtuple("Coords", "x y")
Command = NamedTuple("Command", action=Action, start_coords=Coords, end_coords=Coords)


class ProbablyaFireHazard:
    size = 1000

    def __init__(self, filename: str) -> None:
        self.commands = []

        with open(filename, "r") as file:
            for string in file.read().splitlines():
                match string.split():
                    case ["turn", action, start_coords, "through", end_coords]:
                        action = Action.on if action == "on" else Action.off
                    case ["toggle", start_coords, "through", end_coords]:
                        action = Action.toggle

                command = Command(
                    action,
                    self.str_to_coords(start_coords),
                    self.str_to_coords(end_coords),
                )
                self.commands.append(command)

    def str_to_coords(self, string: str) -> Coords:
        coords = (int(x) for x in string.split(","))
        return Coords(*coords)

    def first(self) -> int:
        self.grid = {(x, y): False for y in range(self.size) for x in range(self.size)}

        for command in self.commands:
            for x in range(command.start_coords.x, command.end_coords.x + 1):
                for y in range(command.start_coords.y, command.end_coords.y + 1):
                    if command.action == Action.on:
                        self.grid[(x, y)] = True
                    elif command.action == Action.off:
                        self.grid[(x, y)] = False
                    else:
                        self.grid[(x, y)] = not self.grid[(x, y)]

        return list(self.grid.values()).count(True)

    def second(self) -> int:
        self.grid = {(x, y): 0 for y in range(self.size) for x in range(self.size)}

        for command in self.commands:
            for x in range(command.start_coords.x, command.end_coords.x + 1):
                for y in range(command.start_coords.y, command.end_coords.y + 1):
                    if command.action == Action.on:
                        self.grid[(x, y)] += 1
                    elif command.action == Action.off:
                        if self.grid[(x, y)] > 0:
                            self.grid[(x, y)] -= 1
                    else:
                        self.grid[(x, y)] += 2

        return sum(self.grid.values())


if __name__ == "__main__":
    app = ProbablyaFireHazard("2015/6/input.txt")

    print(f"First task: {app.first()}")
    print(f"Second task: {app.second()}")
