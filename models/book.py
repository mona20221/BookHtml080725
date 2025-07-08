from extensions import db


class Book(db.Model):
    __tablename__ = 'books'
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    isbn = db.Column(db.String(14))
    publication_year = db.Column(db.Integer)
    copies = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.author_id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'))
    author = db.relationship('Author', backref='books')
    genre = db.relationship('Genre', backref='books')