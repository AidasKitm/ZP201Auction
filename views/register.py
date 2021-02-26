from models.user import User
from werkzeug.security import generate_password_hash
from flask.views import MethodView
from flask import session, redirect, url_for, render_template

class Registration(MethodView):
    def get(self):
        if session.get('username'):
            return redirect(url_for('index'))

        registration_form = ""
        return render_template('registration.html', registration_form=registration_form)



