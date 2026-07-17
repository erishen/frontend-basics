# 异步接口（async/await）
#
# 任务：实现 async GET `/async-items/{item_id}`
#   在内部 await asyncio.sleep(0)（占位异步操作）
#   返回 {"doubled": item_id * 2}

import asyncio
from fastapi import FastAPI

app = FastAPI()

# TODO: 实现 async def 接口，await 后返回翻倍值

@app.get("/async-items/{item_id}")
async def read_async(item_id: int):
    await asyncio.sleep(0)
    return {"doubled": item_id * 2}


if __name__ == "__main__":
    import uvicorn

    # 直接用 `python src/exNN_xxx.py` 启动开发服务器（需先 pip install uvicorn）
    # 接口根地址：http://127.0.0.1:8000/    交互文档：http://127.0.0.1:8000/docs
    uvicorn.run(app, host="127.0.0.1", port=8000)
