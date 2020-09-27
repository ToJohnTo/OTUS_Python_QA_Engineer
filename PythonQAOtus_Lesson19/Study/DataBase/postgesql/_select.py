import psycopg2

connect = psycopg2.connect(
    host='localhost',
    database='test_postgres',
    port=5432,
    user='test_postgres',
    password='test_postgres'
)
cursor = connect.cursor()

# query = "SELECT * from passenger_info WHERE id=1"
query = "SELECT * from passenger_info"

cursor.execute(query)
print(cursor.fetchone())
# print(cursor.fetchmany(2))

# print(result.fetchall())
cursor.close()
connect.close()
