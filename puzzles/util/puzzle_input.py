import os
import urllib3
from dotenv import load_dotenv
load_dotenv()


BASE_URL = 'https://adventofcode.com'
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')


def fetch(year, day):
    url = f'{BASE_URL}/{year}/day/{day}/input'
    cookies = {'Cookie':f'session={GITHUB_TOKEN}'}
    http = urllib3.PoolManager()
    r = http.request('GET', url, headers=cookies)
    return r.data.decode('utf-8').rstrip('\n')
