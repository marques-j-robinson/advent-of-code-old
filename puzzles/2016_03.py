from util.base_solution import BaseSolution


def compare(a, b, c):
    return a+b>c and a+c>b and b+c>a


class Solution(BaseSolution):

    def __init__(self):
        self.year = 2016
        self.day = 3

    def translate(self):
        self.split_by_new_line()
        self.data = [[int(i) for i in l.strip().split()] for l in self.data]

    def part_01(self):
        for l in self.data:
            [a, b, c] = l
            if compare(a, b,c) is True:
                self.p1 += 1

    def part_02(self):
        pass


if __name__ == '__main__':
    s = Solution()
    s.solve()
