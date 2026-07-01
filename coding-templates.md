# 面试手写代码模板

> 面试最高频的手写题，每题都是完整可运行的模板，多写几遍形成肌肉记忆。

---

## 1. 防抖 debounce

触发后等待 delay，期间再触发则重新计时。

```javascript
function debounce(fn, delay) {
  let timer = null;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}

// 用法
input.oninput = debounce(function (e) {
  search(e.target.value);
}, 300);
```

---

## 2. 节流 throttle

固定间隔内只执行一次。

```javascript
function throttle(fn, interval) {
  let lastTime = 0;
  return function (...args) {
    const now = Date.now();
    if (now - lastTime >= interval) {
      lastTime = now;
      fn.apply(this, args);
    }
  };
}

// 用法
window.onscroll = throttle(function () {
  updatePosition();
}, 100);
```

---

## 3. 深拷贝 deepClone

处理循环引用、特殊类型。

```javascript
function deepClone(obj, map = new WeakMap()) {
  if (obj === null || typeof obj !== "object") return obj;
  if (map.has(obj)) return map.get(obj); // 处理循环引用

  // 处理特殊对象
  if (obj instanceof Date) return new Date(obj);
  if (obj instanceof RegExp) return new RegExp(obj.source, obj.flags);

  const clone = Array.isArray(obj) ? [] : {};
  map.set(obj, clone);

  for (const key of Object.keys(obj)) {
    clone[key] = deepClone(obj[key], map);
  }
  return clone;
}
```

---

## 4. new 操作符

```javascript
function myNew(Constructor, ...args) {
  const obj = Object.create(Constructor.prototype);
  const result = Constructor.apply(obj, args);
  return result instanceof Object ? result : obj;
}

// 用法
function Person(name) { this.name = name; }
const p = myNew(Person, "Lei");
```

---

## 5. instanceof

沿原型链查找。

```javascript
function myInstance(left, right) {
  let proto = Object.getPrototypeOf(left);
  const prototype = right.prototype;
  while (proto !== null) {
    if (proto === prototype) return true;
    proto = Object.getPrototypeOf(proto);
  }
  return false;
}
```

---

## 6. call / apply / bind

```javascript
// call
Function.prototype.myCall = function (ctx, ...args) {
  ctx = ctx ?? globalThis;
  const fn = Symbol();
  ctx[fn] = this;
  const result = ctx[fn](...args);
  delete ctx[fn];
  return result;
};

// apply（参数是数组）
Function.prototype.myApply = function (ctx, args = []) {
  ctx = ctx ?? globalThis;
  const fn = Symbol();
  ctx[fn] = this;
  const result = ctx[fn](...args);
  delete ctx[fn];
  return result;
};

// bind（返回新函数）
Function.prototype.myBind = function (ctx, ...outerArgs) {
  const fn = this;
  return function (...innerArgs) {
    return fn.apply(ctx, [...outerArgs, ...innerArgs]);
  };
};
```

---

## 7. Promise

```javascript
class MyPromise {
  constructor(executor) {
    this.state = "pending";
    this.value = undefined;
    this.callbacks = [];

    const resolve = (value) => {
      if (this.state !== "pending") return;
      this.state = "fulfilled";
      this.value = value;
      this.callbacks.forEach((cb) => cb.onFulfilled(value));
    };

    const reject = (reason) => {
      if (this.state !== "pending") return;
      this.state = "rejected";
      this.value = reason;
      this.callbacks.forEach((cb) => cb.onRejected(reason));
    };

    try {
      executor(resolve, reject);
    } catch (err) {
      reject(err);
    }
  }

  then(onFulfilled, onRejected) {
    if (typeof onFulfilled !== "function") onFulfilled = (v) => v;
    if (typeof onRejected !== "function") onRejected = (e) => { throw e; };

    return new MyPromise((resolve, reject) => {
      const handle = (callback) => {
        try {
          const result = callback(this.value);
          if (result instanceof MyPromise) {
            result.then(resolve, reject);
          } else {
            resolve(result);
          }
        } catch (err) {
          reject(err);
        }
      };

      if (this.state === "fulfilled") handle(onFulfilled);
      else if (this.state === "rejected") handle(onRejected);
      else this.callbacks.push({ onFulfilled: () => handle(onFulfilled),
                                  onRejected: () => handle(onRejected) });
    });
  }

  catch(onRejected) {
    return this.then(null, onRejected);
  }
}
```

