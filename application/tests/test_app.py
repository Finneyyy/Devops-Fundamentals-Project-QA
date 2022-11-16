# tests here eventually
from flask import url_for
from flask_testing import TestCase
from application import app,db
from application.models import Author, Book
import os

class TestBase(TestCase):
    # Do a basic setup for all tests
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI= os.environ["DATABASE_URI"], SECRET_KEY=os.environ["secret_key"], DEBUG=True, WTF_CSRF_ENABLED=True)
        return app
    
    def setUp(self):
        db.create_all()
        s_book=Book(book_title="Test1")
        db.session.add(s_book)
        db.session.commit()
        s_author=Author(first_name="Test", last_name="McTest")
        db.session.add(s_author)
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        

class TestBookV(TestBase):
    def test_bk_get(self):
        response=self.client.get(url_for('view_books'))
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Library App',response.data)
        
class TestAuthorV(TestBase):        
    def test_ar_get(self):
        response=self.client.get(url_for('view_author'))
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Add Author', response.data)
        
class TestHome(TestBase):
    def test_homepage(self):
        response=self.client.get(url_for('home'))
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Home', response.data)
        
class TestAddBookView(TestBase):
    def test_view_add_book(self):
        response=self.client.get(url_for('add_book'))
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Add Book',response.data)
        
class TestAddBook(TestBase):
    def test_add_book(self):
        response=self.client.post(url_for('add_book'), data=dict(book_title="New Book", name="test"), follow_redirects=True)
        self.assertIn(b'Add Book', response.data)
        
class TestAddAuthorView(TestBase):
    def test_view_add_author(self):
        response=self.client.get(url_for('add_author'))
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Add Author',response.data)
        
class TestAddAuthor(TestBase):
    def test_add_author(self):
        response=self.client.post(url_for('add_author'), data=dict(first_name="Test", last_name="McTest", follow_redirects=True))
        self.assertIn(b'Redirecting',response.data)
        
class TestViewAddAuthorAdded(TestBase):
    def test_author_added(self):
        response=self.client.get(url_for('book_added', follows_redirects=True))
        self.assertIn(b'View Authors', response.data)


class TestUpdateAuthorView(TestBase):
    def test_view_update_author(self):
        response=self.client.get(url_for('update_author', aid=1))
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Update Author',response.data)

class TestUpdateAuthor(TestBase):
    def test_update_author(self):
        response=self.client.post(url_for('update_author', aid=1), data=dict(first_name="Joe", last_name="Bloggs", follow_redirects=True))
        self.assertIn(b'Update Author',response.data)
        
class TestDelAuthorView(TestBase):
    def test_view_del_author(self):
        response=self.client.get(url_for('delete_author', aid=1))
        self.assertEqual(response.status_code,302)
                
        
class TestDelAuthor(TestBase):
    def test_del_author(self):
        response=self.client.get(url_for('delete_author', aid=1), follow_redirects=True)
        self.assertEqual(response.status_code,200)
        self.assertIn(b'View Authors', response.data)