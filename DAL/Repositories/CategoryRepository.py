from DAL.Entities.Category import Category


class CategoryRepository:

    def __init__(self, db_session):
        self.session = db_session

    def add_category(self, title: str, user_id: int):
        return self.session.add(Category(title=title,
                                         user_id=user_id))

    def get_all_categories_for_user(self, user_id):
        return self.session.query(Category).filter(Category.user_id == user_id).all()
