from flask import redirect, url_for, render_template, session, request, flash
from flask.views import MethodView
from models import db
from models.offer import Offer
from models.user import User
from models.auction import Auction


class AuctionDetails(MethodView):

    def get(self, auction_id):
        auction = Auction.query.filter_by(id=auction_id).first()

        if auction is None:
            return redirect(url_for('index'))

        user = User.query.filter_by(id=auction.user_id).first()
        auction.views += 1
        db.session.commit()

        offers_by_auction = Offer.query.filter_by(
            auction_id=auction.id).order_by(Offer.price.desc()).limit(5).all()
        user_offers = []
        if offers_by_auction is not None:
            for offer in offers_by_auction:
                user_offers.append(User.query.filter_by(id=offer.user_id).first())

        session_user = session.get('username')
        if user.username == session_user:
            session_user = None

        return render_template('auction.html',
                               auction=auction,
                               user=user,
                               offers_by_auction=offers_by_auction,
                               user_offers=user_offers,
                               session=session_user)

    def post(self, auction_id):
        auction = Auction.query.filter_by(id=auction_id).first()

        try:
            new_value = int(request.form['new_price'])
            if new_value < auction.minimum_price:
                raise ValueError

        except ValueError:
            flash("Offered price is too low")
            return redirect(url_for('auction', auction_id=auction_id))
        except Exception:
            flash("Illegal price input")
            return redirect(url_for('auction', auction_id=auction_id))

        user = User.query.filter_by(username=session.get('username')).first()
        new_offer = Offer(auction_id=auction.id, user_id=user.id, price=request.form['new_price'])
        db.session.add(new_offer)
        db.session.commit()
        return redirect(url_for('auction', auction_id=auction_id))
