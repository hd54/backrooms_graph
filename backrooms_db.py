import sqlite3

conn = sqlite3.connect("backrooms.db")
cursor = conn.cursor()

# cursor.execute('''DROP TABLE levels''')
cursor.execute('''CREATE TABLE IF NOT EXISTS levels(
                    level TEXT, 
                    description TEXT, 
                    link TEXT)''')
# conn.commit()

# test
cursor.execute('''SELECT * from levels''')
results = cursor.fetchall()
print(results)
