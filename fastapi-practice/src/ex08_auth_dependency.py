# 依赖注入做鉴权
#
# 任务：定义依赖 get_api_key，从请求头读取 X-API-Key：
#   - 若等于 "secret"，返回该 key
#   - 否则 raise HTTPException(status_code=403, detail="Forbidden")
# GET `/secure/` 使用 Depends(get_api_key)，返回 {"status": "ok"}

from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

# TODO: 1) 定义 get_api_key 依赖
#       2) 实现 GET /secure/ 使用 Depends

def get_api_key(x_api_key: str = Header(None)):
    if x_api_key != "secret":
        raise HTTPException(status_code=403, detail="Forbidden")
    return x_api_key

@app.get("/secure/")
def secure(key: str = Depends(get_api_key)):
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    # 直接用 `python src/exNN_xxx.py` 启动开发服务器（需先 pip install uvicorn）
    # 接口根地址：http://127.0.0.1:8000/    交互文档：http://127.0.0.1:8000/docs
    uvicorn.run(app, host="127.0.0.1", port=8000)
