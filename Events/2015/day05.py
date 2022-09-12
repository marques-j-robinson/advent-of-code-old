from utils.solution import BaseSolution
from utils.string_validation import Validation


class Solution(BaseSolution):

    def format_data(self):
        self.split_by_new_line()

    def part1(self):
        forbidden = ['ab', 'cd', 'pq', 'xy']
        for l in self.data:
            v = Validation(l)
            if v.vowel_count() and v.dup_letters() and v.check_forbidden(forbidden):
                self.p1 += 1

    def part2(self):
        for l in self.data:
            v = Validation(l)
            if v.dup_pairs() and v.repeat_every_other_letter():
                self.p2 += 1
