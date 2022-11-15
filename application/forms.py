from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class AddBook(FlaskForm):
    book_name=StringField('Book Title', validators=[DataRequired(message="This field can't be blank")])
    submit=SubmitField("Submit Book")
    
class AddAuthor(FlaskForm):
    first_name=StringField("First Name", validators=[DataRequired(message="This field can't be blank")])
    last_name=StringField("Last Name", validators=[DataRequired(message="This field can't be blank")])
    book_author=SelectField("Add to Book: ", choices=[])
    submit=SubmitField("Submit Author")
    
class UpdateBook(FlaskForm):
    book_name=StringField("Book Title", validators=[DataRequired(message="This field can't be blank")])
    book1=SelectField("Select Book: ", choices=[])
    submit=SubmitField("Update Book")
    
class UpdateAuthor(FlaskForm):
    update_author_firstname=StringField("First Name", validators=[DataRequired(message="This field can't be blank")])
    update_author_lastname=StringField("Last Name", validators=[DataRequired(message="This field can't be blank")])
    submit=SubmitField("Update Author")