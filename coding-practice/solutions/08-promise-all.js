function promiseAll(promises) {
  return new Promise((resolve, reject) => {
    const results = [];
    let count = 0;
    if (promises.length === 0) return resolve(results);

    promises.forEach((p, i) => {
      Promise.resolve(p).then(
        (value) => {
          results[i] = value;
          if (++count === promises.length) resolve(results);
        },
        reject
      );
    });
  });
}

module.exports = promiseAll;
