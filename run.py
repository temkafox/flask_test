#!flask/bin/python
from app import app, render_template
app.run(debug = True, host='0.0.0.0')