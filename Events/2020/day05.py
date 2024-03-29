import math
from utils.data_translations import DataTranslations


def find_missing(lst):
    return sorted(set(range(lst[0], lst[-1])) - set(lst))


def calc_hi(lo, hi):
    return math.floor((hi+lo)/2)


def calc_lo(lo, hi):
    return math.ceil((hi+lo)/2)


def get_row_id(chars):
    lo = 0
    hi = 127
    for char in chars:
        if char == "F":
            hi = calc_hi(lo, hi)
        elif char == "B":
            lo = calc_lo(lo, hi)
    return lo


def get_col_id(chars):
    lo = 0
    hi = 7
    for char in chars:
        if char == "L":
            hi = calc_hi(lo, hi)
        elif char == "R":
            lo = calc_lo(lo, hi)
    return lo


class Solution(DataTranslations):

    def __init__(self, puzzle_input):
        self.p1 = 0
        self.p2 = 0
        self.data = puzzle_input

    def translate(self):
        self.split_by_new_line()

    def part1(self):
        d = []
        for l in self.data:
            row_id = get_row_id(l[0:7])
            col_id = get_col_id(l[7:])
            score = row_id * 8 + col_id
            if score > self.p1:
                self.p1 = score
            d.append(score)

    def part2(self):
        d = []
        for l in self.data:
            row_id = get_row_id(l[0:7])
            col_id = get_col_id(l[7:])
            score = row_id * 8 + col_id
            d.append(score)
        self.p2 = find_missing(sorted(d))[0]
