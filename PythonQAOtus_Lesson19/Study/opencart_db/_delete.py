import mysql.connector as conn


connect = conn.connect(
    host='localhost',
    database='bitnami_opencart',
    port=3306,
    user='root',
    password='bitnami'
)
cursor = connect.cursor()

query = "DELETE FROM passenger_info  WHERE id=1"
cursor.execute(query)
connect.commit()

cursor.close()
connect.close()
