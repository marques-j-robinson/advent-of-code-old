import re
import sys
import fileinput
from shutil import copyfile
from puzzles.util.util import leading_zero
from dotenv import load_dotenv
load_dotenv()


event = os.getenv('EVENT')
day = os.getenv('DAY')
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
    print(f'Generated puzzle {puzzlename}')
