import mysql.connector as conn


connect = conn.connect(
    host='localhost',
    database='bitnami_opencart',
    port=3306,
    user='root',
    password='bitnami'
)
cursor = connect.cursor()

with open('oc_product.sql', 'r') as file:
    cursor.execute(file.read())

connect.commit()
cursor.close()
connect.close()
