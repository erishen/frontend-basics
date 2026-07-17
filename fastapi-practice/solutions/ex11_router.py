from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()


@router.get("/users/")
def list_users():
    return ["alice", "bob"]


@router.get("/users/{uid}")
def get_user(uid: int):
    return {"user_id": uid}


app.include_router(router)
