// LeetCode 22 · 中等
// 括号生成（回溯）

function generateParentheses(n) {
  const res = [];
  const backtrack = (current, open, close) => {
    if (current.length === 2 * n) {
      res.push(current);
      return;
    }
    if (open < n) backtrack(current + "(", open + 1, close);
    if (close < open) backtrack(current + ")", open, close + 1);
  };
  backtrack("", 0, 0);
  return res;
}

module.exports = generateParentheses;
