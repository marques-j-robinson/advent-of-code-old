from util.base_solution import BaseSolution


class Solution(BaseSolution):

    def __init__(self):
        self.year = 2020
        self.day = 6

    def translate(self):
        self.split_by_empty_line()

    def part_01(self):
        for l in self.data:
            group_set = set()
            every_set = set()
            for idx, s in enumerate(l):
                for i in s:
                    group_set.add(i)
                    count = 1
                    for s2 in l[idx+1:]:
                        if i in s2:
                            count += 1
                    if count == len(l):
                        every_set.add(i)
            self.p1 += len(group_set)

    def part_02(self):
        for l in self.data:
            group_set = set()
            every_set = set()
            for idx, s in enumerate(l):
               for i in s:
                    group_set.add(i)
                    count = 1
                    for s2 in l[idx+1:]:
                        if i in s2:
                            count += 1
                    if count == len(l):
                        every_set.add(i)
            self.p2 += len(every_set)


if __name__ == '__main__':
    s = Solution()
    s.solve()
