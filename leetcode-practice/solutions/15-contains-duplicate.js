// LeetCode 217 · 简单
// 存在重复元素
// 数组中存在任意两个相等元素则返回 true，否则 false。
// TODO: 实现 containsDuplicate

function containsDuplicate(nums) {
  const seen = new Set();
  for (const n of nums) {
    if (seen.has(n)) return true;
    seen.add(n);
  }
  return false;
}

module.exports = containsDuplicate;
