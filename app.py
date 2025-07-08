from flask import Flask, jsonify, request, render_template, url_for
from extensions import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://upu4ozux3dkb0kkpwusa:pWHFUECWXXcfGEo0poKdFWaiEI0cvv@b7zabufywrnnt4i8piy9-postgresql.services.clever-cloud.com:50013/b7zabufywrnnt4i8piy9'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)

from models.author import Author
from models.genre import Genre
from models.book import Book

@app.route('/')
def index():
    return "Main"

@app.route('/authors')
def authors():
    authors = Author.query.all()
    return render_template('authors.html', authors = authors)

@app.route('/genre')
def genre():
    genres = Genre.query.all()
    return render_template('genre.html', genres = genres)

@app.route('/book')
def book():
    books = Book.query.all()
    return render_template('book.html', books=books)

@app.route('/book/add', methods=['GET', 'POST'])
def add_book():
    authors = Author.query.all()
    genres = Genre.query.all()

    message = None

    if request.method == 'POST':
        new_book = Book(
            title=request.form['title'],
            isbn=request.form['isbn'],
            publication_year=request.form['publication_year'],
            copies=request.form['copies'],
            author_id=request.form['author_id'],
            genre_id=request.form['genre_id']
        )
        db.session.add(new_book)
        db.session.commit()
        message = "Kniha bola úspešne pridaná."

    return render_template('add_book.html', authors=authors, genres=genres, message=message)

# redeploy test
if __name__ == '__main__':
    app.run(debug=True)