from flask import Flask, render_template
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
from views.auction import AuctionListing
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app=app)

with app.app_context():
    db.create_all(app=app)

app.add_url_rule('/index', view_func=Index.as_view('index'))
app.add_url_rule('/register', view_func=Registration.as_view('register'))
app.add_url_rule('/login', view_func=Login.as_view('login'))
app.add_url_rule('/logout', view_func=LogOut.as_view('logout'))
app.add_url_rule('/create_auction', view_func=CreateAuction.as_view('create_auction'))
app.add_url_rule('/auction', view_func=AuctionListing.as_view('auction'))

if __name__ == '__main__':
    app.run()
