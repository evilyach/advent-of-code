class IWasToldThereWouldBeNoMath:
    def __init__(self):
        with open("2015/2/input.txt", "r") as f:
            self.sizes = [sorted([int(i) for i in line.strip().split("x")]) for line in f.readlines()]

    def find_total(self, count):
        sum = 0
        for package in self.sizes:
            sum += count(*package)
        return sum

    def find_total_paper_area(self):
        return self.find_total(lambda x, y, z: 3*x*y + 2*y*z + 2*x*z)

    def find_total_ribbon_length(self):
        return self.find_total(lambda x, y, z: 2*x + 2*y + x*y*z)

if __name__ == "__main__":
    task = IWasToldThereWouldBeNoMath()
    print(f"Solution to first part: {task.find_total_paper_area()}")
    print(f"Solution to second part: {task.find_total_ribbon_length()}")
