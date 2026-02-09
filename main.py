from fastapi import Depends, FastAPI 
from models import User
from database import session, engine
import database_models
from sqlalchemy.orm import Session

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Welcome to this webpage"

users = [
    User(id=1, first_name="Nikola", last_name="Jokic", username="Joker", email="joker@gmail.com",password="njokic"),
    User(id=2, first_name="Jamal", last_name="Murray", username="Blue Arrow", email="bluearrow@gmail.com",password="jmurray"),
    User(id=3, first_name="Aaron", last_name="Gordon", username="Mr. Nugget", email="ag@gmail.com",password="agordon")
    
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()

    count = db.query(database_models.User).count

    if count == 0:

        for user in users:
            db.add(database_models.User(**user.model_dump()))
        db.commit()

init_db()

@app.get("/users")
def get_all_users(db: Session = Depends(get_db)):

    db_users = db.query(database_models.User).all()
    return db_users

@app.get("/user/{id}")
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    db_user = db.query(database_models.User).filter(database_models.User.id == id).first()
    if db_user:
        return db_user
    return "User Not Found"

@app.post("/user")
def add_user(user: User, db: Session = Depends(get_db)):
    db.add(database_models.User(**user.model_dump()))
    db.commit()
    return user

@app.put("/user")
def update_user(id: int, user: User, db: Session = Depends(get_db)):
    db_user = db.query(database_models.User).filter(database_models.User.id == id).first()
    if db_user:
        db_user.first_name = user.first_name
        db_user.last_name = user.last_name
        db_user.username = user.username
        db_user.email = user.email
        db_user.password = user.password
        db.commit()
        return "User Updated"
    else:
        return "User Not Found"

@app.delete("/user")
def delete_user(id: int, db: Session = Depends(get_db)):
    db_user = db.query(database_models.User).filter(database_models.User.id == id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return "User Deleted Successfully"
    else:
     return "User Not Found"