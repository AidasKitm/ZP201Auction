from . import db

class Offer(db.Model):
    __tablename__ = 'Offer'

    id = db.Column(db.Integer, primary_key=True)
    auction_id = db.Column(db.Integer, db.ForeignKey('Auction.id'), nullable=False)
    user_id = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)