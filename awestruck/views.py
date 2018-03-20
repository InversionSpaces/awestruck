from flask import render_template
from flask_login import login_user

from awestruck import app
from awestruck.forms import LogForm, RegForm
from awestruck.models import User


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LogForm()
    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data).first()
        if user and user.check_pass(form.password.data):
            login_user(user)
    return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegForm()
    if form.validate_on_submit():
        user = User(form.login.data)
        user.save(form.password.data)
    return render_template("register.html", form=form)


@app.route("/", methods=["GET"])
def main():
    return render_template("main.html")
