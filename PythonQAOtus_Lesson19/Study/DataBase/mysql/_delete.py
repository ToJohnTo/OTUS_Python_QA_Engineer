import pymysql


connect = pymysql.connect(
    host='localhost',
    database='test',
    port=3306,
    user='test',
    password='test'
)
cursor = connect.cursor()

query = "DELETE FROM passenger_info  WHERE id=1"
cursor.execute(query)
connect.commit()

connect.close()
