# TypeScript 面试基础知识

> 全面覆盖 TypeScript 核心知识点，每个概念配可运行代码示例，适合面试快速复习。

---

## 1. 基本类型

TypeScript 在 JavaScript 基础上增加了静态类型系统。先掌握基础类型注解。

```typescript
// 原始类型
let name: string = "Lei";
let age: number = 30;
let isActive: boolean = true;
let nothing: null = null;
let notDefined: undefined = undefined;

// symbol & bigint
let sym: symbol = Symbol("id");
let big: bigint = 9007199254740991n;

// 数组
let nums: number[] = [1, 2, 3];
let strs: Array<string> = ["a", "b"];   // 泛型写法，等价

// 元组 (Tuple)
let pair: [string, number] = ["age", 30];
// 可选元组元素 (TS 4.0+)
let opt: [string, number?] = ["x"];

// 字面量类型
let direction: "up" | "down" = "up";
let code: 200 | 404 = 200;
```

---

## 2. 类型注解 vs 类型推断

TypeScript 编译器会自动推断类型，大多数情况下无需显式注解。

```typescript
// 类型推断 —— 不需要写 :string，TS 自动推断
let msg = "hello";  // 推断为 string
// msg = 123;        // ❌ Error: Type 'number' is not assignable to type 'string'

// 需要显式注解的场景：
// 1. 变量声明时未赋值
let result: string;
result = "done";

// 2. 函数返回值推断复杂时，显式标注更清晰
function calc(a: number, b: number): number {
  return a + b;
}

// 3. 联合类型需要收窄
let id: string | number;
id = "abc";
id = 123;
// id = true;  // ❌
```

---

## 3. any / unknown / never / void

这四个特殊类型是高频考点，务必分清。

```typescript
// any —— 放弃类型检查，任意操作都合法（尽量避免）
let x: any = "hello";
x = 123;
x.foo.bar();   // ✅ 编译通过，但运行时可能崩溃

// unknown —— 类型安全的 any，使用前必须收窄
let y: unknown = "hello";
// y.foo();    // ❌ Error: Object is of type 'unknown'
if (typeof y === "string") {
  console.log(y.toUpperCase());  // ✅ 收窄后可以使用
}
// 类型断言
const len = (y as string).length;

// void —— 函数没有返回值
function log(msg: string): void {
  console.log(msg);
  // 没有 return，或 return undefined
}

// never —— 永远不会返回的类型
// 场景1：永远抛异常的函数
function throwError(msg: string): never {
  throw new Error(msg);
}

// 场景2：无限循环
function infiniteLoop(): never {
  while (true) {}
}

// 场景3：穷尽检查（exhaustive check）
type Shape = "circle" | "square";
function getArea(s: Shape): number {
  switch (s) {
    case "circle": return Math.PI * 1 ** 2;
    case "square": return 1 ** 2;
    default:
      const _exhaustive: never = s;  // 若漏掉某 case，这里会报错
      return _exhaustive;
  }
}
```

**any vs unknown 核心区别：**

| 特性 | any | unknown |
|------|-----|---------|
| 类型安全 | 无 | 有 |
| 直接使用属性/方法 | 可以（危险） | 必须先收窄 |
| 赋值给其他类型 | 可以 | 只接受 unknown/any |
| 推荐程度 | 尽量避免 | 安全替代 any |

---

## 4. 接口 (Interface)

接口是 TypeScript 最核心的结构类型定义方式。

