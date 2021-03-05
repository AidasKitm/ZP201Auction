import os
from tinify import tinify
from flask import redirect, url_for, render_template, session
from flask.views import MethodView
from werkzeug.utils import secure_filename
from models.auction import Auction
from models.user import User
from models import db
from forms.auction_form import AuctionForm


class CreateAuction(MethodView):

    def get(self):
        auction_form = AuctionForm()

        if session.get('username') is None:
            return redirect(url_for('login'))

        return render_template('create_auction.html', auction_form=auction_form)

    def post(self):
        auction_form = AuctionForm()

        if auction_form.validate_on_submit():
            user = User.query.filter_by(username=session.get('username')).first()

            form_image_data = auction_form.auction_image.data
            if form_image_data is not None:
                image_generated_name = user.username + '_' + form_image_data.filename
                image_file = secure_filename(image_generated_name)

                tinify.from_file(form_image_data).to_file(os.path.join("../static/auction_images/",
                                                                       image_file))
            else:
                image_file = "default_image.jpg"
            new_auction = Auction(title=auction_form.title.data,
                                  category=auction_form.category.data,
                                  city=auction_form.city.data,
                                  minimum_price=auction_form.minimal_price.data,
                                  auction_image=image_file,
                                  end_day=auction_form.end_day.data,
                                  end_hour=auction_form.end_hour.data,
                                  description=auction_form.description.data,
                                  user_id=user.id)

            db.session.add(new_auction)
            db.session.commit()

            return redirect(url_for('auction',
                                    auction_id=Auction.query.order_by(Auction.id.desc()).first().id))
        else:
            return redirect(url_for('create_auction'))
