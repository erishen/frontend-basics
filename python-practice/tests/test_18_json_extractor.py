from src.ex18_json_extractor import extract_json, extract_json_field


def test_direct_json():
    result = extract_json('{"name": "Alice", "age": 30}')
    assert result == {"name": "Alice", "age": 30}


def test_json_in_code_block():
    text = """Here is the result:
```json
{"answer": 42}
```
Hope this helps!"""
    result = extract_json(text)
    assert result == {"answer": 42}


def test_json_with_surrounding_text():
    text = 'The answer is {"result": true} as expected.'
    result = extract_json(text)
    assert result == {"result": True}


def test_json_array():
    result = extract_json('Here: [1, 2, 3]')
    assert result == [1, 2, 3]


def test_invalid_json():
    assert extract_json("no json here") is None


def test_extract_field():
    text = 'Result: {"name": "Bob", "score": 95}'
    assert extract_json_field(text, "name") == "Bob"
    assert extract_json_field(text, "score") == 95
    assert extract_json_field(text, "missing", default="N/A") == "N/A"


def test_extract_field_no_json():
    assert extract_json_field("no json", "key") is None
