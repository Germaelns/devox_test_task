from DAL.meta import Base
from sqlalchemy import Column, INTEGER, VARCHAR, PrimaryKeyConstraint, UniqueConstraint


class User(Base):
    __tablename__ = 'user'

    id = Column('id', INTEGER, autoincrement=True)
    name = Column('name', VARCHAR(30), nullable=True)
    surname = Column('surname', VARCHAR(30), nullable=True)
    phone = Column('phone', VARCHAR(13), nullable=False)
    login = Column('login', VARCHAR(50), nullable=False)
    password = Column('password', VARCHAR(50), nullable=False)

    PrimaryKeyConstraint(id, name='PK_User_Id')
    UniqueConstraint(phone, name='UQ_User_phone')