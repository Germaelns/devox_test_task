import requests

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from UI.forms.UserForm import UserForm
from UI.forms.CategoryForm import CategoryForm
from UI.forms.ItemForm import ItemForm
from UI.forms.OrderForm import OrderForm


app = Flask(__name__)
Bootstrap(app)


@app.route('/user', methods=['GET', 'POST'])
def user():
    form = UserForm(csrf_enabled=False)

    if form.validate_on_submit():

        data = {
            "name": form.name.data,
            "surname": form.surname.data,
            "phone": form.phone.data,
            "login": form.login.data,
            "password": form.password.data
        }

        headers = {
            'Content-Type': 'application/json'
        }

        return requests.post("localhost:5001/users", data=data, headers=headers)
    return render_template("user.html", form=form)


@app.route('/category', methods=['GET', 'POST'])
def category():

    form = CategoryForm(csrf_enabled=False)

    if form.validate_on_submit():

        data = {
            "title": form.title.data,
            "user_id": form.user_id.data
        }

        headers = {
            'Content-Type': 'application/json'
        }

        return requests.post("localhost:5001/categories", data=data, headers=headers)

    return render_template("category.html", form=form)


@app.route('/item', methods=['GET', 'POST'])
def item():

    form = ItemForm(csrf_enabled=False)

    if form.validate_on_submit():

        data = {
            "image": form.image.data,
            "title": form.title.data,
            "price": form.price.data,
            "user_id": form.user_id.data,
            "category_id": form.category_id.data,
            "order_id": form.order_id.data,
        }

        headers = {
            'Content-Type': 'application/json'
        }

        return requests.post("localhost:5001/items", data=data, headers=headers)

    return render_template("item.html", form=form)


@app.route('/order', methods=['GET', 'POST'])
def order():

    form = OrderForm(csrf_enabled=False)

    if form.validate_on_submit():

        data = {
            "price": form.price.data,
            "date": form.date.data,
            "description": form.description.data,
            "user_id": form.user_id.data,
            "item_id": form.item_id.data
        }

        headers = {
            'Content-Type': 'application/json'
        }

        return requests.post("localhost:5001/orders", data=data, headers=headers)

    return render_template("order.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
