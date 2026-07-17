# FastAPI 面试高频考点（精简版）

> 面向已经会 Python、正在准备后端 / AI 工程岗的同学。覆盖 FastAPI 最常被问、最常手写的知识点，配合同目录 `fastapi-practice/` 练习区食用更佳。

---

## 1. 第一个应用与启动（必会）

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    # 直接返回字典 / 列表，FastAPI 自动序列化为 JSON
    return {"message": "hello"}


# 启动：uvicorn main:app --reload
#   main   = 文件名（main.py）
#   app    = 暴露的 FastAPI 实例名
# 交互式文档：访问 /docs（Swagger）和 /redoc（ReDoc）
```

---

## 2. 路径参数与查询参数（必考）

```python
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    # item_id 是路径参数（必填），类型声明后 FastAPI 自动做类型校验
    # q 是查询参数（可选），来自 URL 的 ?q=xxx
    return {"item_id": item_id, "q": q}


# 路径 /items/42?q=abc  ->  {"item_id": 42, "q": "abc"}
# 类型不匹配（如 /items/abc）会返回 422
```

---

## 3. 请求体（Pydantic 模型）

```python
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    tax: float | None = None  # 可选字段，默认 None


@app.post("/items/")
def create_item(item: Item):
    # item 由请求体 JSON 自动解析并校验，无需手动 json.loads
    return {"id": 1, "name": item.name, "price": item.price}
```

---

## 4. 查询参数校验（必考）

```python
from fastapi import Query


@app.get("/items/")
def read_items(
    skip: int = 0,
    limit: int = Query(default=10, gt=0, le=100),  # 10 < limit <= 100
):
    # 校验失败（如 limit=200）自动返回 422，无需手写 if
    return {"skip": skip, "limit": limit}
```

---

## 5. 依赖注入（Depends，高频）

```python
from fastapi import Depends


def common_params(q: str | None = None, skip: int = 0, limit: int = 100):
    # 依赖函数：可复用、可组合、可单独测试
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
def read_items(params: dict = Depends(common_params)):
    # FastAPI 先调用 common_params，把结果注入 params
    return params
```

---

## 6. 错误处理（HTTPException）

```python
from fastapi import HTTPException

items = {1: "foo", 2: "bar"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        # 主动抛出，FastAPI 转成对应状态码的 JSON
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]
```

---

## 7. 中间件（Middleware）

```python
from fastapi import Request


@app.middleware("http")
async def add_header(request: Request, call_next):
    # call_next 触发后续处理（路由 / 依赖 / 响应）
    response = await call_next(request)
    response.headers["X-App-Name"] = "fastapi-practice"
    return response
```

---

## 8. 依赖鉴权（Header + Depends）

```python
from fastapi import Header


def get_api_key(x_api_key: str = Header(None)):
    if x_api_key != "secret":
        raise HTTPException(status_code=403, detail="Forbidden")
    return x_api_key


@app.get("/secure/")
def secure(key: str = Depends(get_api_key)):
    # 缺失或错误密钥 -> 403；正确 -> 进入处理函数
    return {"status": "ok"}
```

---

## 9. 后台任务（BackgroundTasks）

```python
from fastapi import BackgroundTasks

notifications = []


def send_email(email: str):
    notifications.append(email)  # 模拟发信


@app.post("/send-notification/")
def send_notification(email: str, background_tasks: BackgroundTasks):
    # 请求返回后，在后台执行，不阻塞响应
    background_tasks.add_task(send_email, email)
    return {"msg": "Notification sent"}
```

---

## 10. 异步接口（async / await）

```python
import asyncio


@app.get("/async-items/{item_id}")
async def read_async(item_id: int):
    # 碰到 IO 等待时用 await，让事件循环去处理别的请求
    await asyncio.sleep(0)  # 真实场景：查库 / 调第三方
    return {"doubled": item_id * 2}
```

---

## 11. 路由模块化（APIRouter）

```python
from fastapi import APIRouter

router = APIRouter()


@router.get("/users/")
def list_users():
    return ["alice", "bob"]


@router.get("/users/{uid}")
def get_user(uid: int):
    return {"user_id": uid}


# 把子路由挂到主 app，大型项目按模块拆分路由文件
app.include_router(router)
```

---

## 12. 跨域（CORSMiddleware，高频）

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # 允许的源
    allow_credentials=False,   # 见下方注意
    allow_methods=["*"],       # 允许的 HTTP 方法
    allow_headers=["*"],       # 允许的请求头
)
```

> **注意**：当 `allow_origins=["*"]` 且 `allow_credentials=True` 时，Starlette 会**回显请求来源**而非返回字面量 `*`（因为带凭证的 `*` 在浏览器中无效）。想要响应头直接是 `*` 就设 `allow_credentials=False`；需要携带 Cookie 时，应把 `allow_origins` 写成具体的源列表。

---

## 13. 测试（TestClient）

```python
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"message": "hello"}
```

> `TestClient` 基于 `httpx` + Starlette，会真实跑完整个请求生命周期（含依赖、中间件、后台任务），是验证接口的最快方式。

---

## 14. 一句话速记

- **返回即 JSON**：视图函数返回 dict / list，FastAPI 自动序列化。
- **类型即校验**：路径 / 查询 / 请求体都靠类型注解自动校验，错了返回 422。
- **Pydantic 管数据**：请求体、响应模型统一用 `BaseModel`。
- **Depends 管复用**：公共参数、鉴权、DB 连接都做成依赖，可单独测。
- **HTTPException 管错误**：主动抛，自动转状态码。
- **中间件管横切**：日志、响应头、CORS 用中间件 / 内置中间件。
- **async 管并发**：IO 密集处用 `await`，别写阻塞调用。
- **APIRouter 管拆分**：大项目按模块挂路由。
- **/docs 管调试**：自带 Swagger，写完就能点。
