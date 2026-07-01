const { describe, it } = require("node:test");
const assert = require("node:assert");

const flat = require("../src/09-flat");

describe("flat", () => {
  it("应完全扁平化嵌套数组", () => {
    assert.deepStrictEqual(flat([1, [2, [3, [4]]]]), [1, 2, 3, 4]);
  });

  it("应支持指定深度", () => {
    assert.deepStrictEqual(flat([1, [2, [3, [4]]]], 1), [1, 2, [3, [4]]]);
    assert.deepStrictEqual(flat([1, [2, [3, [4]]]], 2), [1, 2, 3, [4]]);
  });

  it("应处理空数组", () => {
    assert.deepStrictEqual(flat([]), []);
    assert.deepStrictEqual(flat([[], [[]], []]), []);
  });

  it("不应修改原数组", () => {
    const arr = [1, [2, 3]];
    flat(arr);
    assert.deepStrictEqual(arr, [1, [2, 3]]);
  });
});
