const { describe, it } = require("node:test");
const assert = require("node:assert");
const twoSum = require("../src/11-two-sum");

describe("twoSum", () => {
  it("示例", () => {
    assert.deepStrictEqual(twoSum([2, 7, 11, 15], 9).sort((a, b) => a - b), [0, 1]);
    assert.deepStrictEqual(twoSum([3, 2, 4], 6).sort((a, b) => a - b), [1, 2]);
    assert.deepStrictEqual(twoSum([3, 3], 6).sort((a, b) => a - b), [0, 1]);
  });
});