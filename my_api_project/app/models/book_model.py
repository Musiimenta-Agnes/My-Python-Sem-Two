from app.extensions import db
from datetime import datetime


class Book(db.Model):

    # The tabel name
    __tablename__ = 'book'
   
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    title = db.Column(db.String(20), nullable = False)
    pages = db.Column(db.Integer, nullable = False)
    price = db.Column(db.Integer, nullable = False)
    price_unit = db.Column(db.String(20), nullable = False,default = "UGX")
    publication_date = db.Column(db.Date, nullable = False)
    isbn = db.Column(db.String(30), nullable = False, unique = True)
    genre = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(255), nullable = False)
    image = db.Column(db.String(255), nullable = True)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # user = db.relationship('User', backref = 'books')
    created_at = db.Column(db.DateTime, default = datetime.now())
    updated_at = db.Column(db.DateTime, onupdate = datetime.now())


    def __init__(self, id, title, pages, price_unit, publication_date, isbn, genre, description, image, user_id,user, created_at,update_at ):
        super(Book, self).__init__()

        self.id = id
        self.title = title
        self.pages = pages
        self.price_unit = price_unit
        self.publication_date = publication_date
        self.isbn = isbn
        self.genre = genre
        self.description = description
        self.image= image
        self.user_id = user_id
        self.user = user
        self.pages= pages
        self.publication_date = publication_date
        self.created_at = created_at
        self.updated_at = update_at