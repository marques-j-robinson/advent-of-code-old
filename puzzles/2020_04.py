import re
from util.base_solution import BaseSolution


req_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


validations = {
    "byr": lambda year: len(year) == 4 and 1920 <= int(year) <= 2002,
    "iyr": lambda year: len(year) == 4 and 2010 <= int(year) <= 2020,
    "eyr": lambda year: len(year) == 4 and 2020 <= int(year) <= 2030,
    "hgt": lambda i: check_height(i),
    "hcl": lambda val: re.match(r"^#[0-9a-f]{6}$", val),
    "ecl": lambda val: val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda val: re.match(r"^[0-9]{9}$", val),
    "cid": lambda val: True,
}


def check_height(i):
    re_res = re.match(r"(\d*)([a-z]*)", i)
    val = int(re_res.group(1))
    unit = re_res.group(2)
    if unit != "cm" and unit != "in":
        return False
    if unit == "cm":
        return 150 <= val <= 193
    elif unit == "in":
        return 59 <= val <= 76


class Solution(BaseSolution):

    def __init__(self):
        self.year = 2020
        self.day = 4

    def translate(self):
        self.split_by_empty_line()

    def part_01(self):
        for l in self.data:
            passport = {}
            keys = []
            for item in l:
                [k,v] = item.split(":")
                keys.append(k)
                passport[k] = v
            if len(keys) == 8 or sorted(keys) == sorted(req_keys):
                self.p1 += 1

    def part_02(self):
        for l in self.data:
            passport = {}
            keys = []
            valid = True
            for item in l:
                [k,v] = item.split(":")
                keys.append(k)
                passport[k] = v
            for k in req_keys:
               if valid:
                    valid = k in passport.keys() and validations[k](passport[k])
            if valid:
                self.p2 += 1


if __name__ == '__main__':
    s = Solution()
    s.solve()
