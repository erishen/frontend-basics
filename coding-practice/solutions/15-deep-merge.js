function deepMerge(target, ...sources) {
  for (const source of sources) {
    if (!source || typeof source !== "object") continue;
    for (const key of Object.keys(source)) {
      if (
        typeof target[key] === "object" && target[key] !== null &&
        !Array.isArray(target[key]) &&
        typeof source[key] === "object" && source[key] !== null &&
        !Array.isArray(source[key])
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
