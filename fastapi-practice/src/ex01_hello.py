# FastAPI 入门：第一个接口
#
# 任务：创建一个 GET 接口，路径为 `/`，返回 JSON：
#     {"message": "hello"}
#
# 提示：
#   - from fastapi import FastAPI
#   - 用 @app.get("/") 装饰一个函数
#   - 函数直接返回字典，FastAPI 会自动序列化为 JSON

from fastapi import FastAPI

app = FastAPI()

# TODO: 用 @app.get("/") 定义一个函数，返回 {"message": "hello"}

@app.get("/")
def read_root():
	return {"message": "hello"}


if __name__ == "__main__":
    import uvicorn

    # 直接用 `python src/exNN_xxx.py` 启动开发服务器（需先 pip install uvicorn）
    # 接口根地址：http://127.0.0.1:8000/    交互文档：http://127.0.0.1:8000/docs
    uvicorn.run(app, host="127.0.0.1", port=8000)
