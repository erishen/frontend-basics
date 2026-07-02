// LRU 缓存
// get / put 都要求 O(1) 时间复杂度

class LRUCache {
  /**
   * @param {number} capacity - 缓存容量
   */
  constructor(capacity) {
    // TODO: 在这里实现
    this.capacity = capacity;
    this.cache = new Map();
  }

  /**
   * @param {number} key
   * @returns {number}
   */
  get(key) {
    // TODO: 在这里实现
    if(!this.cache.has(key)) return -1;
    const value = this.cache.get(key);
    this.cache.delete(key);
    this.cache.set(key, value);
    return value;
  }

  /**
   * @param {number} key
   * @param {number} value
   */
  put(key, value) {
    // TODO: 在这里实现
    if(this.cache.has(key)) {
      this.cache.delete(key);
    } else if(this.cache.size >= this.capacity) {
      const oldestKey = this.cache.keys().next().value;
      this.cache.delete(oldestKey);
    }
    this.cache.set(key, value);
  }
}

module.exports = LRUCache;
