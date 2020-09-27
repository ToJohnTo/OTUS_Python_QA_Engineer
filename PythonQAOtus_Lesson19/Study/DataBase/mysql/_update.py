import pymysql

connect = pymysql.connect(
    host='localhost',
    database='test',
    port=3306,
    user='test',
    password='test'
)
cursor = connect.cursor()

id_ = 1
query = f"UPDATE passenger_info SET phone='89064563523' WHERE id={id_}"
cursor.execute(query)

connect.commit()

connect.close()
