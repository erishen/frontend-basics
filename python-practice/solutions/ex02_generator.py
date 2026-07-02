def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def flatten_gen(nested):
    for item in nested:
        if isinstance(item, (list, tuple)):
            yield from flatten_gen(item)
        else:
            yield item
