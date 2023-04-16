from fastapi import FastAPI
from pydantic import BaseModel

# Start server: python -m uvicorn users:app --reload

app = FastAPI()

# Entity User


class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int


users = [User("Jorman", "Espinoza", "https://jormanespinoza.com", 33)]


@app.get("/users")
async def users():
    return users


@app.get("/usersjson")
async def usersjson():
    return [{"name": "Jorman", "surname": "Espinoza", "url": "https://jormanespinoza.com", "age": 33},
            {"name": "Fabio", "surname": "Espinoza", "url": "https://fabioespinoza.com", "age": 24}]
