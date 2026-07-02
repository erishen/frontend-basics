// 异步并发控制（限制并发数）
// 最多同时执行 poolLimit 个异步任务

/**
 * @param {number} poolLimit - 最大并发数
 * @param {any[]} items - 任务参数列表
 * @param {Function} iterator - 异步任务函数 (item, index) => Promise
 * @returns {Promise<any[]>}
 */
async function asyncPool(poolLimit, items, iterator) {
  // TODO: 在这里实现
  const results = [];
  const executing = new Set();

  for(const [i, item] of items.entries()) {
    const p = Promise.resolve().then(() => iterator(item, i));
    results.push(p);
    executing.add(p);

    p.then(() => executing.delete(p));

    if(executing.size >= poolLimit) {
      await Promise.race(executing);
    }
  }
  return Promise.all(results);
}

module.exports = asyncPool;
