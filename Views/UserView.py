from flask.views import MethodView
from flask import request
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from BLL.Sevices.UserService import UserService
from BLL.Sevices.ReadConfigSevice import ReadConfigService
from BLL.Exceptions.WrongNumberException import WrongNumberException


class UserView(MethodView):

    def __init__(self):
        self.engine = create_engine(ReadConfigService.get_postgres_uri())

    def get(self):
        session = sessionmaker(bind=self.engine)()
        users = UserService(session).get_all_users()
        session.close()

        responce_data = dict()
        counter = 0

        for user in users:
            responce_data[counter] = {
                "id": user.id,
                "name": user.name,
                "surname": user.surname,
                "login": user.login,
                "password": user.password
            }

            counter += 1

        return responce_data

    def post(self):
        try:
            data = request.json

            if len(data["phone"]) != 13:
                raise WrongNumberException("Your number is too long")

            session = sessionmaker(bind=self.engine)()
            UserService(session).add_user(data["name"], data["surname"], data["phone"],
                                          data["login"], data["password"])
            session.commit()
            session.close()

            return "User was created!"
        except WrongNumberException:
            return "You have to write full number\nExample: +380637894596"

    def put(self):
        pass

    def delete(self):
        pass
