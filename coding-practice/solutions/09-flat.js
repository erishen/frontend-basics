function flat(arr, depth = Infinity) {
  if (depth <= 0) return arr.slice();
  return arr.reduce((acc, val) =>
    Array.isArray(val)
      ? acc.concat(flat(val, depth - 1))
      : acc.concat(val), []);
}

module.exports = flat;
