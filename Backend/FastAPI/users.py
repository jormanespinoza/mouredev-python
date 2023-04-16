from fastapi import FastAPI
from pydantic import BaseModel

# Start server: python -m uvicorn users:app --reload

app = FastAPI()


# Entity User
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [
    User(
        id=1,
        name="Jorman",
        surname="Espinoza",
        url="https://jormanespinoza.com",
        age=33,
    ),
    User(
        id=2,
        name="Fabio",
        surname="Espinoza",
        url="https://fabioespinoza.com",
        age=24,
    ),
]


@app.get("/usersjson")
async def usersjson():
    return [
        {
            "id": 1,
            "name": "Jorman",
            "surname": "Espinoza",
            "url": "https://jormanespinoza.com",
            "age": 33,
        },
        {
            "id": 2,
            "name": "Fabio",
            "surname": "Espinoza",
            "url": "https://fabioespinoza.com",
            "age": 24,
        },
    ]


@app.get("/users")
async def users():
    return users_list


# Path
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)


# Query
@app.get("/user")
async def user(id: int):
    return search_user(id)


def search_user(id: int):
    try:
        user = list(filter(lambda user: user.id == id, users_list))[0]
        return user
    except:
        return {"error": "No se ha encontrado el usuario"}
