from . import db
from .user import User
import datetime

class Auction(db.Model):
    __tablename__ = 'Auction'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    minimum_price = db.Column(db.Integer, nullable=False)
    auction_image = db.Column(db.String(256), nullable=False)
    end_day = db.Column(db.Date, default=datetime.datetime.now())
    end_hour = db.Column(db.Time, default=datetime.time())
    views = db.Column(db.Integer, default=0)
    offers = db.relationship('Offer', backref='auction', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)

