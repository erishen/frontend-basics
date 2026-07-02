async function asyncPool(poolLimit, items, iterator) {
  const results = [];
  const executing = new Set();

  for (const [i, item] of items.entries()) {
    const p = Promise.resolve().then(() => iterator(item, i));
    results.push(p);
    executing.add(p);

    p.then(() => executing.delete(p));

    if (executing.size >= poolLimit) {
      await Promise.race(executing);
    }
  }
  return Promise.all(results);
}

module.exports = asyncPool;
