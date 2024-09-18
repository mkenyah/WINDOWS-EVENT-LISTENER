import tkinter as tk
import sqlite3
from datetime import datetime
import pygetwindow as gw
import time
import threading

def create_table():
    conn = sqlite3.connect('habit_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS activity_log (
            timestamp TEXT,
            activity TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_activity_to_file():
    while True:
        active_window = gw.getActiveWindow()
        if active_window:
            app_name = active_window.title
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_activity_to_db(app_name)  # Log activity to the database
            with open("activity_log.txt", "a") as log:
                log.write(f"{timestamp} - {app_name}\n")
                print(f"Logged: {timestamp} - {app_name}")
        time.sleep(60)  # Log activity every 60 seconds

def log_activity_to_db(activity):
    conn = sqlite3.connect('habit_tracker.db')
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO activity_log (timestamp, activity) VALUES (?, ?)", (timestamp, activity))
    conn.commit()
    conn.close()

def start_logging():
    threading.Thread(target=log_activity_to_file, daemon=True).start()

def show_logs():
    conn = sqlite3.connect('habit_tracker.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM activity_log ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()
    
    log_display.delete(1.0, tk.END)
    for row in rows:
        log_display.insert(tk.END, f"{row[0]} - {row[1]}\n")

# Ensure the table exists
create_table()

# GUI setup
root = tk.Tk()
root.title("Activity Logger")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

start_button = tk.Button(frame, text="Start Logging", command=start_logging)
start_button.pack(side=tk.LEFT, padx=5)

show_button = tk.Button(frame, text="Show Logs", command=show_logs)
show_button.pack(side=tk.LEFT, padx=5)

log_display = tk.Text(root, width=80, height=20)
log_display.pack(padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
