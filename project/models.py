from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)  # Первичный ключ
    name = Column(String, index=True)
    password = Column(String, index=True)
