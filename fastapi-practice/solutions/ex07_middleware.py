from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.middleware("http")
async def add_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-App-Name"] = "fastapi-practice"
    return response


@app.get("/")
def root():
    return {"ok": True}
