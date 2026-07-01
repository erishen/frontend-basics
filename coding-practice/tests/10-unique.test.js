const { describe, it } = require("node:test");
const assert = require("node:assert");

const { unique, uniqueBy } = require("../src/10-unique");

describe("unique", () => {
  it("应去除重复数字", () => {
    assert.deepStrictEqual(unique([1, 2, 2, 3, 3, 3]), [1, 2, 3]);
  });

  it("应去除重复字符串", () => {
    assert.deepStrictEqual(unique(["a", "b", "a"]), ["a", "b"]);
  });

  it("应处理混合类型", () => {
    assert.deepStrictEqual(unique([1, "1", true, 1]), [1, "1", true]);
  });

  it("应处理空数组", () => {
    assert.deepStrictEqual(unique([]), []);
  });
});

describe("uniqueBy", () => {
  it("应按指定 key 去重", () => {
    const arr = [
      { id: 1, name: "a" },
      { id: 2, name: "b" },
      { id: 1, name: "c" },
    ];
    const result = uniqueBy(arr, "id");
    assert.strictEqual(result.length, 2);
    assert.strictEqual(result[0].name, "a");
    assert.strictEqual(result[1].name, "b");
  });
});
