import mysql.connector
from datetime import datetime

# Replace 'yourpassword' with your actual MySQL root or user password
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="yourpassword",
    database="my_logs"
)

cursor = db.cursor()

shorthands = {
    "l": "lunch start",
    "le": "lunch end",
    "nr": "\n",
    "": "no-input"
}

def log_entry(text):
    if len(text) <= 4:
        text = shorthands.get(text, text)
    if text == "[displays the help chapter, where these shorthands are listed]":
        print("Help:\n", "\n".join(f"{k} --> {v}" for k, v in shorthands.items()))
        return
    now = datetime.now()
    date = now.date()
    weekday = now.strftime("%A")
    time = now.strftime("%H:%M:%S")
    cursor.execute("INSERT INTO daily_logs (date, weekday, time, text) VALUES (%s, %s, %s, %s)", (date, weekday, time, text))
    db.commit()
    print("Entry saved.")

while True:
    text = input("Enter your log (type '-h' for help): ")
    if text == "-h":
        text = "[displays the help chapter, where these shorthands are listed]"
    log_entry(text)
