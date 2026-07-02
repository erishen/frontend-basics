# 列表扁平化
# 展平任意深度的嵌套列表


def flatten(lst):
    """递归展平任意深度的嵌套列表/元组"""
    # TODO: 在这里实现
    result = []
    for item in lst:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def flatten_iter(lst):
    """迭代版本（用栈模拟递归）"""
    # TODO: 在这里实现
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
