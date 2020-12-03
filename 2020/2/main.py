class PasswordPhilosophy:
    def __init__(self):
        self.values = []
        with open("2020/2/input.txt", "r") as file:
            contents = file.readlines()
        contents = [x.strip() for x in contents]
        for x in contents:
            raw = x.split()
            self.values.append([
                raw[0].split("-")[0], raw[0].split("-")[1], raw[1].strip(":"), raw[2]
            ])

    def get_valid_password_count(self, fn):
        count = 0
        for value in self.values:
            if fn(int(value[0]), int(value[1]), value[2], value[3]):
                count += 1
        return count

    def get_valid_password_count_one(self):
        return self.get_valid_password_count(
            lambda min, max, letter, password:
            password.count(letter) in range(min, max + 1)
        )

    def get_valid_password_count_two(self):
        return self.get_valid_password_count(
            lambda min, max, letter, password:
            password[min-1] == letter and password[max-1] != letter or \
            password[min-1] != letter and password[max-1] == letter
        )

if __name__ == "__main__":
    task = PasswordPhilosophy()
    print(f"Solution to first part: {task.get_valid_password_count_one()}")
    print(f"Solution to second part: {task.get_valid_password_count_two()}")
