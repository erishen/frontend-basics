# 上下文管理器
# 实现自定义上下文管理器


from contextlib import contextmanager
import io
import time


class Timer:
    """计时器上下文管理器，记录代码块执行时间"""
    # TODO: 在这里实现 __init__, __enter__, __exit__
    def __init__(self):
        self.elapsed = None

    def __enter__(self):
        self._start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self._start
        return False


@contextmanager
def temp_attr(obj, attr, temp_value):
    """临时修改对象属性，退出时恢复原值"""
    # TODO: 在这里实现
    old_value = getattr(obj, attr)
    setattr(obj, attr, temp_value)
    try:
        yield
    finally:
        setattr(obj, attr, old_value)
