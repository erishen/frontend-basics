const { describe, it } = require("node:test");
const assert = require("node:assert");
const isAnagram = require("../src/16-valid-anagram");

describe("isAnagram", () => {
  it("示例", () => {
    assert.strictEqual(isAnagram("anagram", "nagaram"), true);
    assert.strictEqual(isAnagram("rat", "car"), false);
    assert.strictEqual(isAnagram("a", "ab"), false);
    assert.strictEqual(isAnagram("", ""), true);
  });
});