import pyperclip
from util.puzzle_input import fetch


class Box:

    def __init__(self, sides):
        self.sides = sides
        self.parse_sides()
        self.get_sm_sides()

    def parse_sides(self):
        [l, w, h] = self.sides.split('x')
        self.sides = [int(l), int(w), int(h)]

    def get_sm_sides(self):
        self.sm_sides = self.sides[:]
        self.sm_sides.remove(max(self.sm_sides))

    def surface_area(self):
        [l, w, h] = self.sides
        return 2*l*w + 2*w*h + 2*h*l

    def area(self):
        res = 1
        for i in self.sm_sides:
            res = res * i
        return res

    def perimeter(self):
        return sum([2*i for i in self.sm_sides])

    def volume(self):
        [l, w, h] = self.sides
        return l*w*h


def parse(dimensions):
    wrapping_paper = 0
    ribbon = 0

    for d in dimensions.split('\n'):
        box = Box(d)
        wrapping_paper += box.surface_area() + box.area()
        ribbon += box.perimeter() + box.volume()

    return [wrapping_paper, ribbon]


if __name__ == '__main__':
    # Test Data
    x = fetch(2015, 2)
    [p1, p2] = parse(x)
    pyperclip.copy(p2)
    print(f'part 1:\n{p1}')
    print(f'part 2:\n{p2}')
