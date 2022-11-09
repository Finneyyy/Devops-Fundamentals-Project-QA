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

@app.route('/view_books')
def view_books():
    return render_template('/view_book.html')

@app.route('/delete_books')
def delete_books():
    return render_template('/delete_book.html')