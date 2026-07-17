# 请求体（Pydantic 模型）
#
# 任务：POST `/items/`
#   - 请求体用 Pydantic 模型 Item(name: str, price: float, tax: float | None = None)
#   - 返回 {"id": 1, "name": item.name, "price": item.price, "tax": item.tax}

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    tax: float | None = None


# TODO: 实现 POST /items/，接收 Item 并返回带 id 的字典

@app.post("/items/")
def create_item(item: Item):
    return {"id": 1, "name": item.name, "price": item.price, "tax": item.tax}


if __name__ == "__main__":
    import uvicorn

    # 直接用 `python src/exNN_xxx.py` 启动开发服务器（需先 pip install uvicorn）
    # 接口根地址：http://127.0.0.1:8000/    交互文档：http://127.0.0.1:8000/docs
    uvicorn.run(app, host="127.0.0.1", port=8000)
