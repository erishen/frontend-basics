const { describe, it } = require("node:test");
const assert = require("node:assert");

const curry = require("../src/11-curry");

describe("curry", () => {
  it("应支持逐个传参", () => {
    const add = (a, b, c) => a + b + c;
    const curried = curry(add);
    assert.strictEqual(curried(1)(2)(3), 6);
  });

  it("应支持一次传多个参数", () => {
    const add = (a, b, c) => a + b + c;
    const curried = curry(add);
    assert.strictEqual(curried(1, 2, 3), 6);
    assert.strictEqual(curried(1, 2)(3), 6);
    assert.strictEqual(curried(1)(2, 3), 6);
  });

  it("应保留 this 上下文", () => {
    function multiply(a, b) { return this.factor * a * b; }
    const curried = curry(multiply);
    const ctx = { factor: 10 };
    assert.strictEqual(curried.call(ctx, 2, 3), 60);
  });
});
