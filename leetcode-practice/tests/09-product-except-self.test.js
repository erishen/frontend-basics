const { describe, it } = require("node:test");
const assert = require("node:assert");
const productExceptSelf = require("../src/09-product-except-self");

describe("productExceptSelf", () => {
  it("示例", () => {
    assert.deepStrictEqual(productExceptSelf([1,2,3,4]), [24,12,8,6]);
    assert.deepStrictEqual(productExceptSelf([1,2,3,4,5]), [120,60,40,30,24]);
    assert.deepStrictEqual(productExceptSelf([-1,1,0,-3,3]), [0,0,9,0,0]);
  });
});
