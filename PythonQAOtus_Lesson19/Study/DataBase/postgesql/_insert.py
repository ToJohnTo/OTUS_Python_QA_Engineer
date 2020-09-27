import psycopg2

connect = psycopg2.connect(
    host='localhost',
    database='test_postgres',
    port=5432,
    user='test_postgres',
    password='test_postgres'
)
cursor = connect.cursor()

data = ('Тест', 'Иванов', '9075467356', '100500')
ins = f"INSERT INTO passenger_info (name, surname,phone, flight_num) VALUES {data}"

cursor.execute(ins)
connect.commit()

cursor.close()
connect.close()
