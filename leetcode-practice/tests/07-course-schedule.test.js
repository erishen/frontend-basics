const { describe, it } = require("node:test");
const assert = require("node:assert");
const canFinish = require("../src/07-course-schedule");

describe("canFinish", () => {
  it("示例", () => {
    assert.strictEqual(canFinish(2, [[1, 0]]), true);
    assert.strictEqual(canFinish(2, [[1, 0], [0, 1]]), false);
    assert.strictEqual(canFinish(1, []), true);
  });
});
