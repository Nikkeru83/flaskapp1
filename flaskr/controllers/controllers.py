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

# @app.route('/')
# def index():
#     con = sqlite3.connect(DATABASE)
#     cur = con.cursor()
#     cur.execute('SELECT id, title, price, arrival_day FROM books')  # IDを取得
#     books = [{'id': row[0], 'title': row[1], 'price': row[2], 'arrival_day': row[3]} for row in cur.fetchall()]
#     con.close()

#     return render_template('index.html', books=books)



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
    cur = con.cursor()
    cur.execute('INSERT INTO books (title, price, arrival_day) VALUES (?, ?, ?)', [title, price, arrival_day])
    con.commit()
    con.close()

    return redirect(url_for('index'))


@app.route('/edit', methods=['POST'])
def edit():
    book_id = request.form.get('book_id')

    if not book_id:
        return "エラー: 書籍IDが提供されていません"

    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute('SELECT * FROM books WHERE id = ?', [book_id])
    book = cur.fetchone()
    con.close()

    if not book:
        return "エラー: 該当する書籍データがありません"

    return render_template('edit.html', book=book)



@app.route('/update', methods=['POST'])
def update():
    book_id = request.form['book_id']
    title = request.form['title']
    price = request.form['price']
    arrival_day = request.form['arrival_day']

    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute('UPDATE books SET title=?, price=?, arrival_day=? WHERE id=?', [title, price, arrival_day, book_id])
    con.commit()
    con.close()

    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete():
    book_id = request.form.get('book_id')

    if not book_id:
        return "エラー: 書籍IDが提供されていません"

    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute('DELETE FROM books WHERE id = ?', [book_id])
    con.commit()
    con.close()

    return redirect(url_for('index'))






@app.route('/test')
def test():
    try:
        start = '2024-08-03'
        end = '2024-08-16'

        # yf.pdr_override()
        # df = data.get_data_yahoo('^N225', 'yahoo', start, end)
        # df = data.DataReader('^N225', 'yahoo', start, end)
        df = yf.download('^N225', start, end)
        result = 'success'
        print(type(df))
        print(df.columns)
        print(df.values)
    except:
        result = 'failure'
    return render_template(
        'test.html',
        result = result,
        columns = df.columns,
        data = df.values
    )


