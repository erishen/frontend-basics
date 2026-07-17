const { describe, it } = require("node:test");
const assert = require("node:assert");
const threeSum = require("../src/03-three-sum");

const sortTriples = (arr) =>
  arr.map((t) => t.join(",")).sort().map((s) => s.split(",").map(Number));

describe("threeSum", () => {
  it("示例", () => {
    const result = threeSum([-1, 0, 1, 2, -1, -4]);
    const expected = [[-1, -1, 2], [-1, 0, 1]];
    assert.deepStrictEqual(sortTriples(result), sortTriples(expected));
    assert.deepStrictEqual(threeSum([]), []);
    assert.deepStrictEqual(threeSum([0]), []);
  });
});
