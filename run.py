#!flask/bin/python
from app import app
from config import Configuration
app.run(debug = True, host='0.0.0.0')