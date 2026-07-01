const { describe, it } = require("node:test");
const assert = require("node:assert");

const promiseAll = require("../src/08-promise-all");

describe("promiseAll", () => {
  it("全部成功时返回结果数组", async () => {
    const result = await promiseAll([
      Promise.resolve(1),
      Promise.resolve(2),
      Promise.resolve(3),
    ]);
    assert.deepStrictEqual(result, [1, 2, 3]);
  });

  it("结果顺序应与输入一致", async () => {
    const result = await promiseAll([
      new Promise((r) => setTimeout(() => r("slow"), 50)),
      Promise.resolve("fast"),
    ]);
    assert.deepStrictEqual(result, ["slow", "fast"]);
  });

  it("任一失败则整体失败", async () => {
    try {
      await promiseAll([
        Promise.resolve(1),
        Promise.reject("oops"),
        Promise.resolve(3),
      ]);
      assert.fail("should have rejected");
    } catch (err) {
      assert.strictEqual(err, "oops");
    }
  });

  it("空数组应返回空数组", async () => {
    const result = await promiseAll([]);
    assert.deepStrictEqual(result, []);
  });
});
