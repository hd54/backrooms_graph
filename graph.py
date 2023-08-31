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


# return the array of connections to a level
# serialization is needed because SQLite3 doesn't support array data type
def convert_edges():
    entrance_edges = []
    for result in results:
        identifier, level, description, link, entrance, outlet = result
        for way in entrance:
            entrance_edges.append([way, level])
    # print(entrance_edges)
    return entrance_edges


# display database using pyplot
# each node represent a level and edges represent the connection
def db_to_nodes():
    for result in results:
        identifier, level, description, link, entrance, outlet = result
        G.add_node(level, description=description, link=link)
    edges = convert_edges()
    G.add_edges_from(edges)
    nx.draw_spring(G)
    plt.show()


db_to_nodes()
