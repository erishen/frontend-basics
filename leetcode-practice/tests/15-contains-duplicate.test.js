const { describe, it } = require("node:test");
const assert = require("node:assert");
const containsDuplicate = require("../src/15-contains-duplicate");

describe("containsDuplicate", () => {
  it("示例", () => {
    assert.strictEqual(containsDuplicate([1, 2, 3, 1]), true);
    assert.strictEqual(containsDuplicate([1, 2, 3, 4]), false);
    assert.strictEqual(containsDuplicate([]), false);
    assert.strictEqual(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), true);
  });
});