const { describe, it } = require("node:test");
const assert = require("node:assert");
const letterCombinations = require("../src/04-letter-combinations");

describe("letterCombinations", () => {
  it("示例", () => {
    const expected = ["ad","ae","af","bd","be","bf","cd","ce","cf"];
    assert.deepStrictEqual(
      [...letterCombinations("23")].sort(),
      [...expected].sort()
    );
    assert.deepStrictEqual(letterCombinations(""), []);
    assert.deepStrictEqual([...letterCombinations("2")].sort(), ["a","b","c"].sort());
  });
});
