# 生成器
# 实现各种生成器模式


def fibonacci():
    """斐波那契数列生成器：0, 1, 1, 2, 3, 5, 8, ..."""
    # TODO: 在这里实现
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def chunks(lst, n):
    """将列表按大小 n 分块，yield 每一块"""
    # TODO: 在这里实现
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def flatten_gen(nested):
    """递归展平嵌套列表/元组（生成器版本）"""
    # TODO: 在这里实现
    for item in nested:
        if isinstance(item, (list, tuple)):
            yield from flatten_gen(item)
        else:
            yield item
