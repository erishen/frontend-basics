const { describe, it } = require("node:test");
const assert = require("node:assert");

const myNew = require("../src/04-new");

describe("myNew", () => {
  it("应创建实例并绑定属性", () => {
    function Person(name) { this.name = name; }
    const p = myNew(Person, "Lei");
    assert.strictEqual(p.name, "Lei");
    assert.ok(p instanceof Person);
  });

  it("原型链应正确", () => {
    function Animal(type) { this.type = type; }
    Animal.prototype.speak = function () { return this.type; };
    const a = myNew(Animal, "dog");
    assert.strictEqual(a.speak(), "dog");
  });

  it("构造函数返回对象时应使用该对象", () => {
    function Factory() {
      this.x = 1;
      return { y: 2 };
    }
    const obj = myNew(Factory);
    assert.strictEqual(obj.y, 2);
    assert.strictEqual(obj.x, undefined);
  });
});
