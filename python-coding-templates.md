# Python 面试手写代码模板

> 面试最高频的手写题，每题都是完整可运行的模板，多写几遍形成肌肉记忆。

---

## 1. 装饰器（带参数）

```python
import functools

def retry(max_retries=3, exceptions=(Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    if attempt == max_retries:
                        raise
        return wrapper
    return decorator

# 用法
@retry(max_retries=3, exceptions=(ConnectionError,))
def fetch_data(url):
    import urllib.request
    return urllib.request.urlopen(url).read()
```

---

## 2. 生成器

```python
# 斐波那契
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 取前 10 个
import itertools
list(itertools.islice(fibonacci(), 10))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# 列表分块
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

list(chunks([1,2,3,4,5], 2))  # [[1,2], [3,4], [5]]

# 递归展平
def flatten_gen(nested):
    for item in nested:
        if isinstance(item, (list, tuple)):
            yield from flatten_gen(item)
        else:
            yield item

list(flatten_gen([1, [2, [3, [4]]]]))  # [1, 2, 3, 4]
```

---

## 3. 上下文管理器

```python
# 方式1：类实现
import time

class Timer:
    def __init__(self):
        self.elapsed = None

    def __enter__(self):
        self._start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self._start
        return False  # 不吞异常

with Timer() as t:
    time.sleep(1)
print(f"耗时: {t.elapsed:.2f}s")

# 方式2：contextmanager 装饰器
from contextlib import contextmanager

@contextmanager
def temp_attr(obj, attr, temp_value):
    old_value = getattr(obj, attr)
    setattr(obj, attr, temp_value)
    try:
        yield
    finally:
        setattr(obj, attr, old_value)
```

---

## 4. 单例模式

```python
# 方式1：__new__
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        if not hasattr(self, "_initialized"):
            self.value = value
            self._initialized = True

# 方式2：装饰器
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class DB:
    def __init__(self, url):
        self.url = url
```

---

## 5. LRU 缓存

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)  # 弹出最久未使用
        self.cache[key] = value
```

---

## 6. 列表扁平化

```python
# 递归版
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

flatten([1, [2, [3, [4]]]])  # [1, 2, 3, 4]

# 迭代版（用栈）
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
```

---

## 7. 排序算法

```python
# 快速排序
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 归并排序
def merge_sort(lst):
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

# 堆排序
def heap_sort(lst):
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
```

---

## 8. 二分查找

```python
# 标准二分查找
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

# 找第一个等于 target 的位置（处理重复元素）
def find_first(lst, target):
    lo, hi = 0, len(lst) - 1
    result = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if lst[mid] == target:
            result = mid
            hi = mid - 1  # 继续往左找
        elif lst[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result

# 找最后一个等于 target 的位置
def find_last(lst, target):
    lo, hi = 0, len(lst) - 1
    result = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if lst[mid] == target:
            result = mid
            lo = mid + 1  # 继续往右找
        elif lst[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result
```

---

## 9. 记忆化装饰器

```python
import functools

def memoize(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    wrapper.cache = cache
    return wrapper

# 用法：斐波那契瞬间变 O(n)
@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

fib(100)  # 秒出结果，不加装饰器会算到天荒地老
```

---

## 10. 描述符

```python
# 类型验证描述符
class TypeValidator:
    def __init__(self, name, expected_type):
        self.attr_name = name
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        self.attr_name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, f"_{self.attr_name}", None)

    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"{self.attr_name} must be {self.expected_type.__name__}"
            )
        setattr(obj, f"_{self.attr_name}", value)

# 范围验证描述符
class RangeValidator:
    def __init__(self, name, min_val, max_val):
        self.attr_name = name
        self.min_val = min_val
        self.max_val = max_val

    def __set_name__(self, owner, name):
        self.attr_name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, f"_{self.attr_name}", None)

    def __set__(self, obj, value):
        if not (self.min_val <= value <= self.max_val):
            raise ValueError(
                f"{self.attr_name} must be between {self.min_val} and {self.max_val}"
            )
        setattr(obj, f"_{self.attr_name}", value)

# 用法
class Person:
    name = TypeValidator("name", str)
    age = TypeValidator("age", int)

class Config:
    port = RangeValidator("port", 1, 65535)
```

---

## 11. 生产者-消费者协程

```python
def consumer():
    """消费者：接收值，返回处理结果"""
    value = None
    while True:
        value = yield value * 2 if value is not None else None

def producer(consumer_coro, items):
    """生产者：向消费者发送数据"""
    results = []
    next(consumer_coro)  # 启动（推进到第一个 yield）
    for item in items:
        result = consumer_coro.send(item)
        results.append(result)
    return results

# 用法
c = consumer()
producer(c, [1, 2, 3, 4, 5])  # [2, 4, 6, 8, 10]
```

---

## 12. 深拷贝

```python
def deep_copy(obj, memo=None):
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

    return obj  # 不可变类型直接返回
```

---

## 速查表

| 题目 | 核心思路 | 关键点 |
|------|----------|--------|
| 装饰器 | 三层嵌套：参数→函数→wrapper | `@functools.wraps` 必须加 |
| 生成器 | `yield` + `yield from` | 惰性计算，省内存 |
| 上下文管理器 | `__enter__`/`__exit__` 或 `@contextmanager` | finally 保证清理 |
| 单例 | `__new__` 控制实例创建 | `_initialized` 防止重复 init |
| LRU | `OrderedDict` + `move_to_end` | get/put 都是 O(1) |
| 扁平化 | 递归 or 栈迭代 | `isinstance(item, (list, tuple))` |
| 排序 | 快排分治 / 归并合并 / 堆化 | 时间复杂度都是 O(n log n) |
| 二分查找 | 左右指针逼近 | 注意 `find_first` 和 `find_last` 的区别 |
| 记忆化 | dict 缓存 + 参数做 key | kwargs 要排序后做 tuple |
| 描述符 | `__get__`/`__set__` + `__set_name__` | 比 property 更灵活可复用 |
| 协程 | `yield` 既接收又返回 | `next()` 启动，`send()` 驱动 |
| 深拷贝 | 递归 + memo 处理引用 | 区分可变/不可变类型 |
