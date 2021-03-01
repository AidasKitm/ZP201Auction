from wtforms import StringField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField

class RegistrationForm(FlaskForm):
    first_name = StringField("Please input your first name", validators=[DataRequired("Don't leave empty field")])
    last_name = StringField("Please input your last name", validators=[DataRequired("Don't leave empty field")])
    email = EmailField("Please input your email", validators=[DataRequired(), Email()])
    address = StringField("Please input your address", validators=[DataRequired("Don't leave empty field")])
    username = StringField("Please input your username", validators=[DataRequired("Don't leave empty field")])
    password = PasswordField("Input password", validators=[DataRequired("Bad password")])