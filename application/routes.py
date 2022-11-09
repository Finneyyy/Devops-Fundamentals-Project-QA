from application import app, db
from application.models import Books, Authors
from flask import render_template, request, redirect, url_for

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')