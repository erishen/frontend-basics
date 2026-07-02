// new 操作符
// 模拟 new 的行为

/**
 * @param {Function} Constructor - 构造函数
 * @param  {...any} args - 参数
 * @returns {Object} 新创建的实例
 */
function myNew(Constructor, ...args) {
  // TODO: 在这里实现
  const obj = Object.create(Constructor.prototype);
  const result = Constructor.apply(obj, args);
  return result instanceof Object ? result : obj;
}

module.exports = myNew;
