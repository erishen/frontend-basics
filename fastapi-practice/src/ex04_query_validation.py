# 查询参数校验
#
# 任务：GET `/items/`
#   - skip: int = 0
#   - limit: int = Query(default=10, gt=0, le=100)
# 返回：{"skip": skip, "limit": limit}
# 非法 limit（<=0 或 >100）应自动返回 422

from fastapi import FastAPI, Query

app = FastAPI()

# TODO: 实现 GET /items/，对 limit 做 gt=0, le=100 校验
@app.get("/items/")
def read_items(
    skip: int = 0,
    limit: int = Query(default=10, gt=0, le=100),
):
    return {"skip": skip, "limit": limit}


if __name__ == "__main__":
    import uvicorn

    # 直接用 `python src/exNN_xxx.py` 启动开发服务器（需先 pip install uvicorn）
    # 接口根地址：http://127.0.0.1:8000/    交互文档：http://127.0.0.1:8000/docs
    uvicorn.run(app, host="127.0.0.1", port=8000)
