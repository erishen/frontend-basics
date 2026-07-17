// LeetCode 20 · 简单
// 有效的括号
// 给定仅含 ()[]{} 的字符串，判断括号是否匹配闭合。
// TODO: 实现 isValid

function isValid(s) {
  // TODO: 在这里实现
  const stack = []
  const pair = {")": "(", "]": "[", "}": "{"};
  for(const ch of s) {
    if(ch === "(" || ch === "[" || ch === "{") {
      stack.push(ch);
    } else {
      if(stack.pop() !== pair[ch]) return false;
    }
  }
  return stack.length === 0;
}

module.exports = isValid;
