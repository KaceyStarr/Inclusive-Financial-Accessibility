import sqlite3 
import datetime

conn = sqlite3.connect("expenses.sqlite")
cur = conn.cursor()

while True:
    print("Select an option:")
    