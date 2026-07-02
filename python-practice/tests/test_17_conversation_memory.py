from src.ex17_conversation_memory import estimate_tokens, truncate_history


def test_estimate_tokens_english():
    assert estimate_tokens("hello world") == 2


def test_estimate_tokens_chinese():
    assert estimate_tokens("你好世界") == 4


def test_estimate_tokens_mixed():
    # "hello 你好" → 去掉中文后 "hello  " → 1 个英文单词 + 2 个中文字符 = 3
    assert estimate_tokens("hello 你好") == 3


def test_truncate_basic():
    messages = [
        {"role": "user", "content": "hello"},       # 1 token
        {"role": "assistant", "content": "hi"},      # 1 token
        {"role": "user", "content": "how are you"},   # 3 tokens
    ]
    result = truncate_history(messages, max_tokens=4)
    # 从最新开始: "how are you"(3) + "hi"(1) = 4, 刚好
    assert len(result) == 2
    assert result[0]["content"] == "hi"
    assert result[1]["content"] == "how are you"


def test_truncate_with_system():
    system = {"role": "system", "content": "You are a helpful assistant."}
    messages = [
        {"role": "user", "content": "hello"},
        {"role": "assistant", "content": "hi there"},
    ]
    result = truncate_history(messages, max_tokens=2, system_msg=system)
    assert result[0] == system  # system 始终在最前面
    assert len(result) >= 1


def test_truncate_empty():
    assert truncate_history([], max_tokens=10) == []
