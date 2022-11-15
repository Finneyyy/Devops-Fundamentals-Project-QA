from flask import render_template, request, redirect, url_for
from application import app, db
from application.models import Book, Author
from application.forms import AddBook, AddAuthor, UpdateBook, UpdateAuthor


@app.route('/')
@app.route('/home')
def home(): # This will be the read-list page
    return render_template('index.html')

@app.route('/add_book', methods=['GET','POST'])
def add_book():
    form=AddBook()
    if request.method=="POST":
        name=form.book_name.data
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

# @app.route('/update_book/<>', methods=['GET'])
# def update_book():
#     form=UpdateBook()    
#     if request.method=="POST":
#         book_name=form.book_name.data
#         book=Book.query.filter_by(id=bid).first()
#         book.book=book_name
#         db.session.commit()
#         return redirect(url_for('update_book', bid=book.book))
#     return render_template('update_book.html', form=form)




# ------------------------------------------------------------------ #
#                          Author Section                            #
# ------------------------------------------------------------------ #


@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    form=AddAuthor()
    bookandauthor=Book.query.all()
    for bAndA in bookandauthor:
        book_choice_author=form.book_author.choices.append((bAndA.id, bAndA.book_title))
        # for a in book_choice_author:
        #     #.,lsza;'[[[[[[[[edwwwwwwwwwwwwww' -> Thank my cat for this
        #     return a
    if request.method=="POST":
        first_name=form.first_name.data
        last_name=form.last_name.data
        newbookauthor=Author(first_name=first_name, last_name=last_name)
        db.session.add(newbookauthor)
        db.session.commit()
        return redirect(url_for('author_added', aid=newbookauthor.id))
    return render_template('add_author.html', form=form)


@app.route('/author_added', methods=['GET'])
def author_added():
    return render_template('author_added.html')
    
@app.route('/view_author', methods=['GET'])
def view_author():
    all_authors=Author.query.all()
    return render_template('view_author.html', all_authors=all_authors)

@app.route('/update_author/<int:aid>', methods=['GET', 'POST'])
def update_author(aid):
    form=UpdateAuthor()
    if request.method=="POST":
        author_firstname=form.update_author_firstname.data
        author_lastname=form.update_author_lastname.data
        author=Author.query.filter_by(id=aid).first()
        author.authorf=author_firstname
        author.authorl=author_lastname
        db.session.commit()
        return redirect(url_for('update_author'))
    return render_template('update_author.html', form=form)

@app.route('/delete_author-<int:aid>')
def delete_author(aid):
    author=Author.query.filter_by(id=aid).first()
    db.session.delete(author)
    db.session.commit()
    return redirect(url_for('view_author'))