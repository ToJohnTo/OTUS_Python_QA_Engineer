import sqlite3

connection = sqlite3.connect("../files/data.sqlite")

result = connection.execute("SELECT name, rank, gold FROM users;")

# Получаем заголовки для даных
headers = [row[0] for row in result.description]

for user in result.fetchall():
    print(dict(zip(headers, user)))
