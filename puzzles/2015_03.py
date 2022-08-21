import pyperclip
from util.puzzle_input import fetch


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


if __name__ == '__main__':
    santa = Grid()
    og_santa = Grid()
    robo_santa = Grid()

    # Test Data
    # directions = '>'
    # directions = '^>v<'
    # directions = '^v^v^v^v^v'
    directions = fetch(2015, 3)

    for idx, d in enumerate(directions):
        santa.move(d)
        if is_even(idx):
            og_santa.move(d)
        else:
            robo_santa.move(d)

    p1 = len(santa.seen)
    # pyperclip.copy(p1)
    print(f'part 1:\n{p1}')

    p2 = combine(og_santa.seen, robo_santa.seen)
    pyperclip.copy(p2)
    print(f'part 2:\n{p2}')
