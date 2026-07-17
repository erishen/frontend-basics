from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
def read_items(skip: int = 0, limit: int = Query(default=10, gt=0, le=100)):
    return {"skip": skip, "limit": limit}
