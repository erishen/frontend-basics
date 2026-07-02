# LRU 缓存
# 手动实现 LRU 缓存（不用 functools.lru_cache）
from collections import OrderedDict


class LRUCache:
    """
    使用 OrderedDict 实现 LRU 缓存。
    get / put 都要求 O(1) 时间复杂度。
    """

    def __init__(self, capacity: int):
        # TODO: 在这里实现
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        # TODO: 在这里实现
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # TODO: 在这里实现
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value
