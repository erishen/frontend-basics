import re


def estimate_tokens(text: str) -> int:
    # 中文字符数
    chinese_chars = len(re.findall(r"[\u4e00-\u9fff]", text))
    # 英文单词数（去掉中文后的空格分词）
    english_text = re.sub(r"[\u4e00-\u9fff]", " ", text)
    english_words = len(english_text.split())
    return chinese_chars + english_words


def truncate_history(
    messages: list[dict],
    max_tokens: int,
    system_msg: dict | None = None,
) -> list[dict]:
    result = []
    if system_msg is not None:
        result.append(system_msg)

    # 从最新消息开始往前选
    selected = []
    budget = max_tokens
    for msg in reversed(messages):
        tokens = estimate_tokens(msg["content"])
        if tokens > budget:
            break
        selected.append(msg)
        budget -= tokens

    # 反转回来保持时间顺序
    result.extend(reversed(selected))
    return result
