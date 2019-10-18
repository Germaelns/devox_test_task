from flask.views import MethodView
from flask import request
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError

from BLL.Sevices.CategoryService import CategorySevice
from BLL.Sevices.ReadConfigSevice import ReadConfigService


class CategoryView(MethodView):

    def __init__(self):
        self.engine = create_engine(ReadConfigService.get_postgres_uri())

    def get(self):
        user_id = request.args['user_id']
        session = sessionmaker(bind=self.engine)()
        categories = CategorySevice(session).get_all_categories_for_user(user_id)
        session.close()

        responce_data = dict()
        counter = 0

        for category in categories:
            responce_data[counter] = {
                "id": category.id,
                "title": category.title,
                "user_id": category.user_id
            }

            counter += 1

        return responce_data

    def post(self):
        try:
            data = request.json

            session = sessionmaker(bind=self.engine)()
            CategorySevice(session).add_category(data["title"], data["user_id"])
            session.commit()
            session.close()

            return "Category created!"
        except IntegrityError:
            return "No such user!"

    def put(self):
        pass

    def delete(self):
        pass
