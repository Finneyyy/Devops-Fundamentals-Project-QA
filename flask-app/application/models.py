# db tables here
from application import db, app
from flask_sqlalchemy import SQLAlchemy

class Book(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    book_title=db.Column(db.String(50), nullable=False)
    book_author=db.relationship('Author', backref='book')
   
class Author(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(30), nullable=False)
    last_name=db.Column(db.String(30), nullable=False)
    book_id=db.Column(db.Integer, db.ForeignKey('book.id'))
    def __str__(self):
        return f"Author {self.first_name} {self.last_name}"

#class Book_Author(db.Model):
  #  book_id=
  #  author_id=