const { describe, it } = require("node:test");
const assert = require("node:assert");

// 切换 import 路径：练习时用 src，验证答案时用 solutions
const debounce = require("../src/01-debounce");

describe("debounce", () => {
  it("应在延迟后执行", (_, done) => {
    let called = 0;
    const fn = debounce(() => called++, 50);
    fn();
    assert.strictEqual(called, 0);
    setTimeout(() => {
      assert.strictEqual(called, 1);
      done();
    }, 100);
  });

  it("连续调用只执行最后一次", (_, done) => {
    let result = "";
    const fn = debounce((val) => { result = val; }, 50);
    fn("a");
    fn("b");
    fn("c");
    setTimeout(() => {
      assert.strictEqual(result, "c");
      done();
    }, 100);
  });

  it("应正确传递参数", (_, done) => {
    let received = null;
    const fn = debounce((val) => { received = val; }, 50);
    fn("hello");
    setTimeout(() => {
      assert.strictEqual(received, "hello");
      done();
    }, 100);
  });
});
