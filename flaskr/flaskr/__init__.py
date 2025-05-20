from flask import Flask
app = Flask(__name__, template_folder="templates")
import flaskr.controllers.controllers
import flaskr.controllers.home_ctr

from flaskr import db
db.create_books_table()

if __name__ == '__main__':
    create_tables()  # テーブルを作成
    app.run(debug=True)
