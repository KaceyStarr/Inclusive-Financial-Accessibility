import sqlite3 
import datetime

conn = sqlite3.connect("expenses.db")
cur = conn.cursor()

#function to add a user
def add_user(username, password, budget):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()

    #allows to connect with database
    cursor.execute('''
    INSERT INTO people (username, password, budget) VALUES (?, ?, ?)
    ''', (username, password, budget))

    conn.commit()  
    conn.close()   

# Testing the Code
add_user('test1', 'test2', 1000)
