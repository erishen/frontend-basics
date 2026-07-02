# 生产者-消费者模型
# 使用生成器实现协程模式


def consumer():
    """
    消费者协程：接收值并处理。
    使用 send() 接收数据，yield 返回处理结果。
    每个值 * 2 后返回。
    """
    # TODO: 在这里实现
    value = None
    while True:
        value = yield value * 2 if value is not None else None


def producer(consumer_coro, items):
    """生产者：向消费者发送数据，返回所有结果"""
    # TODO: 在这里实现
    results = []
    next(consumer_coro)
    for item in items:
        result = consumer_coro.send(item)
        results.append(result)
    return results
