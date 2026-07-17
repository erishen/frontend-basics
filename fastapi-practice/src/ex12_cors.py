# 跨域配置（CORSMiddleware）
#
# 任务：添加 CORSMiddleware，允许所有来源（"*"）：
#   allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
# 并提供 GET `/` 返回 {"ok": True}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# TODO: 用 app.add_middleware(CORSMiddleware, ...) 配置跨域

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"ok": True}


if __name__ == "__main__":
    import uvicorn

    # 直接用 `python src/exNN_xxx.py` 启动开发服务器（需先 pip install uvicorn）
    # 接口根地址：http://127.0.0.1:8000/    交互文档：http://127.0.0.1:8000/docs
    uvicorn.run(app, host="127.0.0.1", port=8000)
