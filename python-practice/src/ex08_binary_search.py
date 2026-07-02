# 二分查找
# 各种变体


def binary_search(lst, target):
    """标准二分查找，返回目标索引，不存在返回 -1"""
    # TODO: 在这里实现
    lo, hi = 0, len(lst) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def find_first(lst, target):
    """查找第一个等于 target 的位置（处理重复元素）"""
    # TODO: 在这里实现
    lo, hi = 0, len(lst) - 1
    result = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if lst[mid] == target:
            result = mid
            hi = mid - 1
        elif lst[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result


def find_last(lst, target):
    """查找最后一个等于 target 的位置"""
    # TODO: 在这里实现
    lo, hi = 0, len(lst) - 1
    result = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if lst[mid] == target:
            result = mid
            lo = mid + 1
        elif lst[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result
