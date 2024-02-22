#pip install mysql-connector-python 

import mysql.connector

my_db   = mysql.connector.connect(
    host    = "localhost",
    user    = "root",
    user    = "root"
    db      = "moirai_db"
)

print(my_db)

#used to ececute sql statements
cursor = my_db.cursor()

#execute sql
#cursor.execute("SQL STATEMENT")

user_input    = input("input:")
