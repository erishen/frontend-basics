// LeetCode 70 · 简单
// 爬楼梯
// n 阶楼梯，每次可爬 1 或 2 阶，返回有多少种不同的到第 n 阶的方法。
// TODO: 实现 climbStairs

function climbStairs(n) {
  if (n <= 2) return n;
  let a = 1, b = 2; // dp[i-2], dp[i-1]
  for (let i = 3; i <= n; i++) {
    [a, b] = [b, a + b];
  }
  return b;
}

module.exports = climbStairs;
