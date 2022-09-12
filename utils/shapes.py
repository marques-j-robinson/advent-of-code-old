from .data_formats import int_list, parse_coord
from .math import surface_area, area, perimeter, volume


class Cube:

    def __init__(self, sides):
        self.sides = sides.split('x')
        self.get_sm_sides()

    def get_sm_sides(self):
        self.sm_sides = int_list(self.sides[:])
        self.sm_sides.remove(max(int_list(self.sm_sides)))

    def surface_area(self):
        return surface_area(self.sides)

    def area(self):
        return area(self.sm_sides)

    def perimeter(self):
        return perimeter(self.sm_sides)

    def volume(self):
        return volume(self.sides)


class Grid:

    def __init__(self, directions, origin='0,0'):
        self.directions = directions
        self.coord = origin
        self.seen = [origin]

    def move(self, d):
        [x, y] = parse_coord(self.coord)
        if d == self.directions["up"]:
            y += 1
        elif d == self.directions["right"]:
            x += 1
        elif d == self.directions["down"]:
            y -= 1
        elif d == self.directions["left"]:
            x -= 1
        self.coord = f"{x},{y}"

    def move_auto(self, d):
        self.move(d)
        self.add_seen()

    def add_seen(self):
        if self.coord not in self.seen:
            self.seen.append(self.coord)
