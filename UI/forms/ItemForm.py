from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField


class ItemForm(FlaskForm):

    image = StringField("image"),
    title = StringField("title"),
    price = FloatField("price"),
    user_id = IntegerField("user_id"),
    category_id = IntegerField("category_id"),
    order_id = IntegerField("order_id")