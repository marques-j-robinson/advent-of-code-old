from util.base_solution import BaseSolution
from util.util import parse_coord


up = 'U'
right = 'R'
down = 'D'
left = 'L'


num_pad_1 = {
    '-1,1': 1,
    '0,1': 2,
    '1,1': 3,
    '-1,0': 4,
    '0,0': 5,
    '1,0': 6,
    '-1,-1': 7,
    '0,-1': 8,
    '1,-1': 9
}
num_pad_2 = {
    '0,2': 1,
    '-1,1': 2,
    '0,1': 3,
    '1,1': 4,
    '-2,0': 5,
    '-1,0': 6,
    '0,0': 7,
    '1,0': 8,
    '2,0': 9,
    '-1,-1': 'A',
    '0,-1': 'B',
    '1,-1': 'C',
    '0,-2': 'D'
}


def check_boundry_basic(val):
    if val <= 1 and val >= -1:
        return val
    elif val >= 1:
        return 1
    elif val <= -1:
        return -1


def check_boundry_extended(val):
    if val <= 2 and val >= -2:
        return val
    elif val >= 2:
        return 2
    elif val <= -2:
        return -2


def is_extended_boundry(coord):
    if coord == '-2,0':
        return right
    elif coord == '0,2':
        return down
    elif coord == '2,0':
        return left
    elif coord == '0,-2':
        return up
    else:
        return None


def move(coord, d):
    [x, y] = parse_coord(coord)
    if d == up:
        y += 1
    elif d == right:
        x += 1
    elif d == down:
        y -= 1
    elif d == left:
        x -= 1
    return [x, y]


class Solution(BaseSolution):

    def __init__(self):
        self.year = 2016
        self.day = 2

    def translate(self):
        self.split_by_new_line()

    def part_01(self):
        bathroom_code = []
        cur_coord = '0,0'
        for instructions in self.data:
            for d in instructions:
                [x, y] = move(cur_coord, d)
                x = check_boundry_basic(x)
                y = check_boundry_basic(y)
                cur_coord = f'{x},{y}'
            bathroom_code.append(str(num_pad_1[cur_coord]))
        self.p1 = ''.join(bathroom_code)


    def part_02(self):
        bathroom_code = []
        cur_coord = '-2,0'
        for instructions in self.data:
            for d in instructions:
                valid_d = is_extended_boundry(cur_coord)
                if valid_d is None:
                    [x, y] = move(cur_coord, d)
                    if x == 0:
                        y = check_boundry_extended(y)
                    elif y == 0:
                        x = check_boundry_extended(x)
                    else:
                        x = check_boundry_basic(x)
                        y = check_boundry_basic(y)
                    cur_coord = f'{x},{y}'
                elif valid_d is not None and valid_d == d:
                    [x, y] = move(cur_coord, d)
                    cur_coord = f'{x},{y}'
            bathroom_code.append(str(num_pad_2[cur_coord]))
        self.p2 = ''.join(bathroom_code)


if __name__ == '__main__':
    s = Solution()
    s.solve()
