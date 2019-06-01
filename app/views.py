from app import app
from flask import render_template

db = pymysql.connect("localhost", "root1", "", "langs")

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