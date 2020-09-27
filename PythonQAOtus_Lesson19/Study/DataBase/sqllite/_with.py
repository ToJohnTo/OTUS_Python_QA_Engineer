import sqlite3

connect = sqlite3.connect('passengers.sqlite')

data = ('Тест2', 'Тестовый2', '9066575435', '55555')

ins_str = f"INSERT INTO 'passenger_info' (name, surname,phone, flight_num) VALUES {data}"

with connect:
    connect.execute(ins_str)
    connect.rollback()

connect.commit()
connect.close()
