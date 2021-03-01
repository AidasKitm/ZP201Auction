from flask import redirect, url_for, session
from flask.views import MethodView


class LogOut(MethodView):
    def get(self):
        session.pop('username',default=None)
        return redirect(url_for('index'))