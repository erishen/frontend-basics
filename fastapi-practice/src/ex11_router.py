# 路由模块（APIRouter）
#
# 任务：用 APIRouter 定义用户相关路由，再挂载到 app：
#   GET  `/users/`        -> 返回 ["alice", "bob"]
#   GET  `/users/{uid}`   -> 返回 {"user_id": uid}
# 用 app.include_router(router) 挂载

from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

# TODO: 1) 在 router 上定义两个 GET 路由
#       2) app.include_router(router)

@router.get("/users/")
def list_users():
    return ["alice", "bob"]

@router.get("/users/{uid}")
def get_user(uid: int):
    return {"user_id": uid}

app.include_router(router)


if __name__ == "__main__":
    import uvicorn

    # 直接用 `python src/exNN_xxx.py` 启动开发服务器（需先 pip install uvicorn）
    # 接口根地址：http://127.0.0.1:8000/    交互文档：http://127.0.0.1:8000/docs
    uvicorn.run(app, host="127.0.0.1", port=8000)
