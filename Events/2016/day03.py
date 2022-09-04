from utils.data_translations import DataTranslations


def compare(lengths):
    [a, b, c] = [int(i) for i in lengths]
    return a+b>c and a+c>b and b+c>a


def should_reset(val):
    return val % 3 == 0


class Solution(DataTranslations):

    def __init__(self, puzzle_input):
        self.p1 = 0
        self.p2 = 0
        self.data = puzzle_input
        self.tri_a = []
        self.tri_b = []
        self.tri_c = []

    def translate(self):
        self.split_by_new_line()
        self.data = [l.strip().split() for l in self.data]

    def reset_triangles(self):
        self.tri_a = []
        self.tri_b = []
        self.tri_c = []

    def part1(self):
        for l in self.data:
            if compare(l) is True:
                self.p1 += 1

    def part2(self):
        for idx, l in enumerate(self.data):
            [a, b, c] = l
            self.tri_a.append(a)
            self.tri_b.append(b)
            self.tri_c.append(c)
            if should_reset(idx + 1):
                if compare(self.tri_a) is True:
                    self.p2 += 1
                if compare(self.tri_b) is True:
                    self.p2 += 1
                if compare(self.tri_c) is True:
                    self.p2 += 1
                self.reset_triangles()
