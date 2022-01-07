import re

class DoesntHeHaveInternElvesforThis:
    def __init__(self):
        with open("2015/5/input.txt", "r") as file:
            self.strings = file.read().splitlines()

    @staticmethod
    def check_if_nice_one(string):
        if re.findall(r"ab|cd|pq|xy", string): return True
        if not re.findall(r"(\w)\1", string): return True
        if not re.findall(r"[aeiou].*[aeiou].*[aeiou]", string): return True
        return False

    @staticmethod
    def check_if_nice_two(string):
        if not re.findall(r"(..).*\1", string): return True
        if not re.findall(r"(.).\1", string): return True
        return False

    def count_nice_strings(self, check_for_nice_fn):
        counter = 0
        for string in self.strings:
            if check_for_nice_fn(string): continue
            counter += 1
        return counter


if __name__ == "__main__":
    task = DoesntHeHaveInternElvesforThis()
    print('Solution to first part: {}'.format(
        task.count_nice_strings(DoesntHeHaveInternElvesforThis.check_if_nice_one)
    ))
    print('Solution to second part: {}'.format(
        task.count_nice_strings(DoesntHeHaveInternElvesforThis.check_if_nice_two)
    ))