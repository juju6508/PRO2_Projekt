# Alle Flask-Module
from flask import Flask
from flask import render_template

app = Flask("__name__")

#Startseite
@app.route('/', methods=['get', 'post'])
def startseite():
    return render_template('startseite.html')