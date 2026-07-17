# JavaScript 面试高频考点（精简版）

> 只保留面试最常问的知识点，快速过一遍就能应对大部分 JS 面试题。

---

## 1. var / let / const（必考）

| 特性 | var | let | const |
|------|-----|-----|-------|
| 作用域 | 函数作用域 | 块级作用域 | 块级作用域 |
| 变量提升 | ✅ 提升（值为 undefined） | ✅ 提升（但存在暂时性死区） | ✅ 提升（暂时性死区） |
| 重复声明 | ✅ 允许 | ❌ 报错 | ❌ 报错 |
| 重新赋值 | ✅ | ✅ | ❌ |

```javascript
// var 的坑：没有块级作用域
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// 输出: 3, 3, 3（不是 0, 1, 2）

// let 修复了这个问题
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// 输出: 0, 1, 2

// const 不是完全不可变——对象/数组的内容可以改
const obj = { a: 1 };
obj.a = 2;        // ✅ 可以
obj.b = 3;        // ✅ 可以
// obj = {};       // ❌ 不能重新赋值
```

---

## 2. 数据类型

```javascript
// 原始类型（7 个）—— 不可变，按值访问
typeof "hello"       // "string"
typeof 42            // "number"
typeof true          // "boolean"
typeof undefined     // "undefined"
typeof null          // "object" ← 历史 bug，实际是原始类型
typeof Symbol()      // "symbol"
typeof 10n           // "bigint"

// 引用类型 —— 可变，按引用访问
typeof {}            // "object"
typeof []            // "object" ← 数组也是对象
typeof function(){}  // "function"

// 判断数组
Array.isArray([1, 2])  // true
[].length === 0          // 判断空数组

// 判断 null
value === null

// 判断 undefined
typeof value === "undefined"
```

---

## 3. 闭包（必考）

闭包：函数能够记住并访问它定义时的词法作用域，即使在其外部执行。

```javascript
// 经典闭：计数器
function createCounter() {
  let count = 0;
  return {
    increment() { return ++count; },
    getCount() { return count; }
  };
}
const counter = createCounter();
counter.increment();  // 1
counter.increment();  // 2
counter.getCount();   // 2
// count 变量被"闭包"住了，外部无法直接访问

// 闭包的常见应用：函数工厂
function multiplier(factor) {
  return (number) => number * factor;
}
const double = multiplier(2);
const triple = multiplier(3);
double(5);   // 10
triple(5);   // 15

// 面试陷阱题
function buildFunctions() {
  const funcs = [];
  for (var i = 0; i < 3; i++) {
    funcs.push(function() { return i; });
  }
  return funcs;
}
const fns = buildFunctions();
fns[0]();  // 3（不是 0！）
fns[1]();  // 3
fns[2]();  // 3

// 修复方法1：用 let
for (let i = 0; i < 3; i++) { ... }

// 修复方法2：用 IIFE 创建新作用域
for (var i = 0; i < 3; i++) {
  (function(j) {
    funcs.push(function() { return j; });
  })(i);
}
```

---

## 4. this 指向（必考）

```javascript
// 规则1：默认绑定 —— 全局/普通函数调用
function foo() { console.log(this); }
foo();  // 非严格模式: window；严格模式: undefined

// 规则2：隐式绑定 —— 对象方法调用
const obj = {
  name: "Lei",
  greet() { console.log(`Hi, ${this.name}`); }
};
obj.greet();  // "Hi, Lei"

// 规则3：显式绑定
const greet2 = obj.greet;
greet2.call({ name: "Sun" });   // "Hi, Sun"
greet2.apply({ name: "Sun" });  // 同上，apply 接收数组参数

// 规则4：new 绑定 —— this 指向新创建的实例
function Person(name) {
  this.name = name;
}
const p = new Person("Lei");  // this → p

// 箭头函数：没有自己的 this，继承外层
const obj2 = {
  name: "Lei",
  greet: () => { console.log(this.name); },  // ❌ this 是外层（window）
  greetGood() {
    const inner = () => { console.log(this.name); };  // ✅ this 是 obj2
    inner();
  }
};

// 优先级：new > 显式 > 隐式 > 默认
```

