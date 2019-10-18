from DAL.Entities.Item import Item


class ItemRepository:

    def __init__(self, db_session):

        self.session = db_session

    def create_item(self, image: str, title: str, price: float, user_id: int, category_id: int):
        return self.session.add(Item(image=image,
                                     title=title,
                                     price=price,
                                     user_id=user_id,
                                     category_id=category_id))

    def get_items_for_user(self, user_id):
        return self.session.query(Item).filter(Item.user_id == user_id).all()
