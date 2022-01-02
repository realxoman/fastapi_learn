from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Person(BaseModel):
    name: str


app = FastAPI()


@app.post("/")
def read_root(Person:Person):
    return Person


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
