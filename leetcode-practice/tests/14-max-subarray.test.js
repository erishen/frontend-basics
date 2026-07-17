const { describe, it } = require("node:test");
const assert = require("node:assert");
const maxSubArray = require("../src/14-max-subarray");

describe("maxSubArray", () => {
  it("示例", () => {
    assert.strictEqual(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6);
    assert.strictEqual(maxSubArray([1]), 1);
    assert.strictEqual(maxSubArray([5, 4, -1, 7, 8]), 23);
    assert.strictEqual(maxSubArray([-1, -2, -3]), -1);
  });
});