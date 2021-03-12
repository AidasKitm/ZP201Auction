from flask import Flask
from config import Config
from models.user import User
from models.auction import Auction
from models.offer import Offer
from models import db
from views.index import Index
from views.register import Registration
from views.login import Login
from views.logout import LogOut
from views.create_auction import CreateAuction
from views.auctiondetail import AuctionDetails
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app=app)
socketio = SocketIO(app=app)

app.add_url_rule('/', view_func=Index.as_view('index'))
app.add_url_rule('/register', view_func=Registration.as_view('register'))
app.add_url_rule('/login', view_func=Login.as_view('login'))
app.add_url_rule('/logout', view_func=LogOut.as_view('logout'))
app.add_url_rule('/create_auction', view_func=CreateAuction.as_view('create_auction'))
app.add_url_rule('/auction/<int:auction_id>', view_func=AuctionDetails.as_view('auction'))

# SOCKET -> Tunelis -> komunikuoti tarp 2 prisijungimo taškų -> Server <-> Client

@socketio.on('auction')
def auction(response):
    auction_listing = Auction.query.filter_by(id=response['auctionId']).first()
    offers = Offer.query.filter_by(
        auction_id=auction_listing.id).order_by(Offer.price.desc()).limit(5).all()
    highest_offers = []
    prices = []
    for offer in offers:
        user = User.query.filter_by(id=offer.user_id).first()
        single_offer = {'username': user.username, 'price': offer.price}
        highest_offers.append(single_offer)
        prices.append(single_offer['price'])
    highest_offer = auction_listing.minimum_price
    if prices != []:
        highest_offer = max(prices)

    auction_response = {'id': auction_listing.id,
                        'views':auction_listing.views,
                        'offers': highest_offers,
                        'highest_offer': highest_offer}
    emit('auctionResponse' + str(auction_response['id']), auction_response, broadcast=True)

if __name__ == '__main__':
    db.create_all(app=app)
    socketio.run(app=app, host='0.0.0.0')