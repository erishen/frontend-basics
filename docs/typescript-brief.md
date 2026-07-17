# TypeScript 面试高频考点（精简版）

> 只保留面试最常问的知识点，快速过一遍就能应对大部分 TS 面试题。

---

## 1. 基础类型速查

```typescript
let s: string = "hi";
let n: number = 42;
let b: boolean = true;
let arr: number[] = [1, 2];
let tuple: [string, number] = ["age", 30];
let lit: "up" | "down" = "up";           // 字面量类型
let union: string | number = "x";         // 联合类型
```

---

## 2. any / unknown / never / void（必考）

| 类型 | 含义 | 使用场景 |
|------|------|----------|
| `any` | 放弃类型检查 | 尽量避免 |
| `unknown` | 类型安全的 any，使用前必须收窄 | 替代 any |
| `void` | 函数无返回值 | 函数返回类型 |
| `never` | 永远不会返回 | 抛异常/死循环/穷尽检查 |

```typescript
// unknown 必须先收窄才能用
let y: unknown = "hello";
// y.toUpperCase();  // ❌
if (typeof y === "string") {
  y.toUpperCase();   // ✅
}

// never 用于穷尽检查
type Shape = "circle" | "square";
function area(s: Shape): number {
  switch (s) {
    case "circle": return 1;
    case "square": return 2;
    default:
      const _exhaustive: never = s;  // 漏掉 case 会报错
      return _exhaustive;
  }
}
```

---

## 3. interface vs type（最高频）

| 特性 | interface | type |
|------|-----------|------|
| 声明合并 | ✅ 同名自动合并 | ❌ |
| 扩展方式 | `extends` | `&` |
| 联合类型 | ❌ | ✅ |
| 映射类型 | ❌ | ✅ |
| 推荐场景 | 对象结构、公共 API | 联合类型、复杂类型运算 |

```typescript
// 声明合并 —— interface 独有
interface User { name: string }
interface User { age: number }
const u: User = { name: "Lei", age: 30 };  // 自动合并

// type 可以做联合类型，interface 不行
type Status = "pending" | "success" | "error";
```

**结论：** 对象结构用 interface，其他用 type。

---

## 4. 泛型基础（必考）

```typescript
// 泛型函数
function identity<T>(arg: T): T { return arg; }
identity<string>("hi");   // 显式指定
identity(42);             // 自动推断 T = number

// 泛型约束
interface HasLength { length: number }
function logLen<T extends HasLength>(x: T): T {
  console.log(x.length);
  return x;
}
logLen("hello");    // ✅
// logLen(123);     // ❌ number 没有 length

// 泛型 + keyof
function getProp<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}
const user = { name: "Lei", age: 30 };
getProp(user, "name");   // ✅ 返回 string
// getProp(user, "x");   // ❌
```

---

## 5. 内置工具类型（最常用 6 个）

```typescript
interface User { name: string; age: number; email: string }

// Partial —— 全部变可选（用于更新）
type Update = Partial<User>;
// { name?: string; age?: number; email?: string }

// Required —— 全部变必填
type Full = Required<Partial<User>>;

// Pick —— 选取几个属性
type Basic = Pick<User, "name" | "email">;
// { name: string; email: string }

// Omit —— 排除几个属性
type NoEmail = Omit<User, "email">;
// { name: string; age: number }

// Record —— 键值对类型
type Dict = Record<string, number>;     // { [key: string]: number }

// ReturnType —— 函数返回值类型
function getUser() { return { name: "Lei", age: 30 } }
type UserReturn = ReturnType<typeof getUser>;
// { name: string; age: number }
```

---

## 6. 类型守卫（必考）

四种收窄联合类型的方式：

```typescript
// 1. typeof —— 原始类型
function process(x: string | number) {
  if (typeof x === "string") return x.toUpperCase();
  return x.toFixed(2);
}

// 2. in —— 对象属性
interface Fish { swim(): void }
interface Bird { fly(): void }
function move(a: Fish | Bird) {
  if ("swim" in a) a.swim();
  else a.fly();
}

// 3. instanceof —— 类实例
function speak(pet: Dog | Cat) {
  if (pet instanceof Dog) pet.bark();
  else pet.meow();
}

// 4. 自定义谓词 (is) —— 最灵活
interface Circle { kind: "circle"; radius: number }
interface Square { kind: "square"; side: number }
type Shape = Circle | Square;

function isCircle(s: Shape): s is Circle {
  return s.kind === "circle";
}
function area(s: Shape): number {
  if (isCircle(s)) return Math.PI * s.radius ** 2;
  return s.side ** 2;
}
```

---

## 7. 函数重载

```typescript
function parse(s: string): number;
function parse(s: number): string;
function parse(s: string | number): string | number {
  if (typeof s === "string") return parseInt(s, 10);
  return String(s);
}
const n = parse("123");   // number
const str = parse(123);   // string
```

---

## 8. satisfies（TS 4.9+）

验证类型但不丢失推断信息：

```typescript
// as 会丢失具体类型
const p1 = { red: [255, 0, 0] } as Record<string, string | number[]>;
// p1.red → string | number[]

// satisfies 保留具体类型
const p2 = { red: [255, 0, 0] } satisfies Record<string, string | number[]>;
// p2.red → number[]  ← 保留了！
```

---

## 9. 高频手写题

```typescript
// 手写 DeepReadonly
type DeepReadonly<T> = {
  readonly [K in keyof T]: T[K] extends object
    ? T[K] extends Function ? T[K] : DeepReadonly<T[K]>
    : T[K];
};

// 手写 Pick
type MyPick<T, K extends keyof T> = { [P in K]: T[P] };

// 手写 Awaited（递归解包 Promise）
type MyAwaited<T> = T extends Promise<infer U>
  ? U extends Promise<any> ? MyAwaited<U> : U
  : T;

// 手写 TupleToUnion
type ToUnion<T extends readonly any[]> = T[number];
type X = ToUnion<[string, number, boolean]>;  // string | number | boolean
```

---

## 10. 一句话速记

| 考点 | 要点 |
|------|------|
| any vs unknown | unknown 安全，必须先收窄 |
| never | 永不返回、穷尽检查 |
| interface vs type | 对象用 interface，联合/运算用 type |
| 泛型约束 | `extends` 限制范围 |
| 条件类型 | `T extends U ? X : Y` + `infer` |
| 类型守卫 | typeof / in / instanceof / is |
| satisfies | 验证但不丢失推断 |
| 结构化类型 | 看结构不看名字 |
| 声明合并 | interface 独有，同名自动合并 |
| 品牌类型 | `T & { __brand: B }` 模拟名义类型 |
