// call / apply / bind
// 手动实现 Function.prototype 上的三个方法

function myCall(fn, ctx, ...args) {
  // TODO: 在这里实现
  ctx = ctx ?? globalThis;
  const fnKey = Symbol();
  ctx[fnKey] = fn;
  const result = ctx[fnKey](...args);
  delete ctx[fnKey];
  return result;
}

function myApply(fn, ctx, args = []) {
  // TODO: 在这里实现
  ctx = ctx ?? globalThis;
  const fnKey = Symbol();
  ctx[fnKey] = fn;
  const result = ctx[fnKey](...args);
  delete ctx[fnKey];
  return result;
}

function myBind(fn, ctx, ...outerArgs) {
  // TODO: 在这里实现
  return function(...innerArgs) {
    return fn.apply(ctx, [...outerArgs, ...innerArgs]);
  }
}

module.exports = { myCall, myApply, myBind };
