from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=os.environ["DATABASE_URI"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']=os.environ["secret_key"] # CSRF protection

db=SQLAlchemy(app)

# additional functionality under here
from application import routes
from application import models
from application import forms