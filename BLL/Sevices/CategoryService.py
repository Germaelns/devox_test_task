from DAL.Repositories.CategoryRepository import CategoryRepository


class CategorySevice:

    def __init__(self, db_session):
        self.session = db_session

    def add_category(self, title: str, user_id: int):
        return CategoryRepository(self.session).add_category(title=title, user_id=user_id)

    def get_all_categories_for_user(self, user_id):
        return CategoryRepository(self.session).get_all_categories_for_user(user_id)
