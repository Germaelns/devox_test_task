from DAL.Entities.Order import Order
from DAL.Entities.ItemOrder import ItemOrder


class OrderRepository:

    def __init__(self, db_session):

        self.session = db_session

    def create_order(self, price: float, date: str, description: str, user_id: int, item_id: int):
        self.session.add(Order(price=price,
                               date=date,
                               description=description,
                               user_id=user_id,
                               item_id=item_id))

        order = self.session.query(Order).filter(Order.user_id == user_id and
                                                 Order.item_id == item_id and
                                                 Order.description == description).all()[0]

        self.session.add(ItemOrder(user_id=user_id,
                                   item_id=item_id,
                                   order_id=order.id))

        return 0

    def update_order_description(self, order_id: int, description: str):
        return self.session.query(Order).filter(Order.id == order_id).update(
            {
                "description": description
            }
        )

    def get_orders_for_user(self, user_id):
        return self.session.query(Order).filter(Order.user_id == user_id).all()
