from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField


class CategoryForm(FlaskForm):

    title = StringField("title"),
    user_id = IntegerField("user_id")
