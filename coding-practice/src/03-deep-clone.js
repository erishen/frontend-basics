// 深拷贝 deepClone
// 处理循环引用、Date、RegExp

/**
 * @param {any} obj - 需要深拷贝的对象
 * @returns {any} 深拷贝后的新对象
 */
function deepClone(obj, map = new WeakMap()) {
  // TODO: 在这里实现
  if(obj === null || typeof obj !== "object") return obj;
  if(map.has(obj)) return map.get(obj);

  if(obj instanceof Date) return new Date(obj);
  if(obj instanceof RegExp) return new RegExp(obj.source, obj.flags);

  const clone = Array.isArray(obj) ? [] : {};
  map.set(obj, clone);

  for(const key of Object.keys(obj)) {
    clone[key] = deepClone(obj[key], map)
  }

  return clone;
}

module.exports = deepClone;
