// LeetCode 17 · 中等
// 电话号码的字母组合（迭代）

function letterCombinations(digits) {
  if (!digits) return [];
  const mapping = {
    "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
    "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
  };
  let res = [""];
  for (const d of digits) {
    const next = [];
    for (const prefix of res) {
      for (const ch of mapping[d]) {
        next.push(prefix + ch);
      }
    }
    res = next;
  }
  return res;
}

module.exports = letterCombinations;
