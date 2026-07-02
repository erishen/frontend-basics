// 对象深度合并 deepMerge
// 递归合并对象，数组直接覆盖

/**
 * @param {Object} target
 * @param  {...Object} sources
 * @returns {Object}
 */
function deepMerge(target, ...sources) {
  // TODO: 在这里实现
  for(const source of sources) {
    if(!source || typeof source !== "object") continue;
    for(const key of Object.keys(source)) {
      if (
        typeof target[key] === "object" && target[key] !== null &&
        typeof source[key] === "object" && source[key] !== null &&
        !Array.isArray(target[key]) && !Array.isArray(source[key])
      ) {
        target[key] = deepMerge(target[key], source[key]);
      } else {
        target[key] = source[key];
      }
    }
  }
  return target;
}

module.exports = deepMerge;
