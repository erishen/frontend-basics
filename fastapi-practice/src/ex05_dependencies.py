# 依赖注入（Dependencies）
#
# 任务：定义一个依赖函数 common_params，返回分页参数：
#   q: str | None = None, skip: int = 0, limit: int = 100
# GET `/items/` 使用 Depends(common_params)，返回这些参数：
#   {"q": q, "skip": skip, "limit": limit}

from fastapi import FastAPI, Depends

app = FastAPI()

# TODO: 1) 定义 common_params 依赖函数
#       2) 实现 GET /items/ 使用 Depends

def common_params(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
def read_items(params: dict = Depends(common_params)):
    return params


if __name__ == "__main__":
    import uvicorn

    # 直接用 `python src/exNN_xxx.py` 启动开发服务器（需先 pip install uvicorn）
    # 接口根地址：http://127.0.0.1:8000/    交互文档：http://127.0.0.1:8000/docs
    uvicorn.run(app, host="127.0.0.1", port=8000)
