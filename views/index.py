from flask import render_template, session
from flask.views import MethodView
from models.auction import Auction


class Index(MethodView):
    def get(self):

        auctions = Auction.query.order_by(Auction.id.desc()).all()
        user = session.get('username')
        return render_template('index.html', user=user, auctions=auctions)