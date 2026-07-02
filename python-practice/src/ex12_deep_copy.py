# 深拷贝
# 手动实现深拷贝（不用 copy.deepcopy）


def deep_copy(obj, memo=None):
    """
    手动实现深拷贝。
    支持：dict, list, tuple, set, int, float, str, bool, None
    不需要处理循环引用（简化版）。
    """
    # TODO: 在这里实现
    if memo is None:
        memo = {}

    obj_id = id(obj)
    if obj_id in memo:
        return memo[obj_id]

    if isinstance(obj, dict):
        result = {}
        memo[obj_id] = result
        for k, v in obj.items():
            result[deep_copy(k, memo)] = deep_copy(v, memo)
        return result

    if isinstance(obj, list):
        result = []
        memo[obj_id] = result
        for item in obj:
            result.append(deep_copy(item, memo))
        return result

    if isinstance(obj, tuple):
        result = tuple(deep_copy(item, memo) for item in obj)
        memo[obj_id] = result
        return result

    if isinstance(obj, set):
        result = set()
        memo[obj_id] = result
        for item in obj:
            result.add(deep_copy(item, memo))
        return result

    return obj


