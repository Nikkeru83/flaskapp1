from flaskr import app
from flask import render_template, request, redirect,url_for
import sqlite3
# from pandas_datareader import data
# import pandas as pd
# import matplotlib.pyplot as plt
# %matplotlib inline
# import numpy as np
# import yfinance as yf
# import datetime
# import pandas_datareader.data as web
DATABASE = 'database.db'

@app.route('/')
def index():
    con = sqlite3.connect(DATABASE)
    db_books = con.execute('SELECT * FROM books').fetchall()
    con.close()

    books = []
    for row in db_books:
        books.append({'title': row[0], 'price': row[1], 'arrival_day': row[2]})
    
    return render_template(
        'index.html',
        books=books
    )


@app.route('/form')
def form():
    return render_template(
        'form.html'
    )   

@app.route('/register', methods=['POST'])
def register():
    title = request.form['title']
    price = request.form['price']
    arrival_day = request.form['arrival_day']

    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO books VALUES(?,?,?)',
                [title,price,arrival_day])
    con.commit()
    con.close()
    return redirect(url_for('index')) 

@app.route('/edit', methods=['POST'])
def edit():
    title = request.form.get('title')

    if not title:
        return "エラー: タイトルが提供されていません"

    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute('SELECT * FROM books WHERE title = ?', [title])
    book = cur.fetchone()
    con.close()

    if not book:
        return "エラー: 該当するタイトルのデータがありません"

    return render_template('edit.html', book=book)



@app.route('/update', methods=['POST'])
def update():
    title = request.form['title']
    new_title = request.form.get('new_title', title)  # 別のタイトルがあれば変更、なければ元のタイトルを使う
    price = request.form['price']
    arrival_day = request.form['arrival_day']

    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute('UPDATE books SET title=?, price=?, arrival_day=? WHERE title=?', [new_title, price, arrival_day, title])
    con.commit()
    con.close()

    return redirect(url_for('index'))




@app.route('/test')
def test():
    start = '2019-05-03'
    end = '2024-08-16'

    # yf.pdr_override()
    # df = data.get_data_yahoo('^N225', 'yahoo', start, end)
    # df = data.DataReader('^N225', 'yahoo', start, end)
    # df = yf.download('^N225', start, end)
    return render_template(
        'test.html'
    )


  