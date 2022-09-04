import string
import operator
from utils.data_translations import DataTranslations


class Solution(DataTranslations):

    def __init__(self, puzzle_input):
        self.p1 = 0
        self.p2 = 0
        self.data = puzzle_input
        self.real_rooms = []

    def translate(self):
        self.split_by_new_line()

    def parse_line(self, words):
        [selector_id, check_sum] = words.pop().split('[')
        selector_id = int(selector_id)
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

    def part1(self):
        for line in self.data:
            [words, selector_id, check_sum] = self.parse_line(line.split('-'))
            letters = self.track_letters(words)
            test_check_sum = self.prepare_check_sum(letters)
            if test_check_sum == check_sum:
                self.p1 += selector_id
                self.real_rooms.append([words, selector_id])

    def cesar(self, text, s):
        res = ""
        for i in range(len(text)):
            char = text[i]
            res += chr((ord(char) + s - 97) % 26 + 97)
        return res

    def part2(self):
        for line in self.real_rooms:
            [words, shift_value] = line
            real_name = ''
            for w in words:
                real_name += self.cesar(w, shift_value)
                real_name += ' '
            real_name.strip()
            if 'north' in real_name or 'pole' in real_name:
                self.p2 = shift_value
