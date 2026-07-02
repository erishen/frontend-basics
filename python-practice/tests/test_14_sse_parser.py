from src.ex14_sse_parser import parse_sse


def test_basic_sse():
    raw = """event: message
data: {"content": "Hello"}

event: message
data: {"content": "World"}

event: done
data: [DONE]
"""
    result = parse_sse(raw)
    assert len(result) == 2
    assert result[0] == {"event": "message", "data": '{"content": "Hello"}'}
    assert result[1] == {"event": "message", "data": '{"content": "World"}'}


def test_filter_done():
    raw = """event: msg
data: hello

event: done
data: [DONE]
"""
    result = parse_sse(raw)
    assert len(result) == 1
    assert result[0]["data"] == "hello"


def test_no_trailing_newline():
    raw = """event: msg
data: last"""
    result = parse_sse(raw)
    assert len(result) == 1
    assert result[0]["data"] == "last"


def test_empty():
    assert parse_sse("") == []
