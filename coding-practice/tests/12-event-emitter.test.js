const { describe, it } = require("node:test");
const assert = require("node:assert");

const EventEmitter = require("../src/12-event-emitter");

describe("EventEmitter", () => {
  it("on + emit 应触发回调", () => {
    const ee = new EventEmitter();
    let received = null;
    ee.on("test", (val) => { received = val; });
    ee.emit("test", "hello");
    assert.strictEqual(received, "hello");
  });

  it("应支持多个回调", () => {
    const ee = new EventEmitter();
    let count = 0;
    ee.on("test", () => count++);
    ee.on("test", () => count++);
    ee.emit("test");
    assert.strictEqual(count, 2);
  });

  it("off 应移除指定回调", () => {
    const ee = new EventEmitter();
    let count = 0;
    const fn = () => count++;
    ee.on("test", fn);
    ee.off("test", fn);
    ee.emit("test");
    assert.strictEqual(count, 0);
  });

  it("once 应只触发一次", () => {
    const ee = new EventEmitter();
    let count = 0;
    ee.once("test", () => count++);
    ee.emit("test");
    ee.emit("test");
    assert.strictEqual(count, 1);
  });

  it("emit 应传递多个参数", () => {
    const ee = new EventEmitter();
    let args = [];
    ee.on("test", (...a) => { args = a; });
    ee.emit("test", 1, 2, 3);
    assert.deepStrictEqual(args, [1, 2, 3]);
  });
});
