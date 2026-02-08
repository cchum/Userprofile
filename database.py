from  sqlalchemy.orm import sessionmaker
from sqlalchemy import  create_engine

db_url = "postgresql://postgres:tayden10@localhost:5433/user_profile"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)