import mysql.connector

database = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    passwd= 'Msd1213'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print('Database Created!')