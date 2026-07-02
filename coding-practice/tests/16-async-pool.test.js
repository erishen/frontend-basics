const { describe, it } = require("node:test");
const assert = require("node:assert");

const asyncPool = require("../src/16-async-pool");

describe("asyncPool", () => {
  it("应返回所有结果且保持顺序", async () => {
    const items = [1, 2, 3, 4, 5];
    const results = await asyncPool(2, items, async (item) => {
      await new Promise((r) => setTimeout(r, 10));
      return item * 2;
    });
    assert.deepStrictEqual(results, [2, 4, 6, 8, 10]);
  });

  it("应限制并发数", async () => {
    let running = 0;
    let maxRunning = 0;
    const items = [1, 2, 3, 4, 5, 6];

    await asyncPool(2, items, async (item) => {
      running++;
      maxRunning = Math.max(maxRunning, running);
      await new Promise((r) => setTimeout(r, 30));
      running--;
      return item;
    });

    assert.ok(maxRunning <= 2, `并发数 ${maxRunning} 超过限制 2`);
    assert.strictEqual(maxRunning, 2, "应达到最大并发数");
  });

  it("空列表应返回空数组", async () => {
    const results = await asyncPool(3, [], async (x) => x);
    assert.deepStrictEqual(results, []);
  });

  it("并发数大于任务数时应正常执行", async () => {
    const results = await asyncPool(10, [1, 2], async (item) => item * 3);
    assert.deepStrictEqual(results, [3, 6]);
  });
});
