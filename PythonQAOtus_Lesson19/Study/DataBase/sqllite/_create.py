import sqlite3

connect = sqlite3.connect('passengers.sqlite')

# Создаем курсор - это специальный объект, который делает запросы и получает их результаты
cursor = connect.cursor()

# with open('oc_product.sql', 'r') as file:
#     # file - TextIO type
#     cursor.execute(file.read())

# -----------------------------------------
# data = ('Иван', 'Тестовый', '9031456783', '12557')
# ins_str = f"INSERT INTO 'passenger_info' (name, surname,phone, flight_num) VALUES {data}"

# cursor.execute(ins_str)

# -----------------------------------------
ins_str = f"INSERT INTO 'passenger_info' (name, surname,phone, flight_num) VALUES (?,?,?,?)"
many_data = [
    ('Иван', 'Тестовый', '9031456783', '12557'),
    ('Александр', 'Иванов', '9874366783', '34566'),
    ('Петр', 'Иванов', '9074537356', '34678')
]

cursor.executemany(ins_str, many_data)

connect.commit()
cursor.close()
connect.close()
