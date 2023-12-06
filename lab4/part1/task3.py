import psycopg2

# Подключение к базе данных PostgreSQL
conn = psycopg2.connect(
    dbname='database_name',
    user='username',
    password='password',
    host='host',
    port='port'
)
cursor = conn.cursor()

# Добавление нескольких продуктов в таблицу "products"
cursor.execute("INSERT INTO products (name, price) VALUES ('Product A', 10.99)")
cursor.execute("INSERT INTO products (name, price) VALUES ('Product B', 15.49)")
conn.commit()

conn.close()