import psycopg2


connect = psycopg2.connect(
    host='localhost',
    database='test_postgres',
    port=5432,
    user='test_postgres',
    password='test_postgres'
)
cursor = connect.cursor()

query = "DELETE FROM passenger_info  WHERE id=1"
cursor.execute(query)
connect.commit()

connect.close()