---

## 8. Promise.all

全部成功才成功，任一失败即失败。

```javascript
function promiseAll(promises) {
  return new Promise((resolve, reject) => {
    const results = [];
    let count = 0;
    if (promises.length === 0) return resolve(results);

    promises.forEach((p, i) => {
      Promise.resolve(p).then(
        (value) => {
          results[i] = value;
          if (++count === promises.length) resolve(results);
        },
        reject
      );
    });
  });
}
```

---

## 9. Promise.race

第一个完成的结果。

```javascript
function promiseRace(promises) {
  return new Promise((resolve, reject) => {
    promises.forEach((p) => {
      Promise.resolve(p).then(resolve, reject);
    });
  });
}
```

---

## 10. 数组扁平化 flat

```javascript
// 递归版
function flat(arr) {
  return arr.reduce((acc, val) =>
    Array.isArray(val) ? acc.concat(flat(val)) : acc.concat(val), []);
}

// 迭代版（用栈）
function flatIter(arr) {
  const stack = [...arr];
  const result = [];
  while (stack.length) {
    const item = stack.shift();
    if (Array.isArray(item)) {
      stack.unshift(...item);
    } else {
      result.push(item);
    }
  }
  return result;
}

// 指定深度版
function flatDepth(arr, depth = 1) {
  if (depth <= 0) return arr.slice();
  return arr.reduce((acc, val) =>
    Array.isArray(val)
      ? acc.concat(flatDepth(val, depth - 1))
      : acc.concat(val), []);
}
```

---

## 11. 数组去重

```javascript
// Set（最简洁）
const unique = [...new Set(arr)];

// filter + indexOf
const unique2 = arr.filter((item, index) => arr.indexOf(item) === index);

// reduce
const unique3 = arr.reduce((acc, val) =>
  acc.includes(val) ? acc : [...acc, val], []);

// 对象数组去重（按某个 key）
const uniqueBy = (arr, key) => {
  const seen = new Set();
  return arr.filter((item) => {
    const k = item[key];
    return seen.has(k) ? false : (seen.add(k), true);
  });
};
```

---

## 12. 函数柯里化 curry

把多参数函数变成一系列单参数函数。

```javascript
function curry(fn) {
  return function curried(...args) {
    if (args.length >= fn.length) {
      return fn.apply(this, args);
    }
    return function (...args2) {
      return curried.apply(this, [...args, ...args2]);
    };
  };
}

// 用法
function add(a, b, c) { return a + b + c; }
const curriedAdd = curry(add);
curriedAdd(1)(2)(3);     // 6
curriedAdd(1, 2)(3);     // 6
curriedAdd(1)(2, 3);     // 6
```

---

## 13. 发布订阅 EventEmitter

```javascript
class EventEmitter {
  constructor() {
    this.events = {};
  }

  on(event, fn) {
    (this.events[event] ??= []).push(fn);
    return this;
  }

  off(event, fn) {
    if (!this.events[event]) return;
    this.events[event] = this.events[event].filter((f) => f !== fn);
    return this;
  }

  once(event, fn) {
    const wrapper = (...args) => {
      fn(...args);
      this.off(event, wrapper);
    };
    return this.on(event, wrapper);
  }

  emit(event, ...args) {
    (this.events[event] ?? []).forEach((fn) => fn(...args));
    return this;
  }
}
```

---

## 14. LRU 缓存

用 Map 实现，最近访问的放末尾，淘汰最久未访问的。

