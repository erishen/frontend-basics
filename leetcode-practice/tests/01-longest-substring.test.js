const { describe, it } = require("node:test");
const assert = require("node:assert");
const lengthOfLongestSubstring = require("../src/01-longest-substring");

describe("lengthOfLongestSubstring", () => {
  it("示例", () => {
    assert.strictEqual(lengthOfLongestSubstring("abcabcbb"), 3);
    assert.strictEqual(lengthOfLongestSubstring("bbbbb"), 1);
    assert.strictEqual(lengthOfLongestSubstring("pwwkew"), 3);
    assert.strictEqual(lengthOfLongestSubstring(""), 0);
    assert.strictEqual(lengthOfLongestSubstring("dvdf"), 3);
  });
});
