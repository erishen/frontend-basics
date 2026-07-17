const { describe, it } = require("node:test");
const assert = require("node:assert");
const numIslands = require("../src/08-number-of-islands");

describe("numIslands", () => {
  it("示例", () => {
    const grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"],
    ];
    assert.strictEqual(numIslands(grid), 3);

    const grid2 = [["1","1","1"],["0","1","0"],["1","1","1"]];
    assert.strictEqual(numIslands(grid2), 1);

    assert.strictEqual(numIslands([]), 0);
  });
});
