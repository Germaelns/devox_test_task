from flask.views import MethodView
from flask import request
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError

from BLL.Sevices.OrderService import OrderService
from BLL.Sevices.ReadConfigSevice import ReadConfigService


class OrderView(MethodView):

    def __init__(self):
        self.engine = create_engine(ReadConfigService.get_postgres_uri())

    def get(self):
        user_id = request.args['user_id']
        session = sessionmaker(bind=self.engine)()
        items = OrderService(session).get_orders_for_user(user_id)
        session.close()

        responce_data = dict()
        counter = 0

        for item in items:
            responce_data[counter] = {
                "id": item.id,
                "price": item.price,
                "date": item.date,
                "description": item.description,
                "user_id": item.user_id,
                "item_id": item.item_id
            }

            counter += 1

        return responce_data

    def post(self):
        try:
            data = request.json

            session = sessionmaker(bind=self.engine)()
            OrderService(session).create_order(data["price"],
                                               data["date"],
                                               data["description"],
                                               data["user_id"],
                                               data["item_id"])
            session.commit()
            session.close()

            return {
                "message": "Order created!"
            }
        except IntegrityError:
            return {
                "message": "No such user or item!"
            }

    def put(self):
        try:
            data = request.json

            session = sessionmaker(bind=self.engine)()
            OrderService(session).update_order_description(data["order_id"],
                                                           data["description"])

            session.commit()
            session.close()

        except IndentationError:
            return {
                "message": "No such order"
            }
        except KeyError:
            return {
                "message": "Wrong input data"
            }

    def delete(self):
        pass
