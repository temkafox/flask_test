from flask import Flask, render_template
import pymysql

db = pymysql.connect("localhost", "root", "", "langs")

app = Flask(__name__)

from app import views