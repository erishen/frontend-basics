const { describe, it } = require("node:test");
const assert = require("node:assert");

const LRUCache = require("../src/13-lru");

describe("LRUCache", () => {
  it("基本 get/put", () => {
    const cache = new LRUCache(2);
    cache.put(1, 1);
    cache.put(2, 2);
    assert.strictEqual(cache.get(1), 1);
    assert.strictEqual(cache.get(2), 2);
  });

  it("应淘汰最久未使用的缓存", () => {
    const cache = new LRUCache(2);
    cache.put(1, 1);
    cache.put(2, 2);
    cache.put(3, 3); // 淘汰 key=1
    assert.strictEqual(cache.get(1), -1);
    assert.strictEqual(cache.get(3), 3);
  });

  it("get 应刷新使用时间", () => {
    const cache = new LRUCache(2);
    cache.put(1, 1);
    cache.put(2, 2);
    cache.get(1);     // 刷新 key=1
    cache.put(3, 3);  // 淘汰 key=2（不是 key=1）
    assert.strictEqual(cache.get(2), -1);
    assert.strictEqual(cache.get(1), 1);
    assert.strictEqual(cache.get(3), 3);
  });

  it("put 已存在的 key 应更新值", () => {
    const cache = new LRUCache(2);
    cache.put(1, 1);
    cache.put(1, 10);
    assert.strictEqual(cache.get(1), 10);
  });
});
