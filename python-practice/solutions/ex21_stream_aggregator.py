class StreamAggregator:
    def __init__(self):
        self._tokens: list[str] = []
        self._callbacks: list = []

    def on_token(self, callback):
        self._callbacks.append(callback)

    def feed(self, token: str):
        self._tokens.append(token)
        for cb in self._callbacks:
            cb(token)

    def get_text(self) -> str:
        return "".join(self._tokens)

    def split(self, separator: str = "\n") -> list[str]:
        return self.get_text().split(separator)

    def reset(self):
        self._tokens = []
