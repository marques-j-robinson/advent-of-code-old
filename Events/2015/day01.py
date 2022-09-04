from utils.data_translations import DataTranslations


def step(i):
    if i == '(':
        return 1
    else:
        return -1


class Solution(DataTranslations):

    def __init__(self, puzzle_input):
        self.p1 = 0
        self.p2 = 0
        self.data = puzzle_input

    def part1(self):
        for i in self.data:
            self.p1 += step(i)

    def part2(self):
        cur_floor = 0
        for idx, i in enumerate(self.data):
            if cur_floor == -1 and self.p2 == 0:
                self.p2 = idx
            cur_floor += step(i)
