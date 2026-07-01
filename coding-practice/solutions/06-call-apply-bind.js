function myCall(fn, ctx, ...args) {
  ctx = ctx ?? globalThis;
  const fnKey = Symbol();
  ctx[fnKey] = fn;
  const result = ctx[fnKey](...args);
  delete ctx[fnKey];
  return result;
}

function myApply(fn, ctx, args = []) {
  ctx = ctx ?? globalThis;
  const fnKey = Symbol();
  ctx[fnKey] = fn;
  const result = ctx[fnKey](...args);
  delete ctx[fnKey];
  return result;
}

function myBind(fn, ctx, ...outerArgs) {
  return function (...innerArgs) {
    return myCall(fn, ctx, ...outerArgs, ...innerArgs);
  };
}

module.exports = { myCall, myApply, myBind };
