from flask import Flask
app = Flask(__name__, template_folder="templates")
import flaskr.views.nishihara.select_books_view
import flaskr.views.nishihara.book_register_view
import flaskr.views.stock.test_view

from flaskr import db
db.create_books_table()

if __name__ == '__main__':
    create_tables()  # テーブルを作成
    app.run(debug=True)
