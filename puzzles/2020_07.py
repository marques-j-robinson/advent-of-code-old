from util.base_solution import BaseSolution


target = "shiny gold"


def format_bag(b):
    return b.replace('bags', '').replace('bag', '').strip()


class Solution(BaseSolution):

    def __init__(self):
        self.year = 2020
        self.day = 7

    def translate(self):
        bags = {}
        for line in self.data.split('\n'):
            res = line.strip().partition("contain")
            bag = format_bag(res[0])
            bags[bag] = []
            for i in format_bag(res[2]).replace('.', '').split(','):
                l = i.strip()
                if l != "no other":
                    v = int(l[0])
                    b = l[1:].strip()
                    bags[bag].append((b,v))
        self.data = bags

    def part_01(self):
        p1_bags = {}
        for b in self.data:
            p1_bags[b] = [i[0] for i in self.data[b]]


        for b in p1_bags:
            for i in p1_bags[b]:
                if i in p1_bags:
                    for j in p1_bags[i]:
                        p1_bags[b].append(j)
            p1_bags[b] = set(p1_bags[b])
            if target in p1_bags[b]:
                self.p1 += 1

    def part_02(self):
        self.p2 += self.sum_bags(target) - 1

    def sum_bags(self, root):
        return 1 + sum([i[1] * self.sum_bags(i[0]) for i in self.data[root]])


if __name__ == '__main__':
    s = Solution()
    s.solve()
