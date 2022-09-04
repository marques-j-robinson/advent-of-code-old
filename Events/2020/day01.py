from utils.data_translations import DataTranslations


class Solution(DataTranslations):

    def __init__(self, puzzle_input):
        self.p1 = 0
        self.p2 = 0
        self.data = puzzle_input

    def translate(self):
        self.split_by_new_line()
        self.int_list()

    def part1(self):
        for i in self.data:
            for j in self.data:
                if i+j == 2020:
                    self.p1 = i*j

    def part2(self):
        for i in self.data:
            for j in self.data:
                for k in self.data:
                    if i+j+k == 2020:
                        self.p2 = i*j*k
