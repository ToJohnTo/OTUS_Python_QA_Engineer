import psycopg2

connect = psycopg2.connect(
    host='localhost',
    database='test_postgres',
    port=5432,
    user='test_postgres',
    password='test_postgres'
)
cursor = connect.cursor()

with open('passengers.sql', 'r') as file:
    cursor.execute(file.read())

connect.commit()
cursor.close()
connect.close()
