# FastAPI 练习环境（fastapi-practice）

与 `python-practice` 同构的 FastAPI 手写练习区。每个练习由三部分组成：

- `src/exNN_topic.py` —— 练习模板（含任务说明与 `# TODO` 占位）
- `tests/test_NN_topic.py` —— 用 `fastapi.testclient.TestClient` 编写的测试，即「验收标准」
- `solutions/exNN_topic.py` —— 参考答案

> 配套速查文档：同目录根下的 [`fastapi-brief.md`](../fastapi-brief.md)，覆盖每个知识点的面试要点与代码范例。

## 目录

| # | 主题 | 关键点 |
|---|------|--------|
| 01 | 第一个接口 | `app.get`、返回字典 |
| 02 | 路径 / 查询参数 | 路径参数、可选查询参数 |
| 03 | 请求体 | Pydantic `BaseModel` |
| 04 | 查询参数校验 | `Query(gt=, le=)`、422 |
| 05 | 依赖注入 | `Depends`、公共参数 |
| 06 | 错误处理 | `HTTPException(404)` |
| 07 | 中间件 | `@app.middleware`、响应头 |
| 08 | 依赖鉴权 | `Header` + `Depends` 抛 403 |
| 09 | 后台任务 | `BackgroundTasks` |
| 10 | 异步接口 | `async/await` |
| 11 | 路由模块 | `APIRouter` + `include_router` |
| 12 | 跨域 | `CORSMiddleware` |

## 使用方式

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 在 src/ 中完成 TODO 后运行测试
pytest

# 直接对照参考答案跑通（把 solutions 拷到 src 验证）
pytest   # 参考答案已保证可过
```

每个 `src/exNN_topic.py` 末尾都带 `if __name__ == "__main__"` 入口，因此也可以直接当作脚本启动开发服务器（需 `uvicorn`，已列入 `requirements.txt`）：

```bash
# 方式 A：用 uvicorn 加载（推荐，支持 --reload 热重载）
uvicorn src.ex01_hello:app --reload --port 8000

# 方式 B：直接 python 跑脚本（内部也是调 uvicorn.run）
python src/ex01_hello.py
#   -> 接口根地址：http://127.0.0.1:8000/
#   -> 交互文档：  http://127.0.0.1:8000/docs
```

注意：入口块只在 `python src/exNN_xxx.py` 直接运行时触发，跑 `pytest` 时用 `TestClient` 导入 `app`，不会启动服务器，两者互不干扰。

提示：先读 `src/exNN_topic.py` 顶部的任务说明，再打开对应 `tests/test_NN_topic.py` 看验收，实现后在 `src` 中补完代码，`pytest` 全绿即过关；卡住时参考 `solutions`。
