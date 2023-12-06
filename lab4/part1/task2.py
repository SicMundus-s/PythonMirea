import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)

new_user = ('Eve', 22)
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', new_user)
conn.commit()

conn.close()