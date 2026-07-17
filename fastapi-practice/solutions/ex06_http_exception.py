from fastapi import FastAPI, HTTPException

app = FastAPI()
items = {1: "foo", 2: "bar"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]
