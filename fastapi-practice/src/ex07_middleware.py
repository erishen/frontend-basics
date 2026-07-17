# 中间件（Middleware）
#
# 任务：添加一个中间件，为每个响应加上自定义响应头：
#   X-App-Name: fastapi-practice
# 并提供一个 GET `/` 返回 {"ok": True} 用于测试

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# TODO: 用 @app.middleware("http") 添加中间件，设置响应头

@app.middleware("http")
async def add_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-App-Name"] = "fastapi-practice"
    return response


@app.get("/")
def root():
    return {"ok": True}


if __name__ == "__main__":
    import uvicorn

    # 直接用 `python src/exNN_xxx.py` 启动开发服务器（需先 pip install uvicorn）
    # 接口根地址：http://127.0.0.1:8000/    交互文档：http://127.0.0.1:8000/docs
    uvicorn.run(app, host="127.0.0.1", port=8000)
