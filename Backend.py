import sqlite3

# Connect to SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect("expenses.db")

# Create a cursor object
cur = conn.cursor()

# Create the expenses table if it doesn't exist
cur.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY,
    date DATE,
    description TEXT,
    category TEXT,
    price REAL
)
""")

# Commit the transaction
conn.commit()

# Close the connection
conn.close()