```typescript
// 基本接口
interface User {
  name: string;
  age: number;
  email?: string;          // 可选属性
  readonly id: number;     // 只读属性
}

const user: User = {
  id: 1,
  name: "Lei",
  age: 30,
  // email 可以省略
};
// user.id = 2;   // ❌ Cannot assign to 'id' because it is a read-only property

// 接口继承
interface Animal {
  name: string;
}
interface Dog extends Animal {
  breed: string;
}
const dog: Dog = { name: "Rex", breed: "Husky" };

// 多继承
interface A { a: string }
interface B { b: number }
interface C extends A, B { c: boolean }
const obj: C = { a: "x", b: 1, c: true };

// 索引签名
interface Dictionary {
  [key: string]: number;   // 任意 string key，值为 number
}
const dict: Dictionary = { a: 1, b: 2 };

// 混合索引签名（数字索引）
interface StringArray {
  [index: number]: string;  // 数组形式
}
const arr: StringArray = ["a", "b", "c"];

// 函数类型接口
interface MathFunc {
  (a: number, b: number): number;
}
const add: MathFunc = (a, b) => a + b;

// 接口描述类（构造函数签名）
interface ClockConstructor {
  new (hour: number, minute: number): ClockInterface;
}
interface ClockInterface {
  tick(): void;
}
```

---

## 5. 类型别名 (Type Alias)

```typescript
// 基本类型别名
type ID = string | number;
type Point = { x: number; y: number };

// 联合类型
type Status = "pending" | "success" | "error";
type Result<T> = { ok: true; data: T } | { ok: false; error: string };

// 元组类型别名
type Pair = [string, number];
```

---

## 6. type vs interface（高频面试题）

| 特性 | interface | type |
|------|-----------|------|
| 声明合并 | ✅ 支持（同名自动合并） | ❌ 不支持 |
| 扩展方式 | `extends` | `&` 交叉类型 |
| 计算属性 | ❌ | ✅ |
| 映射类型 | ❌ | ✅ |
| 联合/交叉类型 | ❌ 只能描述对象形状 | ✅ 任意类型组合 |
| 实现(implements) | ✅ class implements | ✅ 也可以（对象类型） |
| 推荐场景 | 公共 API、对象结构 | 复杂类型运算、联合类型 |

```typescript
// 声明合并 —— interface 独有
interface User { name: string }
interface User { age: number }
// 自动合并为 { name: string; age: number }
const u: User = { name: "Lei", age: 30 };

// type 不能声明合并
// type User = { name: string };
// type User = { age: number };  // ❌ Duplicate identifier

// type 可以做 interface 做不到的事
type StringOrNumber = string | number;
type Pair<T> = [T, T];
type Keys = keyof SomeObject;
```

**面试建议：** 对象结构优先用 `interface`，需要联合类型、映射类型、工具类型时用 `type`。

---

## 7. 联合类型与交叉类型

```typescript
// 联合类型 (Union)：A 或 B
type StringOrNum = string | number;
let val: StringOrNum = "hello";
val = 123;  // ✅

// 联合类型的属性访问：只能访问共有成员
function len(x: string | number) {
  // x.toString();  // ✅ 共有方法
  // x.length;      // ❌ number 没有 length
}

// 交叉类型 (Intersection)：A 且 B
type HasName = { name: string };
type HasAge = { age: number };
type Person = HasName & HasAge;
const p: Person = { name: "Lei", age: 30 };

// 合并同名属性会取交集（never）
type A = { x: string };
type B = { x: number };
type C = A & B;  // C.x 的类型是 string & number = never
```

---

## 8. 函数类型

```typescript
// 基本函数类型
function greet(name: string): string {
  return `Hello, ${name}`;
}

// 箭头函数类型
const add = (a: number, b: number): number => a + b;

// 可选参数 & 默认参数
function buildName(first: string, last?: string, prefix = "Mr."): string {
  return `${prefix} ${first} ${last ?? ""}`;
}
buildName("Lei");            // "Mr. Lei "
buildName("Lei", "Sun");     // "Mr. Lei Sun"

// 剩余参数
function sum(...nums: number[]): number {
  return nums.reduce((a, b) => a + b, 0);
}

// 函数重载（overload）—— 面试常考
function parse(s: string): number;
function parse(s: number): string;
function parse(s: string | number): string | number {
  if (typeof s === "string") return parseInt(s, 10);
  return String(s);
}
const n = parse("123");   // 推断为 number
const str = parse(123);   // 推断为 string

// this 参数类型
interface Button {
  label: string;
  onClick(this: Button): void;
}

// 回调函数类型
function fetchData(callback: (data: string, error?: Error) => void): void {
  callback("data");
}
```

