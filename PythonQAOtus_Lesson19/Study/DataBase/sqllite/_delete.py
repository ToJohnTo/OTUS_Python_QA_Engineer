import sqlite3

connect = sqlite3.connect('passengers.sqlite')
cursor = connect.cursor()

query = "DELETE FROM passenger_info  WHERE id=1"

cursor.execute(query)
connect.commit()
cursor.close()
connect.close()
