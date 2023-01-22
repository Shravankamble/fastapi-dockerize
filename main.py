from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return "hello world!"

@app.get("/{name}")
async def customize(name: str):
    return f"hello {name}"