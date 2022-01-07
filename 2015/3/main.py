class PerfectlySphericalHousesinaVacuum:
    def __init__(self):
        with open("2015/3/input.txt", "r") as f:
            self.directions = f.read().strip()

    def calculate_turn(self, move, data):
        if move == "^": data["y"] -= 1
        if move == "v": data["y"] += 1
        if move == "<": data["x"] -= 1
        if move == ">": data["x"] += 1

        data["turns"].add((data["x"], data["y"]))

    def solution_one(self):
        data = {"x": 0, "y": 0, "turns": {(0, 0)}}

        for move in self.directions:
            self.calculate_turn(move, data)

        return len(data["turns"])

    def solution_two(self):
        data = {
            "santa": {"x": 0, "y": 0, "turns": {(0, 0)}},
            "robo_santa": {"x": 0, "y": 0, "turns": {(0, 0)}}
        }

        for turn, move in enumerate(self.directions):
            self.calculate_turn(move, data["santa"] if turn % 2 else data["robo_santa"])

        return len(data["santa"]["turns"] | data["robo_santa"]["turns"])


if __name__ == "__main__":
    task = PerfectlySphericalHousesinaVacuum()
    print(f"Solution to first part: {task.solution_one()}")
    print(f"Solution to second part: {task.solution_two()}")
