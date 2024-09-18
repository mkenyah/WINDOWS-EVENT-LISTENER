import psutil
# import mysql.connector
import pygetwindow as gw
import time
from datetime import datetime

def log_activity():
    with open("activity_log.txt", "a") as log:
        while True:
            active_window = gw.getActiveWindow()
            if active_window:
                app_name = active_window.title
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log.write(f"{timestamp} - {app_name}\n")
                print(f"Logged: {timestamp} - {app_name}")
            time.sleep(60)  # Log activity every 60 seconds

if __name__ == "__main__":
    log_activity()
    
    # USING LOCAL DATABASE
    
    import sqlite3
from datetime import datetime

# Connect to the SQLite database (or create it)
conn = sqlite3.connect('habit_tracker.db')
cursor = conn.cursor()

# Create a table to store activity logs
cursor.execute('''CREATE TABLE IF NOT EXISTS activity_log 
                  (timestamp TEXT, activity TEXT)''')

def log_activity(activity):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO activity_log (timestamp, activity) VALUES (?, ?)", (timestamp, activity))
    conn.commit()

# Example of logging a habit (replace this with actual data tracking logic)
log_activity('Opened Chrome')


# EVENT LISTENER

import wmi

c = wmi.WMI()

# Listen to process creation events
process_watcher = c.Win32_Process.watch_for("creation")

while True:
    new_process = process_watcher()
    print(f"New Process: {new_process.Caption}")
    
    # db
    import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('your_database.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Example: Create a table (if it doesn't exist)
cursor.execute('''
CREATE TABLE IF NOT EXISTS habits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    habit TEXT NOT NULL,
    timestamp TEXT DEFAULT CURRENT_TIMESTAMP
)
''')

# Example: Insert a record
cursor.execute("INSERT INTO habits (habit) VALUES ('Drink Water')")

# Commit changes
conn.commit()

# Example: Fetch all records
cursor.execute("SELECT * FROM habits")
rows = cursor.fetchall()

# Print fetched records
for row in rows:
    print(row)

# Close the connection
conn.close()


