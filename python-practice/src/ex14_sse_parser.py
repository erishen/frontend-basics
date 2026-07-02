"""
AI 场景 02: SSE 流式响应解析
解析 Server-Sent Events 格式的 LLM 流式输出
"""


def parse_sse(raw: str) -> list[dict]:
    """
    解析 SSE 格式的文本，提取所有 event/data 对。
    格式示例:
        event: message
        data: {"content": "Hello"}

        event: done
        data: [DONE]

    返回: [{"event": "message", "data": '{"content": "Hello"}}, ...]
    忽略 data 为 [DONE] 的条目。
    """
    # TODO: 实现
    pass
