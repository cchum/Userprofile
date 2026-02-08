from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):

    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    first_name: Column(String, nullable=False)
    last_name : Column(String, nullable=False)
    username: Column(String, unique=True)
    email: Column(String, unique=True)
    password: Column(String)