---

## 5. 原型与继承（高频）

```javascript
// 每个函数都有 prototype 属性
// 每个对象都有 __proto__（隐式原型）
// 对象.__proto__ === 构造函数.prototype

function Animal(name) {
  this.name = name;
}
Animal.prototype.speak = function() {
  return `${this.name} makes a sound`;
};

const dog = new Animal("Rex");
dog.speak();  // "Rex makes a sound"
// 查找链：dog → Animal.prototype → Object.prototype → null

// ES6 class 语法（本质还是原型继承）
class Animal2 {
  constructor(name) {
    this.name = name;
  }
  speak() {
    return `${this.name} makes a sound`;
  }
}

class Dog extends Animal2 {
  speak() {
    return `${this.name} barks`;
  }
}
const d = new Dog("Rex");
d.speak();  // "Rex barks"

// 判断原型关系
dog instanceof Animal;           // true
Object.getPrototypeOf(dog) === Animal.prototype;  // true
Animal.prototype.isPrototypeOf(dog);              // true

// hasOwnProperty —— 区分自身属性和原型属性
dog.hasOwnProperty("name");     // true（自身）
dog.hasOwnProperty("speak");    // false（原型上）
```

---

## 6. 事件循环 Event Loop（必考）

```javascript
// 执行顺序：同步代码 → 微任务 → 宏任务

console.log("1");                    // 同步

setTimeout(() => {
  console.log("2");                  // 宏任务
}, 0);

Promise.resolve().then(() => {
  console.log("3");                  // 微任务
});

console.log("4");                    // 同步

// 输出顺序: 1, 4, 3, 2

// 微任务（microtask）：Promise.then/catch/finally, queueMicrotask, MutationObserver
// 宏任务（macrotask）：setTimeout, setInterval, I/O, UI rendering

// 微任务在当前宏任务结束后立即全部执行
// 然后执行下一个宏任务
```

---

## 7. Promise 与 async/await（必考）

```javascript
// Promise 三种状态：pending → fulfilled / rejected

const p = new Promise((resolve, reject) => {
  setTimeout(() => resolve("done"), 1000);
});
p.then(val => console.log(val));

// 链式调用
fetch("/api/user")
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.error(err))
  .finally(() => console.log("done"));

// Promise 并发控制
Promise.all([p1, p2, p3]);      // 全部成功才成功，一个失败即失败
Promise.allSettled([p1, p2]);   // 全部完成（不管成败），返回每个结果
Promise.race([p1, p2]);         // 第一个完成的结果（不管成败）
Promise.any([p1, p2]);          // 第一个成功的结果（全失败才失败）

// async/await —— Promise 的语法糖
async function getUser() {
  try {
    const res = await fetch("/api/user");
    const data = await res.json();
    return data;
  } catch (err) {
    console.error(err);
  }
}

// 串行 vs 并行
async function serial() {
  const a = await task1();   // 等 task1 完成
  const b = await task2();   // 再等 task2
}

async function parallel() {
  const [a, b] = await Promise.all([task1(), task2()]);  // 并发
}
```

---

## 8. ES6+ 常用特性

```javascript
// 解构赋值
const { name, age, email = "default@mail.com" } = user;
const [first, , third] = [1, 2, 3];

// 展开运算符
const merged = { ...obj1, ...obj2 };
const combined = [...arr1, ...arr2];

// 可选链 + 空值合并
const city = user?.address?.city ?? "Unknown";

// 模板字符串
const msg = `Hello, ${name}! You are ${age > 18 ? "adult" : "minor"}.`;

// 简写对象
const name = "Lei";
const obj = { name };  // 等价于 { name: name }

// 计算属性名
const key = "email";
const obj2 = { [key]: "lei@test.com" };

// 逻辑赋值运算符（ES2021）
a ||= b;    // a 为假值时赋值
a ??= b;    // a 为 null/undefined 时赋值
a &&= b;    // a 为真值时赋值

// Array.at()（ES2022）
const arr = [1, 2, 3];
arr.at(-1);  // 3（倒数第一个）
```

