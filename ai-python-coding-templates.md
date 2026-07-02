# AI 场景 Python 手写代码模板

> AI 应用工程师面试高频手写题，每题都是真实 AI 工程场景，完整可运行。

---

## 1. RAG 文本分块

```python
def chunk_text(text: str, chunk_size: int, overlap: int = 0) -> list[str]:
    """按字符数分块，支持重叠（防止语义被截断）"""
    if not text or chunk_size <= 0:
        return []
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
        if start >= len(text) or overlap >= chunk_size:
            break
    return chunks
```

---

## 2. SSE 流式响应解析

```python
def parse_sse(raw: str) -> list[dict]:
    """解析 LLM 流式输出的 SSE 格式，过滤 [DONE]"""
    events = []
    current_event = current_data = None
    for line in raw.split("\n"):
        line = line.strip()
        if line.startswith("event:"):
            current_event = line[len("event:"):].strip()
        elif line.startswith("data:"):
            current_data = line[len("data:"):].strip()
        elif line == "":
            if current_event is not None and current_data is not None:
                if current_data != "[DONE]":
                    events.append({"event": current_event, "data": current_data})
            current_event = current_data = None
    # 末尾无空行的情况
    if current_event is not None and current_data is not None:
        if current_data != "[DONE]":
            events.append({"event": current_event, "data": current_data})
    return events
```

---

## 3. 余弦相似度 + Top-K 检索

```python
import math

def cosine_similarity(vec_a: list[float], vec_b: list[float]) -> float:
    """余弦相似度，用于向量检索"""
    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    norm_a = math.sqrt(sum(a * a for a in vec_a))
    norm_b = math.sqrt(sum(b * b for b in vec_b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)

def top_k_similar(query: list[float], vectors: list[list[float]], k: int) -> list[int]:
    """返回与 query 最相似的 top-k 向量索引"""
    scores = [(i, cosine_similarity(query, v)) for i, v in enumerate(vectors)]
    scores.sort(key=lambda x: x[1], reverse=True)
    return [idx for idx, _ in scores[:k]]
```

---

## 4. Prompt 模板引擎

```python
import re

def _resolve(key: str, variables: dict):
    """解析嵌套 key: user.name → variables['user']['name']"""
    val = variables
    for part in key.split("."):
        if isinstance(val, dict) and part in val:
            val = val[part]
        else:
            return None
    return val

def render_template(template: str, variables: dict) -> str:
    """替换 {{variable}}，不存在的变量保留原样"""
    def replacer(match):
        key = match.group(1).strip()
        result = _resolve(key, variables)
        return match.group(0) if result is None else str(result)
    return re.sub(r"\{\{(\s*[\w.]+\s*)\}\}", replacer, template)

def render_with_fallback(template: str, variables: dict, default: str = "") -> str:
    """替换 {{variable}}，不存在的变量用 default 替代"""
    def replacer(match):
        result = _resolve(match.group(1).strip(), variables)
        return default if result is None else str(result)
    return re.sub(r"\{\{(\s*[\w.]+\s*)\}\}", replacer, template)
```

---

## 5. 对话历史截断（Token 预算）

```python
import re

def estimate_tokens(text: str) -> int:
    """简易 token 估算：英文单词数 + 中文字符数"""
    chinese = len(re.findall(r"[\u4e00-\u9fff]", text))
    english = len(re.sub(r"[\u4e00-\u9fff]", " ", text).split())
    return chinese + english

def truncate_history(messages: list[dict], max_tokens: int,
                     system_msg: dict | None = None) -> list[dict]:
    """按 token 预算截断对话，从最新消息往前保留，system 始终保留"""
    result = [system_msg] if system_msg else []
    budget, selected = max_tokens, []
    for msg in reversed(messages):
        tokens = estimate_tokens(msg["content"])
        if tokens > budget:
            break
        selected.append(msg)
        budget -= tokens
    result.extend(reversed(selected))
    return result
```

---

## 6. JSON 提取器（从 LLM 输出提取）

```python
import json, re

def extract_json(text: str) -> dict | list | None:
    """从 LLM 输出中提取 JSON（支持代码块包裹、前后有文字）"""
    text = text.strip()
    # 1. 直接解析
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    # 2. 提取 ```json ... ``` 代码块
    match = re.search(r"```(?:json)?\s*\n?(.*?)\n?\s*```", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1).strip())
        except json.JSONDecodeError:
            pass
    # 3. 找第一个 { 到最后一个 } 或 [ 到 ]
    for s, e in [("{", "}"), ("[", "]")]:
        start, end = text.find(s), text.rfind(e)
        if start != -1 and end > start:
            try:
                return json.loads(text[start:end + 1])
            except json.JSONDecodeError:
                pass
    return None

def extract_json_field(text: str, field: str, default=None):
    """提取 JSON 中指定字段"""
    data = extract_json(text)
    return data.get(field, default) if isinstance(data, dict) else default
```

