// 防抖 debounce
// 触发后等待 delay，期间再触发则重新计时

/**
 * @param {Function} fn - 需要防抖的函数
 * @param {number} delay - 延迟时间（ms）
 * @returns {Function} 防抖后的函数
 */
function debounce(fn, delay) {
  // TODO: 在这里实现
  let timer = null;
  return function(...args) {
    clearTimeout(timer)
    timer = setTimeout(() => fn.apply(this, args), delay);
  }
}

module.exports = debounce;
