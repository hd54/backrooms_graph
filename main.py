import pandas as pd
import sqlite3

conn = sqlite3.connect('backrooms.db')
df = pd.read_sql_query('SELECT * FROM levels', conn)
print(df)
