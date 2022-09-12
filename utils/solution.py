import pyperclip

from .data_formats import DataFormats


class BaseSolution(DataFormats):

    def __init__(self, puzzle_input):
        self.data = puzzle_input
        self.format_data()
        self.p1 = 0
        self.p2 = 0

    def part1(self):
        pass

    def part2(self):
        pass

    def is_part2_empty(self):
        return self.p2 == 0

    def copy_solution(self):
        if self.is_part2_empty():
            print(f'Part 1: {self.p1}')
            pyperclip.copy(str(self.p1))
        else:
            print(f'Part 1: {self.p1}')
            print(f'Part 2: {self.p2}')
            pyperclip.copy(str(self.p2))

    def solve(self):
        self.part1()
        self.part2()
        self.copy_solution()
