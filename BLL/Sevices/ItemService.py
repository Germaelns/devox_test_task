from DAL.Repositories.ItemRepository import ItemRepository


class ItemService:

    def __init__(self, db_session):

        self.session = db_session

    def create_item(self, image: str, title: str, price: float, user_id: int, category_id: int):
        return ItemRepository(self.session).create_item(image=image, title=title, price=price,
                                                        user_id=user_id, category_id=category_id)

    def get_items_for_user(self, user_id):
        return ItemRepository(self.session).get_items_for_user(user_id)