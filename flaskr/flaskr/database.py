import sqlite3
from config import DATABASE

def create_books_table():
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    price REAL,
                    arrival_day TEXT
                )''')
    con.commit()
    con.close()