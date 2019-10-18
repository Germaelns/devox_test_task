from sqlalchemy import Column, INTEGER, VARCHAR, PrimaryKeyConstraint, ForeignKey
from DAL.meta import Base


class Category(Base):
    __tablename__ = "category"

    id = Column('id', INTEGER, autoincrement=True)
    title = Column('title', VARCHAR(1000), nullable=False)
    user_id = Column('user_id', INTEGER, ForeignKey("user.id"), nullable=False)

    PrimaryKeyConstraint(id, name="PK_Category_Id")
