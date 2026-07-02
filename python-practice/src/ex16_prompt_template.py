"""
AI 场景 04: Prompt 模板引擎
实现简单的变量替换和条件渲染
"""


def render_template(template: str, variables: dict) -> str:
    """
    替换模板中的 {{variable}} 占位符。
    - 变量不存在时保留原样
    - 支持嵌套访问: {{user.name}} → variables["user"]["name"]
    """
    # TODO: 实现
    pass


def render_with_fallback(template: str, variables: dict, default: str = "") -> str:
    """
    替换模板变量，不存在的变量用 default 替代。
    """
    # TODO: 实现
    pass
