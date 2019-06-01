from app import app
from app import langs
from flask import render_template


@app.route('/')
def data():
	cursor = db.cursor()
	sql = 'SELECT * FROM langs'
	cursor.execute(sql)
	results = cursor.fetchall()
@app.route('/index')
def main():
	data()
	return render_template('index.html')