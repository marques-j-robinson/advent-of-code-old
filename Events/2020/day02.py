import re
from utils.data_translations import DataTranslations


regex = r"(\d*-\d*) ([a-zA-Z]): ([a-zA-Z]*)([a-zA-Z]*)"


class Validation:

    def __init__(self, data):
        res = re.match(regex, data)
        [min_i, max_i] = [int(i) for i in res.group(1).split("-")]
        self.min = min_i
        self.max = max_i
        self.letter = res.group(2)
        self.password = res.group(3)
        self.count = 0
        self.get_count()

    def get_count(self):
        for l in self.password:
            if l == self.letter:
                self.count += 1

    def check_min_count(self):
        return self.count >= self.min

    def check_max_count(self):
        return self.count <= self.max

    def has_min(self):
        return self.password[self.min -1] == self.letter

    def has_max(self):
        return self.password[self.max -1] == self.letter


class Solution(DataTranslations):

    def __init__(self, puzzle_input):
        self.p1 = 0
        self.p2 = 0
        self.data = puzzle_input

    def translate(self):
        self.split_by_new_line()

    def part1(self):
        for line in self.data:
            v = Validation(line)
            if v.check_min_count() and v.check_max_count():
                self.p1 += 1

    def part2(self):
        for line in self.data:
            v = Validation(line)
            if v.has_min() ^ v.has_max():
                self.p2 += 1