---

## 7. 指数退避重试装饰器

```python
import functools, time

def retry(max_retries: int = 3, base_delay: float = 1.0, exceptions: tuple = (Exception,)):
    """指数退避重试：第 n 次等待 base_delay * 2^(n-1)"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exc = e
                    if attempt < max_retries:
                        time.sleep(base_delay * (2 ** attempt))
            raise last_exc
        return wrapper
    return decorator

# 用法
@retry(max_retries=3, base_delay=1.0, exceptions=(ConnectionError, TimeoutError))
def call_llm_api(prompt: str) -> str:
    ...
```

---

## 8. BM25 关键词检索

```python
import math
from collections import Counter

class BM25Retriever:
    """稀疏检索，RAG 中常与向量检索混合使用"""
    def __init__(self, k1=1.5, b=0.75):
        self.k1, self.b = k1, b
        self.documents, self.doc_lens, self.df = [], [], Counter()
        self.avg_dl = 0

    def add_documents(self, documents: list[str]):
        for doc in documents:
            tokens = doc.lower().split()
            self.documents.append(tokens)
            self.doc_lens.append(len(tokens))
            for t in set(tokens):
                self.df[t] += 1
        self.avg_dl = sum(self.doc_lens) / len(self.documents) if self.documents else 0

    def search(self, query: str, top_k=3) -> list[tuple[int, float]]:
        n = len(self.documents)
        scores = []
        for idx, doc in enumerate(self.documents):
            tf, dl = Counter(doc), self.doc_lens[idx]
            score = sum(
                math.log((n - self.df[t] + 0.5) / (self.df[t] + 0.5) + 1)  # IDF
                * tf.get(t, 0) * (self.k1 + 1)                               # 分子
                / (tf.get(t, 0) + self.k1 * (1 - self.b + self.b * dl / self.avg_dl))  # 分母
                for t in query.lower().split() if self.df[t] > 0
            )
            scores.append((idx, score))
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]
```

---

## 9. 流式响应聚合器

```python
class StreamAggregator:
    """聚合 LLM 流式 token，支持回调和切分"""
    def __init__(self):
        self._tokens, self._callbacks = [], []

    def on_token(self, callback):
        self._callbacks.append(callback)

    def feed(self, token: str):
        self._tokens.append(token)
        for cb in self._callbacks:
            cb(token)

    def get_text(self) -> str:
        return "".join(self._tokens)

    def split(self, separator="\n") -> list[str]:
        return self.get_text().split(separator)

    def reset(self):
        self._tokens = []

# 用法
agg = StreamAggregator()
agg.on_token(lambda t: print(t, end="", flush=True))
for chunk in llm_stream:
    agg.feed(chunk["content"])
```

---

## 10. 响应格式校验（简易 JSON Schema）

```python
def validate_response(data, schema, path="root") -> list[str]:
    """简易 JSON Schema 校验，返回错误列表"""
    errors = []
    expected = schema.get("type")
    type_map = {"string": str, "integer": int, "number": (int, float), "boolean": bool}

    if expected in type_map:
        if expected == "integer" and isinstance(data, bool):
            errors.append(f"{path}: expected integer, got boolean")
        elif not isinstance(data, type_map[expected]):
            errors.append(f"{path}: expected {expected}, got {type(data).__name__}")
    elif expected == "array":
        if not isinstance(data, list):
            errors.append(f"{path}: expected array, got {type(data).__name__}")
        elif "items" in schema:
            for i, item in enumerate(data):
                errors.extend(validate_response(item, schema["items"], f"{path}[{i}]"))
    elif expected == "object":
        if not isinstance(data, dict):
            errors.append(f"{path}: expected object, got {type(data).__name__}")
        else:
            for field in schema.get("required", []):
                if field not in data:
                    errors.append(f"{path}: missing required field '{field}'")
            for key, prop in schema.get("properties", {}).items():
                if key in data:
                    errors.extend(validate_response(data[key], prop, f"{path}.{key}"))
    return errors

# 用法
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "scores": {"type": "array", "items": {"type": "integer"}},
    },
    "required": ["name", "scores"],
}
errors = validate_response(llm_output, schema)
if errors:
    print("LLM 输出格式错误:", errors)
```
