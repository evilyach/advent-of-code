class TobogganTrajectory:
    def __init__(self):
        with open("2020/3/input.txt", "r") as file:
            contents = file.readlines()
        self.map = [x.strip() for x in contents]

    def count_trees(self, X, Y):
        x, y, trees, length = 0, 0, 0, len(self.map[0]) - 1
        while y < len(self.map):
            trees += 1 if self.map[y][x] == "#" else 0
            x = ((x + X) % length) - 1 if length - X - 1 < x <= length - 1 else x + X
            y += Y
        return trees

    def count_trees_one(self):
        return self.count_trees(3, 1)

    def count_trees_two(self):
        return self.count_trees(1, 1) * self.count_trees(3, 1) * \
            self.count_trees(5, 1) * self.count_trees(7, 1) * self.count_trees(1, 2)

if __name__ == "__main__":
    task = TobogganTrajectory()
    print(f"Solution to first part: {task.count_trees_one()}")
    print(f"Solution to second part: {task.count_trees_two()}")
