const { describe, it } = require("node:test");
const assert = require("node:assert");

const deepClone = require("../src/03-deep-clone");

describe("deepClone", () => {
  it("应深拷贝普通对象", () => {
    const obj = { a: 1, b: { c: 2 } };
    const clone = deepClone(obj);
    assert.deepStrictEqual(clone, obj);
    assert.notStrictEqual(clone, obj);
    assert.notStrictEqual(clone.b, obj.b);
  });

  it("应深拷贝数组", () => {
    const arr = [1, [2, [3, 4]]];
    const clone = deepClone(arr);
    assert.deepStrictEqual(clone, arr);
    assert.notStrictEqual(clone, arr);
    assert.notStrictEqual(clone[1], arr[1]);
  });

  it("应处理循环引用", () => {
    const obj = { a: 1 };
    obj.self = obj;
    const clone = deepClone(obj);
    assert.strictEqual(clone.a, 1);
    assert.strictEqual(clone.self, clone);
    assert.notStrictEqual(clone.self, obj);
  });

  it("应处理 Date 和 RegExp", () => {
    const date = new Date("2024-01-01");
    const regex = /hello/gi;
    const obj = { date, regex };
    const clone = deepClone(obj);
    assert.deepStrictEqual(clone.date, date);
    assert.notStrictEqual(clone.date, date);
    assert.strictEqual(clone.regex.source, regex.source);
    assert.strictEqual(clone.regex.flags, regex.flags);
  });

  it("应处理原始类型", () => {
    assert.strictEqual(deepClone(42), 42);
    assert.strictEqual(deepClone("hello"), "hello");
    assert.strictEqual(deepClone(null), null);
    assert.strictEqual(deepClone(undefined), undefined);
  });
});
