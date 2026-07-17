from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    tax: float | None = None


@app.post("/items/")
def create_item(item: Item):
    return {"id": 1, "name": item.name, "price": item.price, "tax": item.tax}
