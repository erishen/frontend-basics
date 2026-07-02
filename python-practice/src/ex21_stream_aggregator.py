"""
AI 场景 09: 流式响应聚合
聚合 LLM 流式输出的 token，支持过滤和回调
"""


class StreamAggregator:
    """
    聚合流式 LLM 响应的 token。
    支持：
    - 逐 token 追加
    - 获取完整文本
    - 按分隔符切分完整回复
    - 注册 on_token 回调
    """

    def __init__(self):
        self._tokens: list[str] = []
        self._callbacks: list = []

    def on_token(self, callback):
        """注册 token 回调"""
        # TODO: 实现
        pass

    def feed(self, token: str):
        """喂入一个 token，触发回调"""
        # TODO: 实现
        pass

    def get_text(self) -> str:
        """获取聚合后的完整文本"""
        # TODO: 实现
        pass

    def split(self, separator: str = "\n") -> list[str]:
        """按分隔符切分完整回复"""
        # TODO: 实现
        pass

    def reset(self):
        """重置聚合器"""
        # TODO: 实现
        pass
