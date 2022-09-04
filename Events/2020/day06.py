from utils.data_translations import DataTranslations


class Solution(DataTranslations):

    def __init__(self, puzzle_input):
        self.p1 = 0
        self.p2 = 0
        self.data = puzzle_input

    def translate(self):
        self.split_by_empty_line()

    def part1(self):
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

    def part2(self):
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
