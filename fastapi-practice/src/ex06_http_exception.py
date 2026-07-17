# 错误处理：HTTPException
#
# 任务：维护一个内存字典 items = {1: "foo", 2: "bar"}
#   GET `/items/{item_id}`：存在则返回字符串；不存在 raise HTTPException(404)

from fastapi import FastAPI, HTTPException

app = FastAPI()
items = {1: "foo", 2: "bar"}

# TODO: 实现 GET /items/{item_id}，缺失时抛 404

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


if __name__ == "__main__":
    import uvicorn

    # 直接用 `python src/exNN_xxx.py` 启动开发服务器（需先 pip install uvicorn）
    # 接口根地址：http://127.0.0.1:8000/    交互文档：http://127.0.0.1:8000/docs
    uvicorn.run(app, host="127.0.0.1", port=8000)
