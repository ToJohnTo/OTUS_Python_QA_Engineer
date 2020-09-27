import mysql.connector as conn


connect = conn.connect(
    host='localhost',
    database='bitnami_opencart',
    port=3306,
    user='root',
    password='bitnami'
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
