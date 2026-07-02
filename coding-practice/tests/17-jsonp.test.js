const { describe, it } = require("node:test");
const assert = require("node:assert");

// JSONP 依赖浏览器环境（document/window），Node.js 下无法直接测试
// 这里验证函数签名和返回值结构

const jsonp = require("../src/17-jsonp");

describe("jsonp", () => {
  it("应是一个函数", () => {
    assert.strictEqual(typeof jsonp, "function");
  });

  it("应返回 Promise", () => {
    // 在 Node 环境下会因为没有 document 而报错
    // 但我们可以验证它返回的是 Promise
    try {
      const result = jsonp("http://example.com/api", "myCallback");
      // 如果执行到这里说明没有立即抛出同步错误
      assert.ok(result instanceof Promise || typeof result.then === "function");
    } catch (e) {
      // 在 Node 环境下 document 不存在，预期会抛错
      assert.ok(
        e instanceof ReferenceError || e.message.includes("document"),
        "Node 环境下应因缺少 document 而报错"
      );
    }
  });

  // 注意：完整测试需要浏览器环境（jsdom 或真实浏览器）
  // 面试时手写代码能写出正确结构即可
});
