from fastapi import FastAPI, HTTPException
from typing import Optional, List, Union, Dict
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def home() -> dict[str, str]:
    return {"data": "message"}


@app.get("/contacts")
async def contacts() -> int:
    return 32


class User(BaseModel):
    id: int
    name: str
    age: int


class Post(BaseModel):
    id: int
    title: str
    body: str
    auther: User

users = [
    {"id": 1, "name": "John", "age": 34},
    {"id": 1, "name": "Don", "age": 44},
    {"id": 1, "name": "Gan", "age": 54}
]
posts = [
    {"id": 1, "title": "News 1", "body": 'Text 1', "auther": users[1]},
    {"id": 2, "title": "News 2", "body": 'Text 2',"auther": users[0]},
    {"id": 3, "title": "News 3", "body": 'Text 3',"auther": users[2]}
]


@app.get("/items")
async def items() -> List[Post]:
    return [Post(**post) for post in posts]


@app.get("/items/{id}")
async def items(id: int) -> dict:
    for post in posts:
        if post['id'] == id:
            return post
    raise HTTPException(status_code=404, detail="post not found")


@app.get("/search")
async def search(post_id: Optional[int] = None) -> Dict[str, Optional[Post]]:
    if post_id:
        for post in posts:
            if post['id'] == post_id:
                return {"data": Post(**post)}
        raise HTTPException(status_code=404, detail="post not found")
    else:
        return {"data": None}
