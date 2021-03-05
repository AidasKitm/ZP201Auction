from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, TimeField, TextAreaField, SelectField, DateField
from wtforms.validators import DataRequired, InputRequired
from flask_wtf.file import FileRequired, FileField
from .categories import categories

class AuctionForm(FlaskForm):
    title = StringField('Auction title', validators=[DataRequired()])
    category = SelectField("Choose category", choices=categories)
    city = StringField('City', validators=[DataRequired()])
    minimal_price = IntegerField('Minimal required price')
    auction_image = FileField('Auction Image') # FileField doesn't work properly
    end_day = DateField('End day', validators=[InputRequired('Input needed')])
    end_hour = TimeField('End hour', validators=[InputRequired('Input needed')])

    description = TextAreaField('Description', validators=[DataRequired()])