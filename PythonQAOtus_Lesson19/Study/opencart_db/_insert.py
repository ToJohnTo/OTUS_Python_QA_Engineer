import mysql.connector as conn


connect = conn.connect(
    host='localhost',
    database='bitnami_opencart',
    port=3306,
    user='root',
    password='bitnami'
)
cursor = connect.cursor()

data = ('Тест', 'Иванов', '9075467356', '100500')
ins = f"INSERT INTO passenger_info (name, surname,phone, flight_num) VALUES {data}"

cursor.execute(ins)
connect.commit()

cursor.close()
connect.close()
