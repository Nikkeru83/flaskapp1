import sqlite3

DATABASE = "database.db"

def create_books_table():
    # データベース接続
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()  

    # 書籍テーブルを作成
    cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            price INTEGER NOT NULL,
            arrival_day DATE NOT NULL
        )
    """)



    # データベース接続を閉じる
    con.commit()
    con.close()


