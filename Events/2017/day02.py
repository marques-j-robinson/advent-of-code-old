from utils.data_translations import DataTranslations, int_list


class Solution(DataTranslations):

    def __init__(self, puzzle_input):
        self.p1 = 0
        self.p2 = 0
        self.data = puzzle_input

    def translate(self):
        """
        Split by new line.
        Then split each line by the TAB character and convert into a list of integers.
        """
        self.split_by_new_line()
        self.data = [int_list(l.strip().split("\t")) for l in self.data]

    def part1(self):
        for row in self.data:
            self.p1 += max(row) - min(row)

    def part2(self):
        for row in self.data:
            for idx, i in enumerate(row):
                for j in row[idx+1:]:
                    m = max([i, j])
                    n = min([i, j])
                    if m%n==0:
                        self.p2 += m//n
