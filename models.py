from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: int
    first_name: str
    last_name :str
    username: str
    email: EmailStr
    password: str