"""
AI 场景 10: 响应格式校验
校验 LLM 输出是否符合预期的 JSON Schema（简化版）
"""


def validate_response(data: dict, schema: dict) -> list[str]:
    """
    简易 JSON Schema 校验器，返回错误列表（空列表表示通过）。
    支持的 schema 类型:
    - {"type": "string"}
    - {"type": "integer"}
    - {"type": "number"}
    - {"type": "boolean"}
    - {"type": "array", "items": {"type": "string"}}
    - {"type": "object", "properties": {...}, "required": [...]}

    错误格式: "field.path: expected X, got Y"
    """
    # TODO: 实现
    pass
