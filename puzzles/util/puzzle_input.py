import os
import urllib3
from dotenv import load_dotenv


def setup_cookies():
    load_dotenv()
    github_token = os.environ.get('GITHUB_SESSION', 'xxx')
    return {'Cookie':f'session={github_token}'}


def fetch(year, day):
    http = urllib3.PoolManager()
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    cookies = setup_cookies()
    r = http.request('GET', url, headers=cookies)
    return r.data.decode('utf-8').rstrip('\n')
