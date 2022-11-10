# db tables here
from application import db, app


class Books(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    book_title=db.Column(db.String(50), nullable=False)
    #author=db.relationship('Author', backref='author')
    
class Authors(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(30), nullable=False)
    last_name=db.Column(db.String(30), nullable=False)
    book_id=db.Column(db.Integer, db.ForeignKey('books.id'))
    
#class BooksAndAuthors():
    