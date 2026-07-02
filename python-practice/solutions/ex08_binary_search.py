def binary_search(lst, target):
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
    lo, hi = 0, len(lst) - 1
    result = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if lst[mid] == target:
            result = mid
            hi = mid - 1  # 继续向左找
        elif lst[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result


def find_last(lst, target):
    lo, hi = 0, len(lst) - 1
    result = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if lst[mid] == target:
            result = mid
            lo = mid + 1  # 继续向右找
        elif lst[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result
