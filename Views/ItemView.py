from flask.views import MethodView
from flask import request
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError

from BLL.Sevices.ItemService import ItemService
from BLL.Sevices.ReadConfigSevice import ReadConfigService


class ItemView(MethodView):

    def __init__(self):
        self.engine = create_engine(ReadConfigService.get_postgres_uri())

    def get(self):
        user_id = request.args['user_id']
        session = sessionmaker(bind=self.engine)()
        items = ItemService(session).get_items_for_user(user_id)
        session.close()

        responce_data = dict()
        counter = 0

        for item in items:
            responce_data[counter] = {
                "id": item.id,
                "image": item.image,
                "title": item.title,
                "price": item.price,
                "user_id": item.user_id,
                "category_id": item.category_id
            }

            counter += 1

        return responce_data

    def post(self):
        try:
            data = request.json

            session = sessionmaker(bind=self.engine)()
            ItemService(session).create_item(data["image"], data["title"], data["price"],
                                             data["user_id"], data["category_id"])
            session.commit()
            session.close()

            return "Item created!"
        except IntegrityError:
            return "No such user!"

    def put(self):
        pass

    def delete(self):
        pass