---

## 9. 类 (Class)

```typescript
// 基本类 + 访问修饰符
class Animal {
  // public 默认，可省略
  public name: string;
  // private 只能在类内部访问
  private age: number;
  // protected 子类可访问
  protected species: string;

  constructor(name: string, age: number, species: string) {
    this.name = name;
    this.age = age;
    this.species = species;
  }

  // 参数属性简写（推荐）
  // constructor(public name: string, private age: number) {}

  get info(): string {
    return `${this.name}, ${this.age} years old`;
  }
}

// 继承
class Dog extends Animal {
  breed: string;

  constructor(name: string, age: number, breed: string) {
    super(name, age, "Canine");  // 必须先调用 super
    this.breed = breed;
  }

  bark(): void {
    console.log("Woof!");
  }
}

// 抽象类 —— 不能实例化，只能被继承
abstract class Shape {
  abstract area(): number;   // 抽象方法，子类必须实现

  describe(): string {
    return `Area is ${this.area()}`;
  }
}

class Circle extends Shape {
  constructor(private radius: number) {
    super();
  }
  area(): number {
    return Math.PI * this.radius ** 2;
  }
}

// 实现接口
interface Printable {
  print(): void;
}

class Report implements Printable {
  print(): void {
    console.log("Printing report...");
  }
}

// 静态成员
class Counter {
  static count = 0;
  static increment(): void {
    Counter.count++;
  }
}
Counter.increment();
console.log(Counter.count);  // 1
```

---

## 10. 泛型 (Generics)

泛型是 TypeScript 类型系统的核心高级特性，面试必考。

```typescript
// 泛型函数
function identity<T>(arg: T): T {
  return arg;
}
const a = identity<string>("hello");  // 显式指定
const b = identity(42);               // 自动推断 T = number

// 泛型接口
interface ApiResponse<T> {
  code: number;
  data: T;
  message: string;
}
type UserResponse = ApiResponse<{ name: string; age: number }>;

// 泛型类
class Stack<T> {
  private items: T[] = [];

  push(item: T): void {
    this.items.push(item);
  }

  pop(): T | undefined {
    return this.items.pop();
  }

  peek(): T | undefined {
    return this.items[this.items.length - 1];
  }
}

const numStack = new Stack<number>();
numStack.push(1);
numStack.push(2);
const top = numStack.pop();  // number | undefined

// 泛型约束 (constraint)
interface HasLength {
  length: number;
}

function logLength<T extends HasLength>(arg: T): T {
  console.log(arg.length);  // ✅ 约束后保证有 length
  return arg;
}
logLength("hello");     // ✅ string 有 length
logLength([1, 2, 3]);   // ✅ array 有 length
// logLength(123);       // ❌ number 没有 length

// 泛型约束 + keyof
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}
const user = { name: "Lei", age: 30 };
getProperty(user, "name");   // ✅ 返回 string
// getProperty(user, "foo"); // ❌ "foo" 不在 user 的 key 中

// 泛型默认值
type Container<T = string> = { value: T };
const c1: Container = { value: "hello" };   // T 默认 string
const c2: Container<number> = { value: 42 }; // 显式指定

// 多泛型参数
function zip<A, B>(a: A[], b: B[]): [A, B][] {
  return a.map((item, i) => [item, b[i]]);
}
const zipped = zip(["a", "b"], [1, 2]);  // [string, number][]
```

---

## 11. 内置工具类型 (Utility Types)

TypeScript 提供大量内置工具类型，面试和实际开发都高频使用。

