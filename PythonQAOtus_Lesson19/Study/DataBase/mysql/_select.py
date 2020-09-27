import pymysql

connect = pymysql.connect(
    host='localhost',
    database='test',
    port=3306,
    user='test',
    password='test'
)
cursor = connect.cursor()

query = "SELECT * from passenger_info WHERE id=1"
# query = "SELECT * from passenger_info"

cursor.execute(query)
print(cursor.fetchone())
# print(cursor.fetchmany(2))

# print(result.fetchall())
cursor.close()
connect.close()
