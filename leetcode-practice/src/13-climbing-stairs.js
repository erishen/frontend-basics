// LeetCode 70 · 简单
// 爬楼梯
// n 阶楼梯，每次可爬 1 或 2 阶，返回有多少种不同的到第 n 阶的方法。
// TODO: 实现 climbStairs

function climbStairs(n) {
  // TODO: 在这里实现
  if(n <= 2) return n;
  let a = 1, b = 2;
  for(let i = 3; i <= n; i++) {
    const next = a + b;
    a = b;
    b = next;
  }
  return b;
}

module.exports = climbStairs;
