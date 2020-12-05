class BinaryBoarding:
    def __init__(self):
        with open("2020/5/input.txt", "r") as file:
            self.seats = file.read().splitlines()
        self.ids = [self.decode(x, True) for x in self.seats]

    def decode(self, seat, weird=False):
        decoded = seat.translate(
            str.maketrans({"F": "0", "B": "1", "R": "1", "L": "0"})
        ) if weird else seat
        return int(decoded[:-3], 2) * 8 + int(decoded[-3:], 2)

    def find_highest(self):
        return max(self.ids)

    def find_mine(self):
        for i in range(0, 128):
            for j in range(0, 8):
                id = self.decode((f"{i:7b}" + f"{j:3b}").replace(" ", "0"))
                if id not in self.ids and id + 1 in self.ids and id - 1 in self.ids:
                    return id

if __name__ == "__main__":
    task = BinaryBoarding()
    print(f"Solution to first part: {task.find_highest()}")
    print(f"Solution to second part: {task.find_mine()}")
