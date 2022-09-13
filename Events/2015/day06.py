import re
from utils.solution import BaseSolution


grid_size = 1000


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


class Solution(BaseSolution):

    def format_data(self):
        self.split_by_new_line()
        self.data = [l.strip() for l in self.data]

    def setupGrid(self):
        self.grid = []
        for idx, _ in enumerate(range(grid_size)):
            self.grid.append([])
            for _ in range(grid_size):
                self.grid[idx].append(Light())

    def get_range(self, start, end):
        return [y for x in self.grid[start[0]:end[0]+1] for y in x[start[1]:end[1]+1]]

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

    def part1(self):
        self.setupGrid()
        for i in self.data:
            [CMD, start, end] = parse_instruction(i)
            self.process_command(CMD, start, end)
        for row in self.grid:
            for light in row:
                if light.on is True:
                    self.p1 += 1

    def part2(self):
        self.setupGrid()
        for i in self.data:
            [CMD, start, end] = parse_instruction(i)
            self.process_command(CMD, start, end)
        for row in self.grid:
            for light in row:
                self.p2 += light.brightness
