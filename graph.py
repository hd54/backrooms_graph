import networkx as nx
import re
import sqlite3
import json
import matplotlib.pyplot as plt

G = nx.DiGraph()

conn = sqlite3.connect('backrooms_site/backrooms.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM levels")
results = cursor.fetchall()


def convert_edges():
    level_pattern = r'(\d+)(.*)'
    enigmatic_pattern = r'\D'
    entrance_edges = []
    for result in results:
        level, description, link, connection = result
        connection = json.loads(connection)
        end_level = re.search(level_pattern, link).group(0)
        for entrance in connection[0]:
            start = re.search(level_pattern, entrance)
            start_level = start.group(0)
            if not re.search(enigmatic_pattern, start_level):
                entrance_edges.append(['Level ' + start_level, 'Level ' + end_level])
    # print(entrance_edges)
    return entrance_edges


def db_to_nodes():
    for result in results:
        level, description, link, connection = result
        G.add_node(level, description=description, link=link)
    edges = convert_edges()
    G.add_edges_from(edges)
    nx.draw_spring(G)
    plt.show()


db_to_nodes()
