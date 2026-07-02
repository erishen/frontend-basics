import json
import re


def extract_json(text: str) -> dict | list | None:
    # 先尝试直接解析
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # 尝试提取 ```json ... ``` 代码块
    match = re.search(r"```(?:json)?\s*\n?(.*?)\n?\s*```", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1).strip())
        except json.JSONDecodeError:
            pass

    # 尝试找第一个 { 或 [ 到最后一个 } 或 ]
    for start_char, end_char in [("{", "}"), ("[", "]")]:
        start = text.find(start_char)
        end = text.rfind(end_char)
        if start != -1 and end != -1 and end > start:
            try:
                return json.loads(text[start:end + 1])
            except json.JSONDecodeError:
                pass

    return None


def extract_json_field(text: str, field: str, default=None):
    data = extract_json(text)
    if data is None:
        return default
    if isinstance(data, dict):
        return data.get(field, default)
    return default
