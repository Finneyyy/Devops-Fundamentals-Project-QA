from application import app, db
from application.models import Books, Authors
from flask import render_template, request, redirect, url_for

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/add_book')
def add_book():
    return render_template('add_book.html')

@app.route('/update_book')
def update_book():
    return render_template('/update_book.html')

@app.route('/delete_book')
def delete_book():
    return render_template('/delete_book.html')