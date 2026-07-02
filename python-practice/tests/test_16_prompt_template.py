from src.ex16_prompt_template import render_template, render_with_fallback


def test_simple_replace():
    result = render_template("Hello {{name}}!", {"name": "Alice"})
    assert result == "Hello Alice!"


def test_missing_var_kept():
    result = render_template("Hello {{name}}!", {})
    assert result == "Hello {{name}}!"


def test_nested_access():
    variables = {"user": {"name": "Bob", "role": "admin"}}
    result = render_template("User: {{user.name}}, Role: {{user.role}}", variables)
    assert result == "User: Bob, Role: admin"


def test_multiple_same_var():
    result = render_template("{{x}} + {{x}} = 2{{x}}", {"x": "a"})
    assert result == "a + a = 2a"


def test_fallback():
    result = render_with_fallback("Hello {{name}}!", {}, default="unknown")
    assert result == "Hello unknown!"


def test_fallback_partial():
    variables = {"name": "Alice"}
    result = render_with_fallback("{{name}} is {{age}}", variables, default="?")
    assert result == "Alice is ?"
