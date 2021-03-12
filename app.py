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

# SOCKET -> Tunelis -> komunikuoti tarp 2 prisijungimo tasku -> Server <-> Client

@socketio.on('auction')
def auction(response):
    selected_auction = Auction.query.filter_by(id=response['auctionId']).first()
    offers = Offer.query.filter_by(auction_id=selected_auction.id).order_by(Offer.price.desc()).limit(5).all()
    biggest_offers = []
    for offer in offers:
        user = User.query.filter_by(id=offer.id).first()
        offer_with_user = {'user': user, 'price': offer.price}
        biggest_offers.append(offer_with_user)

    auction_response = {'id':selected_auction.id, 'views': selected_auction.views, 'offers': biggest_offers}
    emit('auctionResponse' + str(auction_response['id']), auction_response, broadcast=True)


if __name__ == '__main__':
    db.create_all(app=app)
    socketio.run(app=app, host='0.0.0.0')

# Python3 -> sintakse -> loginiu uzdaviniu pasprest

# Vertinimo aplikacija:
#
# Vartotojas gali susikurti vartotojo sasaja.
#
# Įmonė gali susikurti sasaja
#
# Vartotojai gali įvertinti įmone ir palikti komentara prie įmonės įvertinimo.
#
# Vartotojas kuris paliko komentara gali ji pakoreguoti.
#
# Imone gali atsakyti i palikta vartotojo komentara.
