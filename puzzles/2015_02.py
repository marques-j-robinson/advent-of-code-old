from util.base_solution import BaseSolution


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


class Solution(BaseSolution):

    def __init__(self):
        self.year = 2015
        self.day = 2

    def part_01(self):
        for d in self.data.split('\n'):
            box = Box(d)
            self.p1 += box.surface_area() + box.area()

    def part_02(self):
        for d in self.data.split('\n'):
            box = Box(d)
            self.p2 += box.perimeter() + box.volume()


if __name__ == '__main__':
    s = Solution()
    s.solve()
