conn = sqlite3.connect('database.db')
cursor = conn.cursor()

try:
    cursor.execute("BEGIN TRANSACTION")
    cursor.execute("INSERT INTO transactions (amount) VALUES (100)")
    cursor.execute("INSERT INTO transactions (amount) VALUES (200)")
    cursor.execute("COMMIT")
except sqlite3.Error as e:
    print("Ошибка транзакции:", e)
    cursor.execute("ROLLBACK")

conn.close()