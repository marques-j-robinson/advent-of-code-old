from utils.data_translations import DataTranslations


class Solution(DataTranslations):

    def __init__(self, puzzle_input):
        self.p1 = 0
        self.p2 = 0
        self.data = puzzle_input

    def translate(self):
        self.int_list()

    def part1(self):
        prev = self.data[len(self.data) - 1]
        for x in self.data:
            if prev == x:
                self.p1 += x
            prev = x

    def part2(self):
        half = len(self.data) // 2
        for idx, x in enumerate(self.data):
            if idx + half > len(self.data) - 1:
                half_i = self.data[idx - half]
            else:
                half_i = self.data[idx + half]
            if half_i == x:
                self.p2 += x
