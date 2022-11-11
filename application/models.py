# db tables here
from application import db, app
from flask_sqlalchemy import SQLAlchemy

class Book(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    book_title=db.Column(db.String(50), nullable=False)
   # book_authors=db.relationship('Author', backref='authorbr')
   
class Author(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(30), nullable=False)
    last_name=db.Column(db.String(30), nullable=False)
    #book_id=db.Column(db.Integer, db.ForeignKey('book.id'))
    

