from flask import render_template



def hello_world():
    user = {"username": "john", "password":"shouldn't save as text"}
    context = {"user": user, "word2": "something2"}
    return render_template(template_name_or_list="index.html", **context)
