from wtforms.fields import StringField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Write your username',validators=[DataRequired('Bad username')])
    password = PasswordField('Write your password', validators=[DataRequired('Bad password')])