conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("SELECT AVG(age) AS average_age FROM users")
average_age = cursor.fetchone()[0]
print(f"Средний возраст пользователей: {average_age}")

conn.close()