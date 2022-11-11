from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddBook(FlaskForm):
    add_book=StringField('Book Title', validators=[DataRequired(message="This field can't be blank")])
    submit=SubmitField("Submit Book")
    
class AddAuthor(FlaskForm):
    first_name=StringField("First Name", validators=[DataRequired(message="This field can't be blank")])
    last_name=StringField("Last Name", validators=[DataRequired(message="This field can't be blank")])
    submit=SubmitField("Submit Author")
    
class UpdateBook(FlaskForm):
    b_name=StringField("Book Title", validators=[DataRequired(message="This field can't be blank")])
    submit=SubmitField("Update Book")