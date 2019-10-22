from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField


class UserForm(FlaskForm):

    name = StringField("name")
    surname = StringField("surname")
    phone = StringField("phone")
    login = StringField("login")
    password = PasswordField("password")
