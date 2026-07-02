import functools
import time


def retry(max_retries: int = 3, base_delay: float = 1.0, exceptions: tuple = (Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_retries:
                        delay = base_delay * (2 ** attempt)
                        time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator
