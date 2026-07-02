def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def flatten_iter(lst):
    stack = [iter(lst)]
    result = []
    while stack:
        try:
            item = next(stack[-1])
            if isinstance(item, (list, tuple)):
                stack.append(iter(item))
            else:
                result.append(item)
        except StopIteration:
            stack.pop()
    return result
