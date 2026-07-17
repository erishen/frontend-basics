const { describe, it } = require("node:test");
const assert = require("node:assert");
const exist = require("../src/10-word-search");

describe("exist", () => {
  it("示例", () => {
    const board = [
      ["A","B","C","E"],
      ["S","F","C","S"],
      ["A","D","E","E"],
    ];
    assert.strictEqual(exist(board.map((r) => [...r]), "ABCCED"), true);
    assert.strictEqual(exist(board.map((r) => [...r]), "SEE"), true);
    assert.strictEqual(exist(board.map((r) => [...r]), "ABCB"), false);
  });
});
