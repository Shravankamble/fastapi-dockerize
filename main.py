from fastapi import FastAPI, status

app = FastAPI()

users = []

@app.get("/")
async def index():
    return "hello world!"

@app.get("/get/users")
async def post():
    return users

@app.post("/post/users")
async def create_user(name: str):
    users.append(name)
    return f"new user added : {name}"
