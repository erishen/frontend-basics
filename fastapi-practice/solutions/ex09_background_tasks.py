from fastapi import FastAPI, BackgroundTasks

app = FastAPI()
notifications = []


def send_email(email: str):
    notifications.append(email)


@app.post("/send-notification/")
def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email)
    return {"msg": "Notification sent"}
