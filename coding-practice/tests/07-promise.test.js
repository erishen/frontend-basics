const { describe, it } = require("node:test");
const assert = require("node:assert");

const MyPromise = require("../src/07-promise");

describe("MyPromise", () => {
  it("resolve 应触发 then", (_, done) => {
    new MyPromise((resolve) => resolve(42))
      .then((val) => {
        assert.strictEqual(val, 42);
        done();
      });
  });

  it("reject 应触发 catch", (_, done) => {
    new MyPromise((_, reject) => reject("error"))
      .catch((err) => {
        assert.strictEqual(err, "error");
        done();
      });
  });

  it("应支持链式调用", (_, done) => {
    MyPromise.resolve(1)
      .then((v) => v + 1)
      .then((v) => v * 3)
      .then((v) => {
        assert.strictEqual(v, 6);
        done();
      });
  });

  it("then 返回 Promise 应自动解包", (_, done) => {
    MyPromise.resolve(1)
      .then((v) => new MyPromise((resolve) => resolve(v + 10)))
      .then((v) => {
        assert.strictEqual(v, 11);
        done();
      });
  });

  it("异步 resolve 也应正常工作", (_, done) => {
    new MyPromise((resolve) => {
      setTimeout(() => resolve("async"), 50);
    }).then((val) => {
      assert.strictEqual(val, "async");
      done();
    });
  });
});
