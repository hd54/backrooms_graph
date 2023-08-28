import sqlite3

# create the database
conn = sqlite3.connect("backrooms_site/backrooms.db")
cursor = conn.cursor()

# cursor.execute('''DROP TABLE levels''')
cursor.execute('''CREATE TABLE IF NOT EXISTS levels(
                    id INTEGER PRIMARY KEY,
                    level TEXT, 
                    description TEXT, 
                    link TEXT,
                    connection TEXT)''')
conn.commit()

# test
cursor.execute('''SELECT * from levels''')
results = cursor.fetchall()
print(results)
