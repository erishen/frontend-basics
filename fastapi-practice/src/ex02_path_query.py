# 路径参数与查询参数
#
# 任务：GET `/items/{item_id}`
#   - 路径参数 item_id: int
#   - 可选查询参数 q: str | None = None
# 返回：{"item_id": item_id, "q": q}

from fastapi import FastAPI

app = FastAPI()

# TODO: 实现 GET /items/{item_id}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    import uvicorn

    # 直接用 `python src/exNN_xxx.py` 启动开发服务器（需先 pip install uvicorn）
    # 接口根地址：http://127.0.0.1:8000/    交互文档：http://127.0.0.1:8000/docs
    uvicorn.run(app, host="127.0.0.1", port=8000)
