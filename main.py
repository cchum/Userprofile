from fastapi import FastAPI 
from models import User
from database import session, engine
import database_models

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

def init_db():
    db = session()

    count = db.query(database_models.User).count

    if count == 0:

        for user in users:
            db.add(database_models.User(**user.model_dump()))
        db.commit()

init_db()

@app.get("/users")
def get_all_users():
    return users

@app.get("/user/{id}")
def get_user_by_id(id: int):
    for user in users:
        if user.id == id:
            return user
    return "User Not Found"

@app.post("/user")
def add_user(user: User):
    users.append(user)
    return user

@app.put("/user")
def update_user(id: int, user: User):
    for i in range(len(users)):
        if users[i].id == id:
            users[i] = user
            return "User Updated Successfully"

    return "User Not Found"

@app.delete("/user")
def delete_user(id: int):
    for i in range(len(users)):
        if users[i].id == id:
            del users[i]
            return "User Deleted Successfully"
    return "User Not Found"