```typescript
interface User {
  name: string;
  age: number;
  email: string;
  address: string;
}

// Partial<T> —— 所有属性变为可选
// 用于更新场景，只传需要修改的字段
type UpdateUser = Partial<User>;
// { name?: string; age?: number; email?: string; address?: string }

// Required<T> —— 所有属性变为必填
type FullUser = Required<Partial<User>>;
// { name: string; age: number; email: string; address: string }

// Readonly<T> —— 所有属性只读
type FrozenUser = Readonly<User>;
// const fu: FrozenUser = { ... }; fu.name = "x"; ❌

// Pick<T, K> —— 从 T 中选取 K 属性
type UserBasic = Pick<User, "name" | "email">;
// { name: string; email: string }

// Omit<T, K> —— 从 T 中排除 K 属性
type UserWithoutAddr = Omit<User, "address">;
// { name: string; age: number; email: string }

// Record<K, T> —— 构造键为 K、值为 T 的对象类型
type UserMap = Record<string, User>;
// { [key: string]: User }

type Weekday = "Mon" | "Tue" | "Wed" | "Thu" | "Fri";
type Schedule = Record<Weekday, string>;
// { Mon: string; Tue: string; ... }

// Exclude<T, U> —— 从联合类型 T 中排除 U
type T1 = Exclude<"a" | "b" | "c", "a" | "c">;  // "b"

// Extract<T, U> —— 从联合类型 T 中提取 U
type T2 = Extract<"a" | "b" | "c", "a" | "c">;  // "a" | "c"

// NonNullable<T> —— 从 T 中排除 null 和 undefined
type T3 = NonNullable<string | number | null | undefined>;
// string | number

// ReturnType<T> —— 获取函数返回值类型
function getUser() {
  return { name: "Lei", age: 30 };
}
type UserReturn = ReturnType<typeof getUser>;
// { name: string; age: number }

// Parameters<T> —— 获取函数参数类型（元组）
function createUser(name: string, age: number): User {
  return { name, age, email: "", address: "" };
}
type CreateUserParams = Parameters<typeof createUser>;
// [string, number]

// InstanceType<T> —— 获取类的实例类型
class MyClass {
  value = 42;
}
type MyInstance = InstanceType<typeof MyClass>;
// MyClass

// Awaited<T> —— 解包 Promise 类型 (TS 4.5+)
type T4 = Awaited<Promise<Promise<string>>>;  // string
```

---

## 12. 高级类型

### 12.1 条件类型 (Conditional Types)

```typescript
// 基本语法：T extends U ? X : Y
type IsString<T> = T extends string ? "yes" : "no";
type A = IsString<string>;   // "yes"
type B = IsString<number>;   // "no"

// 分布式条件类型（对联合类型逐项应用）
type ToArray<T> = T extends any ? T[] : never;
type C = ToArray<string | number>;  // string[] | number[]

// 非分布式（用 [T] 包裹）
type ToArrayNonDist<T> = [T] extends [any] ? T[] : never;
type D = ToArrayNonDist<string | number>;  // (string | number)[]

// 实际应用：提取 Promise 内部类型
type UnwrapPromise<T> = T extends Promise<infer U> ? U : T;
type E = UnwrapPromise<Promise<string>>;  // string
type F = UnwrapPromise<number>;           // number

// infer 关键字 —— 在条件类型中推断类型变量
type ElementType<T> = T extends (infer U)[] ? U : T;
type G = ElementType<string[]>;   // string
type H = ElementType<number>;     // number

// 提取函数参数类型
type FirstParam<T> = T extends (arg: infer P, ...rest: any[]) => any ? P : never;
type I = FirstParam<(x: string, y: number) => void>;  // string
```

### 12.2 映射类型 (Mapped Types)