---

## 9. 数组高频方法

```javascript
const nums = [1, 2, 3, 4, 5];

// 不改变原数组（纯函数）
nums.map(x => x * 2);          // [2, 4, 6, 8, 10]
nums.filter(x => x > 3);       // [4, 5]
nums.reduce((sum, x) => sum + x, 0);  // 15
nums.find(x => x > 3);         // 4
nums.findIndex(x => x > 3);    // 3
nums.some(x => x > 3);         // true
nums.every(x => x > 0);        // true
nums.flat(2);                  // 展平嵌套数组
nums.flatMap(x => [x, x * 2]); // 先 map 再 flat 一层

// 改变原数组
nums.push(6);       // 末尾添加
nums.pop();         // 末尾删除
nums.unshift(0);    // 开头添加
nums.shift();       // 开头删除
nums.splice(1, 2);  // 从索引1删除2个元素
nums.sort((a, b) => a - b);  // 排序
nums.reverse();     // 反转

// 面试常考：去重
const unique = [...new Set([1, 2, 2, 3, 3])];  // [1, 2, 3]

// 面试常考：扁平化
function flatten(arr) {
  return arr.reduce((acc, val) =>
    Array.isArray(val) ? acc.concat(flatten(val)) : acc.concat(val), []);
}
flatten([1, [2, [3, [4]]]]);  // [1, 2, 3, 4]
// 或者直接用 arr.flat(Infinity)
```

---

## 10. 深拷贝 vs 浅拷贝

```javascript
const original = { a: 1, b: { c: 2 } };

// 浅拷贝
const shallow1 = { ...original };
const shallow2 = Object.assign({}, original);
shallow1.b.c = 99;
console.log(original.b.c);  // 99 ← 原对象也变了

// 深拷贝
const deep = structuredClone(original);  // 现代浏览器原生支持
deep.b.c = 100;
console.log(original.b.c);  // 99 ← 原对象不受影响

// 手动实现简易深拷贝
function deepClone(obj, map = new WeakMap()) {
  if (obj === null || typeof obj !== "object") return obj;
  if (map.has(obj)) return map.get(obj);  // 处理循环引用

  const clone = Array.isArray(obj) ? [] : {};
  map.set(obj, clone);

  for (const key in obj) {
    if (obj.hasOwnProperty(key)) {
      clone[key] = deepClone(obj[key], map);
    }
  }
  return clone;
}
```

---

## 11. 防抖与节流（高频手写题）

```javascript
// 防抖（debounce）：停止触发后等待 delay 才执行
function debounce(fn, delay) {
  let timer = null;
  return function(...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}
// 应用场景：搜索框输入（停止输入后才发请求）

// 节流（throttle）：固定时间内只执行一次
function throttle(fn, interval) {
  let lastTime = 0;
  return function(...args) {
    const now = Date.now();
    if (now - lastTime >= interval) {
      lastTime = now;
      fn.apply(this, args);
    }
  };
}
// 应用场景：滚动事件处理（控制执行频率）
```

---

## 12. 一句话速记

| 考点 | 要点 |
|------|------|
| var/let/const | let/const 块级作用域，const 不能重新赋值 |
| 闭包 | 函数记住定义时的作用域，即使在外层执行 |
| this | 箭头函数没有自己的 this，继承外层 |
| 原型链 | 对象.__proto__ === 构造函数.prototype |
| 事件循环 | 同步 → 微任务 → 宏任务 |
| Promise | 三种状态，async/await 是语法糖 |
| 深/浅拷贝 | structuredClone 或手动递归 |
| 防抖节流 | 防抖等停止，节流控频率 |
| 解构赋值 | 对象/数组都可以解构 |
| 可选链 | `?.` 安全访问深层属性 |
