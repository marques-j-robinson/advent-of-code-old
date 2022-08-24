from util.base_solution import BaseSolution


vowels = 'aeiou'
forbidden_strings = ['ab', 'cd', 'pq', 'xy']


class Validation:

    def __init__(self, val):
        self.val = val

    def vowel_count(self):
        count = 0
        for l in self.val:
            if l in vowels:
                count += 1
        return count >= 3

    def dup_letters(self):
        res = False
        for idx, l in enumerate(self.val):
            if idx > 0:
                if self.val[idx-1] == l:
                    res = True
        return res

    def check_forbidden(self):
        res = True
        for s in forbidden_strings:
            if s in self.val:
                res = False
        return res

    def dup_pairs(self):
        res = False
        for idx, l in enumerate(self.val):
            if idx > 0:
                pair = f"{self.val[idx - 1]}{l}"
                if pair in self.val[idx + 1:]:
                    res = True
        return res

    def repeat_every_other_letter(self):
        res = False
        for idx, l in enumerate(self.val):
            if idx > 1:
                prev = self.val[idx - 2]
                if prev == l:
                    res = True
        return res


class Solution(BaseSolution):

    def __init__(self):
        self.year = 2015
        self.day = 5

    def translate(self):
        self.split_by_new_line()

    def part_01(self):
        for l in self.data:
            v = Validation(l)
            if v.vowel_count() and v.dup_letters() and v.check_forbidden():
                self.p1 += 1

    def part_02(self):
        for l in self.data:
            v = Validation(l)
            if v.dup_pairs() and v.repeat_every_other_letter():
                self.p2 += 1


if __name__ == '__main__':
    s = Solution()
    s.solve()
