const { describe, it } = require("node:test");
const assert = require("node:assert");

const throttle = require("../src/02-throttle");

describe("throttle", () => {
  it("首次调用应立即执行", () => {
    let called = 0;
    const fn = throttle(() => called++, 100);
    fn();
    assert.strictEqual(called, 1);
  });

  it("间隔内重复调用不执行", () => {
    let called = 0;
    const fn = throttle(() => called++, 100);
    fn();
    fn();
    fn();
    assert.strictEqual(called, 1);
  });

  it("间隔过后再次调用应执行", (_, done) => {
    let called = 0;
    const fn = throttle(() => called++, 50);
    fn();
    assert.strictEqual(called, 1);
    setTimeout(() => {
      fn();
      assert.strictEqual(called, 2);
      done();
    }, 100);
  });
});
