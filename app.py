from flask import Flask, render_template
from config import Config
from models.user import User
from models.auction import Auction
from models.offer import Offer
from models import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app=app)

with app.app_context():
    db.create_all(app=app)


if __name__ == '__main__':
    app.run()


# MVC = Model View Controller
# MVT = Model View Template