```typescript
// 基本映射类型
type Readonly2<T> = {
  readonly [K in keyof T]: T[K];
};

type Optional<T> = {
  [K in keyof T]?: T[K];
};

// 键重映射 (TS 4.1+)
type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};
type UserGetters = Getters<{ name: string; age: number }>;
// { getName: () => string; getAge: () => number }

// 去除可选标记
type Concrete<T> = {
  [K in keyof T]-?: T[K];
};
type ConcreteUser = Concrete<{ name?: string; age?: number }>;
// { name: string; age: number }  // 全部变为必填
```

### 12.3 模板字面量类型 (Template Literal Types, TS 4.1+)

```typescript
type EventName = "click" | "focus" | "blur";
type Handler = `on${Capitalize<EventName>}`;
// "onClick" | "onFocus" | "onBlur"

// 字符串操作类型
type Lower = Lowercase<"HELLO">;     // "hello"
type Upper = Uppercase<"hello">;     // "HELLO"
type Cap = Capitalize<"hello">;      // "Hello"
type Uncap = Uncapitalize<"Hello">;  // "hello"

// 组合使用
type CSSProperty = "margin" | "padding";
type CSSDirection = "top" | "right" | "bottom" | "left";
type CSSValue = `${CSSProperty}-${CSSDirection}`;
// "margin-top" | "margin-right" | ... | "padding-left"
```

---

## 13. 类型守卫 (Type Guards)

类型守卫是收窄联合类型的关键手段，面试常考。

```typescript
// typeof 守卫
function process(val: string | number) {
  if (typeof val === "string") {
    return val.toUpperCase();  // 这里 val 是 string
  }
  return val.toFixed(2);       // 这里 val 是 number
}

// in 守卫
interface Fish { swim(): void }
interface Bird { fly(): void }

function move(animal: Fish | Bird) {
  if ("swim" in animal) {
    animal.swim();   // Fish
  } else {
    animal.fly();    // Bird
  }
}

// instanceof 守卫
class Dog { bark() { console.log("woof"); } }
class Cat { meow() { console.log("meow"); } }

function speak(pet: Dog | Cat) {
  if (pet instanceof Dog) {
    pet.bark();
  } else {
    pet.meow();
  }
}

// 自定义类型守卫 (type predicate)
interface Circle { kind: "circle"; radius: number }
interface Square { kind: "square"; side: number }
type Shape2 = Circle | Square;

function isCircle(s: Shape2): s is Circle {
  return s.kind === "circle";
}

function getArea2(s: Shape2): number {
  if (isCircle(s)) {
    return Math.PI * s.radius ** 2;  // s 被收窄为 Circle
  }
  return s.side ** 2;
}

// satisfies 操作符 (TS 4.9+)
// 验证类型但不改变推断结果
const palette = {
  red: [255, 0, 0],
  green: "#00ff00",
} satisfies Record<string, string | number[]>;

// palette.red 推断为 number[]（而非 string | number[]）
// palette.red.toUpperCase();  // ❌ 但类型检查仍生效
// palette.unknown = 1;        // ❌ 不在 Record 的 key 约束内则不报错（satisfies 不限制额外属性）
```

---

## 14. 枚举 (Enum)

```typescript
// 数字枚举
enum Direction {
  Up,       // 0
  Down,     // 1
  Left,     // 2
  Right,    // 3
}
const dir: Direction = Direction.Up;

// 带初始值的数字枚举
enum HttpStatus {
  OK = 200,
  NotFound = 404,
  ServerError = 500,
}

// 字符串枚举
enum Color {
  Red = "RED",
  Green = "GREEN",
  Blue = "BLUE",
}

// 常量枚举（编译时内联，无运行时对象）
const enum LogLevel {
  Debug = 0,
  Info = 1,
  Warn = 2,
  Error = 3,
}
console.log(LogLevel.Info);  // 编译为 console.log(1)

// 枚举的反向映射（仅数字枚举）
enum Num { A = 1 }
Num["A"];     // 1
Num[1];       // "A"  —— 反向映射

// 面试建议：现代 TS 更推荐用联合字面量代替枚举
type Status2 = "active" | "inactive" | "pending";
// 优点：更轻量、tree-shakable、无运行时开销
```

