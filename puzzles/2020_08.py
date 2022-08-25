from util.base_solution import BaseSolution


class Solution(BaseSolution):

    def __init__(self):
        self.year = 2020
        self.day = 8

    def translate(self):
        self.split_by_new_line()
        self.data = [l.split() for l in self.data]

    def part_01(self):
        idx = 0
        history = []

        while idx < len(self.data):
            if idx in history:
                break
            history.append(idx)
            [i, d] = self.data[idx]
            if i == "nop":
                idx += 1
            elif i == "acc":
                self.p1 += int(d)
                idx += 1
            elif i == "jmp":
                idx += int(d)

    def part_02(self):
        idx = 0
        history = []
        back_idx = None
        cur_idx = 0
        change = {
            "nop": "jmp",
            "jmp": "nop",
        }

        while idx < len(self.data):
            if idx in history:
                if back_idx is not None:
                    self.data[back_idx][0] = change[self.data[back_idx][0]]
                if self.data[cur_idx][0] != "acc":
                    back_idx = cur_idx
                    self.data[cur_idx][0] = change[self.data[cur_idx][0]]
                    changed = False
                    for i, v in enumerate(self.data):
                        if changed is False and i > cur_idx and v[0] != "acc":
                            changed = True
                            cur_idx = i
                else:
                    cur_idx += 1
                # reset
                history = []
                idx = 0
                self.p2 = 0
            history.append(idx)
            [i, d] = self.data[idx]
            if i == "nop":
                idx += 1
            elif i == "acc":
                self.p2 += int(d)
                idx += 1
            elif i == "jmp":
                idx += int(d)


if __name__ == '__main__':
    s = Solution()
    s.solve()
