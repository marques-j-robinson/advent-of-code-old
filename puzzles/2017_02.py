from util.base_solution import BaseSolution


class Solution(BaseSolution):

    def __init__(self):
        self.year = 2017
        self.day = 2

    def translate(self):
        self.data = [[int(x) for x in l.strip().split("\t")] for l in self.data.split("\n")]

    def part_01(self):
        for row in self.data:
            self.p1 += max(row) - min(row)

    def part_02(self):
        for row in self.data:
            for idx, i in enumerate(row):
                for j in row[idx+1:]:
                    m = max([i, j])
                    n = min([i, j])
                    if m%n==0:
                        self.p2 += m//n


if __name__ == '__main__':
    s = Solution()
    s.solve()
