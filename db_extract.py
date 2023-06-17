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
            cursor.execute('''INSERT INTO levels VALUES(?,?,?)''',
                           (level_num, level_desc, absolute_href))
            conn.commit()


def connection(url):
    html = requests.get(url)
    bs_obj = BeautifulSoup(html.content, "html.parser")
    content = bs_obj.find('div', {'id': 'page-content'})
    print(content)


connection("https://backrooms-wiki.wikidot.com/level-0")
