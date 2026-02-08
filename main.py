from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def greet():
    return "Welcome to this webpage"

users = [
    User(1, "Nikola", "Jokic", "Joker", "njokic"),
    User(2, "Jamal", "Murray", "Blue Arrow", "jmurray")
]

@app.get("/users")
def get_all_users():
    return users