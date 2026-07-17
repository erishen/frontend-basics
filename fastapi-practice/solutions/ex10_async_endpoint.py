import asyncio
from fastapi import FastAPI

app = FastAPI()


@app.get("/async-items/{item_id}")
async def read_async(item_id: int):
    await asyncio.sleep(0)
    return {"doubled": item_id * 2}
