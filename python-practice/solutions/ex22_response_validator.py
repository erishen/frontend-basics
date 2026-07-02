def validate_response(data, schema, path="root") -> list[str]:
    errors = []
    expected_type = schema.get("type")

    type_map = {
        "string": str,
        "integer": int,
        "number": (int, float),
        "boolean": bool,
    }

    if expected_type in type_map:
        py_type = type_map[expected_type]
        # bool 是 int 的子类，需要特殊处理
        if expected_type == "integer" and isinstance(data, bool):
            errors.append(f"{path}: expected integer, got boolean")
        elif not isinstance(data, py_type):
            actual = type(data).__name__
            errors.append(f"{path}: expected {expected_type}, got {actual}")

    elif expected_type == "array":
        if not isinstance(data, list):
            errors.append(f"{path}: expected array, got {type(data).__name__}")
        elif "items" in schema:
            for i, item in enumerate(data):
                errors.extend(validate_response(item, schema["items"], f"{path}[{i}]"))

    elif expected_type == "object":
        if not isinstance(data, dict):
            errors.append(f"{path}: expected object, got {type(data).__name__}")
        else:
            # 检查 required 字段
            for field in schema.get("required", []):
                if field not in data:
                    errors.append(f"{path}: missing required field '{field}'")
            # 递归校验 properties
            properties = schema.get("properties", {})
            for key, prop_schema in properties.items():
                if key in data:
                    errors.extend(validate_response(data[key], prop_schema, f"{path}.{key}"))

    return errors
