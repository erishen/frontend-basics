// Promise.all
// 全部成功才成功，任一失败即失败

/**
 * @param {Promise[]} promises
 * @returns {Promise<any[]>}
 */
function promiseAll(promises) {
  // TODO: 在这里实现
  return new Promise((resolve, reject) => {
    const results = [];
    let count = 0;
    if(promises.length === 0) return resolve(results);

    promises.forEach((p, i) => {
      Promise.resolve(p).then((value)=>{
        results[i] = value;
        if(++count === promises.length) resolve(results);
      }, reject);
    })
  })
}

module.exports = promiseAll;
