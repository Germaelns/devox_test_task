from DAL.Entities.User import User


class UserRepository:

    def __init__(self, db_session):
        self.session = db_session

    def add_user(self, name: str, surname: str, phone: str, login: str, password: str):
        return self.session.add(User(name=name, surname=surname, phone=phone,
                                     login=login, password=password))

    def get_all_users(self):
        return self.session.query(User).all()
