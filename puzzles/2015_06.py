import re
from util.base_solution import BaseSolution


def parse_instruction(line):
    res = re.match(r"^(\D*) (\d*,\d*) \D* (\d*,\d*)", line)
    [start_x, start_y] = [int(i) for i in res.group(2).split(",")]
    [end_x, end_y] = [int(i) for i in res.group(3).split(",")]
    return [
        res.group(1).strip(),
        (start_x, start_y),
        (end_x, end_y),
    ]


class Light:

    def __init__(self):
        self.on = False
        self.brightness = 0

    def britten(self, i):
        self.brightness += i
        if self.brightness < 0:
            self.brightness = 0

    def toggle(self):
        self.on = not self.on

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False


class Grid:

    def __init__(self, size):
        self.elements = []
        self.size = size
        self.setup()

    def setup(self):
        for idx, _ in enumerate(range(self.size)):
            self.elements.append([])
            for _ in range(self.size):
                self.elements[idx].append(Light())

    def process_command(self, CMD, start, end):
        for light in self.get_range(start, end):
            if CMD == "turn on":
                light.turn_on()
                light.britten(1)
            elif CMD == "toggle":
                light.toggle()
                light.britten(2)
            elif CMD == "turn off":
                light.turn_off()
                light.britten(-1)

    def get_range(self, start, end):
        return [y for x in self.elements[start[0]:end[0]+1] for y in x[start[1]:end[1]+1]]


class Solution(BaseSolution):

    def __init__(self):
        self.year = 2015
        self.day = 6

    def translate(self):
        self.split_by_new_line()
        self.data = [l.strip() for l in self.data]

    def part_01(self):
        G = Grid(1000)
        for i in self.data:
            [CMD, start, end] = parse_instruction(i)
            G.process_command(CMD, start, end)
        for row in G.elements:
            for light in row:
                if light.on is True:
                    self.p1 += 1

    def part_02(self):
        G = Grid(1000)
        for i in self.data:
            [CMD, start, end] = parse_instruction(i)
            G.process_command(CMD, start, end)
        for row in G.elements:
            for light in row:
                self.p2 += light.brightness


if __name__ == '__main__':
    s = Solution()
    s.solve()
