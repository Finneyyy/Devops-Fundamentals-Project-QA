# db tables here
from application import db


class Books(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(50), nullable=False)
    
#class Authors(db.Model):
    