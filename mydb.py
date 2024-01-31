import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'springstudent',
    passwd = 'springstudent'
)

cursorOject = database.cursor()


cursorOject.execute("CREATE DATABASE dcrm")

print("All done!")