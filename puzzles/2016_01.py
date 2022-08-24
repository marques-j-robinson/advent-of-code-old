from util.base_solution import BaseSolution


N = "N"
E = "E"
S = "S"
W = "W"
turns = {
    "NR": E,
    "NL": W,
    "SR": W,
    "SL": E,
    "ER": S,
    "EL": N,
    "WR": N,
    "WL": S,
}


class Grid:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.seen = []

    def add_seen(self):
        coord = self.get_coord()
        if coord not in self.seen:
            self.seen.append(coord)

    def has_seen(self):
        coord = self.get_coord()
        return coord in self.seen

    def get_coord(self):
        return f"{self.x},{self.y}"

    def move(self, direction):
        if direction == N:
            self.y += 1
        elif direction == E:
            self.x += 1
        elif direction == S:
            self.y -= 1
        elif direction == W:
            self.x -= 1

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)


class Solution(BaseSolution):

    def __init__(self):
        self.year = 2016
        self.day = 1

    def translate(self):
        self.data = [(d[0], int(d[1:len(d)])) for d in self.data.split(', ')]

    def part_01(self):
        direction = "N"
        G = Grid()
        for turn, steps in self.data:
            direction = turns[f"{direction}{turn}"]
            while steps > 0:
                steps -= 1
                G.move(direction)
                G.add_seen()

        self.p1 = G.manhattan_distance()

    def part_02(self):
        direction = "N"
        G = Grid()
        for turn, steps in self.data:
            direction = turns[f"{direction}{turn}"]
            while steps > 0:
                steps -= 1
                G.move(direction)
                if self.p2 == 0 and G.has_seen():
                    self.p2 = G.manhattan_distance()
                G.add_seen()


if __name__ == '__main__':
    s = Solution()
    s.solve()
