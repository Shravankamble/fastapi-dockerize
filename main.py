from fastapi import FastAPI, status
from pydantic import BaseModel

class User(BaseModel):
    name: str

app = FastAPI()

users = [] 

@app.get("/", status_code=status.HTTP_200_OK)
async def index():
    return "hello world!"

@app.get("/get/users", status_code=status.HTTP_200_OK)
async def post():
    return users

@app.post("/post/users", status_code=status.HTTP_201_CREATED)
async def create_user(name: User):
    user = name.dict()
    users.append(user)
    return f"new user : {name}"
