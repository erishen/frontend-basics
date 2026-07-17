const { describe, it } = require("node:test");
const assert = require("node:assert");
const isValid = require("../src/12-valid-parentheses");

describe("isValid", () => {
  it("示例", () => {
    assert.strictEqual(isValid("()"), true);
    assert.strictEqual(isValid("()[]{}"), true);
    assert.strictEqual(isValid("{[]}"), true);
    assert.strictEqual(isValid("(]"), false);
    assert.strictEqual(isValid("([)]"), false);
    assert.strictEqual(isValid(""), true);
  });
});