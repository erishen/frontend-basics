// LeetCode 242 · 简单
// 有效的字母异位词
// 两个字符串字母种类与出现次数完全相同则返回 true。
// TODO: 实现 isAnagram

function isAnagram(s, t) {
  // TODO: 在这里实现
  if(s.length !== t.length) return false;

  const count = new Map();
  for(const ch of s) {
    count.set(ch, (count.get(ch) || 0) + 1)
  }

  for(const ch of t) {
    const v = count.get(ch) || 0
    if (v === 0) return false;
    count.set(ch, v - 1)
  }
  
  return true
}

module.exports = isAnagram;
