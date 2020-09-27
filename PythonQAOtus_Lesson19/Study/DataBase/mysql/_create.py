import pymysql
import mysql.connector as conn

connect = conn.connect(
    host='localhost',
    database='test',
    port=3306,
    user='test',
    password='test'
)
cursor = connect.cursor()

with open('passengers.sql', 'r') as file:
    cursor.execute(file.read())

connect.commit()
cursor.close()
connect.close()
