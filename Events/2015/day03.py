from utils.solution import BaseSolution
from utils.shapes import Grid
from utils.data_formats import combine
from utils.math import is_even


directions = {
    "up": "^",
    "right": ">",
    "down": "v",
    "left": "<"
}


# class Grid:

    # def __init__(self):
        # orgin = '0,0'
        # self.coord = orgin
        # self.seen = [orgin]

    # def parse_coord(self):
        # return [int(i) for i in self.coord.split(',')]

    # def append_coord(self):
        # if self.coord not in self.seen:
            # self.seen.append(self.coord)

    # def move(self, d):
        # [x, y] = self.parse_coord()
        # if d == up:
            # y += 1
        # elif d == right:
            # x += 1
        # elif d == down:
            # y -= 1
        # elif d == left:
            # x -= 1
        # self.coord = f'{x},{y}'
        # self.append_coord()


class Solution(BaseSolution):

    def part1(self):
        santa = Grid(directions)
        for d in self.data:
            santa.move_auto(d)
        self.p1 = len(santa.seen)

    def part2(self):
        santa = Grid(directions)
        robo_santa = Grid(directions)
        for idx, d in enumerate(self.data):
            if is_even(idx):
                santa.move_auto(d)
            else:
                robo_santa.move_auto(d)
        self.p2 = combine(santa.seen, robo_santa.seen)
