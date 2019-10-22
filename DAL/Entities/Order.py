from sqlalchemy import Column, INTEGER, VARCHAR, PrimaryKeyConstraint, ForeignKey, FLOAT, DATE
from DAL.meta import Base


class Order(Base):
    __tablename__ = "order"

    id = Column('id', INTEGER, autoincrement=True)
    price = Column('price', FLOAT, nullable=False)
    date = Column('price', DATE, nullable=False)
    description = Column('description', VARCHAR(300), nullable=False)
    user_id = Column('user_id', INTEGER, ForeignKey("user.id"), nullable=False)
    item_id = Column('item_id', INTEGER, ForeignKey("itemorder.item_id"), nullable=False)

    PrimaryKeyConstraint(id, name="PK_Order_Id")
