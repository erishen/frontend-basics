// 数组去重
// 多种实现方式

/**
 * @param {any[]} arr
 * @returns {any[]}
 */
function unique(arr) {
  // TODO: 在这里实现
  return arr.filter((item, index) => arr.indexOf(item) === index)
}

/**
 * 对象数组按指定 key 去重
 * @param {Object[]} arr
 * @param {string} key
 * @returns {Object[]}
 */
function uniqueBy(arr, key) {
  // TODO: 在这里实现
  const seen = new Set();
  return arr.filter((item) =>  {
    const k = item[key];
    return seen.has(k) ? false : (seen.add(k), true);
  });
}

module.exports = { unique, uniqueBy };
