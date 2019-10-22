from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, DateField


class OrderForm(FlaskForm):

    price = FloatField("price"),
    date = DateField("date"),
    description = StringField("description"),
    user_id = IntegerField("user_id"),
    item_id = IntegerField("item_id")
