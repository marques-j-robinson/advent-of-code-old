import operator
from util.base_solution import BaseSolution


class Solution(BaseSolution):

    def __init__(self):
        self.year = 2016
        self.day = 4

    def translate(self):
        self.split_by_new_line()

    def parse_line(self, words):
        [selector_id, check_sum] = words.pop().split('[')
        check_sum = check_sum[:-1]
        return [words, selector_id, check_sum]

    def track_letters(self, words):
        letters = {}
        for w in words:
            for l in w:
                if l not in letters:
                    letters[l] = 1
                else:
                    letters[l] += 1
        alphabetized_letters_asc = sorted(letters)
        letters_alphabetized = {key:letters[key] for key in alphabetized_letters_asc}
        return dict(sorted(letters_alphabetized.items(), key=operator.itemgetter(1), reverse=True))

    def prepare_check_sum(self, letters):
        check_sum = ''
        for k in letters:
            if len(check_sum) < 5:
                check_sum += k
        return check_sum

    def part_01(self):
        for line in self.data:
            [words, selector_id, check_sum] = self.parse_line(line.split('-'))
            letters = self.track_letters(words)
            test_check_sum = self.prepare_check_sum(letters)
            if test_check_sum == check_sum:
                self.p1 += int(selector_id)

    def part_02(self):
        pass


if __name__ == '__main__':
    s = Solution()
    s.solve()
