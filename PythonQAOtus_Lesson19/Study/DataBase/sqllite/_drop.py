import sqlite3

connect = sqlite3.connect('passengers.sqlite')
drop_query = 'DROP TABLE passenger_info'
connect.execute(drop_query)

connect.commit()
connect.close()
