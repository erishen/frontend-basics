"""
AI 场景 07: 指数退避重试装饰器
调用 LLM API 时经常需要重试（限流、超时等）
"""
import functools
import time


def retry(max_retries: int = 3, base_delay: float = 1.0, exceptions: tuple = (Exception,)):
    """
    指数退避重试装饰器。
    - 第 n 次重试等待 base_delay * 2^(n-1) 秒
    - 只重试 exceptions 中指定的异常类型
    - 超过最大重试次数后抛出最后一次异常
    """
    # TODO: 实现
    pass
