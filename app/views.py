from app import app
from flask import render_template, request
import pymysql

db = pymysql.connect("localhost", "root1", "", "langs")

@app.route('/')
def data():
	cursor = db.cursor()
	sql_lang = 'SELECT * FROM lang'
	cursor.execute(sql_lang)
	results = cursor.fetchall()
	#print(results)
	return render_template('index.html', db=results)

@app.route('/req_items', methods=['POST'])
def items():
	print(request)
#@app.route('/index')
#def main():
#	a=data()
#	return render_template('index.html')