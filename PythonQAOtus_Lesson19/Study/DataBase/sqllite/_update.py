import sqlite3

connect = sqlite3.connect('passengers.sqlite')
cursor = connect.cursor()

query = "UPDATE passenger_info SET patronymic='Иванович', name='Тест1234' WHERE id=1"

cursor.execute(query)
connect.commit()

cursor.close()
connect.close()
