from flaskr import app
from flask import render_template, request, redirect,url_for
import sqlite3
DATABASE = 'database.db'

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

