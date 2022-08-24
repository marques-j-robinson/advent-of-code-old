import re
import sys
import fileinput
from shutil import copyfile
from puzzles.util.util import leading_zero


event = 2016
day = 1
puzzlename = f'{event}_{leading_zero(day)}'


if __name__ == '__main__':
    filename = f'puzzles/{puzzlename}.py'
    copyfile('solution_template.py', filename)
    with open(filename, 'r+') as f:
        text = f.read()
        text = re.sub('EVENT', str(event), text)
        text = re.sub('DAY', str(day), text)
        f.seek(0)
        f.write(text)
        f.truncate()
    print(f'Completed generating {puzzlename}')
