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
