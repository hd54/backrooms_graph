from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import sqlite3
import re
import json


# add all hyperlinks of connections to a level (indicated by tag) to array 'conn'
def connection(conn, tag):
    if tag.name == 'p':
        while tag is not None and tag.name == 'p':
            links = tag.find_all('a')
            for link in links:
                if link.next.startswith('Level'):
                    href = link.get('href')
                    link = urljoin('https://backrooms-wiki.wikidot.com', href)
                    conn.append(link)
            tag = tag.findNextSibling()
    elif tag.name == 'ul':
        lists = tag.find_all('li')
        for bullet in lists:
            link = bullet.find('a')
            if link is not None and link.next.startswith('Level'):
                href = link.get('href')
                link = urljoin('https://backrooms-wiki.wikidot.com', href)
                conn.append(link)


# return an array of entrances and exits connecting to the current level (indicated by url)
def get_connection(url):
    html = requests.get(url)
    bs_obj = BeautifulSoup(html.content, "html.parser")
    content = bs_obj.find('div', {'id': 'page-content'})
    entrances = content.find(re.compile('h\\d'), string='Entrances')
    if entrances is None:
        entrances = content.find(re.compile('h\\d'), string='Entrances:')
    exits = content.find(re.compile('h\\d'), string='Exits')
    if exits is None:
        exits = content.find(re.compile('h\\d'), string='Exits:')
    entrance_conn = []
    exit_conn = []
    # temporary fix
    if entrances is not None:
        entrance_tag = entrances.findNextSibling()
        if entrance_tag is not None:
            connection(entrance_conn, entrance_tag)
    if exits is not None:
        exit_tag = exits.findNextSibling()
        if exit_tag is not None:
            connection(exit_conn, exit_tag)
    return [entrance_conn, exit_conn]


# scrap only levels with existing data and add to the database
# the website is a list of 'li' tags. our levels data start at the 84th tag
def level_scrap(url):
    pattern = r'\s-\s[“"]([^”"]+)[”"]'  # GPT
    conn = sqlite3.connect("backrooms_site/backrooms.db")
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
            connect = get_connection(absolute_href)
            print(get_connection(absolute_href))
            serialized_connect = json.dumps(connect)
            cursor.execute('''INSERT INTO levels VALUES(?,?,?,?)''',
                           (level_num, level_desc, absolute_href, serialized_connect))
            conn.commit()

# level_scrap('https://backrooms-wiki.wikidot.com/normal-levels-i')
