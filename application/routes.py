from flask import render_template, request, redirect, url_for
from application import app, db
from application.models import Book, Author
from application.forms import AddBook, AddAuthor, UpdateBook


@app.route('/')
@app.route('/home')
def home(): # This will be the read-list page
    return render_template('index.html')

@app.route('/add_book', methods=['GET','POST'])
def add_book():
    form=AddBook()
    if request.method=="POST":
        name=form.add_book.data
        book=Book(book_title=name)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('book_added'))
    return render_template('add_book.html', form=form)

@app.route('/book_added', methods=['GET'])
def book_added():
    return render_template('book_added.html')

@app.route('/view_books', methods=['GET'])
def view_books():
    all_books=Book.query.all()
    return render_template('view_books.html', all_books=all_books)

@app.route('/update_book')
def update_book(bid):
    form=UpdateBook()
    if request.method=="POST":
        b_name=form.b_name.data
        book=Book.query.filter_by(id=bid).first()
        book.book=b_name
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('update_book.html', form=form)

@app.route('/delete_book')
def delete_book():
    return render_template('delete_book.html')



# ------------------------------------------------------------------ #
#                          Author Section                            #
# ------------------------------------------------------------------ #


@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    form=AddAuthor()
    if request.method=="POST":
        first_name=form.first_name.data
        last_name=form.last_name.data
        newbookauthor=Author(first_name=first_name, last_name=last_name)
        db.session.add(newbookauthor)
        db.session.commit()
        return redirect(url_for('add_author'))
    return render_template('add_author.html', form=form)


@app.route('/author_added', methods=['GET'])
def author_added():
    return render_template(url_for('author_added.html'))
    
@app.route('/view_author', methods=['GET'])
def view_author():
    all_authors=Author.query.all()
    return render_template('view_author.html', all_authors=all_authors)
