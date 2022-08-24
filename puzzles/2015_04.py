import hashlib
from util.base_solution import BaseSolution


def extract(secret_key, count):
    str2hash = f"{secret_key}{count}"
    res = hashlib.md5(str2hash.encode())
    return res.hexdigest()


class Mine:

    def __init__(self, data):
        self.secret_key = data

    def start(self, target):
        zeros = "".join(["0"] * target)
        count = 0
        exit = False
        while exit is False:
            res = extract(self.secret_key, count)
            if res[0:target] == zeros:
                exit = True
            else:
                count += 1
        return count


class Solution(BaseSolution):

    def __init__(self):
        self.year = 2015
        self.day = 4

    def part_01(self):
        mine = Mine(self.data)
        self.p1 = mine.start(5)

    def part_02(self):
        mine = Mine(self.data)
        self.p2 = mine.start(6)


if __name__ == '__main__':
    s = Solution()
    s.solve()
