class NotQuiteLisp:
    def __init__(self, filename):
        self.filename = filename
        self.opening_par = 0
        self.closing_par = 0
        self.diff = 0


    def calc_diff(self):
        self.diff = self.opening_par - self.closing_par


    def first_half(self):
        with open(self.filename, "r") as file:
            for line in file:
                for character in line:
                    if (character is '('):
                        self.opening_par += 1
                    if (character is ')'):
                        self.closing_par += 1

        self.calc_diff()
        print(self.diff)


    def second_half(self):
        counter = 1

        with open(self.filename, "r") as file:
            for line in file:
                for character in line:
                    if (character is '('):
                        self.opening_par += 1
                    if (character is ')'):
                        self.closing_par += 1

                    self.calc_diff()

                    if (self.diff == -1):
                        print("{} at {}".format(counter, self.diff))
                        return

                    counter += 1


if __name__ == "__main__":
    solution = NotQuiteLisp('./input.txt')
    solution.first_half()
    solution.second_half()
