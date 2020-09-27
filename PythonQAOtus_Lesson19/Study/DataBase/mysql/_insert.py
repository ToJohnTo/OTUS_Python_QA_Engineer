import pymysql
import mysql.connector as conn

connect = conn.connect(
    host='localhost',
    database='test',
    port=3306,
    user='test',
    password='test'
)
cursor = connect.cursor()

data = ('Тест', 'Иванов', '9075467356', '100500')
ins = f"INSERT INTO passenger_info (name, surname,phone, flight_num) VALUES {data}"

cursor.execute(ins)
connect.commit()

cursor.close()
connect.close()
