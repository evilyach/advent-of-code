class IWasToldThereWouldBeNoMath:
    def __init__(self):
        with open("2015/2/input.txt", "r") as f:
            self.sizes = [sorted([int(i) for i in line.strip().split("x")]) for line in f.readlines()]

    def find_total_paper_area(self):
        sum = 0
        for package in self.sizes:
            x, y, z = package
            sum += 3*x*y + 2*y*z + 2*x*z
        return sum

    def find_total_ribbon_length(self):
        sum = 0
        for package in self.sizes:
            x, y, z = package
            sum += 2*x + 2*y + x*y*z
        return sum

if __name__ == "__main__":
    task = IWasToldThereWouldBeNoMath()
    print(f"Solution to first part: {task.find_total_paper_area()}")
    print(f"Solution to second part: {task.find_total_ribbon_length()}")
