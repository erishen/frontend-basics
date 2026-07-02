# 缓存 / 记忆化
# 实现 memoize 装饰器
import functools

def memoize(func):
    """
    记忆化装饰器：缓存函数调用结果。
    支持任意位置参数和关键字参数。
    """
    # TODO: 在这里实现
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    wrapper.cache = cache
    return wrapper
