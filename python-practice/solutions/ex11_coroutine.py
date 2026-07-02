def consumer():
    value = None
    while True:
        value = yield value * 2 if value is not None else None


def producer(consumer_coro, items):
    results = []
    next(consumer_coro)  # 启动生成器
    for item in items:
        result = consumer_coro.send(item)
        results.append(result)
    return results
