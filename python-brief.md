# Python 面试高频考点（精简版）

> 只保留面试最常问的知识点，快速过一遍就能应对大部分 Python 面试题。

---

## 1. 可变 vs 不可变（必考）

```python
# 不可变类型：int, float, str, tuple, frozenset, bool
a = "hello"
b = a
a += " world"
print(b)  # "hello" —— b 没变，a 指向了新对象

# 可变类型：list, dict, set, 自定义对象
a = [1, 2, 3]
b = a
a.append(4)
print(b)  # [1, 2, 3, 4] —— b 也跟着变了，因为共享同一个对象

# 面试陷阱：函数默认参数
def bad(lst=[]):       # ❌ 默认参数只创建一次，所有调用共享
    lst.append(1)
    return lst

bad()  # [1]
bad()  # [1, 1]  ← 不是 [1]！

def good(lst=None):    # ✅ 每次调用创建新列表
    if lst is None:
        lst = []
    lst.append(1)
    return lst
```

---

## 2. is vs ==（必考）

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True  —— 值相等
print(a is b)   # False —— 不是同一个对象

# 小整数缓存池（-5 到 256）
x = 256
y = 256
print(x is y)   # True

x = 257
y = 257
print(x is y)   # False（交互式环境可能 True，脚本中 False）

# None 判断用 is
if x is None:
    pass
```

---

## 3. *args 与 **kwargs

```python
def func(a, b, *args, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")       # tuple
    print(f"kwargs={kwargs}")   # dict

func(1, 2, 3, 4, x=10, y=20)
# a=1, b=2
# args=(3, 4)
# kwargs={'x': 10, 'y': 20}

# 解包用法
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
add(*nums)        # 解包列表 → add(1, 2, 3)

params = {"a": 1, "b": 2, "c": 3}
add(**params)     # 解包字典 → add(a=1, b=2, c=3)
```

---

## 4. 列表/字典/集合推导式

```python
# 列表推导
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]

# 嵌套推导
matrix = [[1,2],[3,4],[5,6]]
flat = [x for row in matrix for x in row]  # [1,2,3,4,5,6]

# 字典推导
d = {x: x**2 for x in range(5)}  # {0:0, 1:1, 2:4, 3:9, 4:16}

# 集合推导
s = {x % 5 for x in range(20)}   # {0, 1, 2, 3, 4}

# 生成器表达式（省内存，用圆括号）
gen = (x**2 for x in range(1000000))  # 不立即计算
```

---

## 5. 装饰器（必考）

本质：接收函数，返回新函数，在不修改原函数的前提下增加功能。

```python
import functools

# 基础装饰器
def timer(func):
    @functools.wraps(func)   # 保留原函数的 __name__
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time()-start:.2f}s")
        return result
    return wrapper

@timer
def slow_func():
    import time; time.sleep(1)
    return "done"

slow_func()  # slow_func took 1.00s

