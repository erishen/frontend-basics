from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 注意：allow_origins=["*"] 且 allow_credentials=False 时，
# 响应头才会是字面量 "*"；若 allow_credentials=True，Starlette 会回显请求来源。
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
