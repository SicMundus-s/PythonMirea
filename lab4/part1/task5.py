conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("UPDATE users SET age = 30 WHERE name = 'John'")
conn.commit()

conn.close()