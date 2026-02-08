from fastapi import FastAPI 
from models import User

app = FastAPI()

@app.get("/")
def greet():
    return "Welcome to this webpage"

users = [
    User(id=1, first_name="Nikola", last_name="Jokic", username="Joker", email="joker@gmail.com",password="njokic"),
    User(id=2, first_name="Jamal", last_name="Murray", username="Blue Arrow", email="bluearrow@gmail.com",password="jmurray")
]

@app.get("/users")
def get_all_users():
    return users

@app.get("/user/{id}")
def get_user_by_id(id: int):
    for user in users:
        if user.id == id:
            return user
    return "User Not Found"