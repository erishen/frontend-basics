const { describe, it } = require("node:test");
const assert = require("node:assert");

const deepMerge = require("../src/15-deep-merge");

describe("deepMerge", () => {
  it("应合并简单对象", () => {
    const result = deepMerge({ a: 1 }, { b: 2 });
    assert.deepStrictEqual(result, { a: 1, b: 2 });
  });

  it("应递归合并嵌套对象", () => {
    const result = deepMerge(
      { a: { x: 1, y: 2 } },
      { a: { y: 3, z: 4 } }
    );
    assert.deepStrictEqual(result, { a: { x: 1, y: 3, z: 4 } });
  });

  it("数组应直接覆盖", () => {
    const result = deepMerge({ a: [1, 2] }, { a: [3, 4] });
    assert.deepStrictEqual(result, { a: [3, 4] });
  });

  it("应支持多个源对象", () => {
    const result = deepMerge({ a: 1 }, { b: 2 }, { c: 3 });
    assert.deepStrictEqual(result, { a: 1, b: 2, c: 3 });
  });

  it("后面的同名属性应覆盖前面", () => {
    const result = deepMerge({ a: 1 }, { a: 2 });
    assert.deepStrictEqual(result, { a: 2 });
  });
});
