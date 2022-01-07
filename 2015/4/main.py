import hashlib

class TheIdealStockingStuffer:
    def __init__(self):
        with open("2015/4/input.txt", "r") as f:
            self.secret_key = f.read().strip()

    def find_lowest_positive_number(self, starts_with):
        number = 0
        while True:
            hash = hashlib.md5(f"{self.secret_key}{number}".encode()).hexdigest()
            if hash.startswith(starts_with):
                return number
            number += 1

if __name__ == "__main__":
    task = TheIdealStockingStuffer()
    print(f'Solution to first part: {task.find_lowest_positive_number("00000")}')
    print(f'Solution to second part: {task.find_lowest_positive_number("000000")}')
