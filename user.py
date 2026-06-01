from sqlalchemy import Column, Integer, String, Boolean
from database import Base

# Creates User table in Database

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    is_admin = Column(Boolean, default=False)