// instanceof
// 沿原型链查找

/**
 * @param {any} left - 待检查的对象
 * @param {Function} right - 构造函数
 * @returns {boolean}
 */
function myInstance(left, right) {
  // TODO: 在这里实现
  if (left === null || left === undefined) return false;
  if (typeof left !== "object") return false;
  let proto = Object.getPrototypeOf(left);
  const prototype = right.prototype;

  while(proto !== null){
    if(proto === prototype) return true;
    proto = Object.getPrototypeOf(proto);
  }
  return false;
}

module.exports = myInstance;
