import sqlite3

connect = sqlite3.connect('passengers.sqlite')
cursor = connect.cursor()

# query = "SELECT * from passenger_info WHERE id=2"
query = "SELECT * from passenger_info"

result = cursor.execute(query)
print(result.fetchone())

# print(result.fetchall())
cursor.close()
connect.close()
