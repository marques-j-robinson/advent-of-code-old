from utils.solution import BaseSolution


def step(i):
    if i == '(':
        return 1
    else:
        return -1


def is_basement(floor_id):
    return floor_id == -1


class Solution(BaseSolution):

    def part1(self):
        for i in self.data:
            self.p1 += step(i)

    def part2(self):
        cur_floor = 0
        for idx, i in enumerate(self.data):
            if is_basement(cur_floor) and self.is_part2_empty():
                self.p2 = idx
            cur_floor += step(i)
