from utils.data_translations import DataTranslations


class Solution(DataTranslations):

    def __init__(self, puzzle_input):
        self.p1 = 0
        self.p2 = 0
        self.data = puzzle_input

    def translate(self):
        self.split_by_new_line()
        self.int_list()

    def part1(self):
        for i in self.data:
            self.p1 += i

    def part2(self):
        freq = 0
        seen = []
        idx = 0
        while self.p2 == 0:
            correct_idx = idx % len(self.data)
            i = self.data[correct_idx]
            if freq in seen:
                self.p2 = freq
                break
            else:
                seen.append(freq)
            freq += i
            idx += 1
