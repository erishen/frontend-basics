from src.ex22_response_validator import validate_response


def test_valid_string():
    errors = validate_response("hello", {"type": "string"})
    assert errors == []


def test_invalid_string():
    errors = validate_response(123, {"type": "string"})
    assert len(errors) == 1
    assert "expected string" in errors[0]


def test_valid_integer():
    errors = validate_response(42, {"type": "integer"})
    assert errors == []


def test_bool_not_integer():
    errors = validate_response(True, {"type": "integer"})
    assert len(errors) == 1


def test_valid_object():
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer"},
        },
        "required": ["name", "age"],
    }
    errors = validate_response({"name": "Alice", "age": 30}, schema)
    assert errors == []


def test_missing_required():
    schema = {
        "type": "object",
        "properties": {"name": {"type": "string"}},
        "required": ["name", "email"],
    }
    errors = validate_response({"name": "Alice"}, schema)
    assert len(errors) == 1
    assert "missing required field 'email'" in errors[0]


def test_nested_validation():
    schema = {
        "type": "object",
        "properties": {
            "scores": {
                "type": "array",
                "items": {"type": "integer"},
            }
        },
    }
    errors = validate_response({"scores": [1, "two", 3]}, schema)
    assert len(errors) == 1
    assert "scores[1]" in errors[0]


def test_valid_array():
    schema = {"type": "array", "items": {"type": "string"}}
    errors = validate_response(["a", "b"], schema)
    assert errors == []


def test_invalid_array():
    schema = {"type": "array", "items": {"type": "string"}}
    errors = validate_response("not array", schema)
    assert len(errors) == 1
