const { describe, it } = require("node:test");
const assert = require("node:assert");

const myInstance = require("../src/05-instanceof");

describe("myInstance", () => {
  it("基本类型判断", () => {
    function Animal() {}
    const a = new Animal();
    assert.strictEqual(myInstance(a, Animal), true);
    assert.strictEqual(myInstance(a, Object), true);
  });

  it("继承链判断", () => {
    class A {}
    class B extends A {}
    class C extends B {}
    const c = new C();
    assert.strictEqual(myInstance(c, A), true);
    assert.strictEqual(myInstance(c, B), true);
    assert.strictEqual(myInstance(c, C), true);
  });

  it("不相关的类型", () => {
    assert.strictEqual(myInstance([], Object), true);
    assert.strictEqual(myInstance("str", String), false);
    assert.strictEqual(myInstance({}, Array), false);
  });
});
