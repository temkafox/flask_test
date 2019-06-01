from app import app
from flask import jsonify
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

@app.route('/req_items/<url>', methods=['GET'])
def req_items(url):
	print(url)
	cursor = db.cursor()
	sql_fw = 'SELECT * FROM fw JOIN lang USING(id_lang)'
	cursor.execute(sql_fw)
	results = cursor.fetchall();
	return jsonify(results)
#@app.route('/index')
#def main():
#	a=data()
#	return render_template('index.html')