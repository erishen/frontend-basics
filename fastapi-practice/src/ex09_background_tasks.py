# 后台任务（BackgroundTasks）
#
# 任务：维护一个模块级列表 notifications = []
#   POST `/send-notification/?email=...` 接收一个 email 查询参数
#   使用 BackgroundTasks 在后台把 email 追加到 notifications
#   返回 {"msg": "Notification sent"}
#
# 提示：后台函数签名 def send(email: str): notifications.append(email)

from fastapi import FastAPI, BackgroundTasks

app = FastAPI()
notifications = []

# TODO: 实现 POST /send-notification/，用 BackgroundTasks 追加 email

def send_email(email: str):
    notifications.append(email)

@app.post("/send-notifications/")
def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email)
    return {"msg": "Notification sent"}


if __name__ == "__main__":
    import uvicorn

    # 直接用 `python src/exNN_xxx.py` 启动开发服务器（需先 pip install uvicorn）
    # 接口根地址：http://127.0.0.1:8000/    交互文档：http://127.0.0.1:8000/docs
    uvicorn.run(app, host="127.0.0.1", port=8000)
