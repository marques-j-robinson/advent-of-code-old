from util.base_solution import BaseSolution


def calc_fuel(mass):
    return round(mass//3)-2


def re_calc_fuel(mass, total=0):
    fuel = calc_fuel(mass)
    if fuel <= 0:
        return total
    else:
        total += fuel
        return re_calc_fuel(fuel, total)


class Solution(BaseSolution):

    def __init__(self):
        self.year = 2019
        self.day = 1

    def translate(self):
        self.split_by_new_line()
        self.int_list()

    def part_01(self):
        for m in self.data:
            self.p1 += calc_fuel(m)

    def part_02(self):
        for m in self.data:
            self.p2 += re_calc_fuel(m)


if __name__ == '__main__':
    s = Solution()
    s.solve()
