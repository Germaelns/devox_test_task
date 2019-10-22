from sqlalchemy import Column, INTEGER, VARCHAR, PrimaryKeyConstraint, ForeignKey, FLOAT
from DAL.meta import Base


class Item(Base):
    __tablename__ = "item"

    id = Column('id', INTEGER, autoincrement=True)
    image = Column('image', VARCHAR(1000), nullable=True)
    title = Column('title', VARCHAR(1000), nullable=False)
    price = Column('price', FLOAT, nullable=False)
    user_id = Column('user_id', INTEGER, ForeignKey("user.id"), nullable=False)
    category_id = Column('category_id', INTEGER, ForeignKey("category.id"), nullable=False)
    order_id = Column('order_id', INTEGER, ForeignKey("itemorder.order_id"), nullable=False)

    PrimaryKeyConstraint(id, name="PK_Item_Id")