from utils.data_translations import DataTranslations
from utils.shapes import Grid
from utils.calc import manhattan_distance


directions = {
    "up": "N",
    "right": "E",
    "down": "S",
    "left": "W"
}
turns = {
    "NR": "E",
    "NL": "W",
    "SR": "W",
    "SL": "E",
    "ER": "S",
    "EL": "N",
    "WR": "N",
    "WL": "S"
}


class Solution(DataTranslations):

    def __init__(self, puzzle_input):
        self.p1 = 0
        self.p2 = 0
        self.data = puzzle_input

    def translate(self):
        """
        List of tuples - (direction[str], steps[int])
        """
        self.data = [(d[0], int(d[1:len(d)])) for d in self.data.split(', ')]

    def part1(self):
        direction = directions["up"]
        G = Grid(directions)
        for turn, steps in self.data:
            direction = turns[f'{direction}{turn}']
            while steps > 0:
                steps -= 1
                G.move(direction)
                G.add_seen()
        self.p1 = manhattan_distance(G.x, G.y)

    def part2(self):
        direction = directions["up"]
        G = Grid(directions)
        for turn, steps in self.data:
            direction = turns[f"{direction}{turn}"]
            while steps > 0:
                steps -= 1
                G.move(direction)
                if self.p2 == 0 and G.has_seen():
                    self.p2 = manhattan_distance(G.x, G.y)
                G.add_seen()
