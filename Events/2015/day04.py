import hashlib
from utils.data_translations import DataTranslations


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


class Solution(DataTranslations):

    def __init__(self, puzzle_input):
        self.p1 = 0
        self.p2 = 0
        self.data = puzzle_input

    def part1(self):
        mine = Mine(self.data)
        self.p1 = mine.start(5)

    def part2(self):
        mine = Mine(self.data)
        self.p2 = mine.start(6)
