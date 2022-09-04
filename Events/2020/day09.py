from utils.data_translations import DataTranslations


class Solution(DataTranslations):

    def __init__(self, puzzle_input):
        self.p1 = 0
        self.p2 = 0
        self.data = puzzle_input
        self.l = 25

    def translate(self):
        self.split_by_new_line()
        self.int_list()

    def part1(self):
        idx = 0

        while idx < len(self.data):
            s = self.data[idx:idx+self.l]
            if idx+self.l < len(self.data):
                n = self.data[idx+self.l]
                found = False
                for i in s:
                    for j in s:
                        if i+j == n:
                            found = True
                if found == False:
                    self.p1 = n
            idx += 1

    def part2(self):
        idx = 0

        while idx < len(self.data):
            s = self.data[idx:idx+self.l]
            if idx+self.l < len(self.data):
                n = self.data[idx+self.l]
                found = False
                for i in s:
                    for j in s:
                        if i+j == n:
                            found = True
                if found == False:
                    front_idx = 0
                    back_idx = 1
                    while front_idx < len(self.data):
                        s = [self.data[front_idx]]
                        for i in self.data[back_idx:]:
                            s.append(i)
                            if sum(s) == n:
                                self.p2 = min(s) + max(s)
                        front_idx += 1
                        back_idx += 1
            idx += 1
