const { describe, it } = require("node:test");
const assert = require("node:assert");
const generateParentheses = require("../src/05-generate-parentheses");

describe("generateParentheses", () => {
  it("示例", () => {
    const expected = ["((()))","(()())","(())()","()(())","()()()"];
    assert.deepStrictEqual(
      [...generateParentheses(3)].sort(),
      [...expected].sort()
    );
    assert.deepStrictEqual(generateParentheses(1), ["()"]);
  });
});
