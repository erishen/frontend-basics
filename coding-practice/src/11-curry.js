// 函数柯里化 curry
// 把多参数函数变成一系列单参数函数

/**
 * @param {Function} fn - 原函数
 * @returns {Function} 柯里化后的函数
 */
function curry(fn) {
  // TODO: 在这里实现
  return function curried(...args) {
    if(args.length >= fn.length) {
      return fn.apply(this, args);
    }
    return function(...args2) {
      return curried.apply(this, [...args, ...args2]);
    };
  };
}

module.exports = curry;
