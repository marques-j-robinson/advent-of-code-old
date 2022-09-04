from utils.data_translations import DataTranslations
from utils.shapes import Cube


def calc_wrapping_paper(dimensions):
    box = Cube(dimensions)
    return box.surface_area() + box.area()


def calc_ribbon(dimensions):
    box = Cube(dimensions)
    return box.perimeter() + box.volume()


class Solution(DataTranslations):

    def __init__(self, puzzle_input):
        self.p1 = 0
        self.p2 = 0
        self.data = puzzle_input

    def translate(self):
        self.split_by_new_line()

    def part1(self):
        for d in self.data:
            self.p1 += calc_wrapping_paper(d)

    def part2(self):
        for d in self.data:
            self.p2 += calc_ribbon(d)
