// LeetCode 5 · 中等
// 最长回文子串（中心扩展）

function longestPalindromicSubstring(s) {
  if (!s) return "";
  const n = s.length;
  let start = 0;
  let maxLen = 1;
  const expand = (l, r) => {
    while (l >= 0 && r < n && s[l] === s[r]) { l--; r++; }
    return r - l - 1;
  };
  for (let i = 0; i < n; i++) {
    const len = Math.max(expand(i, i), expand(i, i + 1));
    if (len > maxLen) {
      maxLen = len;
      start = i - Math.floor((len - 1) / 2);
    }
  }
  return s.slice(start, start + maxLen);
}

module.exports = longestPalindromicSubstring;
