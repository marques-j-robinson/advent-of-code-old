import pyperclip
from .puzzle_input import fetch
from .data_translations import DataTranslations
from .util import leading_zero


class BaseSolution(DataTranslations):

    def part_01(self):
        pass

    def part_02(self):
        pass

    def reset(self):
        self.p1 = 0
        self.p2 = 0
        self.data = fetch(self.year, self.day)

    def copy_to_clipboard(self):
        print(f'Solution for {self.year}_{leading_zero(self.day)}')
        print(f'Part 1: {self.p1}')
        if self.p2 == 0:
            pyperclip.copy(str(self.p1))
        else:
            print(f'Part 2: {self.p2}')
            pyperclip.copy(str(self.p2))

    def solve(self, only=None):
        self.reset()
        self.translate()
        if only == 1:
            self.part_01()
        elif only == 2:
            self.part_02()
        else:
            self.part_01()
            self.part_02()
        self.copy_to_clipboard()
