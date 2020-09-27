import mysql.connector as conn


connect = conn.connect(
    host='localhost',
    database='bitnami_opencart',
    port=3306,
    user='root',
    password='bitnami'
)
cursor = connect.cursor()

id_ = 1
query = f"UPDATE passenger_info SET phone='89064563523' WHERE id={id_}"
cursor.execute(query)
connect.commit()

cursor.close()
connect.close()
