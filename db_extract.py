from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import sqlite3
import re


def level_scrap(url):
    pattern = r'\s-\s[“"]([^”"]+)[”"]'
    conn = sqlite3.connect("backrooms.db")
    cursor = conn.cursor()
    html = requests.get(url)
    bs_obj = BeautifulSoup(html.content, "html.parser")
    level_list = bs_obj.find_all("li")
    level_list = level_list[84:]
    for level in level_list:
        anchor = level.find("a")
        level_num = anchor.next
        no_data = level_num.next
        if no_data != ' - [NO DATA]':
            level_desc = re.search(pattern, level.getText())
            if level_desc:
                level_desc = level_desc.group(1)
            else:
                level_desc = ''
            relative_href = anchor.get("href")
            absolute_href = urljoin(url, relative_href)
            # cursor.execute('''INSERT INTO levels VALUES(?,?,?)''',
            #                (level_num, level_desc, absolute_href))
            # conn.commit()


# level_scrap('https://backrooms-wiki.wikidot.com/normal-levels-i')


def connection(url):
    html = requests.get(url)
    bs_obj = BeautifulSoup(html.content, "html.parser")
    content = bs_obj.find('div', {'id': 'page-content'})
    entrances = get_connection('Entrances', content)
    exits = get_connection('Exits', content)
    # what to do with the hyperlink?
    return [entrances, exits]


def get_connection(name, content):
    result = content.find('h1', string='Entrances And Exits:')
    if name == 'Entrances':
        result = result.find_next(re.compile('h\\d'))
    elif name == 'Exits':
        result = result.find_next(re.compile('h\\d'))
        result = result.find_next(re.compile('h\\d'))
    # get all <p>
    connections = []
    next_tag = result.findNextSibling()
    while next_tag.name == 'p':
        links = next_tag.find_all('a')
        for link in links:
            if link.next.startswith('Level'):
                href = link.get('href')
                link = urljoin('https://backrooms-wiki.wikidot.com', href)
                connections.append(link)
        next_tag = next_tag.findNextSibling()
    return connections