```javascript
class LRUCache {
  constructor(capacity) {
    this.capacity = capacity;
    this.cache = new Map();
  }

  get(key) {
    if (!this.cache.has(key)) return -1;
    const value = this.cache.get(key);
    this.cache.delete(key);
    this.cache.set(key, value); // 重新插入，移到末尾
    return value;
  }

  put(key, value) {
    if (this.cache.has(key)) {
      this.cache.delete(key);
    } else if (this.cache.size >= this.capacity) {
      // Map 按插入顺序迭代，第一个就是最久未访问的
      const oldestKey = this.cache.keys().next().value;
      this.cache.delete(oldestKey);
    }
    this.cache.set(key, value);
  }
}
```

---

## 15. 模板字符串解析

把 `"Hello, {{name}}! You are {{age}}."` 替换为实际值。

```javascript
function render(template, data) {
  return template.replace(/\{\{(\w+)\}\}/g, (_, key) => data[key.trim()] ?? "");
}

// 用法
render("Hello, {{name}}! Age: {{age}}.", { name: "Lei", age: 30 });
// "Hello, Lei! Age: 30."

// 支持深层路径 {{user.name}}
function renderDeep(template, data) {
  return template.replace(/\{\{([\w.]+)\}\}/g, (_, path) => {
    return path.trim().split(".").reduce((obj, key) => obj?.[key], data) ?? "";
  });
}

renderDeep("Hi, {{user.name}}", { user: { name: "Lei" } });
// "Hi, Lei"
```

---

## 16. 对象深度合并 deepMerge

```javascript
function deepMerge(target, ...sources) {
  for (const source of sources) {
    if (!source || typeof source !== "object") continue;
    for (const key of Object.keys(source)) {
      if (
        typeof target[key] === "object" && target[key] !== null &&
        typeof source[key] === "object" && source[key] !== null &&
        !Array.isArray(target[key]) && !Array.isArray(source[key])
      ) {
        target[key] = deepMerge(target[key], source[key]);
      } else {
        target[key] = source[key];
      }
    }
  }
  return target;
}

// 用法
deepMerge({ a: 1, b: { c: 2 } }, { b: { d: 3 }, e: 4 });
// { a: 1, b: { c: 2, d: 3 }, e: 4 }
```

---

## 17. 异步并发控制（限制并发数）

```javascript
async function asyncPool(poolLimit, items, iterator) {
  const results = [];
  const executing = new Set();

  for (const [i, item] of items.entries()) {
    const p = Promise.resolve().then(() => iterator(item, i));
    results.push(p);
    executing.add(p);

    p.then(() => executing.delete(p));

    if (executing.size >= poolLimit) {
      await Promise.race(executing);
    }
  }
  return Promise.all(results);
}

// 用法：最多 3 个并发请求
asyncPool(3, urls, (url) => fetch(url));
```

---

## 18. JSONP

```javascript
function jsonp(url, callbackName) {
  return new Promise((resolve, reject) => {
    const script = document.createElement("script");
    const cb = callbackName || "jsonp_" + Date.now();

    window[cb] = (data) => {
      resolve(data);
      delete window[cb];
      document.body.removeChild(script);
    };

    script.src = `${url}?callback=${cb}`;
    script.onerror = () => reject(new Error("JSONP failed"));
    document.body.appendChild(script);
  });
}
```

---

## 速查表

| 题目 | 核心思路 | 复杂度 |
|------|----------|--------|
| debounce | setTimeout + clearTimeout | O(1) |
| throttle | 记录 lastTime 比较 | O(1) |
| deepClone | 递归 + WeakMap 处理循环引用 | O(n) |
| new | Object.create + apply | O(1) |
| instanceof | 沿原型链查找 | O(h) |
| call/apply/bind | Symbol 临时属性 | O(1) |
| Promise | 状态机 + 回调队列 | — |
| Promise.all | 计数器 + Promise.resolve | O(n) |
| flat | reduce + 递归 / 栈迭代 | O(n) |
| 去重 | Set / filter+indexOf | O(n) |
| curry | 参数收集，够了就调用 | O(n) |
| EventEmitter | Map 存事件→回调列表 | O(1) |
| LRU | Map 按插入顺序 | O(1) |
| 模板解析 | replace + 正则 | O(n) |
| deepMerge | 递归合并对象 | O(n) |
| asyncPool | Promise.race 控制并发 | O(n) |
| JSONP | script 标签 + 全局回调 | — |
