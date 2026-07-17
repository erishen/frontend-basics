"""
AI 场景 05: 对话历史截断
根据 token 预算裁剪对话历史，保留最近的对话
"""
import re


def estimate_tokens(text: str) -> int:
    """
    简单估算 token 数：英文按空格分词，中文按字符数，取总和。
    实际生产中会调用 tokenizer，这里做简化。
    """
    # TODO: 实现（英文单词数 + 中文字符数）
    chinese = len(re.findall(r"[\u4e00-\u9fff]", text))
    english = len(re.sub(r"[\u4e00-\u9fff]", " ", text).split())
    return chinese + english


def truncate_history(
    messages: list[dict],  # [{"role": "user", "content": "..."}, ...]
    max_tokens: int,
    system_msg: dict | None = None,  # system 消息始终保留
) -> list[dict]:
    """
    截断对话历史，使总 token 数不超过 max_tokens。
    - system_msg 始终保留在最前面（不计入 max_tokens）
    - 从最新消息开始保留，直到超出预算
    - 返回截断后的消息列表
    """
    # TODO: 实现
    result = [system_msg] if system_msg else []
    buget, selected = max_tokens, []
    for msg in reversed(messages):
        tokens = estimate_tokens(msg["content"])
        if tokens > buget:
            break
        selected.append(msg)
        budget -= tokens 
    result.extend(reversed(selected))
    return result
