class ReportRepair:
    def __init__(self):
        with open("2020/1/input.txt", "r") as file:
            contents = file.readlines()
        self.values = [int(x.strip()) for x in contents]

    def find_2020_from_two(self):
        for i in range(len(self.values)):
            for j in range(len(self.values)):
                if self.values[i] + self.values[j] == 2020:
                    return self.values[i] * self.values[j]

    def find_2020_from_three(self):
        for i in range(len(self.values)):
            for j in range(len(self.values)):
                for k in range(len(self.values)):
                    if self.values[i] + self.values[j] + self.values[k] == 2020:
                        return self.values[i] * self.values[j] * self.values[k]


if __name__ == "__main__":
    task = ReportRepair()
    print(f"Solution to first part: {task.find_2020_from_two()}")
    print(f"Solution to second part: {task.find_2020_from_three()}")
