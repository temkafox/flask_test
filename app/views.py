from app import app
from app import langs
from flask import render_template


@app.route('/index')
def data():
	sql1='select * from lang'
	cursor.execute(sql1)
	data=cursor.fetchall()
	print(data)
	conn.close()

@app.route('/')
def main():
	data()
    return render_template('index.html')

