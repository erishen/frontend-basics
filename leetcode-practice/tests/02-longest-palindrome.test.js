const { describe, it } = require("node:test");
const assert = require("node:assert");
const longestPalindromicSubstring = require("../src/02-longest-palindrome");

describe("longestPalindromicSubstring", () => {
  it("示例", () => {
    assert.ok(["bab", "aba"].includes(longestPalindromicSubstring("babad")));
    assert.strictEqual(longestPalindromicSubstring("cbbd"), "bb");
    assert.strictEqual(longestPalindromicSubstring("a"), "a");
    assert.ok(["a", "c"].includes(longestPalindromicSubstring("ac")));
    assert.strictEqual(longestPalindromicSubstring(""), "");
  });
});
