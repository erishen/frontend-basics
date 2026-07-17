const { describe, it } = require("node:test");
const assert = require("node:assert");
const permutations = require("../src/06-permutations");

const sortPerms = (arr) => arr.map((p) => p.join(",")).sort();

describe("permutations", () => {
  it("示例", () => {
    const expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]];
    assert.deepStrictEqual(
      sortPerms(permutations([1, 2, 3])),
      sortPerms(expected)
    );
    assert.deepStrictEqual(permutations([]), [[]]);
  });
});