---

## 15. 类型断言与类型兼容

```typescript
// as 断言
const someValue: unknown = "hello";
const strLen = (someValue as string).length;

// 双重断言（绕过编译检查，慎用）
const el = document.getElementById("app") as unknown as HTMLDivElement;

// 非空断言 (!)
function getUser2(): User | null {
  return null;
}
const user2 = getUser2()!;  // 告诉编译器一定不是 null/undefined
// user2.name;  // 运行时若为 null 会崩溃

// 可选链 + 空值合并
const email = user2?.email ?? "default@example.com";

// 类型兼容规则（结构化类型系统）
// TS 用"结构"而非"名义"判断类型兼容
interface Named { name: string }
class Person2 {
  name: string;
  age: number;
}
let n2: Named = new Person2();  // ✅ Person2 有 name 属性，结构兼容

// 函数参数兼容性（逆变 vs 双变）
// TS strictFunctionTypes: true 时，函数参数逆变
type AnimalHandler = (a: Animal) => void;
type DogHandler = (d: Dog) => void;
let ah: AnimalHandler = (a) => console.log(a.name);
// let dh: DogHandler = ah;  // ✅ AnimalHandler 可以赋给 DogHandler（逆变）
```

---

## 16. 声明文件与模块

```typescript
// .d.ts 声明文件 —— 为无类型的 JS 库提供类型
// types/lodash.d.ts
declare module "lodash" {
  export function debounce<T extends (...args: any[]) => any>(
    func: T,
    wait?: number
  ): T;

  export function cloneDeep<T>(value: T): T;
  // ...
}

// 全局类型声明
declare global {
  interface Window {
    myCustomAPI: {
      init(): void;
      getData(): Promise<string>;
    };
  }
}
export {};  // 让文件成为模块

// 模块导入导出类型
// 导出类型
export type { User } from "./types";
export interface Config { ... }

// 仅导入类型（不产生运行时 import）
import type { User } from "./types";

// namespace（旧式，现代代码推荐 ES module）
declare namespace JQuery {
  interface Static {
    (selector: string): any;
  }
}
```

---

## 17. 装饰器 (Decorators, TS 5.0+ 标准版)

```typescript
// 类装饰器
function sealed<T extends { new (...args: any[]): {} }>(constructor: T) {
  Object.seal(constructor);
  Object.seal(constructor.prototype);
}

@sealed
class MyClass2 {
  value = 42;
}

// 方法装饰器
function log(
  target: any,
  propertyKey: string,
  descriptor: PropertyDescriptor
) {
  const original = descriptor.value;
  descriptor.value = function (...args: any[]) {
    console.log(`Calling ${propertyKey} with`, args);
    return original.apply(this, args);
  };
}

class Calculator {
  @log
  add(a: number, b: number): number {
    return a + b;
  }
}

// 属性装饰器
function readonly2(target: any, propertyKey: string) {
  Object.defineProperty(target, propertyKey, {
    writable: false,
  });
}

class Config {
  @readonly2
  apiKey = "secret";
}

// 参数装饰器
function required(
  target: any,
  propertyKey: string,
  parameterIndex: number
) {
  // 标记参数为必填（需配合其他逻辑实现）
}

class UserService {
  createUser(@required name: string, age: number) {
    // ...
  }
}
```

---

## 18. 常见面试题精选

### Q1: 实现一个 DeepReadonly<T>

```typescript
type DeepReadonly<T> = {
  readonly [K in keyof T]: T[K] extends object
    ? T[K] extends Function
      ? T[K]
      : DeepReadonly<T[K]>
    : T[K];
};

interface Nested {
  a: { b: { c: number } };
  fn: () => void;
}
type ReadonlyNested = DeepReadonly<Nested>;
// readonly a: { readonly b: { readonly c: number } }
// fn 保持函数不变
```

