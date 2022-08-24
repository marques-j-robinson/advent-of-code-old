from util.base_solution import BaseSolution


up = '^'
right = '>'
down = 'v'
left = '<'


def combine(a, b):
    return len(a + list(set(b) - set(a)))


def is_even(i):
    return i % 2 == 0


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


class Solution(BaseSolution):

    def __init__(self):
        self.year = 2015
        self.day = 3

    def part_01(self):
        santa = Grid()
        for d in self.data:
            santa.move(d)
        self.p1 = len(santa.seen)

    def part_02(self):
        santa = Grid()
        robo_santa = Grid()
        for idx, d in enumerate(self.data):
            if is_even(idx):
                santa.move(d)
            else:
                robo_santa.move(d)
        self.p2 = combine(santa.seen, robo_santa.seen)


if __name__ == '__main__':
    s = Solution()
    s.solve()
