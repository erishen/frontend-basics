function unique(arr) {
  return [...new Set(arr)];
}

function uniqueBy(arr, key) {
  const seen = new Set();
  return arr.filter((item) => {
    const k = item[key];
    return seen.has(k) ? false : (seen.add(k), true);
  });
}

module.exports = { unique, uniqueBy };
