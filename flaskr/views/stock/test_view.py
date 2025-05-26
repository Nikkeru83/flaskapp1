from flaskr import app
from flask import render_template, request, redirect,url_for
import yfinance as yf

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


@app.route('/kensaku', methods=['GET', 'POST'])
def kensaku():
    stock_data = None
    result = "未検索"

    if request.method == 'POST':
        ticker = request.form.get('meigara')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')

        if ticker and start_date and end_date:
            try:
                df = yf.download(ticker, start_date, end_date)
                result = 'success'
                print(type(df))
                print(df.columns)
                print(df.values)
            except Exception as e:
                result = 'failure'
                print(f"エラー発生: {e}")

    return render_template(
        'kensaku.html',
        result=result,
        columns=df.columns if 'df' in locals() else [],
        data=df.values if 'df' in locals() else []
    )

   