#pip install mysql-connector-python 

import mysql.connector

my_db   = mysql.connector.connect(
    host    = "localhost",
    user    = "admin",
    user    = "admin"
)

print(my_db)

