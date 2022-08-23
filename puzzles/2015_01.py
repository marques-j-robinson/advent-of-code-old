from util.base_solution import BaseSolution


class Solution(BaseSolution):

    def __init__(self):
        self.year = 2015
        self.day = 1

    def part_01(self):
        for i in self.data:
            self.p1 += process_instruction(i)

    def part_02(self):
        x = 0
        for idx, i in enumerate(self.data):
            if x == -1 and self.p2 == 0:
                self.p2 = idx
            x += process_instruction(i)


def process_instruction(i):
    if i == '(':
        return 1
    else:
        return -1


if __name__ == '__main__':
    s = Solution()
    s.solve()
