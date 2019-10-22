from sqlalchemy import Column, INTEGER, ForeignKey
from DAL.meta import Base


class ItemOrder(Base):
    __tablename__ = "itemorder"

    user_id = Column('user_id', INTEGER, ForeignKey('user_id'), nullable=False)
    item_id = Column('item_id', INTEGER, ForeignKey('item.id'), nullable=False)
    order_id = Column('order_id', INTEGER, ForeignKey('order.id'), nullable=False)
