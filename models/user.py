from . import db

class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=True)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50),unique=True, nullable=True)
    address = db.Column(db.String(30), nullable=False)
    image = db.Column(db.String(256), nullable=True, default="default_profile_image.jpg")
    auctions = db.relationship('Auction', backref='user', lazy=True)

