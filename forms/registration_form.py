from wtforms import StringField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField

class RegistrationForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired("Don't leave empty field")])
    last_name = StringField("Last name", validators=[DataRequired("Don't leave empty field")])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    address = StringField("Address", validators=[DataRequired("Don't leave empty field")])
    username = StringField("Username", validators=[DataRequired("Don't leave empty field")])
    password = PasswordField("Password", validators=[DataRequired("Bad password")])

