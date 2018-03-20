from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class RegForm(FlaskForm):
    login = StringField("login")
    password = StringField("password")
    submit = SubmitField("submit")

class LogForm(FlaskForm):
    login = StringField("login")
    password = StringField("password")
    submit = SubmitField("submit")