### Q2: 实现 Pick 和 Omit

```typescript
// 手写 Pick
type MyPick<T, K extends keyof T> = {
  [P in K]: T[P];
};

// 手写 Omit
type MyOmit<T, K extends keyof any> = {
  [P in Exclude<keyof T, K>]: T[P];
};
```

### Q3: 实现 Awaited（解包 Promise）

```typescript
type MyAwaited<T> = T extends Promise<infer U>
  ? U extends Promise<any>
    ? MyAwaited<U>   // 递归解包嵌套 Promise
    : U
  : T;

type X = MyAwaited<Promise<Promise<string>>>;  // string
```

### Q4: 实现 TupleToUnion

```typescript
type TupleToUnion<T extends readonly any[]> = T[number];
type Y = TupleToUnion<[string, number, boolean]>;  // string | number | boolean
```

### Q5: 实现 Chainable（链式调用类型）

```typescript
type Chainable<T = {}> = {
  set<K extends string, V>(
    key: K,
    value: V
  ): Chainable<T & { [P in K]: V }>;
  get(): T;
};

declare const config: Chainable;
const result = config
  .set("name", "Lei")
  .set("age", 30)
  .get();
// { name: string; age: number }
```

### Q6: type vs interface 怎么选？

**经验法则：**
- 定义对象结构、类的契约 → `interface`（支持声明合并，对消费方友好）
- 联合类型、交叉类型、映射类型、条件类型 → `type`
- 公共 API 库 → `interface`（允许使用者扩展）
- 组件 Props、复杂类型运算 → `type`

### Q7: 什么是结构化类型（Structural Typing）？

TypeScript 比较类型时看"结构"而非"名字"。

```typescript
interface Point2D { x: number; y: number }
interface Vector2D { x: number; y: number }

const p: Point2D = { x: 1, y: 2 };
const v: Vector2D = p;  // ✅ 结构相同，互相兼容
```

### Q8: 什么是声明合并？

同名 `interface` 会自动合并属性，常用于扩展第三方库类型。

```typescript
// 扩展 Express Request
declare global {
  namespace Express {
    interface Request {
      user?: { id: string; role: string };
    }
  }
}
```

### Q9: 什么是协变、逆变、双变、不变？

```typescript
// 协变 (Covariant)：子类型关系保持方向
// Dog extends Animal → Dog[] extends Animal[]

// 逆变 (Contravariant)：子类型关系反转
// Dog extends Animal → (a: Animal) => void extends (a: Dog) => void
// 函数参数是逆变的（strictFunctionTypes 下）

// 双变 (Bivariant)：两个方向都兼容（方法签名默认，不安全）
interface Handler2 {
  (a: Animal): void;  // 方法语法，双变
}

// 不变 (Invariant)：不允许任何方向赋值
// mutable 数组对元素类型是不变的
let dogs: Dog[] = [];
// let animals: Animal[] = dogs;  // ❌ 不安全（可能 push Cat 进去）
```

### Q10: satisfies 和 as 的区别？

```typescript
// as —— 类型断言，改变编译器看到的类型
const palette1 = {
  red: [255, 0, 0],
} as Record<string, string | number[]>;
// palette1.red 的类型是 string | number[]（丢失了数组信息）

// satisfies —— 类型验证，不改变推断结果
const palette2 = {
  red: [255, 0, 0],
} satisfies Record<string, string | number[]>;
// palette2.red 的类型仍然是 number[]（保留了具体信息）
```

---

## 19. tsconfig.json 常用配置

