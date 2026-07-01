const { describe, it } = require("node:test");
const assert = require("node:assert");

const { render, renderDeep } = require("../src/14-template");

describe("render", () => {
  it("应替换简单变量", () => {
    const result = render("Hello, {{name}}!", { name: "Lei" });
    assert.strictEqual(result, "Hello, Lei!");
  });

  it("应替换多个变量", () => {
    const result = render(
      "{{name}} is {{age}} years old",
      { name: "Lei", age: 30 }
    );
    assert.strictEqual(result, "Lei is 30 years old");
  });

  it("未定义的变量应替换为空字符串", () => {
    const result = render("Hello, {{name}}!", {});
    assert.strictEqual(result, "Hello, !");
  });
});

describe("renderDeep", () => {
  it("应支持深层路径", () => {
    const result = renderDeep(
      "Hi, {{user.name}}!",
      { user: { name: "Lei" } }
    );
    assert.strictEqual(result, "Hi, Lei!");
  });

  it("路径不存在应返回空字符串", () => {
    const result = renderDeep("{{a.b.c}}", { a: {} });
    assert.strictEqual(result, "");
  });
});
