# 装饰器（带参数）
# 实现一个 retry 装饰器，失败时自动重试

import functools


def retry(max_retries=3, exceptions=(Exception,)):
    """
    重试装饰器。
    :param max_retries: 最大重试次数
    :param exceptions: 需要捕获并重试的异常类型
    """
    # TODO: 在这里实现
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    if attempt == max_retries:
                        raise
        return wrapper
    return decorator
