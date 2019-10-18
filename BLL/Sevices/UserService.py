from DAL.Repositories.UserRepository import UserRepository


class UserService:

    def __init__(self, db_session):
        self.session = db_session

    def add_user(self, name: str, surname: str, phone: str, login: str, password: str):
        return UserRepository(self.session).add_user(name=name, surname=surname, phone=phone,
                                                     login=login, password=password)

    def get_all_users(self):
        return UserRepository(self.session).get_all_users()
