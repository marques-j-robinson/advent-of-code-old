import pyperclip
from util.puzzle_input import fetch


def parse(instructions):
    p1=0
    p2=None
    for idx, i in enumerate(instructions):
        if p1 == -1 and p2 is None:
            p2=idx
        if i == '(':
            p1 += 1
        else:
            p1 -= 1
    return [p1, p2]


if __name__ == '__main__':
    pass
    # Test Data
    x = fetch(2015, 1)
    [p1, p2]=parse(x)
    pyperclip.copy(p2)
    print(f'part 1:\n{p1}')
    print(f'part 2:\n{p2}')
