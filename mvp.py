#pip install mysql-connector-python 

import mysql.connector

my_db   = mysql.connector.connect(
    host        = "localhost",
    user        = "root",
    password    = "root",
    database    = "moirai_db",

)

#    table       = "main"

print(my_db)

#used to ececute sql statements
cursor = my_db.cursor()

#execute sql
#cursor.execute("SQL STATEMENT")

user_input    = input("input:")

#save_to_db(id, time, date, user_input)
