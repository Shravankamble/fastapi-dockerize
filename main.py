from fastapi import FastAPI, status
from pydantic import BaseModel
import logging

class User(BaseModel):
    name: str

logging.basicConfig(filename='apps.log', level='INFO')

app = FastAPI()

users: list = [] 

@app.get("/{name}", status_code=status.HTTP_200_OK)
async def index(name: str):
    logging.info(f"message : hello {name}")
    return f"hello {name}!"

@app.get("/get/users", status_code=status.HTTP_200_OK)
async def post():
    return users

@app.post("/post/users", status_code=status.HTTP_201_CREATED)
async def create_user(name: User):
    user = name.dict()
    users.append(user)
    return f"new user : {name}"
