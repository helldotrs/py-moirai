import argparse
import datetime
import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="moirai_db"
)
cursor = db.cursor()

# Function to save user input to the database
def save_to_database(text, comment):
    current_date = datetime.datetime.now().date()
    current_time = datetime.datetime.now().time()
    weekday = current_date.strftime("%A")
    sql = "INSERT INTO punch_records (date, time, weekday, maintext, comment) VALUES (%s, %s, %s, %s, %s)"
    val = (current_date, current_time, weekday, text, comment)
    cursor.execute(sql, val)
    db.commit()

# Function to display the last 'n' entries from the database
def show_events(n):
    sql = "SELECT * FROM punch_records ORDER BY id DESC LIMIT %s"
    cursor.execute(sql, (n,))
    records = cursor.fetchall()
    for record in records:
        print(record)

# Function to display entries for a specified date
def show_date(date):
    sql = "SELECT * FROM punch_records WHERE date = %s"
    cursor.execute(sql, (date,))
    records = cursor.fetchall()
    for record in records:
        print(record)

# Function to remove an entry by ID
def remove_entry(entry_id):
    sql = "DELETE FROM punch_records WHERE id = %s"
    cursor.execute(sql, (entry_id,))
    db.commit()

# Parse command line arguments
parser = argparse.ArgumentParser(description="moirai by hell.rs - Time Clock System")
parser.add_argument("text", help="User input to save in the database")
parser.add_argument("-c", "--comment", help="Add following text to the comment field for the last entry")
parser.add_argument("-se", "--show-events", type=int, help="Display last 'n' database entries")
parser.add_argument("-sd", "--show-date", help="Display entries for specified date (ISO format)")
parser.add_argument("-r", "--remove", help="Remove entry with specified ID")
parser.add_argument("-p", "--plus", type=int, default=8, help="Display current time plus specified number of hours (default: 8)")
args = parser.parse_args()

# Main logic
if args.text:
    if len(args.text) <= 3:
        # Check if text is in dict.txt
        # If specified in dict, append ":text"
        pass
    else:
        save_to_database(args.text, args.comment)
elif args.show_events:
    show_events(args.show_events)
elif args.show_date:
    show_date(args.show_date)
elif args.remove:
    remove_entry(args.remove)
elif args.plus:
    current_time = datetime.datetime.now().time()
    current_time_plus_hours = (datetime.datetime.combine(datetime.date.today(), current_time) + datetime.timedelta(hours=args.plus)).time()
    print(f"Current time plus {args.plus} hours: {current_time_plus_hours}")
