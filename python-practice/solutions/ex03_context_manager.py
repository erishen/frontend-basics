from contextlib import contextmanager
import time


class Timer:
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
    old_value = getattr(obj, attr)
    setattr(obj, attr, temp_value)
    try:
        yield
    finally:
        setattr(obj, attr, old_value)
