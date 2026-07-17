from fastapi import FastAPI, Depends

app = FastAPI()


def common_params(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
def read_items(params: dict = Depends(common_params)):
    return params
