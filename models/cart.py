from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

from sqlalchemy.orm import Mapped, mapped_column

class CartItem(Base):
    __tablename__ = "cart_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    product_id: Mapped[int]
    quantity: Mapped[int] = mapped_column(default=1)