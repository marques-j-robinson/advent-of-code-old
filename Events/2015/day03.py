from utils.data_translations import DataTranslations
from utils.calc import combine, is_even


up = '^'
right = '>'
down = 'v'
left = '<'


class Grid:

    def __init__(self):
        orgin = '0,0'
        self.coord = orgin
        self.seen = [orgin]

    def parse_coord(self):
        return [int(i) for i in self.coord.split(',')]

    def append_coord(self):
        if self.coord not in self.seen:
            self.seen.append(self.coord)

    def move(self, d):
        [x, y] = self.parse_coord()
        if d == up:
            y += 1
        elif d == right:
            x += 1
        elif d == down:
            y -= 1
        elif d == left:
            x -= 1
        self.coord = f'{x},{y}'
        self.append_coord()


class Solution(DataTranslations):

    def __init__(self, puzzle_input):
        self.p1 = 0
        self.p2 = 0
        self.data = puzzle_input

    def part1(self):
        santa = Grid()
        for d in self.data:
            santa.move(d)
        self.p1 = len(santa.seen)

    def part2(self):
        santa = Grid()
        robo_santa = Grid()
        for idx, d in enumerate(self.data):
            if is_even(idx):
                santa.move(d)
            else:
                robo_santa.move(d)
        self.p2 = combine(santa.seen, robo_santa.seen)
