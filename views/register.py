from models.user import User
from werkzeug.security import generate_password_hash
from flask.views import MethodView
from flask import session, redirect, url_for, render_template
from forms.registration_form import RegistrationForm
from models import db

class Registration(MethodView):

    def get(self):
        if session.get('username'):
            return redirect(url_for('index'))

        registration_form = RegistrationForm()
        return render_template('registration.html', registration_form=registration_form, session=session.get('username'))

    def post(self):
        registration_form = RegistrationForm()
        if registration_form.validate_on_submit():
            user = User(first_name=registration_form.first_name.data,
                        last_name=registration_form.last_name.data,
                        username=registration_form.username.data,
                        email=registration_form.email.data,
                        address=registration_form.address.data,
                        password=generate_password_hash(registration_form.password.data))
            db.session.add(user)
            db.session.commit()
        return redirect(url_for('index'))




