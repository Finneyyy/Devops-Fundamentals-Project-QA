from flask import render_template, request, redirect, url_for
from application import app, db
from application.models import Books, Authors
from application.forms import AddBook, AddAuthor


@app.route('/')
@app.route('/home')
def home(): # This will be the read-list page
    return render_template('index.html')

@app.route('/add_book', methods=['GET','POST'])
def add_book():
    form=AddBook()
    if request.method=="POST":
        name=form.add_book.data
        book=Books(book_title=name)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('book_added'))
    return render_template('add_book.html', form=form)

@app.route('/book_added', methods=['GET'])
def book_added():
    return render_template('book_added.html')

@app.route('/view_books', methods=[])
def view_books():
    all_books=Books.query.all()
    
    return render_template('view_books.html')

@app.route('/update_book')
def update_book():
    return render_template('/update_book.html')

@app.route('/delete_book')
def delete_book():
    return render_template('/delete_book.html')



# ------------------------------------------------------------------ #
#                          Author Section                            #
# ------------------------------------------------------------------ #


@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    #return redirect()
    form=AddAuthor()
    if request=="POST":
        first_name=form.first_name.data
        last_name=form.last_name.data
        author=AddAuthor(first_name, last_name)
        db.session.add(author)
        db.session.commit()
    return render_template('add_author.html', form=form)

