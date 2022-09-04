from .data_translations import int_list
from .calc import surface_area, area, perimeter, volume


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

    def __init__(self, directions):
        self.x = 0
        self.y = 0
        self.seen = []
        self.directions = directions

    def move(self, d):
        if d == self.directions["up"]:
            self.y += 1
        elif d == self.directions["right"]:
            self.x += 1
        elif d == self.directions["down"]:
            self.y -= 1
        elif d == self.directions["left"]:
            self.x -= 1

    def get_coord(self):
        return f"{self.x},{self.y}"

    def add_seen(self):
        coord = self.get_coord()
        if coord not in self.seen:
            self.seen.append(coord)

    def has_seen(self):
        coord = self.get_coord()
        return coord in self.seen
