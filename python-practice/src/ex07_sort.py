# 排序算法
# 手写常见排序


def quick_sort(lst):
    """快速排序"""
    # TODO: 在这里实现
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(lst):
    """归并排序"""
    # TODO: 在这里实现
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return _merge(left, right)

def _merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def heap_sort(lst):
    """堆排序"""
    # TODO: 在这里实现
    n = len(lst)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(lst, n, i)

    for i in range(n - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        _heapify(lst, i, 0)
        
    return lst

def _heapify(arr, n, i):
    largest = i
    left, right = 2 * i + 1, 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)
