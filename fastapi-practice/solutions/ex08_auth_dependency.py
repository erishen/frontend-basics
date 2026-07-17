from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()


def get_api_key(x_api_key: str = Header(None)):
    if x_api_key != "secret":
        raise HTTPException(status_code=403, detail="Forbidden")
    return x_api_key


@app.get("/secure/")
def secure(key: str = Depends(get_api_key)):
    return {"status": "ok"}
