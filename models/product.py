from sqlalchemy import Column, Integer, String, Float

from database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String(255),
        nullable=False
    )

    description = Column(
        String(1000)
    )

    price = Column(
        Float,
        nullable=False
    )

    inventory = Column(
        Integer,
        nullable=False,
        default=0
    )