# 带参数的装饰器（三层嵌套）
def repeat(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello {name}")

greet("Lei")  # 打印 3 次 Hello Lei
```

**面试要点：** `@functools.wraps(func)` 一定要加，否则被装饰函数的 `__name__`、`__doc__` 会丢失。

---

## 6. 生成器与迭代器（高频）

```python
# 迭代器：实现了 __iter__ 和 __next__ 的对象
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.high:
            raise StopIteration
        self.current += 1
        return self.current - 1

for x in Counter(1, 5):
    print(x)  # 1, 2, 3, 4

# 生成器：用 yield 的函数，自动实现迭代器协议
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print(next(fib))  # 0
print(next(fib))  # 1
print(next(fib))  # 1
print(next(fib))  # 2

# 生成器的核心价值：惰性计算，省内存
def read_large_file(path):
    with open(path) as f:
        for line in f:
            yield line.strip()

# 不会一次性加载整个文件到内存
for line in read_large_file("big.txt"):
    process(line)
```

**yield vs return：** return 结束函数返回值，yield 暂停函数并产出一个值，下次调用 next() 从暂停处继续。

---

## 7. 上下文管理器（with 语句）

```python
# 方式1：类实现 __enter__ / __exit__
class FileManager:
    def __init__(self, filename, mode):
        self.file = open(filename, mode)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return False  # 不吞掉异常

with FileManager("test.txt", "w") as f:
    f.write("hello")

# 方式2：contextmanager 装饰器（更简洁）
from contextlib import contextmanager

@contextmanager
def managed_file(path, mode):
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()

with managed_file("test.txt", "w") as f:
    f.write("hello")
```

---

## 8. GIL（全局解释器锁）（必考）

**是什么：** CPython 的互斥锁，同一时刻只允许一个线程执行 Python 字节码。

**为什么存在：** CPython 内存管理不是线程安全的，GIL 用最简单的方式保证了线程安全。

**影响与对策：**

```python
# CPU 密集型 → 用多进程（multiprocessing）
from multiprocessing import Process
import os

def cpu_task(n):
    return sum(i * i for i in range(n))

# 多线程对 CPU 密集型没有加速效果（GIL 限制）
# 多进程可以绕过 GIL，真正利用多核

# IO 密集型 → 多线程 / 协程（asyncio）
import asyncio

async def fetch(url):
    await asyncio.sleep(1)  # 模拟网络请求
    return f"response from {url}"

async def main():
    # 并发执行多个 IO 操作
    results = await asyncio.gather(
        fetch("url1"),
        fetch("url2"),
        fetch("url3"),
    )

asyncio.run(main())
```

**一句话总结：** GIL 让 Python 多线程无法并行执行 CPU 密集任务；IO 密集用协程/多线程，CPU 密集用多进程。

---

## 9. 类与继承

```python
class Animal:
    species_count = 0   # 类变量

    def __init__(self, name):
        self.name = name        # 实例变量
        Animal.species_count += 1

    def speak(self):
        raise NotImplementedError

    @classmethod
    def get_count(cls):
        return cls.species_count

    @staticmethod
    def is_domestic(species):
        return species in {"dog", "cat", "cow"}

    def __repr__(self):
        return f"Animal({self.name})"

    def __str__(self):
        return f"I am {self.name}"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # 调用父类 __init__
        self.breed = breed

    def speak(self):
        return "Woof!"

dog = Dog("Rex", "Husky")
print(dog.speak())    # Woof!
print(Dog.get_count())  # 1

# MRO（方法解析顺序）—— 多继承
class A:
    def who(self): return "A"

class B(A):
    def who(self): return "B"

class C(A):
    def who(self): return "C"

class D(B, C):
    pass

print(D().who())    # B
print(D.mro())      # D → B → C → A → object
# Python 用 C3 线性化算法确定 MRO
```

---

## 10. 常用魔术方法

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)

    def __getitem__(self, key):
        if key == 0: return self.x
        if key == 1: return self.y
        raise IndexError

    def __lt__(self, other):
        return len(self) < len(other)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)     # Vector(4, 6)
print(v1 == v2)    # False
print(len(v2))     # 5
print(v2[0])       # 3
```

---

## 11. Lambda / map / filter / reduce

```python
# lambda —— 匿名函数
square = lambda x: x ** 2
add = lambda a, b: a + b

# map —— 对每个元素应用函数
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))  # [1, 4, 9, 16]
# 更 Pythonic 的写法：[x**2 for x in nums]

# filter —— 过滤元素
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]
# 更 Pythonic：[x for x in nums if x % 2 == 0]

# reduce —— 累积计算
from functools import reduce
product = reduce(lambda a, b: a * b, nums)  # 24
# 更 Pythonic：import math; math.prod(nums)
```

**面试建议：** 知道 map/filter/reduce 是什么，但实际代码中推导式更 Pythonic。

---

## 12. 深拷贝 vs 浅拷贝

```python
import copy

original = [[1, 2], [3, 4]]

# 浅拷贝：只复制外层，内层还是引用
shallow = original.copy()        # 或 list(original) 或 original[:]
shallow[0].append(99)
print(original[0])   # [1, 2, 99]  ← 原列表也变了！

# 深拷贝：递归复制所有层
deep = copy.deepcopy(original)
deep[0].append(100)
print(original[0])   # [1, 2, 99]  ← 原列表不受影响

# 一句话：浅拷贝复制对象，深拷贝复制对象及其包含的对象
```

---

## 13. 异常处理

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except (TypeError, ValueError):
    print("Type or value error")
except Exception as e:
    print(f"Other error: {e}")    # 兜底
else:
    print("No error")             # 没异常时执行
finally:
    print("Always execute")       # 总是执行

# 自定义异常
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw {amount}, balance is {balance}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount
```

---

## 14. 一句话速记

| 考点 | 要点 |
|------|------|
| 可变/不可变 | list/dict/set 可变；int/str/tuple 不可变 |
| 默认参数陷阱 | 不要用 `[]` `{}` 做默认值，用 `None` |
| is vs == | is 比较身份（内存地址），== 比较值 |
| 装饰器 | 不修改原函数，增加功能；记得加 `@wraps` |
| 生成器 | yield 惰性计算，省内存，只能遍历一次 |
| GIL | CPU 密集用多进程，IO 密集用协程/多线程 |
| MRO | C3 线性化，`ClassName.mro()` 查看 |
| 深/浅拷贝 | 浅拷贝复制外层，深拷贝递归复制所有层 |
| *args/**kwargs | 解包位置参数 / 关键字参数 |
| 推导式 | 比 map/filter 更 Pythonic |
