from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


if __name__ == "__main__":

    import sys
    import json
    from sqlalchemy import create_engine
    from sqlalchemy import Column, INTEGER, VARCHAR, PrimaryKeyConstraint, UniqueConstraint, FLOAT, ForeignKey

    with open(sys.path[1] + "/config.json") as json_file:
        data = json.load(json_file)
    postgres_uri = data["postgres"]["uri"]

    engine = create_engine(postgres_uri)


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

    class Category(Base):
        __tablename__ = "category"

        id = Column('id', INTEGER, autoincrement=True)
        title = Column('title', VARCHAR(1000), nullable=False)
        user_id = Column('user_id', INTEGER, ForeignKey("user.id"), nullable=False)

        PrimaryKeyConstraint(id, name="PK_Category_Id")

    class Item(Base):
        __tablename__ = "item"

        id = Column('id', INTEGER, autoincrement=True)
        image = Column('image', VARCHAR(1000), nullable=True)
        title = Column('title', VARCHAR(1000), nullable=False)
        price = Column('price', FLOAT, nullable=False)
        user_id = Column('user_id', INTEGER, ForeignKey("user.id"), nullable=False)
        category_id = Column('category_id', INTEGER, ForeignKey("category.id"), nullable=False)

        PrimaryKeyConstraint(id, name="PK_Item_Id")

    Base.metadata.create_all(bind=engine)
