from flask import Flask
from Views.UserView import UserView
from Views.CategoryView import CategoryView
from Views.ItemView import ItemView


app = Flask(__name__)


app.add_url_rule('/app/users', view_func=UserView.as_view('user'))
app.add_url_rule('/app/categories', view_func=CategoryView.as_view('category'))
app.add_url_rule('/app/items', view_func=ItemView.as_view('item'))

app.run()
