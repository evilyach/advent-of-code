class Day1_NotQuiteLisp:
    def __init__(self, filename):
        self.filename = filename
        self.opening_par = 0
        self.closing_par = 0

    def count_par(self):
        with open(self.filename, "r") as file:
            for line in file:
                for character in line:
                    if (character is '('):
                        self.opening_par += 1
                    if (character is ')'):
                        self.closing_par += 1

    def first_half(self):
        self.count_par()
        print(self.opening_par - self.closing_par)

solution = Day1_NotQuiteLisp('./file.txt')
solution.first_half()