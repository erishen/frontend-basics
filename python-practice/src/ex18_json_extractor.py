"""
AI 场景 06: JSON 提取器
从 LLM 输出中提取 JSON（LLM 经常在 JSON 前后加说明文字）
"""
import json


def extract_json(text: str) -> dict | list | None:
    """
    从文本中提取第一个有效的 JSON 对象或数组。
    - 可能被 ```json ... ``` 包裹
    - 可能前后有说明文字
    - 解析失败返回 None
    """
    # TODO: 实现
    pass


def extract_json_field(text: str, field: str, default=None):
    """
    从 LLM 输出中提取 JSON 的指定字段值。
    """
    # TODO: 实现
    pass
