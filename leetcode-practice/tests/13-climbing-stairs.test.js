const { describe, it } = require("node:test");
const assert = require("node:assert");
const climbStairs = require("../src/13-climbing-stairs");

describe("climbStairs", () => {
  it("示例", () => {
    assert.strictEqual(climbStairs(1), 1);
    assert.strictEqual(climbStairs(2), 2);
    assert.strictEqual(climbStairs(3), 3);
    assert.strictEqual(climbStairs(4), 5);
    assert.strictEqual(climbStairs(5), 8);
  });
});