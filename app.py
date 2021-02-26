from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    user = {"username": "john", "password":"shouldn't save as text"}
    context = {"user": user, "word2": "something2"}
    return render_template(template_name_or_list="index.html", **context)


if __name__ == '__main__':
    app.run()


# MVC = Model View Controller
# MVT = Model View Template
