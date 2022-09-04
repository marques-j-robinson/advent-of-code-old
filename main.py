import os
import sys
import importlib
from shutil import copyfile

import urllib3
import pyperclip
from dotenv import load_dotenv


load_dotenv() # take environment variables from .env.
# Code of your application, which uses environment variables (e.g. from
# `os.environ` or `os.getenv`) as if they came from the actual environment.


BASE_URL = 'https://adventofcode.com'
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
EVENT = os.getenv('EVENT')
DAY = os.getenv('DAY')


def leading_zero(n):
    return str(n).zfill(2)


def copy_solution(p1, p2):
    if p2 == 0:
        print(f'Part 1: {p1}')
        pyperclip.copy(str(p1))
    else:
        print(f'Part 1: {p1}')
        print(f'Part 2: {p2}')
        pyperclip.copy(str(p2))


def read_puzzle_input():
    cache_path = f'cache/{EVENT}_{leading_zero(DAY)}'
    puzzle_input_file = open(cache_path, 'r')
    puzzle_input = puzzle_input_file.read()
    puzzle_input_file.close()
    return puzzle_input


def solve():
    print(f'Solution for {EVENT}_{leading_zero(DAY)}')
    puzzle_input = read_puzzle_input()
    # print(puzzle_input)
    s_module = importlib.import_module(f'Events.{EVENT}.day{leading_zero(DAY)}')
    s = s_module.Solution(puzzle_input)
    s.translate()
    s.part1()
    s.part2()
    copy_solution(s.p1, s.p2)


def fetch():
    url = f'{BASE_URL}/{EVENT}/day/{DAY}/input'
    cookies = {'Cookie':f'session={GITHUB_TOKEN}'}
    http = urllib3.PoolManager()
    r = http.request('GET', url, headers=cookies)
    return r.data.decode('utf-8').rstrip('\n')


def save_puzzle_input():
    cache_path = f'cache/{EVENT}_{leading_zero(DAY)}'
    if os.path.exists(cache_path):
        print(f'{EVENT}_{leading_zero(DAY)} PUZZLE INPUT ALREADY STORED IN CACHE!')
    else:
        puzzle_input = fetch()
        with open(cache_path, 'w') as f:
            f.write(puzzle_input)
            f.close()
            print(f'Stored puzzle_input in cache at {cache_path}')


def generate_new_puzzle():
    filename = f'Events/{EVENT}/day{leading_zero(DAY)}.py'
    if os.path.exists(filename):
        print(f'{EVENT}_{leading_zero(DAY)} PUZZLE ALREADY GENERATED!')
    else:
        copyfile('templates/solution.py', filename)
        print(f'Generated puzzle at {filename}')


if __name__ == '__main__':
    cmd_args = sys.argv[1:]
    if '--generate' in cmd_args:
        generate_new_puzzle()
        save_puzzle_input()
    elif len(cmd_args) == 0:
        solve()
    else:
        print('UNKNOWN CMD\nEXITING...')
