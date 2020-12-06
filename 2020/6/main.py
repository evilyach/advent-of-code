class CustomCustoms:
    def __init__(self):
        with open("2020/6/input.txt", "r") as f:
            self.answers = [x.replace("\n", ";") for x in f.read().split("\n\n")]

    def get_answers_count(self, answer):
        return len(set(answer.translate(str.maketrans({";": "", " ": ""}))))

    def get_common_answers_count(self, answer):
        return len(set.intersection(*[set(l) for l in answer.split(";")]))

    def find_sum(self, fn):
        return sum((fn(answer) for answer in self.answers))

    def find_sum_one(self):
        return self.find_sum(self.get_answers_count)

    def find_sum_two(self):
        return self.find_sum(self.get_common_answers_count)

if __name__ == "__main__":
    task = CustomCustoms()
    print(f"Solution to first part: {task.find_sum_one()}")
    print(f"Solution to second part: {task.find_sum_two()}")
