const { describe, it } = require("node:test");
const assert = require("node:assert");

const { myCall, myApply, myBind } = require("../src/06-call-apply-bind");

describe("myCall", () => {
  it("应正确绑定 this", () => {
    function greet(greeting) { return `${greeting}, ${this.name}`; }
    assert.strictEqual(myCall(greet, { name: "Lei" }, "Hi"), "Hi, Lei");
  });
});

describe("myApply", () => {
  it("应正确绑定 this（数组参数）", () => {
    function add(a, b) { return a + b + this.offset; }
    assert.strictEqual(myApply(add, { offset: 10 }, [1, 2]), 13);
  });
});

describe("myBind", () => {
  it("应返回绑定了 this 的新函数", () => {
    function greet(greeting) { return `${greeting}, ${this.name}`; }
    const bound = myBind(greet, { name: "Sun" });
    assert.strictEqual(bound("Hey"), "Hey, Sun");
  });

  it("应支持预设参数", () => {
    function add(a, b) { return a + b; }
    const add5 = myBind(add, null, 5);
    assert.strictEqual(add5(3), 8);
  });
});