```jsonc
{
  "compilerOptions": {
    // 严格模式（推荐全部开启）
    "strict": true,              // 开启所有严格检查
    "noImplicitAny": true,       // 禁止隐式 any
    "strictNullChecks": true,    // null/undefined 不能赋给其他类型
    "strictFunctionTypes": true, // 函数参数逆变

    // 模块
    "module": "ESNext",
    "moduleResolution": "bundler",  // TS 5.0+
    "target": "ES2020",

    // 输出
    "outDir": "./dist",
    "declaration": true,         // 生成 .d.ts
    "sourceMap": true,

    // 互操作
    "esModuleInterop": true,     // 允许 import x from 'cjs-module'
    "allowSyntheticDefaultImports": true,
    "forceConsistentCasingInFileNames": true,

    // 其他
    "skipLibCheck": true,        // 跳过 .d.ts 检查，加速编译
    "resolveJsonModule": true,   // 允许 import data from './data.json'
    "isolatedModules": true      // 确保每个文件可独立编译（Bundler 需要）
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

---

## 20. 实用技巧与模式

### 20.1 类型收窄总结

| 方法 | 适用场景 |
|------|----------|
| `typeof` | 原始类型：string/number/boolean/symbol/bigint |
| `in` | 对象属性存在性检查 |
| `instanceof` | 类实例检查 |
| 自定义谓词 `x is T` | 复杂业务逻辑收窄 |
| 字面量判别 `x.kind` | 判别联合类型 (Discriminated Union) |

### 20.2 判别联合类型 (Discriminated Union)

```typescript
// 用共同字面量属性区分联合成员
interface Success {
  status: "success";
  data: string;
}
interface Failure {
  status: "error";
  error: Error;
}
type Result2 = Success | Failure;

function handle(r: Result2) {
  switch (r.status) {
    case "success":
      console.log(r.data);    // ✅ 收窄为 Success
      break;
    case "error":
      console.log(r.error);   // ✅ 收窄为 Failure
      break;
  }
}
```

### 20.3 品牌类型 (Branded Type / Nominal Type)

TypeScript 是结构化类型，但有时需要名义类型（如区分 UserId 和 OrderId）。

```typescript
// 用品牌属性模拟名义类型
type Brand<T, B extends string> = T & { __brand: B };

type UserId = Brand<number, "UserId">;
type OrderId = Brand<number, "OrderId">;

function getUser(id: UserId): void { /* ... */ }

const uid = 123 as UserId;
const oid = 456 as OrderId;
getUser(uid);  // ✅
// getUser(oid); // ❌ OrderId 不能赋给 UserId
// getUser(123); // ❌ number 不能赋给 UserId
```

### 20.4 常见反模式

```typescript
// ❌ 滥用 any
function bad(x: any): any { return x; }
// ✅ 用泛型
function good<T>(x: T): T { return x; }

// ❌ 过度使用类型断言
const el = document.getElementById("app") as HTMLDivElement;
// ✅ 用类型守卫
const el2 = document.getElementById("app");
if (el2 instanceof HTMLDivElement) {
  el2.innerHTML = "...";
}

// ❌ 对联合类型直接访问非共有属性
function bad2(x: { a: string } | { b: number }) {
  // return x.a;  // ❌
}
// ✅ 先收窄再访问
function good2(x: { a: string } | { b: number }) {
  if ("a" in x) return x.a;
  return x.b;
}
```

---

## 附录：快速记忆清单

| 主题 | 关键词 |
|------|--------|
| any vs unknown | unknown 安全，使用前必须收窄 |
| never | 永不返回、穷尽检查 |
| interface vs type | 声明合并选 interface，复杂运算选 type |
| 泛型约束 | `extends` 限制泛型范围 |
| 条件类型 | `T extends U ? X : Y`，配合 `infer` |
| 工具类型 | Partial / Pick / Omit / Record / ReturnType |
| 类型守卫 | typeof / in / instanceof / is |
| 结构化类型 | 看结构不看名字 |
| satisfies | 验证类型但不丢失推断信息 |
| 品牌类型 | `T & { __brand: B }` 模拟名义类型 |
