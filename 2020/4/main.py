import re, string
class PassportProcessing:
    def __init__(self):
        with open("2020/4/input.txt", "r") as f:
            self.passports = [dict(re.findall(r"(\S+):(\S+)", x))
            for x in [x.replace("\n", " ") for x in f.read().split("\n\n")]]
        self.requirements = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    def validate_passport(self, passport):
        return (
            all(req in passport for req in self.requirements) and \
            1920 <= int(passport["byr"]) <= 2002 and 2010 <= int(passport["iyr"]) <= 2020 and \
            2020 <= int(passport["eyr"]) <= 2030 and len(passport["pid"]) == 9 and ( \
                passport["hgt"][-2:] == "cm" and 150 <= int(passport["hgt"][:-2]) <= 193 or \
                passport["hgt"][-2:] == "in" and 59 <= int(passport["hgt"][:-2]) <= 76
            ) and passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] and \
            passport["hcl"][:1] == "#" and set(passport["hcl"][1:]).issubset(string.hexdigits)
        )

    def count_valid_passports_one(self):
        valid = 0
        for passport in self.passports:
            valid += 1 if all(req in passport for req in self.requirements) else 0
        return valid

    def count_valid_passports_two(self):
        valid = 0
        for passport in self.passports:
            valid += 1 if self.validate_passport(passport) else 0
        return valid

if __name__ == "__main__":
    task = PassportProcessing()
    print(f"Solution to first part: {task.count_valid_passports_one()}")
    print(f"Solution to second part: {task.count_valid_passports_two()}")
