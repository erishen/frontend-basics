function myInstance(left, right) {
  let proto = Object.getPrototypeOf(left);
  const prototype = right.prototype;
  while (proto !== null) {
    if (proto === prototype) return true;
    proto = Object.getPrototypeOf(proto);
  }
  return false;
}

module.exports = myInstance;
