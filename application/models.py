# db tables here
from application import db


class Books(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(50), nullable=False)
    
class Authors(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(30), nullable=False)
    last_name=db.Column(db.String(30), nullable=False)
    book_id=db.Column(db.Integer, db.ForeignKey('books.id'))