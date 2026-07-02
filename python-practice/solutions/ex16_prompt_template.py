import re


def _resolve(key: str, variables: dict):
    """解析嵌套 key，如 user.name → variables['user']['name']"""
    parts = key.split(".")
    val = variables
    for part in parts:
        if isinstance(val, dict) and part in val:
            val = val[part]
        else:
            return None
    return val


def render_template(template: str, variables: dict) -> str:
    def replacer(match):
        key = match.group(1).strip()
        result = _resolve(key, variables)
        if result is None:
            return match.group(0)  # 变量不存在，保留原样
        return str(result)

    return re.sub(r"\{\{(\s*[\w.]+\s*)\}\}", replacer, template)


def render_with_fallback(template: str, variables: dict, default: str = "") -> str:
    def replacer(match):
        key = match.group(1).strip()
        result = _resolve(key, variables)
        if result is None:
            return default
        return str(result)

    return re.sub(r"\{\{(\s*[\w.]+\s*)\}\}", replacer, template)
