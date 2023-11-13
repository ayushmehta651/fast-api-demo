from typing import Union, List
import requests
from fastapi import FastAPI
from pydantic import BaseModel
import json
from models import User, Item, Posts

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item.Item):
    return {"item_name": item.name, "item_id": item_id}

@app.get("/posts")
async def get_posts(response_model=List[Posts.Posts]):
    res = requests.get("https://jsonplaceholder.typicode.com/posts")
    if res.status_code == 200:
        return json.loads(res.content.decode('utf-8'))
    raise HTTPException(status_code=404, detail="Data not fetched")

@app.get("/users")
async def get_users(response_model=List[User.User]):
    res = requests.get("https://jsonplaceholder.typicode.com/users")
    if res.status_code == 200:
        users = json.loads(res.content.decode('utf-8'))
        print(users[0]["id"])
        return users
    raise HTTPException(status_code=404, detail="No user found")
        
