from DAL.Repositories.OrderRepository import OrderRepository


class OrderService:

    def __init__(self, db_session):
        self.session = db_session

    def create_order(self, price: float, date: str, description: str, user_id: int, item_id: int):
        return OrderRepository(self.session).create_order(price=price,
                                                          date=date,
                                                          description=description,
                                                          user_id=user_id,
                                                          item_id=item_id)

    def update_order_description(self, order_id: int, description: str):
        return OrderRepository(self.session).update_order_description(order_id=order_id,
                                                                      description=description)

    def get_orders_for_user(self, user_id):
        return OrderRepository(self.session).get_orders_for_user(user_id)
