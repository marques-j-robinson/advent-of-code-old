from utils.data_translations import DataTranslations


class Solution(DataTranslations):

    def __init__(self, puzzle_input):
        self.p1 = 0
        self.p2 = 0
        self.data = puzzle_input

    def translate(self):
        self.data = [list(line.strip()) for line in self.data.split('\n')]

    def is_tree(self, r, c):
        return self.data[r][c%len(self.data[r])] == '#'

    def part1(self):
        r = 0
        c = 0
        while r+1 < len(self.data):
            c += 3
            r += 1
            if self.is_tree(r, c):
                self.p1 += 1

    def part2(self):
        self.p2 = 1
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        for (dc, dr) in slopes:
            r = 0
            c = 0
            score = 0
            while r+1 < len(self.data):
                c += dc
                r += dr
                if self.is_tree(r, c):
                    score += 1
            self.p2 *= score
