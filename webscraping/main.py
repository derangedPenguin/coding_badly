from typing import Any

import requests as rq
import bs4
from bs4 import BeautifulSoup
from lxml import html
import json

from TUI_util import *

def narrow(soup:BeautifulSoup) -> str:
    tags:set[bs4.Tag] = soup.find_all('p')
    results = []
    for tag in tags:
        if tag.get('a', False):
            results.append(tag)
    print(str(tags))
    return results

def get_page() -> tuple[rq.Response, Any]:
    wiki_page = 'Main_page'#input('\nWhat wiki page should be examined?\n > ')

    print('\nsending HTTP request...')
    resp = rq.get(f'https://en.wikipedia.org/wiki/{wiki_page}')
    print(f'response recieved after {resp.elapsed} with status code {resp.status_code}')

    if resp.status_code != 200:
        print(f'Recieved non-success status code {resp.status_code}')
        return
    
    tree = html.fromstring(resp.content)

    return resp, tree

def main():
    while True:

        resp, tree = get_page()

        soup = BeautifulSoup(resp.content,  'html.parser')

        # output(str(tree.xpath('//a/text()'))) #i dont know how this works
        #check out https://lxml.de/tutorial.html to figure it out better

        output(narrow(soup))

        if not get_yes_no('run again?'):
            break


if __name__ == "__main__":
    main()