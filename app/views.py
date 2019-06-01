from app import app
from flask import render_template
import pymysql

db = pymysql.connect("localhost", "root1", "", "langs")

@app.route('/')
def data():
	cursor = db.cursor()
	sql = 'SELECT * FROM lang'
	cursor.execute(sql)
	results = cursor.fetchall()
	print(results)
	return render_template('index.html')
@app.route('/index')
def main():
	a=data()
	return render_template('index.html')