# 单例模式
# 多种实现方式


class Singleton:
    """使用 __new__ 实现单例"""
    # TODO: 在这里实现
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        if not hasattr(self, "_initialized"):
            self.value = value
            self._initialized = True


def singleton_decorator(cls):
    """使用装饰器实现单例"""
    # TODO: 在这里实现
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance
