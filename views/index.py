from flask import render_template, session
from flask.views import MethodView


class Index(MethodView):
    def get(self):
        user = session.get('username')
        return render_template('index.html', user=user)