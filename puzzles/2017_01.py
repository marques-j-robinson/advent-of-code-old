from util.base_solution import BaseSolution


class Solution(BaseSolution):

    def __init__(self):
        self.year = 2017
        self.day = 1

    def translate(self):
        self.int_list()

    def part_01(self):
        prev = self.data[len(self.data) - 1]
        for x in self.data:
            if prev == x:
                self.p1 += x
            prev = x

    def part_02(self):
        half = len(self.data) // 2
        for idx, x in enumerate(self.data):
            if idx + half > len(self.data) - 1:
                half_i = self.data[idx - half]
            else:
                half_i = self.data[idx + half]
            if half_i == x:
                self.p2 += x


if __name__ == '__main__':
    s = Solution()
    s.solve()
