conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM users WHERE age < 21")
conn.commit()

conn.close()