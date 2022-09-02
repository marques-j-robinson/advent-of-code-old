from util.base_solution import BaseSolution


up = 'U'
right = 'R'
down = 'D'
left = 'L'


num_pad = {
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


def check_boundry(val):
    if val <= 1 and val >= -1:
        return val
    elif val >= 1:
        return 1
    elif val <= -1:
        return -1


def parse_coord(coord):
    return [int(i) for i in coord.split(',')]


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
    return f'{check_boundry(x)},{check_boundry(y)}'


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
                cur_coord = move(cur_coord, d)
            bathroom_code.append(str(num_pad[cur_coord]))
        self.p1 = ''.join(bathroom_code)


    def part_02(self):
        pass


if __name__ == '__main__':
    s = Solution()
    s.solve()
