from flask import Flask, render_template
import pymysql

app = Flask(__name__)

from app import views