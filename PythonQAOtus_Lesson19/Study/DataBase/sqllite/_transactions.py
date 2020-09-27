import sqlite3

connect = sqlite3.connect('passengers.sqlite')
cursor = connect.cursor()

data = ('Тест', 'Тестовый', '9062537836', '67801')
_id = 3
name = 'Тест123'

ins_str = f"INSERT INTO 'passenger_info' (name, surname,phone, flight_num) VALUES {data}"
upd_str = f"UPDATE passenger_info SET flight_num='12557' WHERE id={_id}"
del_str = f"DELETE FROM passenger_info  WHERE name = {name} "

cursor.execute(ins_str)
cursor.execute(upd_str)
# connect.commit()

# connect.rollback()
cursor.close()
# connect.commit()
connect.close()
