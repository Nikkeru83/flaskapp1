from flaskr import app
from flask import render_template, request, redirect,url_for
import sqlite3

DATABASE = 'database.db'

@app.route('/')
def index():
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute('SELECT id, title, price, arrival_day FROM books')  # IDを取得
    books = [{'id': row[0], 'title': row[1], 'price': row[2], 'arrival_day': row[3]} for row in cur.fetchall()]
    con.close()

    return render_template('index.html', books=books)