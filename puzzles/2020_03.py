from util.base_solution import BaseSolution


class Solution(BaseSolution):

    def __init__(self):
        self.year = 2020
        self.day = 3

    def translate(self):
        self.data = [list(line.strip()) for line in self.data.split('\n')]

    def part_01(self):
        r = 0
        c = 0
        while r+1 < len(self.data):
            c += 3
            r += 1
            if self.is_tree(r, c):
                self.p1 += 1

    def part_02(self):
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

    def is_tree(self, r, c):
        return self.data[r][c%len(self.data[r])] == '#'


if __name__ == '__main__':
    s = Solution()
    s.solve()
